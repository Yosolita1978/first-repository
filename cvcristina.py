import requests
import json

URL = "https://www.scriptdash.com/careers/apply"

about = "I have 3+ projects in Python. I work along with API's on all of them, especially with Twitter's API. If you want to see my work with them you can go to my website: yosola.co"

links = ["https://www.linkedin.com/in/elsacristinarodriguez", "http://yosola.co/", "http://twittermimic.yosola.co/", "https://github.com/Yosolita1978"]

cristina = {'name': "Cristina Rodriguez", 'about': about, 'email': "yosola@gmail.com", 'links': links}



r = requests.post(URL, json=cristina)
print (r.text)
