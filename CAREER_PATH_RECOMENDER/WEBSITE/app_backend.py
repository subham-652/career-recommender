import sys
import os
from flask import Flask, render_template, request

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from career_description import career_description

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
  
    scores = {career: 0 for career in career_description.keys()}
    ans = request.form 

    # --- SCORING LOGIC ---
    if ans.get('q1') == 'yes': scores["Software Developer"] += 3; scores["AI Engineer"] += 2
    if ans.get('q2') == 'yes': scores["Data Scientist"] += 3
    if ans.get('q3') == 'yes': scores["AI Engineer"] += 3
    if ans.get('q4') == 'yes': scores["Web Developer"] += 3
    if ans.get('q5') == 'yes': scores["Software Developer"] += 2; scores["Data Scientist"] += 1
    if ans.get('q6') == 'yes': scores["Cyber Security Analyst"] += 3
    if ans.get('q7') == 'yes': scores["Graphic Designer"] += 3
    if ans.get('q8') == 'yes': scores["Digital Marketer"] += 2
    if ans.get('q9') == 'yes': scores["Teacher"] += 3
    if ans.get('q10') == 'yes': scores["Actor"] += 3
    if ans.get('q11') == 'yes': scores["Digital Marketer"] += 2; scores["Actor"] += 1
    if ans.get('q12') == 'yes': scores["Data Scientist"] += 2; scores["AI Engineer"] += 2
    if ans.get('q13') == 'yes': scores["Software Developer"] += 1; scores["Web Developer"] += 1
    if ans.get('q14') == 'yes': scores["Entrepreneur"] += 3
    if ans.get('q15') == 'yes': scores["Entrepreneur"] += 2; scores["Software Developer"] += 1
    if ans.get('q16') == 'yes': scores["AI Engineer"] += 1; scores["Software Developer"] += 1
    if ans.get('q17') == 'yes': scores["Graphic Designer"] += 2
    if ans.get('q18') == 'yes': scores["Data Scientist"] += 2
    if ans.get('q19') == 'yes': scores["Teacher"] += 1; scores["Digital Marketer"] += 1; scores["Actor"] += 1
    if ans.get('q20') == 'yes': scores["Entrepreneur"] += 2

    sorted_careers = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    top_3 = []
    for i in range(3):
        name = sorted_careers[i][0]
        top_3.append({
            'name': name,
            'score': sorted_careers[i][1],
            'desc': career_description.get(name, "Excellent career choice!")
        })

    return render_template('index.html', top_results=top_3)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
