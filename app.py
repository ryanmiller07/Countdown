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
print(d)
# "with" notation
with st.sidebar:
    st.title("Countdown")

future_date = d - (date.today())
days = future_date.days

#years = ((d - (date.today())) / 365 )
#print(years)

##months = ((d - (date.today())) / 12 )
##print(months)
years ,days = divmod(days, 365)
months, days = divmod(days, 30.44)

print(years)
print(months)
print(days)

st.title("Amount of years, months, and days")
st.header(f"{years} : {months} : {days}")