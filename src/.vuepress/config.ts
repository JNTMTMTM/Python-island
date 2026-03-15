import { defineUserConfig } from "vuepress";

import theme from "./theme.js";

export default defineUserConfig({
  base: "/",

  lang: "zh-CN",
  title: "Pyisland 文档站",
  description: "Python island 文档站",

  theme,

  // 和 PWA 一起启用
  // shouldPrefetch: false,
});
