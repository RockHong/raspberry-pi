import argparse
import urllib2
import subprocess
import json

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