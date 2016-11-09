import re
import requests
url='http://www.mosigra.ru/'
data=requests.get(url)
list_http_old=re.findall(r'[http]+[s]?[:]..[w]+\.[a-zA-Z]+\.[a-zA-Z0-9_\/]+',str(data.content))
#print(len(list_http_old))
list_http=[]
i=0
for b in list_http_old:
    if b not in list_http and list_http_old[i].rfind(url,0,len(url))!=-1:
        list_http.append(b)
    else:
        pass
    i+=1
#print(list_http)
#print(len(list_http))
i=0
j=0
n=len(list_http)
while i<n:       #должно быть i<len(list_http)
    i=i+1
    data2=requests.get(list_http[i])
    temp=re.findall(r'[http]+[s]?[:]..[w]+\.[a-zA-Z]+\.[a-zA-Z0-9_\/]+',str(data2.content))
    for b in temp:
        if b not in list_http and temp[j].rfind(url,0,len(url))!=-1:
            list_http.append(b)
        else:
            pass
        j+=1
    j=0
list_http.append('http://www.mosigra.ru/')
#print(len(list_http))
i=0
while i<20:      #должно быть i<len(list_http)
    i=i+1
    data=requests.get(list_http[i])
    list_all=re.findall(r'\w+\.?[a-zA-Z0-9&!#$%&*+?^_`{|}~,-]*@\w+\.?\w+[.][a-z]{2,3}',str(data.content))
    list_un=[]
    for a in list_all:
        if a not in list_un:
            list_un.append(a)
        else:
            pass
print(list_un,len(list_un))
