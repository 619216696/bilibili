from bilibili.items import BilibiliItem
from bilibili.mysql import sql
import requests
import scrapy
import json
import time
import random

class bilibili(scrapy.Spider):

    name = 'bilibili'
    allowed_domains = ['bilibili.com']
    url = 'http://space.bilibili.com/ajax/member/GetInfo'

    uas = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
        'Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
        'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
        'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
        'Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)']

    #proxies = [
    #    'http://124.42.118.242:3128',
    #    'http://118.178.124.33:3128',
    #    'http://120.132.71.212:80',
    #    'http://139.129.166.68:3128',
    #    'http://171.36.182.202:8118',
    #    'http://117.78.37.198:8000',
    #    'http://111.155.116.235:8123',

#]

    def start_requests(self):
        results = sql.not_requests()
        for i in range(0,len(results)):
            time.sleep(random.uniform(3,4))
            ua = random.choice(self.uas)
            head = {
                'Referer': 'http://space.bilibili.com/' + str(random.randint(10000, 20000)) + '/',
                'User-Agent': ua
            }
            payload = {
                'mid':str(results[i][0]),
                #'csrf': 'null'
            }
           # proxy = random.choice(self.proxies)
            yield scrapy.FormRequest(url=self.url,formdata=payload,callback=self.parse,headers=head,meta={'page':str(results[i][0])})

    def parse(self, response):
        try:
            sql.delete_requested(response.meta['page'])
            item = BilibiliItem()
            jsdict = json.loads(response.text)
            jsdata = jsdict['data']
            item['name_'] = str(jsdata['name'])
            item['uid'] = jsdata['mid']
            item['play_num'] = jsdata['playNum']
            item['sex'] = jsdata['sex']
            if 'birthday' in jsdata.keys():
                item['birthday'] = jsdata['birthday'][5:]
            else:
                item['birthday'] = ''
            if 'place' in jsdata.keys():
                item['area'] = jsdata['place']
            else:
                item['area'] = ''
            if 'regtime' in jsdata.keys():
                reg_time = time.localtime(jsdata['regtime'])
                item['reg_time'] = time.strftime('%Y-%m-%d',reg_time)
            else:
                item['reg_time'] = ''
            item['coins'] = jsdata['coins']
            item['article'] = jsdata['article']
            item['level_'] = jsdata['level_info']['current_level']
            item['exp'] = jsdata['level_info']['current_exp']
            item['description'] = jsdata['description']
            url = 'http://api.bilibili.com/x/relation/stat?vmid='+response.meta['page']+'&jsonp=jsonp'
            try:
                data = requests.get(url).text
                js_fans = json.loads(data)
                item['following'] = js_fans['data']['following']
                item['fans'] = js_fans['data']['follower']
            except:
                pass
            return item
        except:
            print('uid:%d 不存在'%(int(response.meta['page'])))



