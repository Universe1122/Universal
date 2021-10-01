from bs4 import BeautifulSoup
import requests
import json

def getData():
    url = "https://www.boannews.com"
    result = []
        
    res = requests.get("https://www.boannews.com/media/t_list.asp", headers = fakeUserAgent())
    soup = BeautifulSoup(res.content.decode("euc-kr") , "html.parser", from_encoding='euc-kr')
    
    news_list = soup.select(".news_list")
    
    for i, news in enumerate(news_list):
        result.append({})
        result[i]["link"] = url + news.select("a")[0].get("href")
        result[i]["title"] = news.select(".news_txt")[0].get_text()
        result[i]["date"] = news.select(".news_writer")[0].get_text()
        result[i]["date"] = replaceDate(result[i]["date"][result[i]["date"].find("|")+2 :])
        
        if len(news.select("a > img")) == 0:
            result[i]["img"] = "None"
        else:
            result[i]["img"] = url + news.select("a > img")[0].get("src")
            
    result = json.dumps(result, indent = 4, ensure_ascii = False)
    return result