import json
import requests

API_link_streamko="https://globaldid.streamco.org/api"
updates=requests.get(API_link_streamko+f"/cdr?_login=TLC&_password=4mdZsJlP&date_from=1653435628&date_to=1652894706&with_unanswered=1").json()
print(updates)
