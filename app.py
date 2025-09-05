from flask import Flask, request, jsonify
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Initialize TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

@app.route('/')
def home():
    return "Plagiarism Detection API is running."

@app.route('/check-plagiarism', methods=['POST'])
def check_plagiarism():
    data = request.get_json()
    source_text = data.get('source')
    suspicious_text = data.get('suspicious')

    if not source_text or not suspicious_text:
        return jsonify({'error': 'Both source and suspicious texts are required.'}), 400

    # Vectorize and compute similarity
    tfidf_matrix = vectorizer.fit_transform([source_text, suspicious_text])
    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

    # Threshold for flagging plagiarism
    threshold = 0.75
    flagged = similarity_score > threshold

    result = {
        'flagged': flagged,
        'similarity_score': round(similarity_score, 3),
        'reason': 'High textual overlap detected via cosine similarity.',
        'suggestion': 'Consider asking the student to explain their sources or rewrite the section.'
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
