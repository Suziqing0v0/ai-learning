# Day 95 · TF-IDF 文本向量与余弦相似度检索
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

folder = os.path.dirname(os.path.abspath(__file__))
chunks_path = os.path.join(folder, "chunks.json")

with open(chunks_path, "r", encoding="utf-8") as f:
    chunks = json.load(f)

texts = [item["text"] for item in chunks]

vectorizer = TfidfVectorizer(
    analyzer="char",
    ngram_range=(2,3),
)

queries = [
    "为什么热量不能自发从低温传到高温？",
    "卡诺效率公式是什么？",
    "第二定律是否说明房间永远不会自己变整齐？",
    "今天食堂的午饭是什么？",
]

X_chunks = vectorizer.fit_transform(texts)


for query in queries:
    X_query = vectorizer.transform([query])
    scores = cosine_similarity(X_query, X_chunks)[0]
    order = np.argsort(scores)[::-1][:3]
    print(f"\n问题:{query}")
    if scores[order[0]] < 0.1:
        print("可能没有足够资料，不能强行回答")
    else:
        for idx in order:
            print(
                f"chunk_id:{chunks[idx]['id']} "
                f"相似度:{scores[idx]:.4f}"
            )
            print(f"{texts[idx][:80]}\n")

