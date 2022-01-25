"""
p039:获取外网ip
"""
import requests
import json

if __name__ == '__main__':

    url = "http://httpbin.org/ip"

    r = requests.get(url)
    # print(r.text)

    ip = json.loads(r.text)["origin"]
    print("我的外网IP：", ip)
