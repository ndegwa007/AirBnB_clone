#!/usr/bin/python3
import models
from models import storage
from models.state import State

st = State()
st2 = State()
st.name = "Alabama"
st2.name = "Minnesota"
storage.new(st)
storage.new(st2)
storage.save()
storage.close()
print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))
first_state_id = list(storage.all(State).values())[0].id
print("First state: {}".format(storage.get(State, first_state_id)))
