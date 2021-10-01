from flask import Flask, Response, jsonify
from bs4 import BeautifulSoup
import json
import requests

from feature import boannews

app = Flask(__name__)

@app.route('/')
def main():
    res = Response("who are you")
    res.headers["Access-Control-Allow-Origin"] = "*"

    return res
    
@app.route("/boannews")
def get_boannews():
    result = boannews.getData()
    return response(result)

@app.route("/dailysecu")
def dailysecu():
    url = "https://www.dailysecu.com"
    result = []
    
    res = requests.get("https://www.dailysecu.com/news/articleList.html?view_type=sm", headers = fakeUserAgent())
    soup = BeautifulSoup(res.content, "html.parser", from_encoding="euc-kr")
    
    news_list = soup.select(".list-block")
    
    for i, news in enumerate(news_list):
        result.append({})
        result[i]["title"] = news.select(".list-titles")[0].get_text()
        result[i]["link"] = url + news.select(".list-titles > a")[0].get("href")
        result[i]["date"] = news.select(".list-dated")[0].get_text()
        result[i]["date"] = replaceDate(result[i]["date"][result[i]["date"].find(" |", 3) + 3 : ])
        
        if len(news.select(".list-image")) == 0:
            result[i]["img"] = "None"
        else:
            test = news.select(".list-image")[0]["style"]
            test = url + "/news" + test[test.find("(.") + 2 : len(test)-1]
            result[i]["img"] = test
    
    result = json.dumps(result, indent = 4, ensure_ascii = False)
    
    return response(result)
    

# @app.route("/naver_realtime")
# def naver_realtime():
#     url = "https://datalab.naver.com/keyword/realtimeList.naver?age=all&where=main"
#     result = []

#     options = webdriver.ChromeOptions()
#     options.add_argument('headless')
#     options.add_argument("disable-gpu")
#     options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
    
#     driver = webdriver.Chrome(executable_path='/var/www/universal/chromedriver', chrome_options=options)
#     driver.implicitly_wait(10)
    
#     driver.get(url)

#     ranking_list = driver.find_elements_by_css_selector("span.item_title")
#     for i, rank_list in enumerate(ranking_list):
#         result.append({})
        
#         result[i]["rank"] = i+1
#         result[i]["rank_name"] = rank_list.text
#         result[i]["url"] = "https://search.naver.com/search.naver?query=" + rank_list.text
    
#     result = json.dumps(result, indent = 4, ensure_ascii = False)
    
#     driver.close()
#     return response(result)

@app.route("/changwon_computer")
def changwon_computer():
    url = "http://www.changwon.ac.kr/ce/na/ntt/selectNttList.do?mi=6627&bbsId=2187"
    post_url = "http://www.changwon.ac.kr/ce/na/ntt/selectNttInfo.do?mi=6627&nttSn={}"
    result = []
    
    res = requests.get(url, headers = fakeUserAgent())
    soup = BeautifulSoup(res.content, "html.parser", from_encoding="euc-kr")
    
    board_lists = soup.select("#nttTable > tbody > tr")
    
    for i, board_list in enumerate(board_lists):
        result.append({})
        
        if len(board_list.select(".btn_red")) != 0:
            result[i]["notice"] = "true"
            result[i]["title"] = board_list.select(".nttInfoBtn")[0].get_text().strip()[2:]
        else:
            result[i]["notice"] = "false"
            result[i]["title"] = board_list.select(".nttInfoBtn")[0].get_text().strip()
            
        result[i]["date"] = replaceDate(board_list.select("td")[3].get_text())
        result[i]["link"] = post_url.format(board_list.select("a")[0].get("data-id"))
    
    result = json.dumps(result, indent = 4, ensure_ascii = False)
    
    return response(result)

@app.route("/changwon_waggle")
def changwon_waggle():
    url = "http://portal.changwon.ac.kr/homePost/list.do?common=portal&homecd=portal&bno=1291"
    post_url = "http://portal.changwon.ac.kr/homePost/"
    result = []
    
    res = requests.get(url, headers = fakeUserAgent())
    soup = BeautifulSoup(res.content, "html.parser", from_encoding = "euc-kr")
    
    board_lists = soup.select(".board-list > tbody > tr")
    for i, board_list in enumerate(board_lists):
        result.append({})
        
        if len(board_list.select("td > img")) != 0:
            result[i]["notice"] = "true"
        else:
            result[i]["notice"] = "false"
            
        result[i]["title"] = board_list.select(".left > a")[0].get_text().strip()
        result[i]["link"] = post_url + board_list.select(".left > a")[0].get("href")
        result[i]["date"] = replaceDate(board_list.select("td")[2].get_text().strip())
    
    result = json.dumps(result, indent = 4, ensure_ascii = False)
    return response(result)
    
@app.route("/kisa_notice")
def kisa_notice():
    url = "https://www.kisa.or.kr/notice/notice_List.jsp"
    result = []
    
    res = requests.get(url, headers = fakeUserAgent())
    soup = BeautifulSoup(res.content, "html.parser", from_encoding = "euc-kr")
    
    board_lists = soup.select(".bbs_lst > tbody > tr")
    for i, board_list in enumerate(board_lists):
        if i == 5:
            break
        
        result.append({})
        result[i]["title"] = board_list.select(".lft > a")[0].get_text().strip()
        result[i]["link"] = "https://www.kisa.or.kr/" + board_list.select(".lft > a")[0].get("href")
        result[i]["date"] = replaceDate(board_list.select("td")[2].get_text().strip())
    
    result = json.dumps(result, indent = 4, ensure_ascii = False)
    return response(result)

def response(data):
    res = Response(data);
    res.headers["Access-Control-Allow-Origin"] = "*"
    
    return res
    
def fakeUserAgent():
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }

def replaceDate(date):
    date = date.replace("년 ", ".")
    date = date.replace("월 ", ".")
    date = date.replace("일", "")
    date = date.replace("-", ".")
    
    return date

if __name__ == '__main__':
    app.run(port = 7202, debug=True);