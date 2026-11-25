# Day 97 · 读取并检查 LLM 应用评估集
import json
import os

folder = os.path.dirname(os.path.abspath(__file__))
cases_path = os.path.join(folder, "cases.json")

with open(cases_path, "r", encoding="utf-8") as f:
    cases = json.load(f)

ids = [case["id"] for case in cases]

if len(ids) != len(set(ids)):
    print("评估集存在重复ID")
else:
    print(f"案例数: {len(cases)}, ID均唯一")

    for case in cases:
        print(
            f"{case['id']} | "
            f"{case['mode']} | "
            f"{case['topic']} | "
            f"风险:{case['risk']}"
)