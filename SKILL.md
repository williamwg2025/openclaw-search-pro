---
name: search-pro
displayName: Search Pro
version: 1.0.2
description: 搜索增强工具，支持多引擎聚合搜索、内容提取、结果去重。需要联网访问搜索引擎 API。所有文件存储在 skills/search-pro/ 目录。
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

| 脚本 | 功能 | 网络访问 | 文件写入 |
|------|------|---------|---------|
| `multi-search.py` | 多引擎搜索 | ✅ 是 | ❌ 否 |
| `free_search.py` | 免费搜索引擎 | ✅ 是 | ❌ 否 |
| `baidu_search.py` | 百度搜索 | ✅ 是 | ❌ 否 |
| `extract.py` | 内容提取 | ✅ 是 | ❌ 否 |

**注意：** 搜索历史功能需要手动实现，当前版本不自动保存历史

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
**路径说明：** 所有文件存储在 `~/.openclaw/workspace/skills/search-pro/`

- **读取：**
  - `config/search-config.json` - 搜索配置（可选）
  - `config/api-keys.json` - API 密钥（可选）
- **写入：**
  - 当前版本不自动写入文件
  - 搜索结果输出到命令行
- **extract.py 限制：**
  - ✅ 仅提取网页内容
  - ✅ 不读取本地文件
  - ✅ 不访问内网地址（完整检查 HTTP 和 HTTPS）

### 数据安全
- **不上传：** 不上传用户配置文件或敏感数据
- **搜索查询：** 会发送到配置的搜索引擎（百度、必应等），这是搜索功能的必要条件
- **API 密钥：** 存储在本地配置文件，不发送到除 API 提供商外的第三方

### API 密钥（可选）
**免费搜索：** 无需 API Key，直接使用

**可选 API 配置：**
```bash
# 方法 1: 环境变量
export TAVILY_API_KEY="your-key"

# 方法 2: 配置文件（推荐）
# 编辑 config/search-config.json
{
  "tavily": {
    "api_key": "your-key"
  }
}
```

**安全建议：**
- 配置文件权限：`chmod 600 config/search-config.json`
- 不要将 API Key 提交到 Git
- 使用环境变量更安全（不写入文件）

---

**作者：** @williamwg2025  
**版本：** 1.0.1  
**许可证：** MIT-0
