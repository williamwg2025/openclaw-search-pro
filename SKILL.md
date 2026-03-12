---
name: search-pro
displayName: Search Pro
version: 1.0.1
description: 搜索增强工具，支持多引擎聚合搜索、内容提取、结果去重。需要联网访问搜索引擎 API。
license: MIT-0
acceptLicenseTerms: true
tags: search, web, research, productivity, network
---

# Search Pro - 搜索增强工具

强大的多引擎搜索工具，让搜索更准确、更全面。

---

## ✨ 功能特性

- 🔍 **多引擎聚合** - 免费搜索引擎 + 可选 API
- 📄 **内容提取** - URL 内容提取
- 📊 **结果去重** - 智能去重 + 排序
- 💾 **搜索历史** - 历史记录 + 收藏
- 📈 **质量分析** - 搜索质量评估

---

## 🚀 安装

```bash
cd ~/.openclaw/workspace/skills
# 技能已安装在：~/.openclaw/workspace/skills/search-pro
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

| 脚本 | 功能 | 网络访问 |
|------|------|---------|
| `multi-search.py` | 多引擎搜索 | ✅ 是 |
| `free_search.py` | 免费搜索引擎 | ✅ 是 |
| `baidu_search.py` | 百度搜索 | ✅ 是 |
| `extract.py` | 内容提取 | ✅ 是 |
| `history.py` | 搜索历史 | ❌ 否 |

---

## 🔒 安全说明

### 网络访问 ⚠️
**本技能需要联网访问外部服务：**
- 免费搜索引擎（360、搜狗等）
- 百度搜索引擎
- 可选：Tavily API（需配置 API Key）

**网络权限：**
- 出站 HTTPS 请求（443 端口）
- 不监听任何端口
- 不运行服务器

### 文件访问
- **读取：** 仅限 `~/.openclaw/workspace/search-pro/` 目录
- **写入：** 搜索历史保存到 `~/.openclaw/workspace/search-pro/history/`
- **extract.py 限制：** 仅提取网页内容，不读取本地文件

### 数据安全
- **不上传：** 不上传用户配置文件或敏感数据
- **不存储：** 搜索查询不存储到外部服务器
- **本地历史：** 搜索历史仅保存在本地

### API 密钥（可选）
如使用 Tavily API：
```bash
# 配置 API Key（可选）
export TAVILY_API_KEY="your-key"
```

---

**作者：** @williamwg2025  
**版本：** 1.0.1  
**许可证：** MIT-0
