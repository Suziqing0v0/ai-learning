# Day 91 · HuggingFace 分词器与 BERT 输出
import torch
from transformers import BertTokenizer, BertModel

MODEL_NAME = "prajjwal1/bert-tiny"
MODEL_REVISION = "6f75de8b60a9f8a2fdf7b69cbd86d9e64bcb3837"

tokenizer = BertTokenizer.from_pretrained(
    MODEL_NAME,
    revision=MODEL_REVISION,
    local_files_only=True,
)

model = BertModel.from_pretrained(
    MODEL_NAME,
    revision=MODEL_REVISION,
    local_files_only=True,
)
model.eval()

text = "I love learning AI"

inputs = tokenizer(text, return_tensors="pt")

tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

with torch.no_grad():
    outputs = model(**inputs)

print("tokens:", tokens)
print("input_ids:", inputs["input_ids"])
print("attention_mask:", inputs["attention_mask"])
print("input_ids 形状:", inputs["input_ids"].shape)
print("attention_mask 形状:", inputs["attention_mask"].shape)
print("last_hidden_state 形状:", outputs.last_hidden_state.shape)
print("pooler_output 形状:", outputs.pooler_output.shape)
print("[CLS] 前 5 个数值:", outputs.last_hidden_state[:, 0, :5])

