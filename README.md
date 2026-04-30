# 🧠 AI Fact Checker Chatbot

## 📌 Project Overview

AI Fact Checker Chatbot is a web-based application that analyzes a given statement and predicts whether it is **True, False, or Uncertain**.
The system uses a combination of rule-based logic, Natural Language Processing (NLP), and Wikipedia-based knowledge to estimate factual correctness.

This project demonstrates the practical use of AI concepts for solving real-world problems like misinformation.

---

## 🎯 Objectives

* To analyze user statements
* To classify statements as True, False, or Uncertain
* To provide a confidence score
* To build a simple chatbot interface

---

## 🚀 Features

* Chatbot-style interface
* Real-time fact checking
* Confidence score output
* Wikipedia-based verification
* NLP-based uncertainty detection

---

## 🛠️ Technologies Used

* Python
* Flask
* HTML, CSS, JavaScript
* Wikipedia API

---

## ⚙️ System Working

1. User enters a statement
2. ML module provides initial confidence score
3. Wikipedia module fetches related information
4. NLP module detects uncertainty
5. Final score is calculated
6. Result is displayed

---

## 📊 Example Outputs

| Input                | Output |
| -------------------- | ------ |
| Earth is flat        | False  |
| India is in Asia     | True   |
| Sun rises in west    | False  |
| Water boils at 100°C | True   |

---

## ▶️ How to Run the Project

### Step 1: Install Required Libraries

```
pip install flask wikipedia nltk
```

### Step 2: Run the Application

```
python app.py
```

### Step 3: Open in Browser

```
http://127.0.0.1:5000
```

---

## 📂 Project Structure

```
AI_Fact_Checker/
│── app.py
│── model.py
│── wiki_check.py
│── nlp_analysis.py
│── templates/
│   └── index.html
│── static/
│   └── style.css
```

---

## ⚠️ Limitations

* Not 100% accurate
* Depends on keyword-based logic
* Wikipedia results may sometimes be irrelevant

---

## 🔮 Future Scope

* Use advanced AI models like BERT
* Improve semantic understanding
* Integrate multiple data sources
* Increase accuracy

---

## 👩‍💻 Author

**Kavya Sharma**
B.Tech Computer Science Engineering
Lovely Professional University

---

## 📚 References

* Wikipedia
* Python Documentation
* Flask Documentation
* NLP Concepts

---
