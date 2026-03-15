---
title: 项目架构
icon: sitemap
order: 1
---

# 项目架构

本文档介绍 Pyisland 项目的整体架构设计和代码组织结构。

## 技术选型

### Python 版本 (PySide6 分支)

- **GUI 框架**: PySide6 - Qt 的 Python 绑定
- **样式系统**: QSS (Qt Style Sheets)
- **系统调用**: PowerShell、ctypes、Windows API

### Rust 版本 (Tauri 分支)

- **应用框架**: Tauri 2
- **后端语言**: Rust
- **前端技术**: TypeScript + Vite

## 目录结构

### PySide6 分支结构

```
Python-island/
├── app/                      # 主应用代码
│   ├── __init__.py           # 包初始化
│   ├── island.py             # 主窗口，整合所有模块
│   ├── utils.py              # 工具函数
│   ├── core/                 # 核心功能模块
│   │   ├── worker.py         # 后台工作线程
│   │   ├── config.py         # 配置常量
│   │   └── icons.py          # 图标枚举类
│   ├── ui/                   # UI 组件模块
│   │   ├── controls.py       # 控制面板组件
│   │   ├── status_bar.py     # 状态栏组件
│   │   ├── url_dialog.py     # URL 检测对话框
│   │   └── settings.py       # 设置窗口
│   ├── services/             # 服务模块
│   │   ├── clipboard.py      # 剪贴板服务
│   │   ├── system_status.py  # 系统状态服务
│   │   ├── brightness.py     # 亮度控制服务
│   │   └── tray.py           # 托盘服务
│   └── animations/           # 动画效果模块
│       └── effects.py        # 展开/收起动画
├── resources/                # 资源文件
│   ├── icons/                # 图标资源
│   │   ├── controls/         # 控制图标
│   │   └── system/          # 系统状态图标
│   └── styles/               # 样式文件
│       └── style.qss         # QSS 样式
├── main.py                   # 应用入口
└── requirements.txt          # 依赖列表
```

### Tauri 分支结构

```
tauri-island/
├── src/                      # 前端代码
│   ├── main.ts               # 主界面逻辑
│   ├── styles.css            # 样式
│   └── settings.ts           # 设置页逻辑
├── src-tauri/
│   └── src/
│       └── lib.rs            # Rust 后端
├── index.html                # 主界面
└── settings.html             # 设置页
```

## 模块说明

### 核心模块 (core/)

| 模块 | 说明 |
|------|------|
| `worker.py` | 后台工作线程，执行耗时操作 |
| `config.py` | 配置常量，包括尺寸、时间间隔等 |
| `icons.py` | 图标枚举类，统一管理图标资源 |

### UI 模块 (ui/)

| 模块 | 说明 |
|------|------|
| `controls.py` | 控制面板组件，包含亮度/音量滑块 |
| `status_bar.py` | 状态栏组件，显示 WiFi/蓝牙/电池状态 |
| `url_dialog.py` | URL 检测对话框，处理剪贴板 URL |
| `settings.py` | 设置窗口，应用配置界面 |

### 服务模块 (services/)

| 模块 | 说明 |
|------|------|
| `clipboard.py` | 剪贴板服务，URL 检测和打开 |
| `system_status.py` | 系统状态服务，获取 WiFi/蓝牙/电池信息 |
| `brightness.py` | 亮度控制服务，获取和设置系统亮度 |
| `tray.py` | 托盘服务，系统托盘图标和菜单 |

### 动画模块 (animations/)

| 模块 | 说明 |
|------|------|
| `effects.py` | 展开/收起动画效果、圆角遮罩 |

## 数据流

```
用户操作 → UI 组件 (ui/)
         → 服务层 (services/) → Windows API
         → 状态更新 → UI 组件重新渲染
```

## 配置管理

所有配置常量集中在 `app/core/config.py` 文件中：

```python
# 防抖时间（毫秒）
DEBOUNCE_DELAY = 180

# 状态栏更新间隔（毫秒）
STATUS_UPDATE_INTERVAL = 5000

# 窗口尺寸
ISLAND_WIDTH = 300
ISLAND_HEIGHT = 50
```

## 扩展开发

### 添加新功能步骤

1. 在 `app/services/` 目录下创建新的服务类
2. 在 `app/ui/` 目录下创建新的 UI 组件
3. 在 `app/core/config.py` 中添加配置常量
4. 在 `app/island.py` 中整合新模块
5. 在 `resources/styles/style.qss` 中添加相应的样式
