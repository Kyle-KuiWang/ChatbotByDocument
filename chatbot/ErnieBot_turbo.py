import requests
import json


with open("./config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

API_KEY = config['GPT-API']
SECRET_KEY = config['SECRET_KEY']


def ErnieBot(prompt, sys_msg):
    prompt = prompt[0:11000]
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + get_access_token()
    payload = json.dumps({
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    return json.loads(response.text)['result']


def get_access_token():
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))
