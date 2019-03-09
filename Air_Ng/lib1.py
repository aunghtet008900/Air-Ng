#-*- coding: utf-8 -*-
import requests,base64,re
from . import exceptions

class geo_lookup(object):


      def __init__(self,host):
          self.host = host

      def show_all(self):
          return self.__geo()


      def __geo(self):
          try:
             r = requests.get(f"http://ip-api.com/json/{self.host}")
             if r:
                return r.json()
          except ConnectionError:
             raise exceptions.air_ConnectionError('Internet Connection Error')

      @property
      def info_name(self):
          return self.__geo()['as']

      @property
      def city(self):
          return self.__geo()['city']

      @property
      def country(self):
          return self.__geo()['country']

      @property
      def countryCode(self):
          return self.__geo()['countryCode']

      @property
      def isp(self):
          return self.__geo()['isp']

      @property
      def lat(self):
          return self.__geo()['lat']

      @property
      def lon(self):
          return self.__geo()['lon']

      @property
      def org(self):
          return self.__geo()['org']

      @property
      def query(self):
          return self.__geo()['query']

      @property
      def region(self):
          return self.__geo()['region']

      @property
      def regionName(self):
          return self.__geo()['regionName']

      @property
      def status(self):
          return self.__geo()['status']

      @property
      def timezone(self):
          return self.__geo()['timezone']

      @property
      def zip(self):
          return self.__geo()['zip']

class cms_detector(object):

      def __init__(self,target):
          self.target = target
          self.__dat = self.__detect()

      @property
      def data(self):
          return self.__dat

      @property
      def __auth(self):
          return b'GE2DQMTGGNTDCZBYGNRWIYLDMYYDCODBGYYGMN3CGQ2GEZJSMNQWKOJSGQ2DCNRRME2TIYZTHEYDSNJWGFSDCOJRGYYGMMDCMFTDMZDFHA2TONLB'

      def __detect(self):
          try:
              r = requests.get(
              f"https://whatcms.org/APIEndpoint/Detect?key={base64.b32decode(self.__auth).decode('utf-8')}&url={self.target}"
                   )
              if r.json():
                 return r.json()['result']
          except ConnectionError:
              raise exceptions.air_ConnectionError('Internet Connection Error')


class revIp(object):

      __list = []

      def __init__(self,host):
          self.host = host
          self.__rev()

      @property
      def show_list_Ip(self):
          return self.__list

      @property
      def __dat(self):
          if self.host.startswith('https://'): return self.host[8:]
          elif self.host.startswith('http://'): return self.host[7:]
          else: return self.host

      def __rev(self):
          _dat = {'remoteAddress':self.__dat,'key':''}
          try:
              r = requests.post(
                  "https://domains.yougetsignal.com/domains.php",
                  data = _dat
                  )
              if r.json()['status'] == 'Success':
                 for ip in r.json()['domainArray']:
                     revIp.__list.append(ip[0])
                 return revIp.__list
              else:
                 return 'No Reverse Ip Found'
          except ConnectionError:
              raise exceptions.air_ConnectionError('Internet Connection Error')

class traceroute:

      def __init__(self,target):
          self.target = target
          
      def __repr__(self):
          return self.__start()
         
      def __start(self):
          try:
             r = requests.get(f"https://api.hackertarget.com/mtr/?q={self.target}")
             if r:
                return r.text
          except ConnectionError:
             raise exceptions.air_ConnectionError('Internet Connection Error')              

class subdomain(object):

      __hs = []

      def __init__(self,domain):
          self.domain = domain
          self.__site = 'https://dnsdumpster.com/'
          self.__request()
          
      @property
      def list(self):
          return self.__hs

      def __request(self):
          try: 
              __getToken = requests.get(self.__site).text
              __token = re.findall("value=\'(.*?)\'",__getToken)[0]
              _ = requests.post(
                           self.__site,
                           cookies = {'csrftoken':__token },
                           data = {
                                   'csrfmiddlewaretoken': __token,
                                   'targetip': self.domain
                                },
                           headers = {'Referer':self.__site}
                           )
              if _:
                 for host in re.findall('http://(.*?)"',_.text):
                     self.__hs.append(host)
          except ConnectionError:
              raise exceptions.air_ConnectionError('Internet Connection Error')    
              
