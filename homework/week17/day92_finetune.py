# Day 92 · 微调 bert-tiny 完成情感分类
import torch
from torch.utils.data import TensorDataset, DataLoader
from torch.optim import AdamW
from transformers import BertTokenizer, BertForSequenceClassification

MODEL_NAME = "prajjwal1/bert-tiny"
MODEL_REVISION = "6f75de8b60a9f8a2fdf7b69cbd86d9e64bcb3837"

torch.manual_seed(42)
model = BertForSequenceClassification.from_pretrained(
    MODEL_NAME,
    revision=MODEL_REVISION,
    num_labels=2,
    local_files_only=True,
)

train_texts = [
    "I love this product",
    "This movie is wonderful",
    "The food tastes great",
    "I am very happy today",
    "The service was excellent",
    "That was a fantastic experience",
    "The book is interesting",
    "I enjoy learning AI",
    "This result is amazing",
    "Everything worked perfectly",
    "I hate this product",
    "This movie is terrible",
    "The food tastes awful",
    "I am very sad today",
    "The service was horrible",
    "That was a boring experience",
    "The book is confusing",
    "I dislike learning this",
    "This result is disappointing",
    "Everything went wrong",
]

train_labels = [1] * 10 + [0] * 10

test_texts = [
    "I really love this movie",
    "This product is terrible",
    "The food was delicious",
    "I feel unhappy today",
    "What an excellent service",
    "This was awful and boring",
]

tokenizer = BertTokenizer.from_pretrained(
    MODEL_NAME,
    revision=MODEL_REVISION,
    local_files_only=True,
)

train_enc = tokenizer(
    train_texts,
    padding=True,
    truncation=True,
    return_tensors="pt",
)

test_enc = tokenizer(
    test_texts,
    padding=True,
    truncation=True,
    return_tensors="pt",
)

test_labels = [1, 0, 1, 0, 1, 0]

train_labels = torch.tensor(train_labels)
test_labels = torch.tensor(test_labels)

train_dataset = TensorDataset(
    train_enc["input_ids"],
    train_enc["attention_mask"],
    train_enc["token_type_ids"],
    train_labels
)
test_dataset = TensorDataset(
    test_enc["input_ids"],
    test_enc["attention_mask"],
    test_enc["token_type_ids"],
    test_labels
)

generrator = torch.Generator().manual_seed(42)
train_loader = DataLoader(train_dataset, batch_size=5, shuffle=True, generator=generrator)
test_loader = DataLoader(test_dataset, batch_size=5, shuffle=False, generator=generrator)

optimizer = AdamW(model.parameters(), lr=3e-4)

for epoch in range(5):
    model.train()
    total_loss = 0
    for batch in train_loader:
        input_ids, attention_mask, token_type_ids, labels = batch
        optimizer.zero_grad()
        out = model(input_ids=input_ids,attention_mask=attention_mask, token_type_ids=token_type_ids, labels=labels)
        loss = out.loss
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

    avg_loss = total_loss / len(train_loader)
    print(f"平均loss={avg_loss}")

    correct = 0
    total = 0
    model.eval()
    with torch.no_grad():
        for batch in train_loader:  
            input_ids, attention_mask, token_type_ids, labels = batch
            out = model(input_ids=input_ids,attention_mask=attention_mask, token_type_ids=token_type_ids, labels=labels)
            pred = out.logits.argmax(dim=1)
            correct += (pred == labels).sum().item()
            total += labels.size(0)
        acc_train = correct / total
    print(f"训练集epoch {epoch}: acc={acc_train}")
    
    correct = 0
    total = 0
    with torch.no_grad():
        for batch in test_loader:  
            input_ids, attention_mask, token_type_ids, labels = batch
            out = model(input_ids=input_ids,attention_mask=attention_mask, token_type_ids=token_type_ids, labels=labels)
            pred = out.logits.argmax(dim=1)
            correct += (pred == labels).sum().item()
            total += labels.size(0)
        acc_test = correct / total
    print(f"测试集epoch {epoch}: acc={acc_test}")

model.save_pretrained("homework/week17/tiny_sentiment")
tokenizer.save_pretrained("homework/week17/tiny_sentiment")    