# Deep Space Rogue | 远航

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Web-blue.svg" alt="Web">
  <img src="https://img.shields.io/badge/Storage-localStorage-green.svg" alt="localStorage">
  <img src="https://img.shields.io/badge/License-MIT-brightgreen.svg" alt="MIT License">
</p>

<p align="center">
  <b>一款以文明演进与宇宙探索为主题的文字经营游戏</b><br>
  <i>从篝火营地出发，发展科技、调配人力、积累资源，最终迈向星际时代</i>
</p>

---

## 游戏简介

《远航》是一款运行在浏览器中的文字经营游戏。你将从一个资源匮乏的早期聚落开始，通过建造设施、研究技术、分配人口与管理资源，逐步解锁更复杂的生产链，推动文明不断升级。

当前版本已经改为纯前端运行：

- 游戏逻辑全部在浏览器内执行
- 不依赖远端服务器
- 存档保存在浏览器 `localStorage`
- 游戏数据已直接内嵌在前端脚本中

---

## 核心玩法

- 建造：消耗资源解锁新建筑、资源与职业
- 研究：消耗知识推进科技树，打开后续发展路线
- 人力：在不同职业之间调配人口，平衡生产与消耗
- 资源：管理基础资源、工业资源与高阶资源的增长
- 事件：查看当前事件条目与效果说明

---

## 快速开始

### 方式一：直接打开

由于当前游戏数据已经内嵌到 [index.js](./index.js)，可以直接打开 [game.html](./game.html) 运行。

### 方式二：本地预览（推荐）

项目保留了 `vite`，可用于本地静态预览：

```bash
npm install
npm run dev
```

然后在浏览器中打开终端输出的本地地址。

### 存档说明

- 游戏进度自动保存在浏览器 `localStorage`
- 页面顶部提供“重置存档”按钮，可直接重新开局
- 更换浏览器、清空站点数据或手动清理本地存储后，存档会丢失

---

## 游戏数据

原始游戏配置仍保存在 `data/` 目录中，便于维护和编辑：

| 文件 | 说明 |
|------|------|
| `data/building.dat` | 建筑定义（消耗、解锁、效果） |
| `data/resource.dat` | 资源定义（初始解锁、容量） |
| `data/profession.dat` | 职业定义（可分配性、效果） |
| `data/research.dat` | 研究定义（消耗、解锁、效果） |
| `data/event.dat` | 事件定义（描述、权重、效果） |

运行时使用的是 [index.js](./index.js) 中内嵌的数据副本。

---

## 项目结构

当前文档只展示前端运行相关结构：

```text
Deep-Space-Rogue/
├── data/               # 原始游戏配置数据
├── game.html           # 游戏主页面
├── index.html          # 入口页面/说明页
├── index.js            # 前端游戏逻辑、本地引擎、内嵌数据
├── style.css           # 页面样式
├── package.json        # 本地预览脚本（vite）
├── package-lock.json   # 依赖锁定
├── tool/               # 开发辅助脚本
└── README.md           # 项目说明
```

---

## 当前实现

- 纯前端本地运行
- 浏览器端资源自动结算
- 建筑、研究、人力分配可直接在前端计算
- 本地存档与重置存档
- 自适应布局与面板缩放

---

## 开发说明

如果你准备继续扩展内容，优先关注以下文件：

- [index.js](./index.js)：核心逻辑、状态管理、UI 渲染
- [style.css](./style.css)：界面布局与视觉样式
- `data/*.dat`：原始内容配置，可作为后续平衡调整来源

当前前端逻辑已经不再依赖远端接口，因此新增内容时，默认应直接修改前端逻辑与本地数据。

---

## 开源协议

本项目采用 [MIT License](./LICENSE)。

```text
Copyright (c) 2026 GameOneByOne
```
