# Search Pro - 自研搜索引擎

多引擎聚合搜索工具，支持 DuckDuckGo、Bing、Google、Tavily。

[English Version](README_EN.md)

---

## ✨ 功能特性

- 🔍 **多引擎聚合** - DuckDuckGo + Bing + Google + Tavily
- 📄 **内容提取** - 自动提取网页正文
- 📊 **结果去重** - 智能去重 + 相关性排序
- 💾 **搜索历史** - 历史记录 + 收藏
- ⚙️ **可配置** - 灵活启用/禁用引擎

---

## 🚀 安装

```bash
cd /root/.openclaw/workspace/skills
git clone https://github.com/williamwg2025/openclaw-search-pro.git search-pro
chmod +x search-pro/scripts/*.py
```

---

## 📖 使用

### 基本搜索

```bash
# 使用默认引擎（DuckDuckGo）
python3 search-pro/scripts/multi-search.py "OpenClaw 技能"

# 使用所有引擎
python3 search-pro/scripts/multi-search.py "OpenClaw 技能" --all-engines

# 指定引擎
python3 search-pro/scripts/multi-search.py "OpenClaw 技能" --engine bing

# 限制结果数
python3 search-pro/scripts/multi-search.py "OpenClaw 技能" --max-results 20
```

---

## ⚙️ 配置引擎

编辑 `config/search-config.json`：

```json
{
  "engines": {
    "duckduckgo": {"enabled": true},
    "bing": {"enabled": true, "apiKey": "YOUR_BING_API_KEY"},
    "google": {"enabled": false, "apiKey": "", "searchEngineId": ""},
    "tavily": {"enabled": false, "apiKey": ""}
  }
}
```

### 获取 API Key

| 引擎 | 获取方式 | 免费额度 |
|------|----------|----------|
| DuckDuckGo | 无需 API Key | 无限 |
| Bing | https://www.microsoft.com/en-us/bing/apis/bing-web-search-api | 1000 次/月 |
| Google | https://developers.google.com/custom-search/v1/overview | 100 次/天 |
| Tavily | https://tavily.com | 1000 次/月 |

---

## 🛠️ 脚本说明

| 脚本 | 功能 |
|------|------|
| `custom_search.py` | 自研搜索引擎核心 |
| `multi-search.py` | 多引擎搜索 |
| `extract.py` | 内容提取 |

---

## 🔍 搜索策略

**默认策略：**
1. DuckDuckGo（首选，免费）
2. Bing（补充，中文好）
3. Google（英文/技术内容）
4. Tavily（AI 优化）

**智能路由：**
- 中文内容 → Bing > DuckDuckGo
- 英文内容 → Google > DuckDuckGo
- 技术文档 → Google > Tavily

---

## 📄 许可证

MIT-0

---

**作者：** @williamwg2025  
**版本：** 1.0.0
