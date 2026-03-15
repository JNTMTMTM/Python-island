---
title: 分支概览
icon: code-branch
order: 1
---

# 分支概览

Pyisland 项目有多个分支版本，采用不同的技术栈实现，以满足不同用户的需求。

## 分支对比

| 分支 | 技术栈 | 特点 | 适用场景 |
|------|--------|------|----------|
| [pyislandPyside6](./pyislandPyside6.md) | Python + PySide6 | 功能完整，稳定可靠 | 日常使用 |
| [tauri-island](./tauri-island.md) | Rust + Tauri 2 | 性能更强，新技术 | 追求性能 |
| [pyisland-wanku](./pyisland-wanku.md) | Python + PySide6 | 高仿真 iOS，功能丰富 | 追求美观 |
| [harmony](./harmony.md) | Python + PySide6 | 精简实现，占用小 | 轻量使用 |

## 如何选择

### 选择 pyislandPyside6 如果...

- 你需要一个稳定、功能完整的版本
- 你想自定义和扩展功能
- 你熟悉 Python/PySide6

### 选择 tauri-island 如果...

- 你追求更好的性能和响应速度
- 你想体验 Tauri 2 和 Rust 技术
- 你需要更小的安装包体积

### 选择 pyisland-wanku 如果...

- 你追求高仿真 iOS 灵动岛外观
- 你需要录屏功能
- 你需要媒体控制和歌词显示
- 你喜欢毛玻璃效果和多巴胺配色

### 选择 harmony 如果...

- 你追求轻量级实现
- 你不需要太多高级功能
- 你喜欢简洁的界面

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
│ pyislandPyside6  │  │   harmony   │  │ pyislandGemini   │
│ (PySide6 稳定版) │  │  (精简版)   │  │   (废弃)         │
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

如果你想为项目贡献新功能，建议：

1. 基于 `pyislandPyside6` 分支创建新分支
2. 实现你的功能
3. 提交 Pull Request
