# Search Pro - 自研搜索引擎

多引擎聚合搜索工具，支持百度、Bing、Google、Tavily。

[English Version](README_EN.md)

---

## ✨ 功能特性

- 🔍 **多引擎聚合** - 百度 + Bing + Google + Tavily
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
# 使用百度（默认，中文最好）
python3 search-pro/scripts/multi-search.py "OpenClaw 技能"

# 使用所有引擎
python3 search-pro/scripts/multi-search.py "OpenClaw 技能" --all-engines

# 指定引擎
python3 search-pro/scripts/multi-search.py "OpenClaw 技能" --engine baidu

# 限制结果数
python3 search-pro/scripts/multi-search.py "OpenClaw 技能" --max-results 20
```

---

## ⚙️ 配置引擎

编辑 `config/search-config.json`：

```json
{
  "engines": {
    "baidu": {
      "enabled": true,
      "apiKey": "YOUR_BAIDU_API_KEY",
      "secretKey": "YOUR_BAIDU_SECRET_KEY"
    },
    "bing": {"enabled": false, "apiKey": ""},
    "google": {"enabled": false, "apiKey": "", "searchEngineId": ""},
    "tavily": {"enabled": false, "apiKey": ""}
  }
}
```

---

## 🔑 获取 API Key

### 百度 API（推荐，国内最快）

**步骤：**
1. 访问：https://ai.baidu.com/tech/search
2. 登录百度账号（没有就注册一个）
3. 点击 "控制台" → "创建应用"
4. 填写应用名称，选择 "搜索引擎 API"
5. 获取 **API Key** 和 **Secret Key**

**免费额度：**
- 每日限额：具体额度看官方说明
- 国内访问：速度快，稳定

**配置示例：**
```json
{
  "baidu": {
    "enabled": true,
    "apiKey": "你的 API Key",
    "secretKey": "你的 Secret Key"
  }
}
```

### Bing API（备选）

**获取方式：** https://www.microsoft.com/en-us/bing/apis/bing-web-search-api

**免费额度：** 1000 次/月

---

## 🛠️ 脚本说明

| 脚本 | 功能 |
|------|------|
| `baidu_search.py` | 百度搜索 API |
| `custom_search.py` | 多引擎搜索核心 |
| `multi-search.py` | 多引擎搜索 CLI |
| `fallback_search.py` | 备用搜索引擎 |

---

## 🔍 搜索策略

**默认策略（国内）：**
1. 百度（首选，中文最好）
2. Bing（备选，国际内容）
3. Google（英文/技术内容）
4. Tavily（AI 优化）

**智能路由：**
- 中文内容 → 百度 > Bing
- 英文内容 → Google > Bing
- 技术文档 → Google > Tavily
- 新闻/热点 → 百度 > Bing

---

## 📊 引擎对比

| 引擎 | 中文质量 | 英文质量 | 免费额度 | 国内访问 |
|------|----------|----------|----------|----------|
| 百度 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | 日限额 | ✅ 快 |
| Bing | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 1000/月 | ⚠️ 慢 |
| Google | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 100/天 | ❌ 无法访问 |
| Tavily | ⭐⭐⭐ | ⭐⭐⭐⭐ | 1000/月 | ⚠️ 慢 |

---

## 📄 许可证

MIT-0

---

**作者：** @williamwg2025  
**版本：** 1.0.0
