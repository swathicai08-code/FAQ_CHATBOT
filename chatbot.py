import json
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load FAQ data
with open("faq_data.json", "r", encoding="utf-8") as file:
    faqs = json.load(file)

questions = [faq["question"] for faq in faqs]
answers = [faq["answer"] for faq in faqs]


# Text preprocessing
def preprocess(text):
    text = text.lower()

    # Keep only letters, numbers and spaces
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    # Remove extra spaces
    text = " ".join(text.split())

    return text


processed_questions = [preprocess(q) for q in questions]

vectorizer = TfidfVectorizer()

question_vectors = vectorizer.fit_transform(processed_questions)


def get_answer(user_question):

    user_question = preprocess(user_question)

    user_vector = vectorizer.transform([user_question])

    similarity = cosine_similarity(
        user_vector,
        question_vectors
    )

    index = similarity.argmax()

    score = similarity[0][index]

    if score < 0.30:
        return "Sorry! I couldn't find an answer for that question."

    return answers[index]