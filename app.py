from datetime import datetime
import datetime as dt
from datetime import date, timedelta
import streamlit as st
from time import sleep


with st.sidebar:
    st.title("Countdown")
# st.slider("hello",1,100,50)
if "inputDate" not in st.session_state:
    st.session_state["inputDate"] = " "

if "inputTime" not in st.session_state:
    st.session_state["inputTime"] = None
st.title('_Countdown timer_')
col1,col2 = st.columns(2)

with col1:
    
    #print(date.today())
    d = st.date_input(
    "Enter an upcoming date",
    dt.date(int(date.today().strftime('%Y')), int(date.today().strftime('%m')),int(date.today().strftime('%d')))
)
with col2:
    # st.title("")
    # st.title("")
    # st.title("")
    #st.title("")
    t = st.time_input('Enter a time of the upcoming date.', st.session_state["inputTime"])

st.session_state["inputTime"] = t

    
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

st.header("Amount of years, months, and days")
st.header(f"{years} : {months} : {days}")

if "hmsHeader" not in st.session_state:
    st.session_state["hmsHeader"] = " "

countdown = st.empty()
combine_time_future = datetime.combine(d,t)
# hms = st.header("")
# oldhmsText = ""
st.header("Amount of hours, minutes, and seconds")
hms = st.header(st.session_state["hmsHeader"])
while True:
    sleep(1)
    current_time = datetime.now()
    difference_time = combine_time_future - current_time
    hours, seconds = divmod(difference_time.seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    print("Hours " , hours)
    print("Minutes ", minutes)
    print("Seconds ", seconds)
    text = f"{hours} : {minutes} : {seconds}"
    st.session_state["hmsHeader"] = text
    st.experimental_rerun()
    #print(difference_time)
    # oldhmsText = f"{hours} : {minutes} : {seconds}"
    if difference_time <= timedelta(0):
        break
    st.experimental_rerun()

