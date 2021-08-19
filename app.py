from flask import Flask, render_template, request
import smtplib

OWN_EMAIL = "jaynd194@gmail.com"
OWN_PASSWORD = "Jaynarayan@20"

app = Flask(__name__)
app.secret_key = "jaynarayan@2021"

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

@app.route("/", methods=["GET", "POST"])
@app.route("/#contact", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def myForm():
    if request.method == "POST":
        data = request.form
        print(data)
        send_email(data["name"], data["email"], data["subject"], data["comments"])
        # return redirect(url_for("home"))
        return render_template("index.html", msg_sent=True)
    return render_template("index.html", msg_sent=False)


def send_email(name, email, subject, message):
    email_message_websiter = f"Subject: {subject}\n\n" \
                             f"Name: {name.title()}\n" \
                             f"Email: {email}\n\n" \
                             f"Message:\n{message}"

    email_message_user = f"Subject:Thank You {name.title()}, your message has been received!\n\n" \
                         f"Hey {name.title()},\n" \
                         f"Thank you for the Message.\n" \
                         f"Allow me some time to get back to you.\n\n" \
                         f"Best Regards,\n" \
                         f"Jay\n" \
                         f"www.jaynarayandas.com"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        if '@' in email:
            connection.sendmail(OWN_EMAIL, "jaynarayan94@gmail.com", email_message_websiter)
            connection.sendmail(OWN_EMAIL,email , email_message_user)

if __name__ == "__main__":
    app.run(debug=True)
