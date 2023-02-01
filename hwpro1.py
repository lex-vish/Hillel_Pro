from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/vacancy/", methods=['GET', 'POST'])
def vacancy():
    return "all vacancies"

@app.route("/vacancy/<id>/", methods=['GET', 'PUT'])
def show_vacancy_content():
    return "inside vacancy with id"

@app.route("/vacancy/<id>/events/", methods=['GET', 'POST'])
def events():
    return "all events"

@app.route("/vacancy/<id>/events/<event_id>/", methods=['GET', 'PUT'])
def show_event_content():
    return "inside event with id"

@app.route("/vacancy/history/", methods=['GET'])
def vacancy_history():
    return "history of vacancy"

@app.route("/user/", methods=['GET', 'PUT'])
def user_main_page():
    return "main page of user, dashboard of user"

@app.route("/user/calendar/", methods=['GET'])
def user_calendar():
    return "user\'s calendar"

@app.route("/user/mail/", methods=['GET'])
def user_mail():
    return "user\'s mail"

@app.route("/user/settings/", methods=['GET', 'PUT'])
def user_settings():
    return "user\'s settings"

@app.route("/user/documents/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def user_documents():
    return "user\'s documents"

@app.route("/user/templates/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def user_templates():
    return "user\'s templates"

if __name__ == "__main__":
    app.run()