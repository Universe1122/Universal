from flask import Flask, Response, jsonify
from bs4 import BeautifulSoup
import json
import requests
from selenium import webdriver
import time

from feature import boannews

app = Flask(__name__)

boannews_result = []
dailysecu_result = []
changwon_computer_result = []
changwon_waggle_result = []
kisa_result = []
hackerone_result = []

@app.route('/')
def main():
    res = Response("who are you")
    res.headers["Access-Control-Allow-Origin"] = "*"

    return res
    
@app.route("/boannews")
def get_boannews():
    if len(boannews_result) != 0 and time.time() - float(boannews_result[0]["cache"]) <= 5 * 60:
        result = json.dumps(boannews_result, indent = 4, ensure_ascii = False)
        return response(result)

    url = "https://www.boannews.com"
    del boannews_result[:]
        
    res = requests.get("https://www.boannews.com/media/t_list.asp", headers = fakeUserAgent())
    soup = BeautifulSoup(res.content.decode("euc-kr") , "html.parser", from_encoding='euc-kr')
    
    news_list = soup.select(".news_list")
    
    for i, news in enumerate(news_list):
        boannews_result.append({})
        boannews_result[i]["link"] = url + news.select("a")[0].get("href")
        boannews_result[i]["title"] = news.select(".news_txt")[0].get_text()
        boannews_result[i]["date"] = news.select(".news_writer")[0].get_text()
        boannews_result[i]["date"] = replaceDate(boannews_result[i]["date"][boannews_result[i]["date"].find("|")+2 :])
        boannews_result[i]["cache"] = time.time()

        if len(news.select("a > img")) == 0:
            boannews_result[i]["img"] = "None"
        else:
            boannews_result[i]["img"] = url + news.select("a > img")[0].get("src")
    
    result = json.dumps(boannews_result, indent = 4, ensure_ascii = False)
    return response(result)

@app.route("/dailysecu")
def dailysecu():
    if len(dailysecu_result) != 0 and time.time() - float(dailysecu_result[0]["cache"]) <= 5 * 60:
        result = json.dumps(dailysecu_result, indent = 4, ensure_ascii = False)
        return response(result)

    url = "https://www.dailysecu.com"
    del dailysecu_result[:]
    
    res = requests.get("https://www.dailysecu.com/news/articleList.html?view_type=sm", headers = fakeUserAgent())
    soup = BeautifulSoup(res.content, "html.parser", from_encoding="euc-kr")
    
    news_list = soup.select(".list-block")
    
    for i, news in enumerate(news_list):
        dailysecu_result.append({})
        dailysecu_result[i]["title"] = news.select(".list-titles")[0].get_text()
        dailysecu_result[i]["link"] = url + news.select(".list-titles > a")[0].get("href")
        dailysecu_result[i]["date"] = news.select(".list-dated")[0].get_text()
        dailysecu_result[i]["date"] = replaceDate(dailysecu_result[i]["date"][dailysecu_result[i]["date"].find(" |", 3) + 3 : ])
        dailysecu_result[i]["cache"] = time.time()
        
        if len(news.select(".list-image")) == 0:
            dailysecu_result[i]["img"] = "None"
        else:
            test = news.select(".list-image")[0]["style"]
            test = url + "/news" + test[test.find("(.") + 2 : len(test)-1]
            dailysecu_result[i]["img"] = test
    
    result = json.dumps(dailysecu_result, indent = 4, ensure_ascii = False)
    
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
    if len(changwon_computer_result) != 0 and time.time() - float(changwon_computer_result[0]["cache"]) <= 5 * 60:
        result = json.dumps(changwon_computer_result, indent = 4, ensure_ascii = False)
        return response(result)

    url = "http://www.changwon.ac.kr/ce/na/ntt/selectNttList.do?mi=6627&bbsId=2187"
    post_url = "http://www.changwon.ac.kr/ce/na/ntt/selectNttInfo.do?mi=6627&nttSn={}"
    
    del changwon_computer_result[:]
    
    res = requests.get(url, headers = fakeUserAgent())
    soup = BeautifulSoup(res.content, "html.parser", from_encoding="euc-kr")
    
    board_lists = soup.select("#nttTable > tbody > tr")
    
    for i, board_list in enumerate(board_lists):
        changwon_computer_result.append({})
        
        if len(board_list.select(".btn_red")) != 0:
            changwon_computer_result[i]["notice"] = "true"
            changwon_computer_result[i]["title"] = board_list.select(".nttInfoBtn")[0].get_text().strip()[2:]
        else:
            changwon_computer_result[i]["notice"] = "false"
            changwon_computer_result[i]["title"] = board_list.select(".nttInfoBtn")[0].get_text().strip()
            
        changwon_computer_result[i]["date"] = replaceDate(board_list.select("td")[3].get_text())
        changwon_computer_result[i]["link"] = post_url.format(board_list.select("a")[0].get("data-id"))
        changwon_computer_result[i]["cache"] = time.time()
    
    result = json.dumps(changwon_computer_result, indent = 4, ensure_ascii = False)
    
    return response(result)

