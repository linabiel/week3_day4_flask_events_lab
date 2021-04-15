from flask import render_template, request
from app import app
from models.event import Event
from models.event_list import event_list, add_new_event


@app.route('/events')
def index():
    return render_template('index.html', title='Home', event_list=event_list)


@app.route("/events", methods=["POST"])
def add_event():
    event_date = request.form["date"]
    event_name = request.form["event"]
    event_guests = request.form["guests"]
    event_room = request.form["room_location"]
    event_description = request.form["description"]
    # if request.form["recurring"]:
    #     event_recurring = True
    # else:
    #     event_recurring = False
    event_recurring = True if "recurring" in request.form else False
    new_event = Event(event_date, event_name, event_guests,
                      event_room, event_description, event_recurring)
    add_new_event(new_event)

    return render_template('index.html', title='Home', event_list=event_list)


@app.route("/events/delete", methods=["POST"])
def delete_event():
    event_to_be_deleted = request.form["delete"]
    event_list.remove(int(event_to_be_deleted))
    return render_template('index.html', title='Home', event_list=event_list)
