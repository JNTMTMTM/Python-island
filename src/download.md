---
home: true
icon: home
title: Pyisland 灵动岛
heroImage: /island_c.svg
heroText: 立即下载 Pyisland
tagline: 根据需求选择适合您的 Pyisland 版本
actions:
  - text: pyislandPyside6
    icon: download
    link: /download
  - text: pyisland-wanku
    icon: download
    link: /guide/getting-started
  - text: tauri-island
    icon: download
    link: /guide/features
---

---

<div class="download-container">

## pyislandPyside6

**稳定可靠版**

- 基于 Python + PySide6
- 功能完整，经过充分测试
- 适合日常使用
- 易于自定义和扩展


---

## pyisland-wanku

**高仿真 iOS 版**

- 高仿真 iOS 灵动岛外观
- 支持录屏功能
- 媒体控制和歌词显示
- 毛玻璃效果和多巴胺配色


---

## tauri-island

**高性能版**

- 基于 Tauri 2 + Rust
- 性能更强，响应更快
- 安装包体积更小
- 追求极致体验


---

</div>


::: tip 系统要求
- Windows 10/11 (64位)
:::

::: warning 注意事项
- 部分安全软件可能会误报，请添加信任
- 首次运行需要安装依赖，可能需要较长时间
- 建议关闭杀毒软件后再安装
:::

::: info
如果您在使用过程中遇到问题，可以通过以下方式获取帮助：
1. 查看 [文档](/branches/overview)
2. 提交 [Issue](https://github.com/Python-island/Python-island/issues)
3. 加入交流群讨论
:::

---

<style>
.download-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
  padding: 1rem;
  background: var(--vp-c-bg-soft);
  border-radius: 12px;
}

.download-container h2 {
  grid-column: 1 / -1;
  color: var(--vp-c-brand-1);
  margin: 0;
  padding: 0;
  font-size: 1.5rem;
  border: none;
}

.download-container hr {
  display: none;
}

.download-container h3 {
  color: var(--vp-c-brand-1);
  margin: 0 0 0.5rem 0;
  font-size: 1.25rem;
}

.download-container p {
  margin: 0.25rem 0;
}

.download-container ul {
  margin: 0.75rem 0;
  padding-left: 1.25rem;
}

.download-container li {
  margin: 0.25rem 0;
  color: var(--vp-c-text-1);
}

.download-container strong {
  color: var(--vp-c-text-2);
}

@media (max-width: 768px) {
  .download-container {
    grid-template-columns: 1fr;
  }
}
</style>
