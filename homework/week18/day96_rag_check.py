# Day 96 · 不调用 API，只验收 RAG 检索和 prompt 上下文
import os
import sys

folder = os.path.dirname(os.path.abspath(__file__))
project = r"D:\ai-learning\super-ppt"
sys.path.insert(0, project)

import rag

source_path = os.path.join(folder, "source.md")

chunks = rag.load_chunks(source_path)
hits = rag.retrieve("卡诺效率公式是什么？", chunks, top_k=3)

print(f"块数: {len(chunks)}")
for hit in hits:
    print(f"{hit['id']} score={hit['score']:.4f}")

print("\n上下文预览：")
print(rag.format_context(hits))

missing = rag.retrieve("今天食堂的午饭是什么？", chunks, top_k=3)
print(f"\n无资料问题命中数: {len(missing)}")
