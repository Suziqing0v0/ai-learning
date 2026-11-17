# Day 93 · 评估本地微调模型并做模型选择
import torch
import time
from transformers import BertTokenizer, BertForSequenceClassification

MODEL_DIR = "homework/week17/tiny_sentiment"

tokenizer = BertTokenizer.from_pretrained(MODEL_DIR, local_files_only=True)
model = BertForSequenceClassification.from_pretrained(MODEL_DIR, local_files_only=True)
model.eval()

test_texts = [
    "I absolutely love this movie",
    "I really hate waiting this long",
    "The result exceeded my expectations",
    "This experience left me disappointed",
    "I do not like this product",
    "The film was not good at all",
    "The food was not bad",
    "The staff were friendly and helpful",
    "I regret buying this item",
    "What a delightful surprise",
    "This is exactly what I wanted",
    "I would never recommend this service",
]

test_labels = [1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0]

correct = 0
total = 0
inc = 0
total_time = 0
for text, true_label in zip(test_texts,test_labels):
    print(f"原文：{text}")
    print(f"真实标签：{true_label}")
    inputs = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
    start = time.perf_counter()
    
    with torch.no_grad():
        outputs = model(**inputs)
    elapsed_ms = (time.perf_counter() - start) * 1000
    prob = torch.softmax(outputs.logits, dim=-1)[0]
    pred_label = prob.argmax().item()
    print(f"预测标签：{pred_label}")
    print(f"推理时间：{elapsed_ms}ms")
    print(f"积极类概率：{prob[1].item()}")


    total_time += elapsed_ms
    total += 1
    if pred_label == true_label:
        correct += 1
    else:
        inc += 1

print(f"预测正确 {correct} / {total}")
acc = correct / total
print(f"准确率：约{acc:.4f}")
print(f"错误数量：{inc}")
mean_time = total_time / len(test_texts)
print(f"平均单句延迟：约{mean_time:.1f}ms")


    
    
    
    