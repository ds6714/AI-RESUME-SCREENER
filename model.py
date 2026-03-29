import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Sample training data
data = {
    "resume": [
        "python machine learning data science",
        "java spring boot backend developer",
        "sql excel data analyst dashboard"
    ],
    "role": [
        "Data Scientist",
        "Software Developer",
        "Data Analyst"
    ]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["resume"])

model = LogisticRegression()
model.fit(X, df["role"])

def predict_role(text):
    X_input = vectorizer.transform([text])
    prediction = model.predict(X_input)[0]
    confidence = max(model.predict_proba(X_input)[0])
    return prediction, confidence
def extract_skills(text):
    skills = ["python", "java", "sql", "machine learning", "data science"]
    found_skills = []

    for skill in skills:
        if skill in text.lower():
            found_skills.append(skill)

    return found_skills
def match_score(resume_text, job_desc):
    resume_words = set(resume_text.lower().split())
    job_words = set(job_desc.lower().split())

    match = resume_words.intersection(job_words)
    score = len(match) / len(job_words) * 100

    return round(score, 2)
