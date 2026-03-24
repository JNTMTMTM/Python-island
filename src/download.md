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
<div class="card-header">
<span class="version-tag tag-stable">稳定版</span>
</div>

<h3 class="card-title">pyislandPyside6</h3>
<p class="card-desc">基于 Python + PySide6 构建的成熟稳定版本</p>

<div class="card-section">
<div class="section-label">
核心特性
</div>
<ul class="feature-list">
<li>功能完整，经过充分测试验证</li>
<li>适合日常使用场景</li>
<li>易于自定义和二次开发</li>
<li>社区支持完善，文档齐全</li>
</ul>
</div>

<div class="card-section">
<div class="section-label">
适用人群
</div>
<p class="target-text">追求稳定可靠的用户</p>
</div>

<button class="download-btn btn-primary" type="button">
立即下载
</button>
</div>

<div class="version-card">
<div class="card-header">
<span class="version-tag tag-featured">美化版</span>
</div>

<h3 class="card-title">pyisland-wanku</h3>
<p class="card-desc">高仿真 iOS 灵动岛体验</p>

<div class="card-section">
<div class="section-label">
核心特性
</div>
<ul class="feature-list">
<li>极致仿真 iOS 灵动岛外观</li>
<li>支持录屏功能</li>
<li>媒体控制和歌词显示</li>
<li>毛玻璃效果和多巴胺配色</li>
</ul>
</div>

<div class="card-section">
<div class="section-label">
适用人群
</div>
<p class="target-text">追求高颜值和丰富功能的用户</p>
</div>

<button class="download-btn btn-featured" type="button">
立即下载
</button>
</div>

<div class="version-card">
<div class="card-header">
<span class="version-tag tag-perf">高性能</span>
</div>

<h3 class="card-title">tauri-island</h3>
<p class="card-desc">基于 Tauri 2 + Rust 的全新实现</p>

<div class="card-section">
<div class="section-label">
核心特性
</div>
<ul class="feature-list">
<li>性能更强，响应更迅速</li>
<li>安装包体积更小</li>
<li>原生系统集成度高</li>
<li>更低的资源占用</li>
</ul>
</div>

<div class="card-section">
<div class="section-label">
适用人群
</div>
<p class="target-text">追求性能和轻量化的用户</p>
</div>

<button class="download-btn btn-perf" type="button">
立即下载
</button>
</div>

</div>

::: tip 系统要求
- Windows 10/11 (64位)
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
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.version-card {
  position: relative;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  border-radius: 16px;
  padding: 1.5rem;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
}

.version-card:hover {
  border-color: var(--vp-c-brand-1);
  transform: translateY(-4px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

/* Card Header */
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 0.75rem;
}

.version-tag {
  font-size: 0.7rem;
  padding: 0.3rem 0.7rem;
  border-radius: 20px;
  font-weight: 600;
  letter-spacing: 0.3px;
}

.tag-stable {
  background: linear-gradient(135deg, #3b82f6, #2563eb);
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

.version-icon {
  font-size: 2rem;
  opacity: 0.2;
}

.card-title {
  margin: 0 0 0.5rem 0;
  font-size: 1.4rem;
  font-weight: 700;
  color: var(--vp-c-text-1);
  line-height: 1.3;
}

.card-desc {
  margin: 0 0 1.25rem 0;
  color: var(--vp-c-text-2);
  font-size: 0.95rem;
  line-height: 1.5;
}

.card-section {
  margin-bottom: 1rem;
}

.section-label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--vp-c-brand-1);
  text-transform: uppercase;
  letter-spacing: 0.8px;
  margin-bottom: 0.75rem;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid var(--vp-c-brand-1);
}

.section-icon {
  font-size: 0.9rem;
}

.feature-list {
  margin: 0;
  padding: 0;
  list-style: none;
}

.feature-list li {
  position: relative;
  padding-left: 1.25rem;
  margin: 0.5rem 0;
  color: var(--vp-c-text-1);
  font-size: 0.95rem;
  line-height: 1.5;
}

.feature-list li::before {
  content: "";
  position: absolute;
  left: 0;
  top: 0.55rem;
  width: 6px;
  height: 6px;
  background: var(--vp-c-brand-1);
  border-radius: 50%;
}

.target-text {
  margin: 0;
  padding: 0.05rem 1rem;  background: var(--vp-c-bg);
  border-radius: 8px;
  color: var(--vp-c-text-2);
  font-size: 0.9rem;
  font-style: italic;
}

/* Buttons */
.download-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  width: 100%;
  padding: 0.85rem 1rem;
  margin-top: auto;
  border: none;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
  font-family: inherit;
  border-radius: 10px;
  transition: all 0.25s ease;
}

.download-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.download-btn:active {
  transform: translateY(0);
}

.fa-download {
  font-size: 1rem;
  transition: transform 0.2s;
}

.download-btn:hover .fa-download {
  transform: translateY(2px);
}

.btn-primary {
  background: linear-gradient(135deg, #3b82f6, #2563eb);
  color: white;
}

.btn-primary:hover {
  background: linear-gradient(135deg, #2563eb, #1d4ed8);
}

.btn-featured {
  background: linear-gradient(135deg, #f59e0b, #ec4899);
  color: white;
}

.btn-featured:hover {
  background: linear-gradient(135deg, #ec4899, #db2777);
}

.btn-perf {
  background: linear-gradient(135deg, #8b5cf6, #06b6d4);
  color: white;
}

.btn-perf:hover {
  background: linear-gradient(135deg, #7c3aed, #0891b2);
}

@media (max-width: 768px) {
  .version-grid {
    grid-template-columns: 1fr;
  }
  
  .version-icon {
    display: none;
  }
}
</style>
