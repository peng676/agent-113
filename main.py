# -*- coding: utf-8 -*-
"""
特工-113 主入口
多Agent代码质量自动化管控系统
"""

from agents.scan_agent import ScanAgent
from agents.refactor_agent import RefactorAgent
from agents.verify_agent import VerifyAgent

def run_code_agent_system(repo_url):
    print("===== 特工-113 代码管控系统启动 =====")
    
    # 1. 代码扫描
    scanner = ScanAgent()
    issues = scanner.analyze_repo(repo_url)
    print(f"[扫描完成] 发现 {len(issues)} 个代码问题")

    # 2. 自动重构
    refactor = RefactorAgent()
    fixed_code = refactor.generate_fix(issues)
    print("[重构完成] 已生成修复代码")

    # 3. 自动验证
    verifier = VerifyAgent()
    result = verifier.run_test(fixed_code)
    print(f"[验证完成] 结果：{result}")

    print("===== 全流程执行完毕 =====")
    return result

if __name__ == "__main__":
    # 测试入口
    run_code_agent_system("https://github.com/yourname/yourproject")
