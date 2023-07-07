import requests
import streamlit as st
from streamlit_lottie import  st_lottie

#=============function to convert
@st.cache
def conn(val1,val2,amt):
    url = f'https://api.apilayer.com/currency_data/convert?to={val2}&from={val1}&amount={amt}'


    payload = {}
    headers= {"apikey": "3DPMnrLyoZQVDscZKWDpE91WMcq9pVwr"}

    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code
    result = response.text.splitlines()
    str1=str(result[-2])
    str1.lstrip()
    str1=str1.split(": ")
    return str1[-1]




st.set_page_config(page_title="Currency Exchange",page_icon=":currency_exchange:",layout="wide")
col1,col2=st.columns(2)

st.header("Currency Exchange :currency_exchange:")
st.write("Made with :heart: by Ujjwal Tiwari")

def img(url):
    res=requests.get(url)
    if(res.status_code!=200):
        return None
    else:
        return res.json()

imagee=img("https://assets2.lottiefiles.com/packages/lf20_ta0lnlos.json")

st.markdown("---------------")


left_col,middle_col,right_col=st.columns(3)
with left_col:
    val1=st.selectbox("Select Currency 1",['AFN','EUR','ALL','DZD','USD','EUR','AOA','XCD','XCD','ARS','AMD','AWG','AUD','EUR','AZN','BSD','BHD','BDT','BBD','BYN','EUR','BZD','XOF','BMD','INR','BTN','BOB','BOV','USD','BAM','BWP','NOK','BRL','USD','BND','BGN','XOF','BIF','CVE','KHR','XAF','CAD','KYD','XAF','XAF','CLP','CLF','CNY','AUD','AUD','COP','COU','KMF','CDF','XAF','NZD','CRC','XOF','HRK','CUP','CUC','ANG','EUR','CZK','DKK','DJF','XCD','DOP','USD','EGP','SVC','USD','XAF','ERN','EUR','SZL','ETB','EUR','FKP','DKK','FJD','EUR','EUR','EUR','XPF','EUR','XAF','GMD','GEL','EUR','GHS','GIP','EUR','DKK','XCD','EUR','USD','GTQ','GBP','GNF','XOF','GYD','HTG','USD','AUD','EUR','HNL','HKD','HUF','ISK','INR','IDR','XDR','IRR','IQD','EUR','GBP','ILS','EUR','JMD','JPY','GBP','JOD','KZT','KES','AUD','KPW','KRW','KWD','KGS','LAK','EUR','LBP','LSL','ZAR','LRD','LYD','CHF','EUR','EUR','MOP','MKD','MGA','MWK','MYR','MVR','XOF','EUR','USD','EUR','MRU','MUR','EUR','XUA','MXN','MXV','USD','MDL','EUR','MNT','EUR','XCD','MAD','MZN','MMK','NAD','ZAR','AUD','NPR','EUR','XPF','NZD','NIO','XOF','NGN','NZD','AUD','USD','NOK','OMR','PKR','USD','PAB','USD','PGK','PYG','PEN','PHP','NZD','PLN','EUR','USD','QAR','EUR','RON','RUB','RWF','EUR','SHP','XCD','XCD','EUR','EUR','XCD','WST','EUR','STN','SAR','XOF','RSD','SCR','SLL','SGD','ANG','XSU','EUR','EUR','SBD','SOS','ZAR','SSP','EUR','LKR','SDG','SRD','NOK','SEK','CHF','CHE','CHW','SYP','TWD','TJS','TZS','THB','USD','XOF','NZD','TOP','TTD','TND','TRY','TMT','USD','AUD','UGX','UAH','AED','GBP','USD','USD','USN','UYU','UYI','UYW','UZS','VUV','VES','VND','USD','USD','XPF','MAD','YER','ZMW','ZWL','XBA','XBB','XBC','XBD','XTS','XXX','XAU','XPD','XPT','XAG','AFA','FIM','ALK','ADP','ESP','FRF','AOK','AON','AOR','ARA','ARP','ARY','RUR','ATS','AYM','AZM','RUR','BYB','BYR','RUR','BEC','BEF','BEL','BOP','BAD','BRB','BRC','BRE','BRN','BRR','BGJ','BGK','BGL','BUK','HRD','HRK','CYP','CSJ','CSK','ECS','ECV','GQE','EEK','XEU','FIM','FRF','FRF','FRF','GEK','RUR','DDM','DEM','GHC','GHP','GRD','FRF','GNE','GNS','GWE','GWP','ITL','ISJ','IEP','ILP','ILR','ITL','RUR','RUR','LAJ','LVL','LVR','LSM','ZAL','LTL','LTT','LUC','LUF','LUL','MGF','MWK','MVQ','MLF','MTL','MTP','FRF','MRO','FRF','MXP','RUR','FRF','MZE','MZM','NLG','ANG','NIC','PEH','PEI','PEN','PES','PLZ','PTE','FRF','ROK','ROL','RON','RUR','FRF','FRF','FRF','ITL','STD','CSD','EUR','SKK','SIT','ZAL','SDG','RHD','ESA','ESB','ESP','SDD','SDP','SRG','SZL','CHC','RUR','TJR','IDR','TPE','TRL','TRY','RUR','TMM','UGS','UGW','UAK','SUR','USS','UYN','UYP','RUR','VEB','VEF','VEF','VEF','VNC','YDD','YUD','YUM','YUN','ZRN','ZRZ','ZMK','ZWC','ZWD','ZWD','ZWN','ZWR','XFO','XRE','XFU'])
    val1=val1.strip()

with middle_col:
    st_lottie(imagee,height="250px",key="coding")

