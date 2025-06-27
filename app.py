from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

# OpenAI API açarı mühit dəyişəni ilə oxunur
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create_cv", methods=["POST"])
def create_cv():
    user_data = request.json.get("data")
    prompt = f"CV üçün məlumat: {user_data}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    result = response["choices"][0]["message"]["content"]
    return jsonify({"cv": result})

# Render üçün uyğun host və port ayarları
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


