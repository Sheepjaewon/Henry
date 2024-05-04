import requests as req

#url read 
url = 'http://search.naver.com'
res=req.get(url, params={'query':'정쳐기'})

#print9res.text