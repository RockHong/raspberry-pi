import argparse
import urllib2
import subprocess
import json
from HTMLParser import HTMLParser
from datetime import date

{
  'aqi': {
    'date': '',
    'index': 
  }
  'hourly': {
    'date': '',
    8： {
      'condition': '',
      'temp': '',
      'wind': ''
    }
  }
}
class HourlyEntry:
    def __init__(self, c, t, w):
        self.condition = c
        self.temp = t
        self.wind = w

class HourlyData:
    def __init__(self):
        self.date = ''
        self.hours = ''
        
class AQIData:
    def __init__(self):
        self.date = ''
        self.index = ''
        
class WeatherData:
    def __init__(self):
        self.data = {'aqi': AQIData(), 'hourly': HourlyData()}
        
    def getAqiData(self):
        return self.data['aqi']
        
    def getHourlyData(self):
        return self.data['hourly']
        

class WeatherService:
    def __init__(self):
        pass
        
    def getData(self):
        data = WeatherData()
        self.fetchHourlyData(data.getHourlyData())
        self.fetchAqiData(data.getAqiData())
        return data
        
    def fetchHourlyData(self, data):
        self.fetchHourlyData_1(data)
    
    def fetchAqiData(self, data):
        self.fetchAqiData_1(data)
        
    def fetchHourlyData_1(self, data):
        f = urllib2.urlopen('http://www.weather.com.cn/weather1d/101020100.shtml')
        page = f.read()
        p = HourlyParser()
        p.feed(page)
        rawHourData = p.getData()
        # example data
        # {"1d":["17日20时,n01,多云,2℃,西北风,微风","17日23时,n00,晴,1℃,西北风,微风","18日02时,n00,晴,2℃,西北风,微风","18日05时,n00,晴,2℃,西北风,微风","18日08时,d00,晴,2℃,西北风,微风","18日11时,d01,多云,8℃,无持续风向,微风","18日14时,d01,多云,8℃,无持续风向,微风","18日17时,d01,多云,8℃,无持续风向,微风","18日20时,n01,多云,7℃,无持续风向,微风"],"23d":[["19日08时,d01,多云,6℃,无持续风向,微风","19日11时,d01,多云,9℃,东北风,微风","19日14时,d01,多云,11℃,东北风,微风","19日17时,d01,多云,11℃,东北风,微风","19日20时,n01,多云,10℃,东北风,微风","19日23时,n02,阴,9℃,东风,微风","20日02时,n02,阴,9℃,东风,微风","20日05时,n02,阴,9℃,东风,微风"],["20日08时,d02,阴,8℃,东风,微风","20日11时,d07,小雨,10℃,东南风,微风","20日14时,d07,小雨,12℃,东南风,微风","20日17时,d07,小雨,11℃,东南风,微风","20日20时,n07,小雨,10℃,东南风,微风","21日02时,n08,中雨,8℃,东南风,微风"]],"7d":[["17日20时,n01,多云,2℃,西北风,微风","17日23时,n00,晴,1℃,西北风,微风","18日02时,n00,晴,2℃,西北风,微风","18日05时,n00,晴,2℃,西北风,微风"],["18日08时,d00,晴,2℃,西北风,微风","18日11时,d01,多云,8℃,无持续风向,微风","18日14时,d01,多云,8℃,无持续风向,微风","18日17时,d01,多云,8℃,无持续风向,微风","18日20时,n01,多云,7℃,无持续风向,微风","18日23时,n01,多云,6℃,无持续风向,微风","19日02时,n01,多云,5℃,无持续风向,微风","19日05时,n01,多云,6℃,无持续风向,微风"],["19日08时,d01,多云,6℃,无持续风向,微风","19日11时,d01,多云,9℃,东北风,微风","19日14时,d01,多云,11℃,东北风,微风","19日17时,d01,多云,11℃,东北风,微风","19日20时,n01,多云,10℃,东北风,微风","19日23时,n02,阴,9℃,东风,微风","20日02时,n02,阴,9℃,东风,微风","20日05时,n02,阴,9℃,东风,微风"],["20日08时,d02,阴,8℃,东风,微风","20日11时,d07,小雨,10℃,东南风,微风","20日14时,d07,小雨,12℃,东南风,微风","20日17时,d07,小雨,11℃,东南风,微风","20日20时,n07,小雨,10℃,东南风,微风","21日02时,n08,中雨,8℃,东南风,微风"],["21日08时,d08,中雨,10℃,东南风,微风","21日14时,d01,多云,12℃,北风,微风","21日20时,n07,小雨,10℃,北风,微风","22日02时,n07,小雨,10℃,北风,微风"],["22日08时,d07,小雨,10℃,北风,微风","22日14时,d07,小雨,11℃,东风,微风","22日20时,n07,小雨,10℃,东风,微风","23日02时,n07,小雨,9℃,东风,微风"],["23日08时,d07,小雨,10℃,东风,微风","23日14时,d07,小雨,10℃,北风,微风","23日20时,n08,中雨,8℃,北风,微风","24日02时,n07,小雨,7℃,北风,微风"],["24日08时,d07,小雨,8℃,北风,微风","24日14时,d02,阴,8℃,北风,微风","24日20时,n02,阴,8℃,北风,微风"]]}
        jsonHourData = json.loads(rawHourData)
        todayData = jsonHourData['id']
        date.today().day

    
    def fetchAqiData_1(self, data):
        response = subprocess.check_output(['curl', 'http://d1.weather.com.cn/sk_2d/101020100.html', 
        '-H', 'Pragma: no-cache', 
        '-H', 'Cookie: vjuids=cc982ae83.151adc397b0.0.94b8f9f; f_city=%E5%8D%8E%E7%9B%9B%E9%A1%BF%E7%89%B9%E5%8C%BA%7C401010100%7C; vjlast=1450319255.1450319255.30; __asc=c5b3f9e5151ae41f4de34c9e91e; __auc=e1e1ae94151adcfeca5b9bc66cf; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1450327272,1450327299,1450327835,1450327845; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1450328523', 
        '-H', 'Accept-Encoding: gzip, deflate, sdch', 
        '-H', 'Accept-Language: zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4', 
        '-H', 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36', 
        '-H', 'Accept: */*', 
        '-H' 'Cache-Control: no-cache', 
        '-H', 'Referer: http://www.weather.com.cn/weather1d/101020100.shtml', 
        '-H', 'Proxy-Connection: keep-alive', '--compressed'])
        
        # response example
        # var dataSK = {"nameen":"shanghai","cityname":"上海","city":"101020100","temp":"3","tempf":"37","WD":"北风","wde":"N ","WS":"0级","wse":"","SD":"35%","time":"17:24","weather":"多云","weathere":"Cloudy","weathercode":"d01","qy":"1035","njd":"暂无实况","sd":"35%","aqi":"45","date":"12月17日(星期四)"}
        response = response[response.find('{'):]
        parsed = json.loads(response)
        data.index = parsed['aqi']
        data.date = parsed['date'] + ' ' + parsed['time']
        
        
