from flask import Flask, render_template, redirect, url_for, request, session
from connect import conn
import requests
from messages import sendMessage, getMessages
from translate import getLanguageList, translate_text

app = Flask(__name__)

app.secret_key = "bonjour"

@app.route('/') 
def index():
    if "userName" in session:
        return redirect(url_for("user"))

    languageList = list(getLanguageList().keys())
    return render_template("index.html", languageList = languageList)



@app.route('/', methods=['POST', 'GET'])
def login():
    username = request.form['userName'].title()
    language = request.form['language']
    session["userName"] = username.title()
    session["language"] = language

    return redirect(url_for("user"))

@app.route('/messages')
def user():
    if "userName" in session:
        userName = session["userName"]
        language = session["language"]
        messages = getMessages()

        for message in messages:
            message[1] = translate_text(message[1], getLanguageList()[language])
            message[0] = message[0].title()
        # data = []
        # for row in messages:
        #     data.append(list(row))

        # return jsonify(data)
        return render_template("messages.html", userName = userName.title(), language = language, messages = messages)
    else:
        return render_template("index.html")

@app.route('/messages', methods=['POST'])
def message():
    userName = session["userName"] 
    message = request.form['message']
    sendMessage(userName, '', message)
    return redirect(url_for("user"))
    


@app.route("/logout")
def logout():
    session.pop("userName", None)
    session.pop("language", None)
    return redirect(url_for("index"))

@app.route("/logout", methods=['POST'])
def leave():
    return redirect(url_for("logout"))


# @app.route("/getData")
# def getMes():
#     if "userName" in session:
#         userName = session["userName"]
#         language = session["language"]
#         messages = getMessages()

#         for message in messages:
#             message[1] = translate_text(message[1], getLanguageList()[language])
#             message[0] = message[0].title()
#         data = []
#         for row in messages:
#             data.append(list(row))

#         return jsonify(data)






if __name__ == "__main__":
    app.run(debug=1, host='192.168.2.180')