from flask import Flask, render_template, request, session, redirect, url_for
from forms import SignupForm, LoginForm,OrderForm
from logger import logger

app = Flask(__name__)

app.secret_key = "development-key"

app.app_context().push()


@app.route('/')
def index():
    if "email" in session:
        logger.info(session["email"] + " : Accessed /index")
        return render_template("index.html", user=session["email"].split("@")[0])
    else:
        logger.info("Guest : Accessed /index")
        return render_template("index.html", user="Guest")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if "email" in session:
        logger.info(session["email"] + " : Redirecting to /index from /signup")
        return redirect(url_for("index"))

    form = SignupForm()

    if request.method == "POST":
        if form.validate() == False:
            logger.info("Guest : Submitted a bad signup form.")
            return render_template("signup.html", form=form)
        else:
            session["email"] = form.email.data
            logger.info(session["email"] + " : Successfully signed up - redirecting to /index")
            return redirect(url_for("index"))
    elif request.method == "GET":
        logger.info("Guest : Accessed /signup")
        return render_template("signup.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if "email" in session:
        logger.info(session["email"] + " : Redirecting to /index from /login")
        return redirect(url_for("index"))

    form = LoginForm()

    if request.method == "POST":
        if form.validate() == False:
            logger.info("Guest : Submitted a bad login form.")
            return render_template("login.html", form=form)
        else:
            session["email"] = form.email.data
            logger.info(session["email"] + " : Successfully logged in - redirecting to /index")
            return redirect(url_for("index"))
    elif request.method == "GET":
        logger.info("Guest : Accessed /login")
        return render_template("login.html", form=form)



@app.route("/order", methods=["GET", "POST"])
def order():
    form = OrderForm()
    if request.method == "POST":
        if form.validate() == False:
            if "email" in session:
                logger.info(session["email"] + " : Submitted a bad order form.")
            else:
                logger.info("Guest : Submitted a bad order form.")
            return render_template("order.html", form=form)
        else:
            if "email" in session:
                logger.info(session["email"] + " : Placed an order. Details - " + str(form.data))
            else:
                logger.info("Guest : Placed an order. Details - " + str(form.data))

                
            return render_template("order.html", status="Order placed")
    elif request.method == "GET":
        if "email" in session:
            logger.info(session["email"] + " : Accessed /order")
        else:
            logger.info("Guest : Accessed /order")
        return render_template("order.html", form=form)



if __name__ == '__main__':
    app.run(debug=True)
