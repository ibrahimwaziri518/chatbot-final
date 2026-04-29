from flask import Flask, render_template, request

app = Flask(__name__)

def chatbot_reply(msg):
    user = msg.lower().strip()

    # Greetings
    if any(word in user for word in ["hello", "hi", "hey"]):
        return "Hello! Welcome to Skyline University Chatbot. How may I assist you today?"

    # About Skyline
    elif any(word in user for word in ["about skyline", "tell me about 
skyline", "history of skyline"]):
        return "Skyline University Nigeria is a private university located 
in Kano, Nigeria. It was established to provide quality education, modern 
learning facilities, and global academic standards."

    # Admission
    elif any(word in user for word in ["admission", "apply", 
"application", "form"]):
        return "Admission forms are available on the Skyline University 
portal. You can apply online."

    # Courses
    elif any(word in user for word in ["courses", "course", "programs", 
"department"]):
        return """Available courses at Skyline University include:
1. Computer Science
2. Software Engineering
3. Cyber Security
4. Accounting
5. Business Administration
6. Economics
7. International Relations
8. Mass Communication"""

    # Fees
    elif any(word in user for word in ["fees", "fee", "tuition", 
"payment"]):
        return "Please contact the bursary department or visit the portal 
for current tuition and payment details."

    # Contact
    elif any(word in user for word in ["contact", "phone", "email", 
"number"]):
        return """Skyline University Contact Details:
Email: info@sun.edu.ng
Website: www.sun.edu.ng"""

    # Location
    elif any(word in user for word in ["location", "address", "where"]):
        return "Skyline University is located in Kano, Nigeria."

    # Hostel
    elif any(word in user for word in ["hostel", "accommodation"]):
        return "Hostel accommodation is available for students. Please 
contact student affairs for details."

    # Help
    elif any(word in user for word in ["help", "commands"]):
        return "You can ask about Skyline University, admission, courses, 
fees, hostel, location, contact and more."

    # Bye
    elif any(word in user for word in ["bye", "goodbye"]):
        return "Goodbye! Thanks for chatting with Skyline University 
Chatbot."

    # Default
    else:
        return "Sorry, I don't fully understand. Please ask about 
admission, courses, fees, hostel, contact or location."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg")
    return chatbot_reply(userText)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
