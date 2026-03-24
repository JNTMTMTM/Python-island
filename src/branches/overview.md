---
title: 分支概览
icon: info
order: 1
---

# 分支概览

::: info
Pyisland 项目有多个分支版本，采用不同的技术栈实现，以满足不同用户的需求。
:::

## 分支对比

| 分支 | 技术栈 | 特点 | 适用场景 |
|------|--------|------|----------|
| [pyislandPyside6](./pyislandPyside6.md) | Python + PySide6 | 功能完整，稳定可靠 | 日常使用 |
| [pyislandQT](./pyislandQT.md) | Python + PyQt5 | 事件驱动，轻量高效 | 轻量使用 |
| [tauri-island](./tauri-island.md) | Rust + Tauri 2 | 性能更强，新技术 | 追求性能 |
| [pyisland-wanku](./pyisland-wanku.md) | Python + PySide6 | 高仿真 iOS，功能丰富 | 追求美观 |

## 如何选择

### 选择 pyislandPyside6 如果...

::: tip 稳定优先
- 你需要一个稳定、功能完整的版本
- 你想自定义和扩展功能
- 你熟悉 Python/PySide6
:::

### 选择 pyislandQT 如果...

::: tip 轻量优先
- 你追求轻量级实现和低资源占用
- 你喜欢事件驱动架构
- 你需要稳定可靠的灵动岛基础功能
- 你熟悉 Python/PyQt5
:::

### 选择 tauri-island 如果...

::: tip 性能优先
- 你追求更好的性能和响应速度
- 你想体验 Tauri 2 和 Rust 技术
- 你需要更小的安装包体积
:::

### 选择 pyisland-wanku 如果...

::: tip 颜值优先
- 你追求高仿真 iOS 灵动岛外观
- 你需要录屏功能
- 你需要媒体控制和歌词显示
- 你喜欢毛玻璃效果和多巴胺配色
:::

## 分支关系

```
                    ┌─────────────────────┐
                    │   初始版本 (废弃)    │
                    └──────────┬──────────┘
                               │
           ┌───────────────────┼───────────────────┐
           │                   │                   │
           ▼                   ▼                   ▼
┌──────────────────┐  ┌─────────────┐  ┌──────────────────┐
│ pyislandPyside6  │  │ pyislandQT  │  │ pyislandGemini   │
│ (PySide6 稳定版) │  │ (PyQt5 轻量版)│  │   (废弃)         │
└────────┬─────────┘  └──────┬──────┘  └──────────────────┘
         │                   │
         │                   │
         ▼                   ▼
┌──────────────────┐  ┌──────────────────┐
│  pyisland-wanku  │  │   tauri-island   │
│ (高仿真 iOS 版)   │  │  (Rust 重写版)   │
└──────────────────┘  └──────────────────┘
```

## 查看特定分支

要查看特定分支的内容：

```bash
# 切换到指定分支
git checkout <branch-name>

# 查看远程分支
git fetch origin
git checkout -b <branch-name> origin/<branch-name>
```

## 贡献分支

::: tip 贡献指南
如果你想为项目贡献新功能，建议：
1. 基于 `pyislandPyside6` 或 `pyislandQT` 分支创建新分支
2. 实现你的功能
3. 提交 Pull Request
:::
