#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试Code Review Agent的Hello World程序
功能：输出"Hello, World!"，但包含一个典型的Python 3语法错误
作者：测试用例
日期：2026-02-27
"""

# 定义主函数
def main():
    """程序主函数"""
    # 定义要输出的字符串
    message = "Hello, World!"
    
    # 【语法错误点】：Python 3中print是函数，必须带括号，此处故意省略
    # 错误类型：SyntaxError (Missing parentheses in call to 'print')
    print message  

    # 额外的测试逻辑（无错误）
    print("当前Python版本要求：3.x")  # 这一行是正确的，对比用

# 程序入口
if __name__ == "__main__":
    # 调用主函数
    main()
