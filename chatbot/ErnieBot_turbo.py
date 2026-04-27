import requests
import json

with open("./config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# V2 版本只需要这一个 KEY
API_KEY = config['API-KEY']


def ErnieBot(prompt, sys_msg):
    prompt = prompt[0:11000]

    # 文心一言 V2 接口（OpenAI 兼容协议）
    url = "https://qianfan.baidubce.com/v2/chat/completions"


    payload = json.dumps({
        "model": "ernie-5.0-thinking-preview",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3
    })

    # V2 认证方式：直接用 Bearer + API Key
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }

    response = requests.request("POST", url, headers=headers, data=payload.encode("utf-8"))
    res_json = json.loads(response.text)
    response.encoding = "utf-8"
    # print(response.text)

    # V2 返回格式兼容 OpenAI
    return res_json["choices"][0]["message"]["content"]