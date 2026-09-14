# A tuple can be used as a record that represents an item in the event list.

def Handle_Event_1():
    print("Event_1")

def Handle_Event_2():
    print("Event_2")

Event_List = [(1.3, Handle_Event_1), (3.3, Handle_Event_2), (4.5, Handle_Event_1)]

for ev in Event_List:
    (time, event_handler) = ev
    event_handler()  # Add two parentheses and include 
                     # arguments, if any
                     