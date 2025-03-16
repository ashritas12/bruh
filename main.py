from flask import Flask, jsonify
import random

app = Flask(__name__)

bruh_variations = [
    "bruzz are we deaduzz 💔",
    "Nah she's 🥀 got u🥀 blushing 🥀 twin 🥀 ah 🥀 hell 🥀 nah 🥀 twin 🥀 u 🥀 gotta 🥀lock up twin 🥀 bruh 🥀 this not even u twin 🥀 on fonem grave bru 🥀 euaahh",
    "sybau", "what the bruh", "bruzzzzzzzz"
]


@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Bruzz Chatbot</title>
        <style>
            body {
                background-image: url('sigmasigmaboy.jpg'); 
                background-size: cover;
                background-position: center;
                font-family: Arial, sans-serif;
                text-align: center;
                color: #00FF9C;
                padding: 50px;
                font-size: 30px;
                }
            input[type="text"] {
                padding: 10px;
                width: 300px;
                font-size: 16px;
                margin-top: 10px;
            }
            button {
                padding: 10px 20px;
                font-size: 16px;
                margin-top: 10px;
                cursor: pointer;
            }
        </style>
        <script>
            async function getBruh() {
                let response = await fetch('/get_bruh');
                let data = await response.json();
                document.getElementById("response").innerText = data.response;
            }
        </script>
    </head>
    <body>
        <h2>Bruh Moment</h2>
        <input type="text" id="userInput" placeholder="Type anything...">
        <button onclick="getBruh()">Send</button>
        <p id="response"></p>
    </body>
    </html>
    """


@app.route("/get_bruh", methods=["GET"])
def get_bruh():
    return jsonify({"response": random.choice(bruh_variations)})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
