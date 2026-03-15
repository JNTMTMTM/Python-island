---
title: harmony
icon: layer-group
order: 4
---

# harmony

这是 Pyisland 项目的 **精简版**，基于 Python 和 PySide6 构建，专注于核心功能，代码简洁，占用资源少。

## 技术栈

- **Python 3.7+**
- **PySide6**: Qt 的 Python 绑定
- **QSS**: 界面样式定制

## 功能列表

### 核心功能

- ✅ 灵动岛胶囊形态设计
- ✅ 实时时间显示
- ✅ 点击展开/收起控制面板
- ✅ 鼠标拖动位置
- ✅ 自动收缩（失去焦点）

### 系统控制

- ✅ 亮度调节（滑动条 + 防抖）
- ✅ 音量调节（滑动条 + 防抖）

### 系统监控

- ✅ WiFi 状态显示
- ✅ 蓝牙状态显示
- ✅ 电池状态显示

## 项目特点

### 精简设计

- 代码量少，易于理解和维护
- 没有复杂的服务模块划分
- 核心功能集中实现

### 轻量运行

- 依赖较少
- 启动快速
- 资源占用低

## 项目结构

```
harmony/
├── app/
│   ├── __init__.py
│   ├── island.py      # 核心功能实现
│   └── utils.py      # 工具函数
├── resources/
│   ├── icons/        # 图标资源
│   └── styles/       # 样式文件
├── main.py           # 入口文件
└── README.md
```

## 安装运行

```bash
# 克隆并切换分支
git clone https://github.com/Python-island/Python-island.git
cd Python-island
git checkout harmony

# 安装依赖
pip install PySide6 comtypes

# 运行
python main.py
```

## 与其他分支对比

| 特性 | pyislandPyside6 | pyisland-wanku | harmony |
|------|-----------------|----------------|---------|
| 代码复杂度 | 中等 | 高 | 低 |
| 功能丰富度 | 完整 | 最丰富 | 精简 |
| 系统托盘 | ✅ | ✅ | ❌ |
| 设置窗口 | ✅ | ✅ | ❌ |
| 剪贴板监控 | ✅ | ✅ | ❌ |
| 录屏功能 | ❌ | ✅ | ❌ |
| 歌词显示 | ❌ | ✅ | ❌ |
| 国际化 | ❌ | ✅ | ❌ |

## 适用人群

- 喜欢简洁界面的用户
- 追求轻量级实现的用户
- 想要学习项目代码的开发者

## 注意事项

1. 没有系统托盘图标
2. 没有设置窗口
3. 没有剪贴板 URL 检测功能

## 相关链接

- [GitHub 仓库](https://github.com/Python-island/Python-island/tree/harmony)
