from flask import Flask, render_template,request,session,redirect,url_for
from flask_mail import Mail,Message
app = Flask(__name__)
app.secret_key = 'super-secret-key'

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USE_TLS=False,
    MAIL_USERNAME = "husnainabbasi947514@gmail.com",
    MAIL_PASSWORD = "mqsvbsififybnqjg"
    
)
mail = Mail(app)
@app.route("/")
def home():
      return render_template("index.html")
@app.route("/thanks")
def thanks():
      return render_template("thanks.html")
@app.route("/portfolio-details")
def portfolio():
      return render_template("portfolio-details.html")
@app.route("/contact",methods = ['GET', 'POST'])
def contact():
      if(request.method=='POST'):
            
            
          
           name = request.form.get('name')
           email = request.form.get('email')
          
           message = request.form.get('message')
           
           msg = Message('Hello', sender = email, recipients = ["husnainabbasi947514@gmail.com"])
           msg.body = message
           mail.send(msg)
           return redirect (url_for("thanks"))
      return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
