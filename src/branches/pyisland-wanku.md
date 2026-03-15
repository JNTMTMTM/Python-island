---
title: pyisland-wanku
icon: star
order: 3
---

# pyisland-wanku

::: info
这是 Pyisland 项目的 **高仿真 iOS 风格版本**，基于 Python 和 PySide6 构建，完美还原了 iOS 17+ 灵动岛的设计美学。
:::

## 技术栈

- **Python 3.8+**
- **PySide6**: Qt 的 Python 绑定
- **winsdk**: Windows SDK 绑定
- **psutil**: 系统信息获取
- **opencv-python + mss**: 录屏功能
- **pyperclip + keyboard**: 剪贴板和全局热键

## 功能列表

### 核心功能

- ✅ 智能鼠标穿透（默认完全穿透，不干扰桌面操作）
- ✅ 多态吸附（支持上/左/右侧吸附）
- ✅ 自动形态切换（顶部横向，侧边纵向）
- ✅ 32px 超大圆角设计
- ✅ 实时时间显示（中文日期/星期格式）

### 视觉效果

- ✅ 毛玻璃效果（Windows Acrylic/Fluent 模糊）
- ✅ 多巴胺配色系统（#FF6B6B 珊瑚红、#4ECDC4 蒂芙尼蓝、#FFE66D 明黄）
- ✅ Segoe UI Variable 字体系统

### 媒体功能

- ✅ SMTC 音乐识别（支持 Spotify、网易云等）
- ✅ 歌曲信息显示（歌名/艺术家）
- ✅ Apple Music 风格控制按钮
- ✅ 音乐可视化动画（实时频谱）

### 系统控制

- ✅ 音量调节（渐变滑块）
- ✅ 亮度调节（渐变滑块）
- ✅ 电池状态监控
- ✅ WiFi/蓝牙状态监控

### 实用功能

- ✅ 剪贴板链接监控
- ✅ 全局热键（Alt+O）
- ✅ 链接打开反馈提示

### 特色功能

::: info 完整录屏系统
- 一键捕获屏幕
- 自动保存为 MP4
- iOS 风格按钮设计
- 实时录制计时器
- 呼吸感红点提示
:::

::: info 国际化支持
- 中文 (zh)
- 英文 (en)
:::

## 界面预览

### 配色方案

| 颜色 | 值 | 用途 |
|------|-----|------|
| 珊瑚红 | #FF6B6B | 主色 |
| 蒂芙尼蓝 | #4ECDC4 | 辅色 |
| 明黄 | #FFE66D | 点缀色 |

### 滑块渐变

音量与亮度滑块采用 **蓝-粉-绿** 三色梦幻渐变填充。

## 项目结构

```
pyisland-wanku/
├── app/
│   ├── core/              # 核心模块
│   ├── ui/                # UI 组件
│   ├── services/         # 服务模块
│   └── animations/       # 动画
├── resources/
│   ├── icons/            # 图标资源
│   └── styles/          # 样式文件
├── dynamic_island.py    # 主程序
├── requirements.txt     # 依赖列表
└── video/               # 录屏保存目录
```

## 安装运行

```bash
# 克隆并切换分支
git clone https://github.com/Python-island/Python-island.git
cd Python-island
git checkout pyisland-wanku

# 安装依赖
pip install -r requirements.txt

# 运行
python dynamic_island.py
```

## 核心依赖

::: details 点击展开
```txt
PySide6
psutil
winsdk
pycaw
screen-brightness-control
opencv-python
mss
numpy
pyperclip
keyboard
```
:::

## 适用人群

::: tip
- 追求 iOS 灵动岛外观的用户
- 需要录屏功能的用户
- 喜欢毛玻璃和现代化设计的用户
:::

## 更新日志

### V1.7 (最新)

- 媒体识别增强
- 链接打开提示优化

### V1.6

- 音乐控制面板重构
- 录屏模块美化
- 系统图标升级为 iOS 风格

### V1.5

- 引入多巴胺配色
- 32px 全局圆角
- 录屏反馈增强

### V1.4

- 录屏功能上线
- 国际化支持

### V1.3

- 音乐模式动态扩展
- 蓝牙设备监控
- 毛玻璃背景

## 相关链接

- [GitHub 仓库](https://github.com/Python-island/Python-island/tree/pyisland-wanku)
