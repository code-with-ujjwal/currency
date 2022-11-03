
import requests
def coon():

    url = "https://api.apilayer.com/currency_data/convert?to=INR&from=EUR&amount=2"

    payload = {}
    headers= {
      "apikey": "OO9ZQREcI2k6kjX0TjkHKG1B8kgVi78M"
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code
    result = response.text.splitlines()
    ye1=str(result[1]).split(": ")
    ye1=ye1[-1]

    if(ye1=='false,'):
        return -1
    else:
        str1=str(result[-2])
        str1.lstrip()
        str1=str1.split(": ")
        return str1
    print(status_code)
    print(result)