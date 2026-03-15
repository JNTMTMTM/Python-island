import { hopeTheme } from "vuepress-theme-hope";

import navbar from "./navbar.js";
import sidebar from "./sidebar.js";

export default hopeTheme({
  hostname: "https://python-island.github.io",

  author: {
    name: "Pyisland",
    url: "https://github.com/Python-island/Python-island",
  },

  logo: "/island_c.svg",

  repo: "Python-island/Python-island",

  docsDir: "src",

  // 导航栏
  navbar,

  // 侧边栏
  sidebar,

  // 页脚
  footer: "<a href='https://beian.miit.gov.cn/' target='_blank'>苏ICP备...号</a> | <img src='/gabatb.png' alt='公安备案图标' style='height:16px;vertical-align:middle;margin-right:4px;'><a href='https://beian.mps.gov.cn/#/query/webSearch?code=...' target='_blank'>苏公网安备...号</a>",
  displayFooter: true,

  // 多语言配置
  metaLocales: {
    editLink: "在 GitHub 上编辑此页",
  },

  // 启用 Markdown 功能
  markdown: {
    align: true,
    attrs: true,
    codeTabs: true,
    component: true,
    demo: true,
    figure: true,
    gfm: true,
    imgLazyload: true,
    imgSize: true,
    include: true,
    mark: true,
    plantuml: true,
    spoiler: true,
    sub: true,
    sup: true,
    tabs: true,
    tasklist: true,
    vPre: true,
  },

  // 插件配置
  plugins: {
    icon: {
      prefix: "fa6-solid:",
    },
  },
});
