#!/usr/bin/env python3
"""
Search Pro - Content Extractor
内容提取脚本

Usage: python3 extract.py --url https://example.com

Security: 仅提取网页内容，不读取本地文件
"""

import argparse
import sys

def extract_from_url(url: str):
    """从 URL 提取内容
    
    Security:
    - 仅支持 http:// 和 https:// 协议
    - 不读取本地文件（file://）
    - 不访问内网地址
    """
    print("📄 Search Pro - Content Extractor")
    print("=" * 50)
    print(f"🔗 提取 URL: {url}")
    
    # 安全检查：仅允许 http/https
    if not url.startswith(('http://', 'https://')):
        print("❌ 错误：仅支持 http:// 和 https:// 协议")
        print("   不支持 file:// 或其他协议")
        return False
    
    # 安全检查：阻止内网地址
    blocked_prefixes = [
        'http://localhost',
        'http://127.',
        'http://10.',
        'http://172.16.',
        'http://172.17.',
        'http://172.18.',
        'http://172.19.',
        'http://172.2',
        'http://172.3',
        'http://192.168.',
        'http://0.0.0.0',
    ]
    
    for prefix in blocked_prefixes:
        if url.lower().startswith(prefix):
            print(f"❌ 错误：不允许访问内网地址")
            return False
    
    print("\n✅ URL 验证通过")
    print("\n提示：完整功能需要集成 web_fetch 或 requests + BeautifulSoup")
    print("示例代码：")
    print("  import requests")
    print("  from bs4 import BeautifulSoup")
    print("  response = requests.get(url)")
    print("  soup = BeautifulSoup(response.text, 'html.parser')")
    print("  print(soup.get_text())")
    
    return True

def main():
    parser = argparse.ArgumentParser(description='内容提取工具')
    parser.add_argument('--url', help='要提取的网页 URL（仅支持 http/https）')
    
    args = parser.parse_args()
    
    if not args.url:
        print("用法：python3 extract.py --url <URL>")
        print("\n示例:")
        print("  python3 extract.py --url https://example.com")
        print("\n安全限制:")
        print("  - 仅支持 http:// 和 https:// 协议")
        print("  - 不支持 file:// 本地文件")
        print("  - 不访问内网地址")
        return
    
    success = extract_from_url(args.url)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
