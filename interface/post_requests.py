import requests,json

# 发送post请求
url1='http://httpbin.org/post'
payload={'qq群名':"selenium",'qq群号':'106014970'}

# 通过json.dumps方法将Python字符串转换成json类型
payload=json.dumps(payload)

# 发送请求
r=requests.post(url=url1,data=payload)

# 获取结果
print(r.text)

# 返回为json类型,可以通过r.json方法来查看结果
print(r.json())