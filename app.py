import streamlit as st

#1. TEXT

 #title
st.title("This is a title")
st.header("This is a header")
st.subheader("This is a subheader")
st.markdown('### This is a markdown')
st.text("This is a text")
st.markdown("[link to youtube](https://youtube.com)")

html_page = """
<div> 
<p> This is custom html </p>
</div>
"""
st.markdown(html_page,unsafe_allow_html=True)

#file

file = st.file_uploader("Pick a file")

# Error text
st.success("Successful")

st.info("This is an info alert ")

st.warning("This is a warning ")

st.error("This shows an error ")

st.exception("NameError")

# Getting Help Info From Python
#st.help(range)

# Writing Text/Super Fxn
st.write("Text with write")

st.write("Python Range with write",range(10))

# Images
from PIL import Image 
img = Image.open("pic.png")
st.image(img,width=300,caption='Streamlit Images')


#2. MEDIA

# Videos
#video_file = open("example.mp4",'rb')
#video_bytes = video_file.read()
#st.video(video_bytes)

# Audio
# audio_file = open("",'rb')
# audio_bytes = audio_file.read()
# st.audio(audio_bytes,format='audio/mp3')

# Widget
# Checkbox
if st.checkbox("Check to make visible "):
	st.text("check box")

# Radio Button
status = st.radio("Ths is a radio button",('Active','Inactive'))
if status == 'Active':
	st.text("Status is Active")
else:
	st.warning("Not Active Yet")


# SelectBox
occupation = st.selectbox("Selectbox example",['Data Scientist','Programmer','Doctor','Businessman'])
st.write("You selected this option",occupation)

# MultiSelect
location = st.multiselect("Multiselect example",("London","New York","Accra","Kiev","Berlin","New Delhi"))
st.write("You selected",len(location),"location")


# Slider
salary = st.slider("This is a slider",1000,10000)

# Buttons
st.button("Simple Button")


# Text Input
name = st.text_input("Text input ","Type Here...")
if st.button('Submit'):
    result = name.title()
    st.success(result)
else:
    st.write("Press the above button..")

# Text Area
c_text = st.text_area("Text area","Type Here...")
if st.button('Analyze'):
    c_result = c_text.lower()
    st.success(c_result)
else:
    st.write("Press the above button..")


#  Date Input
import datetime,time
today = st.date_input("Date input today",datetime.datetime.now())


# Time Input
t = st.time_input("Time input",datetime.time())

# SIDE Bar
st.sidebar.header("Side Bar Header")
st.sidebar.text("Hello")
st.sidebar.text_input("")


# Display JSON
st.text("Display JSON")
st.json({'name':'hello','age':34})

# Display Raw Code
st.text("Display Raw Code")
st.code("import numpy as np")


st.text("Display Raw Code Alternative Method")
with st.echo():
	# This will also be shown
	import pandas as pd 

	df = pd.DataFrame()


# Progress Bar
# import time
# my_bar = st.progress(0)
# for p  in range(10):
# 	my_bar.progress(p +1)

# Spinner
with st.spinner("Waiting .."):
	time.sleep(5)
st.success("Finished!")

# Placeholder with empty
# age = st.empty()
# age.text("Your Age")
# Replace with image
# age.image(img)


# Cache For Performance
@st.cache
def run_multiple():
	return range(100)
# Display the result of function
st.write(run_multiple())







#3. DATA SCIENCE

import pandas as pd
df = pd.read_csv('iris.csv')

#m1
st.dataframe(df.head())

#m2
st.write(df.head())

#table

st.table(df.head())


#4. PLOT 

import seaborn as sns
import matplotlib.pyplot as plt

#area

st.area_chart(df.head(10))

#bar

st.bar_chart(df.head(10))

#line

st.line_chart(df.head())

#heatmap

fig, ax = plt.subplots()
sns.heatmap(df.corr(), ax=ax)
st.write(fig)
