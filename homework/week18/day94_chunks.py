# Day 94 · 文档切分：固定窗口 + 重叠
import os
import json

folder = os.path.dirname(os.path.abspath(__file__))
source_path = os.path.join(folder, "source.md")
chunks_path = os.path.join(folder, "chunks.json")

with open(source_path, "r", encoding="utf-8") as f:
    text = f.read()

print(f"文档总字符数：{len(text)}")

chunks = []
chunk_size = 220
overlap = 40
start = 0
count = 0

while start < len(text):
    end = start + chunk_size
    chunk = text[start: end]
    start = end - overlap
    
    if not chunk.strip():
        continue
    
    count += 1
    item = {
        "id": f"chunk-{count:03d}",
        "source": "source.md",
        "text": chunk,
    }
    chunks.append(item)
    print(f"chunk-{count:03d}: {len(chunk)}字符\ntext={chunk[:60]}")
    
print(f"块数: {len(chunks)}")

with open(chunks_path, "w", encoding="utf-8") as f:
    json.dump(chunks, f, ensure_ascii=False, indent=2)




    