""" Used libraries in the code """
from flask import Flask

app = Flask(__name__)


# @app.route("/")
# def page_index():
#     return"Главная страничка"



# @app.route("/profile/")
# def page_profile():
#     return "Профиль пользователя"


@app.route("/line/<deep>")
def page_profile(deep):
    """Function return user lent in the page"""
    print(deep)
    print(type(deep))
    return f"<h1>Лента пользователя {deep}</h1>"







app.run()
