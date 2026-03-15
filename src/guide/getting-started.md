---
title: 快速开始
icon: rocket
order: 1
---

# 快速开始

本指南将帮助你快速安装和运行 Pyisland 项目。

::: info 环境要求
- **操作系统**: Windows 10/11
- **Python**: 3.11+
:::

## 安装步骤

### 1. 克隆仓库

```bash
git clone https://github.com/Python-island/Python-island.git
cd Python-island
```

### 2. 选择分支

项目有多个分支版本，建议使用以下稳定版本：

::: info 分支选择
| 分支 | 技术栈 | 适用场景 |
|------|--------|----------|
| `pyislandPyside6` | Python + PySide6 | 稳定版，功能完整 |
| `tauri-island` | Rust + Tauri 2 | 性能优先，新技术体验 |
| `pyisland-wanku` | Python + PySide6 | 高仿真 iOS 风格 |
| `harmony` | Python + PySide6 | 精简版，占用小 |
:::

切换到指定分支：

```bash
# 例如切换到 pyislandPyside6 分支
git checkout pyislandPyside6
```

### 3. 安装 Python 依赖

::: tip 推荐方式
使用虚拟环境隔离依赖：
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
:::

或直接安装：

```bash
pip install -r requirements.txt
```

### 4. 运行应用

```bash
python main.py
```

## 首次使用

首次运行后，你将看到：

1. **灵动岛出现在屏幕顶部** - 显示当前时间
2. **系统托盘图标** - 位于任务栏右下角

### 基本操作

- **点击灵动岛**: 展开/收起控制面板
- **拖动灵动岛**: 调整位置
- **右键托盘图标**: 打开设置或退出

## 常见问题

::: warning 托盘图标不显示
确保 `resources/icons/controls/tray.png` 文件存在。
:::

::: warning 亮度调节无效
可能需要以管理员权限运行程序。
:::

::: danger 模块导入错误
确保通过 `python main.py` 运行，而不是直接运行子模块文件。
:::