with right_col:

    val2=st.selectbox("Select Currency 2",['AFN','EUR','ALL','DZD','USD','EUR','AOA','XCD','XCD','ARS','AMD','AWG','AUD','EUR','AZN','BSD','BHD','BDT','BBD','BYN','EUR','BZD','XOF','BMD','INR','BTN','BOB','BOV','USD','BAM','BWP','NOK','BRL','USD','BND','BGN','XOF','BIF','CVE','KHR','XAF','CAD','KYD','XAF','XAF','CLP','CLF','CNY','AUD','AUD','COP','COU','KMF','CDF','XAF','NZD','CRC','XOF','HRK','CUP','CUC','ANG','EUR','CZK','DKK','DJF','XCD','DOP','USD','EGP','SVC','USD','XAF','ERN','EUR','SZL','ETB','EUR','FKP','DKK','FJD','EUR','EUR','EUR','XPF','EUR','XAF','GMD','GEL','EUR','GHS','GIP','EUR','DKK','XCD','EUR','USD','GTQ','GBP','GNF','XOF','GYD','HTG','USD','AUD','EUR','HNL','HKD','HUF','ISK','INR','IDR','XDR','IRR','IQD','EUR','GBP','ILS','EUR','JMD','JPY','GBP','JOD','KZT','KES','AUD','KPW','KRW','KWD','KGS','LAK','EUR','LBP','LSL','ZAR','LRD','LYD','CHF','EUR','EUR','MOP','MKD','MGA','MWK','MYR','MVR','XOF','EUR','USD','EUR','MRU','MUR','EUR','XUA','MXN','MXV','USD','MDL','EUR','MNT','EUR','XCD','MAD','MZN','MMK','NAD','ZAR','AUD','NPR','EUR','XPF','NZD','NIO','XOF','NGN','NZD','AUD','USD','NOK','OMR','PKR','USD','PAB','USD','PGK','PYG','PEN','PHP','NZD','PLN','EUR','USD','QAR','EUR','RON','RUB','RWF','EUR','SHP','XCD','XCD','EUR','EUR','XCD','WST','EUR','STN','SAR','XOF','RSD','SCR','SLL','SGD','ANG','XSU','EUR','EUR','SBD','SOS','ZAR','SSP','EUR','LKR','SDG','SRD','NOK','SEK','CHF','CHE','CHW','SYP','TWD','TJS','TZS','THB','USD','XOF','NZD','TOP','TTD','TND','TRY','TMT','USD','AUD','UGX','UAH','AED','GBP','USD','USD','USN','UYU','UYI','UYW','UZS','VUV','VES','VND','USD','USD','XPF','MAD','YER','ZMW','ZWL','XBA','XBB','XBC','XBD','XTS','XXX','XAU','XPD','XPT','XAG','AFA','FIM','ALK','ADP','ESP','FRF','AOK','AON','AOR','ARA','ARP','ARY','RUR','ATS','AYM','AZM','RUR','BYB','BYR','RUR','BEC','BEF','BEL','BOP','BAD','BRB','BRC','BRE','BRN','BRR','BGJ','BGK','BGL','BUK','HRD','HRK','CYP','CSJ','CSK','ECS','ECV','GQE','EEK','XEU','FIM','FRF','FRF','FRF','GEK','RUR','DDM','DEM','GHC','GHP','GRD','FRF','GNE','GNS','GWE','GWP','ITL','ISJ','IEP','ILP','ILR','ITL','RUR','RUR','LAJ','LVL','LVR','LSM','ZAL','LTL','LTT','LUC','LUF','LUL','MGF','MWK','MVQ','MLF','MTL','MTP','FRF','MRO','FRF','MXP','RUR','FRF','MZE','MZM','NLG','ANG','NIC','PEH','PEI','PEN','PES','PLZ','PTE','FRF','ROK','ROL','RON','RUR','FRF','FRF','FRF','ITL','STD','CSD','EUR','SKK','SIT','ZAL','SDG','RHD','ESA','ESB','ESP','SDD','SDP','SRG','SZL','CHC','RUR','TJR','IDR','TPE','TRL','TRY','RUR','TMM','UGS','UGW','UAK','SUR','USS','UYN','UYP','RUR','VEB','VEF','VEF','VEF','VNC','YDD','YUD','YUM','YUN','ZRN','ZRZ','ZMK','ZWC','ZWD','ZWD','ZWN','ZWR','XFO','XRE','XFU'])
    val2=val2.strip()




left_col2,middle_col2,right_col2=st.columns(3)
with left_col2:
   amt= st.number_input(label="Enter Amount")

with middle_col2:
    st.markdown('')






with right_col2:
    if(val1==val2 or amt==0):
        st.write("Converted Amount")
        st.success(f"{amt}"+" "+f"{val2}")

    else:
        
        try:
            st.write("Converted Amount:")
            url = f'https://api.exchangerate.host/convert?from={val1}&to={val2}&amount={amt}&places=2&format=TSV'
            response = requests.get(url)
            data = response.text
            liss=data.split('\t')
            dis=str(liss[-1].strip("\n"))
            dis=dis.replace(",",".")
            st.success(f"{dis}"+" "+f"{val2}")
            




            
        except:
            st.write("Error Occured: :sad:")
            st.warning('API Error!   You Exhausted your monthly limit 100/100 request', icon="⚠️")
        


st.markdown('<style> body{text-align:center;} #MainMenu,footer{visibility:hidden;} .css-1dp5vir{visibility:hidden;} .css-1jfmq1g e16nr0p31{display:none;}</style>',unsafe_allow_html=True)


