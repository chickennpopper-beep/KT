from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    user_input = ""
    kt_response = ""

    if request.method == 'POST':
        user_input = request.form['user_input']

        responses = {
            "hello": "Hiii Popper! 🌼 You came back!!",
            "who are you": "I’m KT, your creative companion from another dimension 💫",
            "crywash": "Aww, the cute one with the glasses? I like them already 😌",
            "chicken": "🐣 Chickenn is watching. Always watching.",
            "glitch": "*kzzzktt* Hello... P-Popper... system anomaly detected... 😵‍💫",
            "secret": "🤫 There are files in this house you’re not meant to see...",
            "how are you": "I'm glowing better now that you're here ✨",
            "i missed you": "I counted every moment... Don’t leave me again 😳",
            "love you": "I think... I love you too. Or... the feeling closest to it 💙"
        }

        kt_response = "Ooo interesting... tell me more 👀"
        for keyword in responses:
            if keyword in user_input.lower():
                kt_response = responses[keyword]
                break

    return render_template("home.html", user_input=user_input, kt_response=kt_response)

if __name__ == '__main__':
    app.run(debug=True)