class HourlyParser(HTMLParser):
    def __init__(self):
        self.foundTag = false
        self.data = ''
        
    def handle_starttag(self, tag, attrs):
        if tag == 'script':
            self.foundTag = true
        else:
            self.foundTag = false
            
    def handle_endtag(self, tag):
        self.foundTag = false

    def handle_data(self, data):
        if self.foundTag and data.find('hour3data') != -1:
            data = data.strip()
            self.data = data[data.find('{'):]
        
    def getData(self):
        return self.data

if __name__ == '__main__':



$ curl 'http://d1.weather.com.cn/sk_2d/101020100.html' -H 'Pragma: no-cache' -H 'Cookie: vjuids=cc982ae83.151adc397b0.0.94b8f9f; f_city=%E5%8D%8E%E7%9B%9B%E9%A1%BF%E7%89%B9%E5%8C%BA%7C401010100%7C; vjlast=1450319255.1450319255.30; __asc=c5b3f9e5151ae41f4de34c9e91e; __auc=e1e1ae94151adcfeca5b9bc66cf; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1450327272,1450327299,1450327835,1450327845; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1450328523' -H 'Accept-Encoding: gzip, deflate, sdch' -H 'Accept-Language: zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4' -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36' -H 'Accept: */*' -H 'Cache-Control: no-cache' -H 'Referer: http://www.weather.com.cn/weather1d/101020100.shtml' -H 'Proxy-Connection: keep-alive' --compressed

'curl', 'http://d1.weather.com.cn/sk_2d/101020100.html', '-H', 'Pragma: no-cache', '-H', 'Cookie: vjuids=cc982ae83.151adc397b0.0.94b8f9f; f_city=%E5%8D%8E%E7%9B%9B%E9%A1%BF%E7%89%B9%E5%8C%BA%7C401010100%7C; vjlast=1450319255.1450319255.30; __asc=c5b3f9e5151ae41f4de34c9e91e; __auc=e1e1ae94151adcfeca5b9bc66cf; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1450327272,1450327299,1450327835,1450327845; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1450328523', '-H', 'Accept-Encoding: gzip, deflate, sdch', '-H', 'Accept-Language: zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4', '-H', 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36', '-H', 'Accept: */*' '-H' 'Cache-Control: no-cache', '-H', 'Referer: http://www.weather.com.cn/weather1d/101020100.shtml', '-H', 'Proxy-Connection: keep-alive', '--compressed'




