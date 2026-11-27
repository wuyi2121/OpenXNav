#!/usr/bin/env python3
"""Generate README GIFs with protected red-to-yellow trajectory colors.

Requires ffmpeg, curl, and Pillow. Source videos are cached outside the repository.
Run: python3 scripts/generate_demo_gifs.py
"""

import argparse
from colorsys import hsv_to_rgb
from pathlib import Path
import subprocess
import tempfile

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
VIDEO_BASE = "https://wuyi2121.github.io/UrbanAgent/video/"
CLIPS = (
    ("agentic", "long/coffee.mp4", 8, 7.5, 1.5),
    ("vln", "semantic/semantic1_final.mp4", 8, 5, 1),
    ("poi", "poi/luckin/luckin1_final.mp4", 7, 5, 1),
    ("long-horizon", "long/long_final.mp4", 20, 5, 1),
)


def run(*args):
    subprocess.run([str(arg) for arg in args], check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source-dir", type=Path,
        default=Path(tempfile.gettempdir()) / "openxnav-video-sources",
    )
    args = parser.parse_args()
    args.source_dir.mkdir(parents=True, exist_ok=True)
    output_dir = ROOT / "assets" / "demos"
    output_dir.mkdir(parents=True, exist_ok=True)

    for name, video_path, start, duration, speed in CLIPS:
        source = args.source_dir / f"openxnav-{name}.mp4"
        if not source.exists():
            partial = source.with_suffix(".part")
            run("curl", "-sSL", "--fail", "--retry", 2, "--max-time", 180,
                VIDEO_BASE + video_path, "-o", partial)
            partial.replace(source)

        inputs = ("ffmpeg", "-v", "error", "-ss", start, "-t", duration,
                  "-i", source)
        frames = (f"setpts=(PTS-STARTPTS)/{speed},fps=8,trim=duration=5,"
                  "scale=480:-1:flags=lanczos")
        with tempfile.TemporaryDirectory(prefix="openxnav-palette-") as tmp:
            palette = Path(tmp) / "palette.png"
            run(*inputs, "-vf", frames + ",palettegen=max_colors=192:reserve_transparent=0",
                "-frames:v", 1, "-y", palette)

            # A full-frame palette favors vegetation over the thin trajectory.
            # Reserve 64 entries for red/orange/yellow, including darker and
            # less saturated edge colors introduced by video compression and scaling.
            with Image.open(palette) as image:
                image = image.convert("RGBA")
                colors = list(image.getdata())
                colors[192:] = [
                    (*[round(channel * 255) for channel in hsv_to_rgb(hue / 42, saturation, value)], 255)
                    for value in (0.45, 0.65, 0.85, 1.0)
                    for saturation in (0.65, 1.0)
                    for hue in range(8)
                ]
                image.putdata(colors)
                image.save(palette)

            target = output_dir / f"urbanagent-{name}.gif"
            # Nearest-color mapping keeps narrow trajectory lines free of
            # green background dithering. trim prevents trailing frozen frames.
            run(*inputs, "-i", palette, "-filter_complex",
                f"[0:v]{frames}[v];[v][1:v]paletteuse=dither=none:diff_mode=rectangle",
                "-t", 5, "-an", "-loop", 0, "-y", target)
            print(f"{target.relative_to(ROOT)}: {target.stat().st_size / 1024**2:.2f} MiB")


if __name__ == "__main__":
    main()
