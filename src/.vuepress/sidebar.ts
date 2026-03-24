import { sidebar } from "vuepress-theme-hope";

export default sidebar({
  "/guide/": [
    {
      text: "使用指南",
      icon: "book",
      children: [
        "/guide/getting-started.md",
        "/guide/features.md",
      ],
    },
  ],
  "/develop/": [
    {
      text: "开发指南",
      icon: "code",
      children: [
        "/develop/architecture.md",
        "/develop/contribution.md",
      ],
    },
  ],
  "/branches/": [
    {
      text: "分支版本",
      icon: "code-branch",
      children: [
        "/branches/overview.md",
        "/branches/pyislandPyside6.md",
        "/branches/pyislandQT.md",
        "/branches/tauri-island.md",
        "/branches/pyisland-wanku.md"
      ],
    },
  ],
});
