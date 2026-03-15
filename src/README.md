---
home: true
icon: home
title: Pyisland 灵动岛
heroImage: /island_c.svg
bgImage: https://theme-hope-assets.vuejs.press/bg/6-light.svg
bgImageDark: https://theme-hope-assets.vuejs.press/bg/6-dark.svg
bgImageStyle:
  background-attachment: fixed
heroText: Pyisland
tagline: 用 Python 开发，运行在 Windows 上的现代灵动岛控制中心
actions:
  - text: 快速开始
    icon: rocket
    link: /guide/getting-started
    type: primary
  - text: 功能介绍
    icon: lightbulb
    link: /guide/features

highlights:
  - header: 什么是 Pyisland?
    image: /assets/image/box.svg
    bgImage: https://theme-hope-assets.vuejs.press/bg/3-light.svg
    bgImageDark: https://theme-hope-assets.vuejs.press/bg/3-dark.svg
    highlights:
      - title: 仿 macOS 灵动岛设计
        icon: mobile-screen
        details: 采用现代胶囊形状设计，为 Windows 带来 iOS 风格的灵动体验

      - title: 多种技术实现
        icon: code
        details: 提供 PySide6 (Python) 和 Tauri 2 (Rust) 两种技术版本

      - title: 丰富的系统集成
        icon: gauge-high
        details: 集成亮度/音量控制、系统状态监控、剪贴板监控等实用功能

  - header: 核心功能
    image: /assets/image/markdown.svg
    bgImage: https://theme-hope-assets.vuejs.press/bg/2-light.svg
    bgImageDark: https://theme-hope-assets.vuejs.press/bg/2-dark.svg
    features:
      - title: 智能展开/收起
        icon: arrows-up-down
        details: 点击展开显示控制面板，失去焦点自动收缩

      - title: 亮度调节
        icon: sun
        details: 滑动条调节系统亮度，支持防抖机制

      - title: 音量控制
        icon: volume-high
        details: 实时调节系统音量

      - title: 系统状态监控
        icon: network-wired
        details: 实时显示 WiFi、蓝牙、电池状态

      - title: 剪贴板监控
        icon: clipboard
        details: 自动检测剪贴板中的 URL 并提供快捷打开选项

      - title: 鼠标拖动
        icon: hand
        details: 支持鼠标拖动调整灵动岛位置

  - header: 多种分支版本
    image: /assets/image/ui.svg
    bgImage: https://theme-hope-assets.vuejs.press/bg/5-light.svg
    bgImageDark: https://theme-hope-assets.vuejs.press/bg/5-dark.svg
    highlights:
      - title: pyislandPyside6
        icon: python
        details: 基于 PySide6 的 Python 实现，稳定可靠

      - title: tauri-island
        icon: rust
        details: 基于 Tauri 2 + Rust 的全新实现，性能更强

      - title: pyisland-wanku
        icon: star
        details: 高仿真 iOS 风格版本，支持录屏、媒体控制

      - title: harmony
        icon: layer-group
        details: 精简版实现，占用小，功能实用

  - header: 技术栈
    image: /assets/image/features.svg
    bgImage: https://theme-hope-assets.vuejs.press/bg/1-light.svg
    bgImageDark: https://theme-hope-assets.vuejs.press/bg/1-dark.svg
    features:
      - title: PySide6
        icon: python
        details: Qt 的 Python 绑定，强大的 GUI 框架

      - title: Tauri 2
        icon: rust
        details: Rust 构建的轻量级应用框架

      - title: Windows API
        icon: windows
        details: 调用系统底层 API 实现硬件控制

      - title: QSS 样式
        icon: paintbrush
        details: Qt Style Sheets 定制现代化 UI

copyright: false
footer: MIT 许可证 | 版权所有 © 2024 Python-island
---

# Pyisland

**Pyisland** 是一个用 Python 开发，可以运行在 Windows 上的灵动岛（Dynamic Island）项目。它仿照 macOS 的灵动岛设计，为 Windows 用户带来类似的交互体验。

## 快速导航

- **[使用指南](/guide/getting-started)** - 安装和运行项目
- **[功能介绍](/guide/features)** - 详细功能说明
- **[开发指南](/develop/architecture)** - 开发架构和代码说明
- **[分支版本](/branches/overview)** - 了解各分支差异

## 支持的平台

::: info
目前仅支持 **Windows 10/11** 系统，因为使用了 Windows 特定的 API 调用。
:::

## 开源协议

本项目采用 [MIT 许可证](https://opensource.org/licenses/MIT)。
