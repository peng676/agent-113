class ScanAgent:
    def __init__(self):
        pass

    def analyze_repo(self, repo_url):
        # 模拟代码扫描逻辑
        issues = [
            {"type": "code_style", "level": "normal", "desc": "变量命名不规范"},
            {"type": "security", "level": "high", "desc": "潜在SQL注入风险"},
            {"type": "performance", "level": "normal", "desc": "循环可优化"}
        ]
        return issues
