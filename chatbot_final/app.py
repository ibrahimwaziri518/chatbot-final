from flask import Flask, render_template, request

app = Flask(__name__)

def chatbot_reply(msg):
    user = msg.lower()

    if user == "hello":
        return "Hello! Welcome to Skyline University Chatbot."
    elif user == "admission":
        return "Admissions are currently open."
    elif user == "courses":
        return "Courses include Computer Science, Accounting, Business Administration."
    elif user == "fees":
        return "Please contact bursary for fees details."
    elif user == "location":
        return "Skyline University is located in Kano State, Nigeria."
    elif user == "help":
        return "Commands: hello, admission, courses, fees, location, help, bye"
    elif user == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_response():
    msg = request.args.get("msg")
    return chatbot_reply(msg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
