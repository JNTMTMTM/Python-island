---
title: tauri-island
icon: star
order: 2
---

# tauri-island

这是 Pyisland 项目的 **全新重构版本**，基于 Tauri 2 和 Rust 构建，提供更强大的性能和更好的用户体验。

::: tip
这是唯一一个非 Python 实现的分支，展示了项目向更现代技术栈的演进。
:::

## 技术栈

- **Tauri 2**: 下一代桌面应用框架
- **Rust**: 高性能系统编程语言
- **TypeScript**: 前端开发
- **Vite**: 构建工具
- **Windows API**: 系统功能调用

## 功能列表

### 核心功能

- ✅ 胶囊状悬浮窗设计
- ✅ 实时时间显示
- ✅ 鼠标悬浮展开/移开收缩
- ✅ 系统托盘

### 媒体功能

- ✅ 音乐歌词显示（LRCLIB.net & 网易云）
- ✅ 媒体控制（上一曲/播放/下一曲）
- ✅ SMTC 集成

### 通知功能

- ✅ WiFi 连接/断开通知
- ✅ 蓝牙设备连接通知

### 实用功能

- ✅ 剪贴板链接监控
- ✅ 多链接列表管理
- ✅ 全局快捷键（Alt+O）

## 项目结构

```
tauri-island/
├── src/                    # 前端代码
│   ├── main.ts             # 主界面逻辑
│   ├── styles.css          # 样式文件
│   └── settings.ts         # 设置页逻辑
├── src-tauri/
│   ├── src/
│   │   └── lib.rs          # Rust 后端
│   ├── Cargo.toml
│   └── tauri.conf.json
├── index.html              # 主界面
├── settings.html           # 设置页
└── package.json
```

## 安装运行

```bash
# 克隆并切换分支
git clone https://github.com/Python-island/Python-island.git
cd Python-island
git checkout tauri-island

# 安装依赖
cd tauri-island
npm install

# 开发模式
npx tauri dev

# 构建安装包
npx tauri build
```

## 构建产物

| 类型 | 路径 |
|------|------|
| MSI | `src-tauri/target/release/bundle/msi/DynamicIsland_0.1.0_x64_en-US.msi` |
| NSIS | `src-tauri/target/release/bundle/nsis/DynamicIsland_0.1.0_x64-setup.exe` |

## 适用人群

::: tip
- 追求性能的极客用户
- Rust 爱好者
- 想体验最新技术的开发者
:::

## 特点对比

| 特性 | pyislandPyside6 | tauri-island |
|------|-----------------|--------------|
| 性能 | 较快 | 极快 |
| 安装包大小 | 较大 | 极小 |
| 依赖 | Python | Node.js + Rust |
| 可扩展性 | 高 | 中 |

## 相关链接

- [GitHub 仓库](https://github.com/Python-island/Python-island/tree/tauri-island)
- [Tauri 官网](https://tauri.app/)
