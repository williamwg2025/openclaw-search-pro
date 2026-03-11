#!/usr/bin/env python3
"""
Multi-Engine Search Script
Usage: python3 multi-search.py "搜索关键词" [--all-engines]
"""

import argparse
import sys
from pathlib import Path

# 导入自研搜索引擎
sys.path.insert(0, str(Path(__file__).parent))
from custom_search import CustomSearchEngine

class Colors:
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    CYAN = '\033[0;36m'
    BLUE = '\033[0;34m'
    NC = '\033[0m'
    BOLD = '\033[1m'

def print_header(text):
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.NC}")
    print(f"{Colors.BOLD}{Colors.CYAN}{text:^60}{Colors.NC}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.NC}\n")

def main():
    parser = argparse.ArgumentParser(description='多引擎搜索')
    parser.add_argument('query', type=str, help='搜索关键词')
    parser.add_argument('--max-results', type=int, default=10, help='最大结果数')
    parser.add_argument('--all-engines', action='store_true', help='使用所有引擎')
    parser.add_argument('--engine', type=str, choices=['duckduckgo', 'bing', 'google', 'tavily'], help='指定引擎')
    args = parser.parse_args()
    
    print_header("🔍 Search Pro - 自研搜索引擎")
    
    # 创建搜索引擎实例
    search_engine = CustomSearchEngine()
    
    # 如果指定 --all-engines，启用所有引擎
    if args.all_engines:
        for engine_name in search_engine.config['engines']:
            search_engine.config['engines'][engine_name]['enabled'] = True
        print(f"{Colors.BLUE}使用所有可用引擎{Colors.NC}\n")
    
    # 如果指定特定引擎
    if args.engine:
        for engine_name in search_engine.config['engines']:
            search_engine.config['engines'][engine_name]['enabled'] = (engine_name == args.engine)
        print(f"{Colors.BLUE}使用引擎：{args.engine}{Colors.NC}\n")
    
    # 执行搜索
    print(f"{Colors.BOLD}搜索：{args.query}{Colors.NC}")
    print(f"{Colors.BOLD}最大结果：{args.max_results}{Colors.NC}\n")
    
    results = search_engine.search(args.query, max_results=args.max_results)
    
    if not results:
        print(f"{Colors.YELLOW}未找到结果{Colors.NC}")
        return
    
    # 按引擎分组统计
    engine_stats = {}
    for result in results:
        engine = result.get('engine', 'unknown')
        engine_stats[engine] = engine_stats.get(engine, 0) + 1
    
    print(f"{Colors.GREEN}找到 {len(results)} 个结果:{Colors.NC}")
    for engine, count in engine_stats.items():
        print(f"  {engine}: {count} 个")
    print()
    
    # 显示结果
    for i, result in enumerate(results, 1):
        print(f"{Colors.BOLD}{i}. {result['title']}{Colors.NC}")
        print(f"   链接：{Colors.CYAN}{result['url']}{Colors.NC}")
        print(f"   来源：{Colors.YELLOW}{result['engine']}{Colors.NC}")
        print(f"   评分：{result['score']}")
        if result.get('content'):
            content = result['content'][:200] + '...' if len(result.get('content', '')) > 200 else result.get('content', '')
            print(f"   摘要：{content}")
        print()

if __name__ == '__main__':
    main()
