---
title: pyislandPyside6
icon: star
order: 1
---

# pyislandPyside6

::: info
这是 Pyisland 项目的 **稳定版**，基于 Python 和 PySide6 构建，提供了完整的灵动岛功能。
:::

## 技术栈

- **Python 3.11+**
- **PySide6**: Qt 的 Python 绑定
- **QSS**: 界面样式定制
- **Windows API**: 系统功能调用

## 功能列表

### 核心功能

- ✅ 灵动岛胶囊形态设计
- ✅ 实时时间显示
- ✅ 点击展开/收起控制面板
- ✅ 鼠标拖动位置
- ✅ 自动收缩（失去焦点）

### 系统控制

- ✅ 亮度调节（滑动条）
- ✅ 防抖机制
- ✅ 系统托盘
- ✅ 设置窗口

### 系统监控

- ✅ WiFi 状态显示
- ✅ 蓝牙状态显示
- ✅ 电池状态显示

### 实用功能

- ✅ 剪贴板 URL 检测
- ✅ 快捷打开链接

## 项目结构

```
pyislandPyside6/
├── app/
│   ├── core/              # 核心模块
│   │   ├── config.py      # 配置常量
│   │   ├── icons.py      # 图标枚举
│   │   └── worker.py     # 后台线程
│   ├── ui/                # UI 组件
│   │   ├── controls.py    # 控制面板
│   │   ├── status_bar.py # 状态栏
│   │   ├── url_dialog.py # URL 对话框
│   │   └── settings.py   # 设置窗口
│   ├── services/         # 服务模块
│   │   ├── brightness.py # 亮度服务
│   │   ├── clipboard.py  # 剪贴板服务
│   │   ├── system_status.py # 系统状态
│   │   └── tray.py       # 托盘服务
│   ├── animations/       # 动画效果
│   │   └── effects.py
│   └── island.py         # 主窗口
├── resources/
│   ├── icons/            # 图标资源
│   └── styles/           # 样式文件
├── main.py               # 入口文件
└── requirements.txt      # 依赖列表
```

## 安装运行

```bash
# 克隆并切换分支
git clone https://github.com/Python-island/Python-island.git
cd Python-island
git checkout pyislandPyside6

# 安装依赖
pip install -r requirements.txt

# 运行
python main.py
```

## 适用人群

::: tip
- 需要稳定版本的日常用户
- 想要自定义功能的开发者
- Python 学习者
:::

## 相关链接

- [GitHub 仓库](https://github.com/Python-island/Python-island/tree/pyislandPyside6)
