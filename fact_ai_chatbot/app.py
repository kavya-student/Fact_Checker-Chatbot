from flask import Flask, render_template, request, jsonify
from model import predict
from wiki_check import check_wikipedia, fact_match_score
from nlp_analysis import analyze_text

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    text = request.json["message"]

    # ML prediction
    try:
        ml_pred, ml_prob = predict(text)
    except Exception as e:
        print("ML Error:", e)
        ml_prob = 0.5

    # Wikipedia check
    try:
        wiki_score, wiki_text = check_wikipedia(text)
    except Exception as e:
        print("Wiki Error:", e)
        wiki_score, wiki_text = 0.3, "No reliable source found"

    # Fact matching (NEW)
    try:
        similarity = fact_match_score(text, wiki_text)
        wiki_score = similarity
    except:
        pass

    # NLP analysis
    try:
        nlp_score = analyze_text(text)
    except:
        nlp_score = 0.5

    # Reduce bad wiki impact
    if wiki_score < 0.3:
        final_score = (0.8 * ml_prob) + (0.2 * nlp_score)
    else:
        final_score = (0.7 * ml_prob) + (0.2 * wiki_score) + (0.1 * nlp_score)

    # Result decision
    if final_score > 0.7:
        result = "✅ Likely TRUE"
    elif final_score < 0.4:
        result = "❌ Likely FALSE"
    else:
        result = "⚠️ UNCERTAIN"

    reply = f"""
🧠 Result: {result}

📊 Confidence: {round(final_score*100,2)}%

🔍 Analysis:
ML: {round(ml_prob*100,2)}%
Wiki Match: {round(wiki_score*100,2)}%
NLP: {round(nlp_score*100,2)}%

📚 Info:
{wiki_text[:200]}...
"""

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)