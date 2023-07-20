#!/usr/bin/python3
import models
from models import storage
from state import State

st = State()
st2 = State()
st.name = "Alabama"
st2.name = "Minnesota"
storage.new(st)
storage.new(st2)
storage.save()
storage.close()
