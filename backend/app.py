from flask import Flask, request, jsonify
from flask_cors import CORS 
import os
from utils import read_file, calculate_similarity_hashing

app = Flask(__name__)
CORS(app)  

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/compare', methods=['POST'])
def compare_files():
    file1 = request.files['file1']
    file2 = request.files['file2']

    path1 = os.path.join(UPLOAD_FOLDER, file1.filename)
    path2 = os.path.join(UPLOAD_FOLDER, file2.filename)

    file1.save(path1)
    file2.save(path2)

    text1 = read_file(path1)
    text2 = read_file(path2)

    similarity = calculate_similarity_hashing(text1, text2)
    return jsonify({'similarity': round(similarity, 2)})

if __name__ == '__main__':
    app.run(debug=True)
