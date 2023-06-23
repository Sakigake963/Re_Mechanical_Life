import requests as req

res=req.get("https://zipcloud.ibsnet.co.jp/api/search?zipcode=9650006")

print(res.text)

desc="banana"
res=req.post("URL",json={"food":desc})
