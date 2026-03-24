---
title: pyislandQT
icon: star
order: 1
---

# pyislandQT

::: info
这是 Pyisland 项目的 **纯 PyQt 分支**，基于 Python 和 PyQt5 构建，采用事件驱动架构，提供轻量高效的灵动岛体验。

本分支由 [星灿长风v](https://github.com/StarWindv) 进行开发维护。
:::

## 技术栈

- **Python >= 3.10**
- **PyQt5**: Qt 的 Python 绑定
- **asyncio**: 异步事件循环
- **[windows-bluetooth-watcher](https://github.com/starwindv/windows-bluetooth-watcher)**: 由 rust 提供支持的高性能蓝牙连通监听库

## 功能列表

### 核心功能

- ✅ 灵动岛胶囊形态设计
- ✅ 实时时间显示
- ✅ 鼠标悬停展开 / 移开收缩
- ✅ DebugServer 调试服务器

### 系统控制（托盘菜单）

- ✅ 置顶窗口
- ✅ 点击穿透
- ✅ 位置锁定
- ✅ 防抖机制
- ✅ 系统托盘

### 系统监控

- ✅ WiFi / 网络状态监控
- ✅ 蓝牙设备连接监控

### 通知功能

- ✅ 网络连接 / 断开通知（动画展示）
- ✅ 蓝牙设备连接 / 断开通知（动画展示）

### 实用功能

- ✅ 全局截图快捷键 ( ctrl+shift+z)

## 项目结构

```
PyIsland
├── __init__.py
├── Configure.py
├── Debugger
│   └── server.py
├── Display
│   ├── Container.py
│   └── Island.py
├── EventBus
│   ├── Bus.py
│   └── EventDefine.py
├── instance.py
├── main.py
├── Monitor
│   ├── BlueToothMonitor.py
│   ├── KeyBoardMonitor.py
│   ├── Monitor.py
│   └── NetworkMonitor.py
└── Pluging
    ├── __init__.py
    └── Screenshot.py
```

## 事件驱动模型

程序基于**事件总线**进行模块间通信，实现松耦合设计：

1. **事件定义**: `EventCode` 枚举定义所有事件类型（网络恢复、蓝牙连接、鼠标悬停等）
2. **事件发布**: 任何模块可调用 `event_manager.publish(event_code, data)` 触发事件
3. **事件订阅**: 模块通过 `subscribe(event_code, callback)` 注册回调函数
4. **队列处理**: 事件进入队列，由定时器驱动串行处理，避免界面卡顿

```python
# Monitor 检测到网络恢复 -> 发布事件
event_manager.publish(EventCode.NETWORK_RESTORE)

# Island 已订阅该事件 -> 回调触发
self._handle_notification(event_data) -> show_notification()
```

## 配置管理

- **单例模式**: `ConfigManager` 确保全局唯一配置实例
- **配置文件**: 存储在 `~/.island.config`（JSON 格式）
- **默认配置**: 内置默认值，自动创建 / 补全缺失配置项
- **动态属性**: 配置项直接作为类属性访问（如 `CONFIG_MANAGER.ISLAND_INIT_WIDTH`）

## 动画系统

基于 PyQt5 的属性动画框架实现流畅过渡：

| 动画类型 | 实现方式 |
|---------|---------|
| 大小动画 | `QPropertyAnimation` 控制窗口几何尺寸 |
| 圆角动画 | 自定义 `radius` 属性实现胶囊圆角变化 |
| 字体动画 | `content_font_size` 属性控制文字大小平滑过渡 |
| 透明度动画 | 控制内容标签的淡入淡出 |
| 缓动曲线 | `QEasingCurve.OutBack` 实现弹性效果 |

## 监控系统

- **异步监控线程**: 继承 `QThread` 并集成 `asyncio` 事件循环
- **网络监控**: 通过异步 DNS 查询检测网络连通性
- **蓝牙监控**: 使用rust编写的高性能库来注册蓝牙事件回调
- **配置化间隔**: 监控间隔通过配置文件动态调整

## 安装运行

### 方式一：pip 安装

```bash
git clone https://github.com/starwindv/PyIsland.git
cd PyIsland
pip install .
```

### 方式二：直接克隆

```bash
git clone https://github.com/Python-island/Python-island.git
cd Python-island
git checkout pyislandQT
pip install .
```

### 运行程序

#### 唤醒服务（普通模式）

```powershell
PS:Path> _island_instance
```

#### 守护进程模式（后台运行，无多余窗口）

```powershell
PS:Path> island
```

::: tip 托盘功能
运行后程序会在系统托盘显示图标，支持以下操作：

- **置顶窗口**（默认关闭）
- **点击穿透**（默认关闭）
- **位置锁定**（默认关闭）
- **测试网络通知**（用于动画测试）
- **测试蓝牙通知**（用于动画测试）
- **退出程序**
:::

## 适用人群

::: tip
- 需要稳定版本的日常用户
- 追求低资源占用的用户
- 想要轻量化实现的开发者
- Python / PyQt5 学习者
:::

## 相关链接

- [GitHub 仓库（Python-island）](https://github.com/Python-island/Python-island/tree/pyislandQT)
- [GitHub 仓库（StarWindv/PyIsland）](https://github.com/starwindv/PyIsland)
