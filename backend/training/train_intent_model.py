import pandas as pd
from sklearn.model_selection import train_test_split
from datasets import Dataset

from transformers import (
    DistilBertTokenizerFast,
    DistilBertForSequenceClassification,
    TrainingArguments,
    Trainer
)

# Load Dataset
df = pd.read_csv("datasets/intent_dataset.csv")

# Convert Intent Labels to Numbers
labels = df["intent"].unique()

label2id = {
    label: idx
    for idx, label in enumerate(labels)
}

id2label = {
    idx: label
    for label, idx in label2id.items()
}

df["label"] = df["intent"].map(label2id)

# Train-Test Split
train_texts, test_texts, train_labels, test_labels = train_test_split(
    df["query"],
    df["label"],
    test_size=0.2,
    random_state=42
)

# Tokenizer
tokenizer = DistilBertTokenizerFast.from_pretrained(
    "distilbert-base-uncased"
)

train_encodings = tokenizer(
    train_texts.tolist(),
    truncation=True,
    padding=True
)

test_encodings = tokenizer(
    test_texts.tolist(),
    truncation=True,
    padding=True
)

train_dataset = Dataset.from_dict({
    "input_ids": train_encodings["input_ids"],
    "attention_mask": train_encodings["attention_mask"],
    "label": train_labels.tolist()
})

test_dataset = Dataset.from_dict({
    "input_ids": test_encodings["input_ids"],
    "attention_mask": test_encodings["attention_mask"],
    "label": test_labels.tolist()
})

# Model
model = DistilBertForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=len(labels)
)

# Training Arguments
training_args = TrainingArguments(
    output_dir="models/intent_classifier",
    num_train_epochs=5,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    save_strategy="epoch",
    logging_steps=5
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset
)

# Train
trainer.train()

# Save Model
model.save_pretrained(
    "models/intent_classifier"
)

tokenizer.save_pretrained(
    "models/intent_classifier"
)

print("\nModel Training Complete")
print("Saved To:")
print("models/intent_classifier")

print("\nIntent Mapping:")
print(label2id)