# 🚀 Deep Space Rogue | 远航

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Web-blue.svg" alt="Web">
  <img src="https://img.shields.io/badge/Engine-Vanilla%20JS-informational" alt="Vanilla JS">
  <img src="https://img.shields.io/badge/Storage-localStorage-green.svg" alt="localStorage">
  <img src="https://img.shields.io/badge/License-MIT-brightgreen.svg" alt="MIT License">
</p>

<p align="center">
  <b>一款文字肉鸽 / 文明演进经营游戏</b><br>
  <i>从篝火时代起步，发展产业链、推进科技树，最终迈向星际文明</i>
</p>

---

## 项目状态（请先看这里）

本仓库当前以 **前端版本** 为主：

- ✅ 主游戏运行在浏览器（HTML + CSS + JavaScript）
- ✅ 核心逻辑在 `index.js` 的 `LocalGameEngine`
- ✅ 进度保存在浏览器 `localStorage`
- ⚠️ 仓库中仍保留 Python/FastAPI 旧代码，仅作历史参考，**已不作为当前运行入口**

---

## 快速开始

### 推荐方式（本地开发）

```bash
npm install
npm run dev
```

然后打开终端输出的本地地址（通常是 `http://localhost:5173`）。

### 生产预览

```bash
npm run build
npm run preview
```

---

## 运行入口

- `index.html`：启动页 / 展示页（飞船动画）
- `game.html`：游戏主界面（资源、建筑、人力、研究、事件）

---

## 前端代码结构（当前重点）

### `index.js`

核心逻辑文件，包含：

- **内嵌数据**：`EMBEDDED_DATA`
  - 资源 / 建筑 / 职业 / 研究 / 事件定义
- **本地引擎**：`LocalGameEngine`
  - `tick()` 资源结算
  - `build()` 建造
  - `research()` 研究
  - `dispatch()` 人力分配
  - `save()/load/reset()` 存档管理
- **渲染层**
  - `renderResources / renderBuildings / renderProfessions / renderResearches / renderEvents`
- **交互与反馈**
  - toast 提示
  - tooltip 说明
  - 资源浮动数字
  - 建筑脉冲动画
  - 研究完成全屏通知
  - 顶部“重置存档”按钮

### `style.css`

UI与动效样式：

- 面板网格布局（事件、资源、操作、人力、研究）
- 响应式布局（窄屏下自动降列）
- 按钮与职业操作样式
- tooltip / toast 样式
- 浮动数字、脉冲、全屏通知动画
- `--ui-scale` 动态缩放变量（由 JS 根据窗口尺寸更新）

### `game.html`

游戏UI骨架页面：

- 顶栏状态与重置按钮
- 五大核心面板容器
- 挂载 `index.js`（当前唯一游戏脚本入口）

### `index.html`

视觉启动页：

- 飞船 SVG 动画
- 背景扫描线、地平线、发光文字等效果

---

## 存档机制

- 键名：`dsr_local_save_v1`
- 存储位置：浏览器 `localStorage`
- 自动保存时机：建造、研究、人力变更、时间结算等
- 可通过游戏内“重置存档”按钮清档重开

> 注意：更换浏览器、清理站点数据后，存档会丢失。

---

## 数据维护说明

当前运行使用的是 `index.js` 中的 `EMBEDDED_DATA`。

仓库中的 `data/*.dat` 仍可作为平衡配置参考，但**不会自动驱动前端运行**。如果你修改了 `data/*.dat`，需要同步到 `index.js` 的内嵌数据。

---

## 目录概览

```text
Deep-Space-Rogue/
├── game.html            # 游戏页面（主入口）
├── index.html           # 启动页
├── index.js             # 前端本地引擎 + UI逻辑 + 内嵌数据
├── style.css            # 样式与动画
├── data/                # 原始配置数据（参考/维护用）
├── package.json         # Vite 脚本
├── package-lock.json
├── requirements.txt     # 旧 Python 依赖（历史遗留）
├── main.py              # 旧后端入口（已废弃）
├── mainWithPC.py        # 旧桌面入口（已废弃）
└── README.md
```

---

## 后续开发建议（前端方向）

1. 建立 `data/*.dat -> index.js` 自动同步脚本，避免双份数据手改
2. 增加版本化存档（兼容字段迁移）
3. 拆分 `index.js`（engine/ui/data 分文件）降低维护成本
4. 为关键数值平衡添加调试面板或可视化工具

---

## 开源协议

本项目采用 [MIT License](./LICENSE)。
