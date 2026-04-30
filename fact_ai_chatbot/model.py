def predict(text):
    text = text.lower()

    false_facts = [
        "earth is flat",
        "sun rises in west",
        "india is in europe"
    ]

    true_facts = [
        "india is in asia",
        "water boils at 100",
        "earth revolves around the sun"
    ]

    for fact in false_facts:
        if fact in text:
            return "False", 0.1

    for fact in true_facts:
        if fact in text:
            return "True", 0.9

    return "Uncertain", 0.5