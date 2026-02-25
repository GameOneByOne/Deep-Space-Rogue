# 🚀 Deep Space Rogue | 远航

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13+-blue.svg" alt="Python 3.13+">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License">
  <img src="https://img.shields.io/badge/Status-DEMO-orange.svg" alt="DEMO">
</p>

<p align="center">
  <b>一款背景是宇宙探索的文字肉鸽游戏</b><br>
  <i>从篝火旁的原住民到驾驶星际飞船的指挥官，见证文明的每一次跃迁</i>
</p>

---

## 🎮 游戏简介

《远航》是一款以宇宙探索为背景的文字类 Roguelike 游戏。你将扮演一个文明的引导者，从最初的原始部落开始，逐步发展科技、建造设施、调配人力资源，最终迈向星际航行时代。

### ✨ 核心特色

- **🌍 文明演进**：从石器时代到星际文明，经历完整的科技树发展
- **🏗️ 五大模块**：建筑、职业、资源、研究、事件五大系统深度联动
- **🎯 策略经营**：合理分配人力资源，平衡资源产出与消耗
- **🌌 分支选择**：大量随机事件与科技分支，每局体验不同
- **💻 双端支持**：本地 tkinter 客户端 + Web 在线版本，随时畅玩

---

## 🚀 快速开始

### 环境要求

- **Python** = 3.13+

### 本地运行

```bash
# 克隆仓库
git clone https://github.com/GameOneByOne/Deep-Space-Rogue.git
cd Deep-Space-Rogue

# 运行本地版本（tkinter GUI）
python mainWithPC.py
```

### Web 版本

```bash
# 启动服务端
python main.py

# 浏览器访问
open http://localhost:8000
```

或者访问在线演示：**https://gameonebyone.github.io/Deep-Space-Rogue/**

---

## 🎯 游戏系统

### 🏗️ 建筑系统
从简单的「篝火」到复杂的「曲率引擎」，每种建筑都会解锁新的可能性：
- 消耗资源建造
- 解锁新职业与资源
- 提供被动产出或特殊效果

### 👥 职业系统
合理分配人力资源是游戏的核心：
- **空闲者**：人口增长的基础
- **猎人/农民/伐木工**：基础资源产出
- **学者**：推进科技研究
- **工程师/飞行员**：星际时代的高级职业

### 💎 资源系统
管理多种资源的产出与消耗：
- 基础资源：食物、木材、石材
- 工业资源：金属、燃料、能源
- 高级资源：知识、科技点数、星际货币

### 🔬 研究系统
解锁新建筑与职业的关键：
- 消耗知识进行研究
- 多分支科技树
- 关键科技改变游戏进程

### 📜 事件系统
随机事件带来挑战与机遇：
- 自然灾害、资源发现
- 文明抉择、道德困境
- 外星接触、星际冒险

---

## 📊 游戏数据

所有游戏内容均通过 JSON 数据文件配置，位于 `data/` 目录：

| 文件 | 说明 |
|------|------|
| `building.dat` | 建筑定义（成本、效果、解锁条件） |
| `resource.dat` | 资源定义（产出、消耗、上限） |
| `profession.dat` | 职业定义（产出、前置条件） |
| `research.dat` | 研究定义（成本、效果） |
| `event.dat` | 事件定义（触发条件、选项） |

---

## 🛠️ 项目结构

```
Deep-Space-Rogue/
├── 📁 data/              # 游戏数据配置文件
├── 📁 tool/              # 开发工具脚本
├── 🐍 main.py            # Web 服务端入口 (FastAPI)
├── 🐍 mainWithPC.py      # 本地 GUI 入口 (tkinter)
├── 🐍 GameEngine.py      # 游戏核心引擎
├── 🐍 GameBuilding.py    # 建筑管理模块
├── 🐍 GameResource.py    # 资源管理模块
├── 🐍 GameProfession.py  # 职业管理模块
├── 🐍 GameResearch.py    # 研究管理模块
├── 🐍 GameEvent.py       # 事件管理模块
├── 🐍 GameEffect.py      # 效果执行器
├── 🐍 GameUI.py          # 本地 GUI 界面
├── 🌐 index.html         # Web 版启动页面
├── 🌐 game.html          # Web 版游戏页面
├── 🎨 style.css          # Web 版样式
├── ⚙️ style.js           # Web 版逻辑
└── 📄 README.md          # 本文件
```

---

## 🗺️ 开发路线

- [x] 基础游戏框架搭建
- [x] 建筑、资源、职业、研究四大模块
- [x] 事件系统（基础 UI）
- [x] 完整的科技树（原始时代 → 星际航行）
- [x] Web 版本上线
- [ ] 事件系统完善（随机触发、分支剧情）
- [ ] 存档系统
- [ ] 成就系统
- [ ] 更多随机事件
- [ ] 多语言支持

---

## 🤝 参与贡献

欢迎 Issue 和 PR！在提交之前，请确保：

1. 代码符合项目现有风格
2. 测试通过本地运行
3. 更新相关文档

---

## 📄 开源协议

本项目采用 [MIT License](LICENSE) 开源协议。

```
Copyright (c) 2026 GameOneByOne
```

---

<p align="center">
  <b>🌟 觉得好玩的话，点个 Star 支持一下吧！</b>
</p>
