def analyze_text(text):
    uncertainty_words = ["maybe", "probably", "i think", "might"]

    score = 1.0

    for word in uncertainty_words:
        if word in text.lower():
            score -= 0.2

    return max(score, 0)