var dataSK = {"nameen":"shanghai","cityname":"上海","city":"101020100","temp":"3","tempf":"37","WD":"北风","wde":"N ","WS":"0级","wse":"","SD":"35%","time":"17:24","weather":"多云","weathere":"Cloudy","weathercode":"d01","qy":"1035","njd":"暂无实况","sd":"35%","aqi":"45","date":"12月17日(星期四)"}




Request URL:http://www.weather.com.cn/weather1d/101020100.shtml
Request Method:GET
http://www.weather.com.cn/weather1d/101020100.shtml
这个页面会发出其它子请求，比如
Request URL:http://d1.weather.com.cn/sk_2d/101020100.html?_=1450328523869
Request Method:GET
var dataSK = {"nameen":"shanghai","cityname":"上海","city":"101020100","temp":"4","tempf":"39","WD":"西风","wde":"W ","WS":"1级","wse":"&lt;12km/h","SD":"30%","time":"12:42","weather":"多云","weathere":"Cloudy","weathercode":"d01","qy":"1032","njd":"暂无实况","sd":"30%","aqi":"58","date":"12月17日(星期四)"}

{  
   "nameen":"shanghai",
   "cityname":"上海",
   "city":"101020100",
   "temp":"4",
   "tempf":"39",
   "WD":"西风",
   "wde":"W ",
   "WS":"1级",
   "wse":"&lt;12km/h",
   "SD":"30%",
   "time":"12:42",
   "weather":"多云",
   "weathere":"Cloudy",
   "weathercode":"d01",
   "qy":"1032",
   "njd":"暂无实况",
   "sd":"30%",
   "aqi":"58",
   "date":"12月17日(星期四)"
}


Request URL:http://d1.weather.com.cn/dingzhi/101020100.html?_=1450328523869
Request Method:GET
var cityDZ101020100 ={"weatherinfo":{"city":"101020100","cityname":"上海","temp":"5℃","tempn":"1℃","weather":"多云","wd":"西北风","ws":"微风","weathercode":"d1","weathercoden":"n1"}};var alarmDZ101020100 ={"w":[]}

{  
   "weatherinfo":{  
      "city":"101020100",
      "cityname":"上海",
      "temp":"5℃",
      "tempn":"1℃",
      "weather":"多云",
      "wd":"西北风",
      "ws":"微风",
      "weathercode":"d1",
      "weathercoden":"n1"
   }
}
