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

::: info
请选择适合您的版本进行下载。每个版本都有其独特的特点，请根据您的需求选择。
:::

<div class="version-grid">

<div class="version-card">
<span class="version-tag tag-stable">稳定版</span>

### pyislandPyside6

基于 Python + PySide6 构建的成熟稳定版本

**核心特性**

- 功能完整，经过充分测试验证
- 适合日常使用场景
- 易于自定义和二次开发
- 社区支持完善，文档齐全

**适用人群**

追求稳定可靠的用户

[:fontawesome-solid-star: 查看详情](/branches/pyislandPyside6)
</div>

<div class="version-card">
<span class="version-tag tag-featured">美化版</span>

### pyisland-wanku

高仿真 iOS 灵动岛体验

**核心特性**

- 极致仿真 iOS 灵动岛外观
- 支持录屏功能
- 媒体控制和歌词显示
- 毛玻璃效果和多巴胺配色

**适用人群**

追求高颜值和丰富功能的用户

[:fontawesome-solid-sparkles: 查看详情](/branches/pyisland-wanku)
</div>

<div class="version-card">
<span class="version-tag tag-perf">高性能</span>

### tauri-island

基于 Tauri 2 + Rust 的全新实现

**核心特性**

- 性能更强，响应更迅速
- 安装包体积更小
- 原生系统集成度高
- 更低的资源占用

**适用人群**

追求性能和轻量化的用户

[:fontawesome-solid-bolt: 查看详情](/branches/tauri-island)
</div>

</div>

::: tip 系统要求
- Windows 10/11 (64位)
- Python 3.8+ (仅限 Python 版本)
- 管理员权限（首次运行）
:::

::: warning 注意事项
- 部分安全软件可能会误报，请添加信任
- 首次运行需要安装依赖，可能需要较长时间
- 建议关闭杀毒软件后再安装
:::

::: info 获取帮助
如果您在使用过程中遇到问题，可以通过以下方式获取帮助：
1. 查看 [文档](/branches/overview)
2. 提交 [Issue](https://github.com/Python-island/Python-island/issues)
3. 加入交流群讨论
:::

<style>
.version-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.version-card {
  position: relative;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  border-radius: 16px;
  padding: 1.5rem;
  padding-top: 2.5rem;
  transition: all 0.3s ease;
}

.version-card:hover {
  border-color: var(--vp-c-brand-1);
  transform: translateY(-4px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.version-tag {
  position: absolute;
  top: 1rem;
  right: 1rem;
  font-size: 0.7rem;
  padding: 0.25rem 0.6rem;
  border-radius: 20px;
  font-weight: 500;
}

.tag-stable {
  background: #3b82f6;
  color: white;
}

.tag-featured {
  background: linear-gradient(135deg, #f59e0b, #ec4899);
  color: white;
}

.tag-perf {
  background: linear-gradient(135deg, #8b5cf6, #06b6d4);
  color: white;
}

.tag-light {
  background: #10b981;
  color: white;
}

.version-card h3 {
  margin: 0 0 0.75rem 0;
  font-size: 1.3rem;
  color: var(--vp-c-text-1);
}

.version-card > p {
  margin: 0 0 1rem 0;
  color: var(--vp-c-text-2);
  font-size: 0.95rem;
}

.version-card strong {
  display: block;
  font-size: 0.85rem;
  color: var(--vp-c-text-2);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-top: 1rem;
  margin-bottom: 0.5rem;
}

.version-card ul {
  margin: 0;
  padding-left: 1.2rem;
}

.version-card li {
  margin: 0.35rem 0;
  color: var(--vp-c-text-1);
  font-size: 0.95rem;
}

.version-card a {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--vp-c-brand-1);
  text-decoration: none;
  font-weight: 500;
  margin-top: 1.25rem;
  padding-top: 1rem;
  border-top: 1px solid var(--vp-c-divider);
  transition: color 0.2s;
}

.version-card a:hover {
  color: var(--vp-c-brand-2);
}

@media (max-width: 768px) {
  .version-grid {
    grid-template-columns: 1fr;
  }
}
</style>
