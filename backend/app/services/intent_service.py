from transformers import (
    DistilBertTokenizerFast,
    DistilBertForSequenceClassification
)
    
import torch

MODEL_PATH = "models/intent_classifier"

tokenizer = DistilBertTokenizerFast.from_pretrained(
    MODEL_PATH
)

model = DistilBertForSequenceClassification.from_pretrained(
    MODEL_PATH
)

intent_labels = {
    0: "Disease Diagnosis",
    1: "Fertilizer Recommendation",
    2: "Irrigation Advice",
    3: "Pest Management",
    4: "Weather Advice",
    5: "Crop Recommendation",
    6: "Yield Improvement",
    7: "Market Price Information",
    8: "General Agriculture Questions"
}


def predict_intent(text):

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True
    )

    outputs = model(**inputs)

    prediction = torch.argmax(
        outputs.logits,
        dim=1
    ).item()

    return {
        "intent": intent_labels[prediction]
    }