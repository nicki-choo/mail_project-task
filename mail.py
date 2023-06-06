from flask import Flask
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

app = Flask(__name__)
mail = Mail(app)

load_dotenv()

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'nickidummyacc@gmail.com'
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
mail = Mail(app)


@app.route('/')
def email():
    msg = Message("Welcome to Flask Email",
                  sender='nickidummyacc@gmail.com',
                  recipients=["270168718@yoobeestudent.ac.nz"])
    msg.body = 'Hello Flask message sent from Flask-Mail'
    mail.send(msg)

    return 'Email Sent Successfully!'




if __name__ == '__main__':
    app.run(debug=True)