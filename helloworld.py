#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python Hello World程序
功能：输出"Hello, World!"和系统信息
作者：测试用例
日期：2026-02-27
"""

import sys

def main():
    """主函数"""
    # 输出Hello World
    print("Hello, World!")
    
    # 输出系统信息
    print(f"Python版本: {sys.version}")
    print(f"版本信息: {sys.version_info}")

if __name__ == "__main__":
    main()
