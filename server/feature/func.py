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