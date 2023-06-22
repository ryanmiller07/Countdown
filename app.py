import datetime
from datetime import date
import streamlit as st
# st.slider("hello",1,100,50)
st.title("Countdown timer")
print(date.today())
st.write("enter a date")
d = st.date_input(
    "Enter an upcoming date",
    datetime.date(int(date.today().strftime('%Y')), int(date.today().strftime('%m')),int(date.today().strftime('%d')))
)

# "with" notation
with st.sidebar:
    st.title("Countdown")