@app.route("/changwon_waggle")
def changwon_waggle():
    if len(changwon_waggle_result) != 0 and time.time() - float(changwon_waggle_result[0]["cache"]) <= 5 * 60:
        result = json.dumps(changwon_waggle_result, indent = 4, ensure_ascii = False)
        return response(result)

    url = "http://portal.changwon.ac.kr/homePost/list.do?common=portal&homecd=portal&bno=1291"
    post_url = "http://portal.changwon.ac.kr/homePost/"
    del changwon_waggle_result[:]
    
    res = requests.get(url, headers = fakeUserAgent())
    soup = BeautifulSoup(res.content, "html.parser", from_encoding = "euc-kr")
    
    board_lists = soup.select(".board-list > tbody > tr")
    for i, board_list in enumerate(board_lists):
        changwon_waggle_result.append({})
        
        if len(board_list.select("td > img")) != 0:
            changwon_waggle_result[i]["notice"] = "true"
        else:
            changwon_waggle_result[i]["notice"] = "false"
            
        changwon_waggle_result[i]["title"] = board_list.select(".left > a")[0].get_text().strip()
        changwon_waggle_result[i]["link"] = post_url + board_list.select(".left > a")[0].get("href")
        changwon_waggle_result[i]["date"] = replaceDate(board_list.select("td")[2].get_text().strip())
        changwon_waggle_result[i]["cache"] = time.time()

    result = json.dumps(changwon_waggle_result, indent = 4, ensure_ascii = False)
    return response(result)
    
@app.route("/kisa_notice")
def kisa_notice():
    if len(kisa_result) != 0 and time.time() - float(kisa_result[0]["cache"]) <= 5 * 60:
        result = json.dumps(kisa_result, indent = 4, ensure_ascii = False)
        return response(result)

    url = "https://www.kisa.or.kr/notice/notice_List.jsp"
    del kisa_result[:]
    
    res = requests.get(url, headers = fakeUserAgent())
    soup = BeautifulSoup(res.content, "html.parser", from_encoding = "euc-kr")
    
    board_lists = soup.select(".bbs_lst > tbody > tr")
    for i, board_list in enumerate(board_lists):
        if i == 5:
            break
        
        kisa_result.append({})
        kisa_result[i]["title"] = board_list.select(".lft > a")[0].get_text().strip()
        kisa_result[i]["link"] = "https://www.kisa.or.kr/" + board_list.select(".lft > a")[0].get("href")
        kisa_result[i]["date"] = replaceDate(board_list.select("td")[2].get_text().strip())
        kisa_result[i]["cache"] = time.time()
    
    result = json.dumps(kisa_result, indent = 4, ensure_ascii = False)
    return response(result)

@app.route("/hackerone")
def hackerone():
    if len(hackerone_result) != 0 and time.time() - float(hackerone_result[0]["cache"]) <= 5 * 60:
        result = json.dumps(hackerone_result, indent = 4, ensure_ascii = False)
        return response(result)

    url = "https://hackerone.com/hacktivity?querystring=&filter=type:public&order_direction=DESC&order_field=latest_disclosable_activity_at&followed_only=false&collaboration_only=false"
    del hackerone_result[:]

    driver = initSelenium()
    driver.get(url)
    driver.implicitly_wait(3)
    time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    board_list = soup.select("div.card > div.card__content > div.infinite-scroll-component__outerdiv > div.infinite-scroll-component > div.fade")

    if len(board_list) == 0:
        hackerone_result.append({"result" : "error", "cache" : time.time()})
    else:
        for l in board_list:
            hackerone_result.append({
                "up_cnt" : l.select("span")[0].text,
                "title" : l.select("strong")[0].text,
                "target" : l.select("strong > a.daisy-link")[1].text, # l.select("strong > a.daisy-link")[1]["href"]
                "severity" : l.select("div.spec-severity-rating")[0].text,
                "image" : l.select("img.daisy-avatar--medium")[0]["src"],
                "timestamp" : l.select("span.spec-hacktivity-item-timestamp")[0].text,
                "link" : l.select("a.hacktivity-item__publicly-disclosed")[0]["href"],
                "cache" : time.time()
            })

    driver.close()
    result = json.dumps(hackerone_result, indent = 4, ensure_ascii = False)
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

def initSelenium():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome("./chromedriver", options=options)
    return driver

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 7202, debug=True)