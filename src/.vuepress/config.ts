import { defineUserConfig } from "vuepress";

import theme from "./theme.js";

export default defineUserConfig({
  base: "/",

  lang: "zh-CN",
  title: "Pyisland 文档站",
  description: "用 Python 开发，运行在 Windows 上的灵动岛控制中心",

  theme,

  // PWA 支持（可选）
  // shouldPrefetch: false,
});
