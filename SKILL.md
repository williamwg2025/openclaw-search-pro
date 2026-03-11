---
name: search-pro
displayName: Search Pro
version: 1.0.0
description: 搜索增强工具，支持多引擎聚合搜索、内容提取、结果去重。让搜索更准确、更全面。
license: MIT-0
acceptLicenseTerms: true
tags: search, web, research, productivity
---

# Search Pro - 搜索增强工具

强大的多引擎搜索工具，让搜索更准确、更全面。

---

## ✨ 功能特性

- 🔍 **多引擎聚合** - Tavily + Bing + Google
- 📄 **内容提取** - URL/PDF/文档内容提取
- 📊 **结果去重** - 智能去重 + 排序
- 💾 **搜索历史** - 历史记录 + 收藏
- 📈 **质量分析** - 搜索质量评估

---

## 🚀 安装

```bash
cd /root/.openclaw/workspace/skills
git clone https://github.com/williamwg2025/openclaw-search-pro.git search-pro
chmod +x search-pro/scripts/*.py
```

---

## 📖 使用

### 多引擎搜索

```bash
python3 search-pro/scripts/multi-search.py "OpenClaw 技能开发"
```

### 内容提取

```bash
python3 search-pro/scripts/extract.py --url https://example.com
```

---

## 🛠️ 脚本

| 脚本 | 功能 |
|------|------|
| `multi-search.py` | 多引擎搜索 |
| `extract.py` | 内容提取 |
| `history.py` | 搜索历史 |

---

**作者：** @williamwg2025  
**版本：** 1.0.0
