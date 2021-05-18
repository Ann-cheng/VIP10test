import requests

# 发送get请求
url1='https://www.wanandroid.com/'
r=requests.get(url=url1)
print(r.text)

# 发送带参数的get请求
url2='https://cn.bing.com/'
    # 参数
payload = {'k':'android'}
r= requests.get(url=url2,params=payload)
print(r.status_code)