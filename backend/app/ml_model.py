# app/ml_model.py
from typing import Dict
from functools import lru_cache
import logging

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

logger = logging.getLogger(__name__)

# ✅ Real, public, multilingual abusive language model (Indic + English)
# https://huggingface.co/Hate-speech-CNERG/indic-abusive-allInOne-MuRIL
MODEL_NAME = "Hate-speech-CNERG/indic-abusive-allInOne-MuRIL"


@lru_cache(maxsize=1)
def load_model_and_tokenizer():
    """
    Load the HuggingFace model + tokenizer once and cache them.
    Called automatically on the first prediction.
    """
    logger.info(f"Loading model: {MODEL_NAME}")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
    model.eval()
    logger.info("Model loaded successfully.")
    return tokenizer, model


def _interpret_label(label_id: int, raw_label: str) -> Dict:
    """
    Interpret model output into:
      - is_hate (bool)
      - category (str)
    According to the model card:
      LABEL_0 -> Normal
      LABEL_1 -> Abusive
    """
    label_lower = raw_label.lower().strip()

    if label_id == 1 or "1" in label_lower or "abus" in label_lower:
        is_hate = True
        category = "ABUSIVE"
    else:
        is_hate = False
        category = "NON_HATE"

    return {"is_hate": is_hate, "category": category}


def predict_single(text: str, language: str = "auto") -> Dict:
    """
    Run the abusive-language model on a single text and return a normalized prediction.
    The model is multilingual; we keep `language` for your future extensions.
    """
    tokenizer, model = load_model_and_tokenizer()

    # Tokenize input
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128,
    )

    # Forward pass
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits  # [batch_size, num_labels]

    # Convert logits -> probabilities
    probs = torch.softmax(logits, dim=-1)[0]  # [num_labels]
    score_tensor, idx_tensor = torch.max(probs, dim=0)

    score = float(score_tensor.item())
    label_id = int(idx_tensor.item())
    raw_label = model.config.id2label[label_id]

    interpretation = _interpret_label(label_id, raw_label)
    is_hate = interpretation["is_hate"]
    category = interpretation["category"]

    # Severity: if abusive -> use score, else 1 - score (risk scale)
    if is_hate:
        severity = score
        explanation = (
            f"Model predicted '{raw_label}' (abusive) with confidence {score:.2f}."
        )
    else:
        severity = 1.0 - score
        explanation = (
            f"Model predicted '{raw_label}' (normal) with confidence {score:.2f}."
        )

    severity = max(0.0, min(1.0, severity))
    severity = round(severity, 2)

    lang_out = language if language != "auto" else "unknown"

    return {
        "is_hate": is_hate,
        "category": category,
        "severity": severity,
        "language": lang_out,
        "confidence": round(score, 3),
        "explanation": explanation,
    }
