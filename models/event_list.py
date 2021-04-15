from models.event import Event

event1 = Event("April 15th", "Party", 50, "Room 1", "30th Birthday Party", False)
event2 = Event("May 20th", "Gig", 3000, "Room 5", "Radiohead", True)
event3 = Event("June 5th", "Wedding", 150, "Room 7", "Lina's Wedding", False)
event_list = [event1, event2, event3]

def add_new_event(new_event):
    event_list.append(new_event)