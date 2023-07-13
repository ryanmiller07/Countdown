from datetime import datetime
import datetime as dt
from datetime import date, timedelta
import streamlit as st
with st.sidebar:
    st.title("Countdown")
# st.slider("hello",1,100,50)
col1,col2 = st.columns(2)
with col1:
    st.title("Countdown timer")
    #print(date.today())
    d = st.date_input(
    "Enter an upcoming date",
    dt.date(int(date.today().strftime('%Y')), int(date.today().strftime('%m')),int(date.today().strftime('%d')))
)
with col2:
    st.title("")
    st.title("")
    st.title("")
    st.title("")
    t = st.time_input('Enter a time of the upcoming date.')

    

countdown = st.empty()
combine_time_future = datetime.combine(d,t)
while True:
    current_time = datetime.now()
    difference_time = combine_time_future - current_time
    print(difference_time)
    if difference_time <= timedelta(0):
        break

# "with" notation
future_date = d - (date.today())
days = future_date.days

#years = ((d - (date.today())) / 365 )
#print(years)

##months = ((d - (date.today())) / 12 )
##print(months)
years ,days = divmod(days, 365)
months, days = divmod(days, 30.44)

#print(years)
#print(months)
#print(days)

st.title("Amount of years, months, and days")
st.header(f"{years} : {months} : {days}")
