from flask import Flask
from flask import request

app = Flask(__name__)

vacancies_data =[
{
    "id": 1,
    "creation_date": "01.02.2023",
    "status": 1,
    "company": "some company",
    "contacts_ids": [1,2],
    "description": "vacancy description",
    "position_name": "Python dev",
    "comment": "My comment",
    "user_id": 1
    },
{
    "id": 2,
    "creation_date": "01.02.2023",
    "status": 1,
    "company": "some company",
    "contacts_ids": [3,4],
    "description": "vacancy description",
    "position_name": "Junior Python dev",
    "comment": "My comment",
    "user_id": 1
    },
{
    "id": 3,
    "creation_date": "20.02.2023",
    "status": 1,
    "company": "some company",
    "contacts_ids": [1,2],
    "description": "vacancy description",
    "position_name": "Junior Python dev",
    "comment": "My comment",
    "user_id": 1
    }
]

events_data = [
    {
        "id": 1,
        "vacancy_id": 1,
        "descriptions": "Some description",
        "event_date": "01.02.2023",
        "title": "Event title for 1 vacancy",
        "due_to_date": "05.02.2023",
        "status": 1
    },
    {
        "id": 2,
        "vacancy_id": 2,
        "descriptions": "Some description",
        "event_date": "01.02.2023",
        "title": "Event title for 2 vacancy",
        "due_to_date": "07.02.2023",
        "status": 1
    },
    {
        "id": 3,
        "vacancy_id": 3,
        "descriptions": "Some description",
        "event_date": "01.02.2023",
        "title": "Event title for 3 vacancy",
        "due_to_date": "08.02.2023",
        "status": 1
    },
]

@app.route("/vacancy/", methods=['GET', 'POST'])
def vacancy():
    return vacancies_data

@app.route("/vacancy/<vacancy_id>/", methods=['GET', 'PUT'])
def show_vacancy_content(vacancy_id):
    for vacancy in vacancies_data:
        if vacancy["id"] == vacancy_id:
            return vacancy

@app.route("/vacancy/<vacancy_id>/events/", methods=['GET', 'POST'])
def events(vacancy_id):
    event_list = []
    for event in events_data:
        if event["vacancy_id"] == vacancy_id:
            return event_list

@app.route("/vacancy/<vacancy_id>/events/<event_id>/", methods=['GET', 'PUT'])
def show_event_content(event_id):
    for event in events_data:
        if event["event_id"] == event_id:
            return event

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