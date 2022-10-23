import requests
import streamlit as st
from streamlit_lottie import  st_lottie


st.set_page_config(page_title="Currency Exchange",page_icon=":currency_exchange:",layout="wide")
col1,col2=st.columns(2)

st.header("Currency Exchange :currency_exchange:")
st.write("Made with :heart: by Preeti & Palasha")

def img(url):
    res=requests.get(url)
    if(res.status_code!=200):
        return None
    else:
        return res.json()

imagee=img("https://assets2.lottiefiles.com/packages/lf20_ta0lnlos.json")

st.markdown("---------------")
left_col,middle_col,right_col=st.columns(3)
f= open("list.txt","r")
with left_col:
    val1=st.selectbox("Select Currency 1",[x for x in f.readlines()])
    val1=val1.strip()

with middle_col:
    st_lottie(imagee,height="250px",key="coding")

with right_col:
    f.seek(0)
    val2=st.selectbox("Select Currency 2",[x for x in f.readlines()])
    val2=val2.strip()

f.close()


left_col2,middle_col2,right_col2=st.columns(3)
with left_col2:
   amt= st.number_input(label="Enter Amount")

with middle_col2:
    st.write("##")


url = f'https://api.apilayer.com/currency_data/convert?to={val2}&from={val1}&amount={amt}'


payload = {}
headers= {
  "apikey": "3DPMnrLyoZQVDscZKWDpE91WMcq9pVwr"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text.splitlines()
str1=str(result[-2])
str1.lstrip()
str1=str1.split(": ")



with right_col2:
    st.write("Converted Amount")
    st.text(str1[-1]+" "+f"{val2}")





