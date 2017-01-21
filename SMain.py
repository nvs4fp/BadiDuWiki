# -*- coding:utf-8 -*-
'''
'从百度百科中获得到10000个李姓名人，供我们给宝宝起名用
'08-Jan-2017
'Levi Li
'''
import requests
import re
from bs4 import BeautifulSoup
#start with 盛一伦 出演漂亮的李慧珍-白浩宇
START_URL='http://baike.baidu.com/link?url=_XTJDly7Gw8LrIAkklPJ5ZfaqEXnxchufDxP5u5DQmgbyVtDCHxAn7ci-jeLuv5V1---YPIWpkIYVefjjP9DPzj4aKm6V-BOeD3vecfjsBA1z2rWtusTKSt0tdpVlrEg'
START_URL_M='http://baike.baidu.com/item/%E6%BC%82%E4%BA%AE%E7%9A%84%E6%9D%8E%E6%85%A7%E7%8F%8D/20109279'
'''
Class BaiduSpidler response for raw info getting
#------------------------------------------------------------------------------------'''
class BaiduSpidler():
    def __init__(self,url):
        self.m_target_url=url
        self.m_text=''
    def ConnAndGetRawInfoHtmlFromBaidu(self):
        res=requests.get(self.m_target_url,timeout = 3, allow_redirects = True)
        print('Getting data from : ',self.m_target_url)
        res.encoding = 'utf-8'
        self.m_text=res.text
    def OutPutGetedRawMaterialInfo(self):
        self.ConnAndGetRawInfoHtmlFromBaidu()
        return self.m_text
'''
GetActorProductsInfo Get all the products of one actor
#------------------------------------------------------------------------------------'''
class GetActorProductsInfo():
    def __init__(self,doc):
        self.soup=BeautifulSoup(doc)
        self.movies=[]
    def GetActorProductList(self):
        for a_link in self.soup.find_all('a'):
            if a_link.has_attr('data-lemmaid') and 'item' in a_link['href'] and a_link.string:
                #str_link='%d:'%(idx)+a_link.string+'---http:/baike.baidu.com'+str(a_link.get('href'))
                self.movies.append([a_link.string,'http:/baike.baidu.com'+a_link.get('href')])
        return (self.movies)

'''
GetMovieActorsInfo Get all the actors from one movie
#------------------------------------------------------------------------------------'''
class GetActorsFromMovie():
    def __init__(self,doc):
        self.soup=BeautifulSoup(doc)
        self.actors=[]
    def GetMovieActorsList(self):
        for a_div in self.soup.find_all('div'):
            if a_div.has_attr('id') and a_div['id']=='marqueeViewport_actor':
                self.actors_list=a_div.find_all('a')
                self.GetMovieActorsInfo()
             #print(a_div)
    def GetMovieActorsInfo(self):
        for m_actor in self.actors_list:
            if m_actor.has_attr('data-lemmaid'):
                print(m_actor)
        pass
if __name__=='__main__':
    '''
    c_baiduSpidler=BaiduSpidler(START_URL_M)
    s_rawMaterialInfo=c_baiduSpidler.OutPutGetedRawMaterialInfo()
    m_mySoup=GetActorProductsInfo(s_rawMaterialInfo)
    print(m_mySoup.GetActorProductList())
    '''
    c_baiduSpidler=BaiduSpidler(START_URL_M)
    s_rawMaterialInfo=c_baiduSpidler.OutPutGetedRawMaterialInfo()
    m_mySoup=GetActorsFromMovie(s_rawMaterialInfo)
    m_mySoup.GetMovieActorsList()
