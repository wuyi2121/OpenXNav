<div align="center">

# OpenXNav

### Towards Generalist Embodied Navigation

**One System, Many Navigation Tasks.**

Han Zheng · Zhe Chen · Yijian Li · Ming Yang · Tong Qin

**Shanghai Jiao Tong University**

[![Project Page](https://img.shields.io/badge/Project-UrbanAgent-1f6feb?logo=googlechrome&logoColor=white)](https://wuyi2121.github.io/UrbanAgent/)
[![Video Demos](https://img.shields.io/badge/Video-Real--World_Demos-ea4335?logo=youtube&logoColor=white)](https://wuyi2121.github.io/UrbanAgent/#agent)
![Code Coming Soon](https://img.shields.io/badge/Code-Coming_Soon-6e7681?logo=github&logoColor=white)

</div>

<div align="justify">

## 🌍 What is OpenXNav?

OpenXNav is a generalist embodied navigation system in the open world, with four core highlights:

- **Open Semantics:** Enable natural human-robot interaction through open-vocabulary understanding and flexible multimodal instructions.
- **Unified Navigation:** Unify object search, instruction following, target tracking, social navigation, POI navigation, urban navigation and other tasks across indoor and outdoor environments.
- **Accessible Deployment:** Provide an open-source, modular framework for easy deployment across different robotic embodiments in open world.
- **Continuous Evolution:** Continuously benefit from advances in foundation models, navigation policies, and robot control.

<p align="center">
  <img src="assets/system.png" alt="OpenXNav: a generalist embodied navigation system in the open world, featuring Open Semantics, Unified Navigation, Accessible Deployment, and Continuous Evolution." width="100%">
</p>

## 🧭 OpenXNav · v0.1

- **UrbanAgent:** A Zero-Shot Agentic System for Long-Horizon Urban Navigation.
- **First milestone:** OpenXNav v0.1 explores generalist embodied navigation in real-world urban environments.
- **Core approach:** Combine vision-language models, digital map tools, and real-time navigation.

<!-- GIF excerpts from https://wuyi2121.github.io/UrbanAgent/video/:
     Regenerate with: python3 scripts/generate_demo_gifs.py
     long/coffee.mp4: 00:08–00:15.5, played at 1.5× source speed.
     semantic/semantic1_final.mp4: 00:08–00:13.
     poi/luckin/luckin1_final.mp4: 00:07–00:12.
     long/long_final.mp4: 00:20–00:25.
-->
<table>
  <tr>
    <th width="50%" align="center">🧠 Agentic Navigation</th>
    <th width="50%" align="center">👀 Vision-Language Navigation</th>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <p><a href="https://wuyi2121.github.io/UrbanAgent/#agent"><img src="assets/demos/urbanagent-agentic.gif" alt="UrbanAgent interpreting a coffee request and calling POI and map tools" width="100%"></a></p>
      <p>Understand instructions and execute tasks with tools.</p>
      <a href="https://wuyi2121.github.io/UrbanAgent/#agent"><sub>Watch demo ↗</sub></a>
    </td>
    <td width="50%" align="center" valign="top">
      <p><a href="https://wuyi2121.github.io/UrbanAgent/#vln"><img src="assets/demos/urbanagent-vln.gif" alt="UrbanAgent following a sidewalk with multiple camera views" width="100%"></a></p>
      <p>Follow sidewalks with language and visual cues.</p>
      <a href="https://wuyi2121.github.io/UrbanAgent/#vln"><sub>Watch demo ↗</sub></a>
    </td>
  </tr>
  <tr>
    <th width="50%" align="center">📍 Point-of-Interest Navigation</th>
    <th width="50%" align="center">🗺️ Long-Horizon Urban Navigation</th>
  </tr>
  <tr>
    <td width="50%" align="center" valign="top">
      <p><a href="https://wuyi2121.github.io/UrbanAgent/#poinav"><img src="assets/demos/urbanagent-poi.gif" alt="UrbanAgent approaching the entrance of a Luckin Coffee storefront" width="100%"></a></p>
      <p>Locate storefronts and navigate to their entrances.</p>
      <a href="https://wuyi2121.github.io/UrbanAgent/#poinav"><sub>Watch demo ↗</sub></a>
    </td>
    <td width="50%" align="center" valign="top">
      <p><a href="https://wuyi2121.github.io/UrbanAgent/#amap"><img src="assets/demos/urbanagent-long-horizon.gif" alt="UrbanAgent following a route with digital map guidance and local navigation" width="100%"></a></p>
      <p>Follow kilometer-scale routes with digital map guidance.</p>
      <a href="https://wuyi2121.github.io/UrbanAgent/#amap"><sub>Watch demo ↗</sub></a>
    </td>
  </tr>
</table>

<p align="center">
  <a href="https://wuyi2121.github.io/UrbanAgent/"><strong>Explore UrbanAgent &amp; Watch Real-World Demos →</strong></a>
</p>

## 🚀 Roadmap

- [x] v0.1 — UrbanAgent: Long-Horizon Urban Navigation.
- [ ] v1.0 — OpenXNav: Generalist Embodied Navigation.
- [ ] Full Open-Source Release.

## 📖 Citation

If you find this work useful in your research, please cite:

```bibtex
@misc{zheng2026urbanagent,
  author = {Zheng, Han and Chen, Zhe and Li, Yijian
            and Yang, Ming and Qin, Tong},
  title  = {{UrbanAgent}: A Zero-Shot Agentic System
            for Long-Horizon Urban Navigation},
  year   = {2026},
  url    = {https://wuyi2121.github.io/UrbanAgent/},
  note   = {Project page}
}
```

</div>

---

<p align="center"><sub>Star or watch this repository for future updates and releases.</sub></p>
