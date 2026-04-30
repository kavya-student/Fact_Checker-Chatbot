import wikipedia

def extract_topic(text):
    text = text.lower()

    stop_words = ["is", "are", "was", "the", "a", "an", "in", "of"]
    words = [w for w in text.split() if w not in stop_words]

    return " ".join(words[:3])  # take important keywords

def check_wikipedia(query):
    try:
        topic = extract_topic(query)

        results = wikipedia.search(topic)
        if not results:
            return 0.3, "No reliable source found"

        page = wikipedia.page(results[0])
        summary = page.summary.lower()

        return 0.8, summary

    except Exception as e:
        print("Wiki Error:", e)
        return 0.3, "No reliable source found"


def fact_match_score(statement, summary):
    words = statement.lower().split()

    match = 0
    for word in words:
        if word in summary:
            match += 1

    return match / len(words)