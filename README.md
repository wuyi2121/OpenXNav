<div align="center">

# OpenXNav

### A Generalist Embodied Navigation System in the Open World

Han Zheng · Zhe Chen · Yijian Li · Ming Yang · Tong Qin*

**Shanghai Jiao Tong University**

![arXiv Coming Soon](https://img.shields.io/badge/arXiv-Coming_Soon-b31b1b?logo=arxiv&logoColor=white)
[![Project Page](https://img.shields.io/badge/Project-UrbanAgent-1f6feb?logo=googlechrome&logoColor=white)](https://wuyi2121.github.io/UrbanAgent/)
[![Bilibili Video](https://img.shields.io/badge/Video-Bilibili-fb7299?logo=bilibili&logoColor=white)]()
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

**UrbanAgent** represents our first step towards generalist embodied navigation.

- **Research Focus:** Long-horizon autonomous navigation in real-world urban environments.
- **Core Approach:** Integrating vision-language models, digital map tools, and real-time navigation within a unified framework.

<!-- GIF excerpts from https://wuyi2121.github.io/UrbanAgent/video/:
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
    </td>
    <td width="50%" align="center" valign="top">
      <p><a href="https://wuyi2121.github.io/UrbanAgent/#vln"><img src="assets/demos/urbanagent-vln.gif" alt="UrbanAgent following a sidewalk with multiple camera views" width="100%"></a></p>
      <p>Follow sidewalks with language and visual cues.</p>
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
    </td>
    <td width="50%" align="center" valign="top">
      <p><a href="https://wuyi2121.github.io/UrbanAgent/#amap"><img src="assets/demos/urbanagent-long-horizon.gif" alt="UrbanAgent following a route with digital map guidance and local navigation" width="100%"></a></p>
      <p>Follow kilometer-scale routes with digital map guidance.</p>
    </td>
  </tr>
</table>

<p align="center">
  <a href="https://wuyi2121.github.io/UrbanAgent/"><strong>Explore UrbanAgent &amp; Watch Real-World Demos →</strong></a>
</p>

## 🚀 Roadmap

- [x] Preview OpenXNav v0.1 — UrbanAgent.
- [ ] Release OpenXNav v1.0 — Generalist Embodied Navigation.
- [ ] Release source code and deployment.

## 📖 Citation

If you find this work useful in your research, please cite:

```bibtex
@misc{zheng2026urbanagent,
  author = {Zheng, Han and Chen, Zhe and Li, Yijian and Yang, Ming and Qin, Tong},
  title  = {{UrbanAgent}: A Zero-Shot Agentic System for Long-Horizon Urban Navigation},
  year   = {2026},
  url    = {https://wuyi2121.github.io/UrbanAgent/},
  note   = {Project page}
}
```

## 📄 License

This project is licensed under the [Apache License 2.0](LICENSE).

</div>

---

<p align="center"><sub>Star or watch this repository for future updates and releases.</sub></p>
