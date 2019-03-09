#-*- coding: utf-8 -*-
import requests,socket,hashlib,re,whois
from requests.exceptions import ConnectionError,MissingSchema,ConnectTimeout
from . import exceptions

class header_check(object):

      def __init__(self,host,timeout=5):
          self.host = host
          self.timeout = timeout

      @property
      def check(self):
          try:
              r = requests.get(self.host,timeout=self.timeout)
              if r.headers:
                 r.headers.update(status=str(r.status_code))
                 r.headers.update(sha256_page=hashlib.sha256(r.content).hexdigest())
                 return r.headers
          except ConnectionError:
              raise exceptions.air_ConnectionError('Internet Connection Error')
          except MissingSchema:
              raise exceptions.air_ErrorSchema('No Schema Available')             
          except ConnectTimeout:
              raise exceptions.air_ConnectionTimeout('Internet Connection Timeout')

class port_scanner():

      __open = []

      def __init__(
                   self,
                   host,
                   list_port_to_scan=[21,22,80,443,465,587,993,995,8000,8080,3306,5666,8443]
                   ):
          '''
          You Can change list port scan !
          '''
          self.host = host
          self.list_port_to_scan = list_port_to_scan
          self.start_scan()


      def __scan(self,port):
          sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          sock.settimeout(0.25)
          res = sock.connect_ex((self.host,port))
          if res == 0:
             port_scanner.__open.append(port)
          sock.close()

      @property
      def start_scan(self):
          for p in self.list_port_to_scan:
              self.__scan(p)

      @property
      def show_port_open(self):
          return port_scanner.__open

class takeover(object):

      def __init__(self,target):
          self.target = target

      @property
      def __dat(self):
          return {'Cargo': '<title>404 &mdash; File not found</title>', 'Tave': '<h1>Error 404: Page Not Found</h1>', 'Shopify': 'Sorry\\, this shop is currently unavailable\\.', 'Webflow': '<p class=\\"description\\">The page you are looking for doesn\\\'t exist or has been moved.</p>', 'Heroku': 'no-such-app.html|<title>no such app</title>|herokucdn.com/error-pages/no-such-app.html', 'Wordpress': 'Do you want to register', 'Tictail': 'to target URL: <a href=\\"https://tictail.com|Start selling on Tictail.', 'Tumbler': "Whatever you were looking for doesn\\'t currently exist at this address.", 'Thinkific': 'You may have mistyped the address or the page may have moved.', 'Fastly': 'Fastly error\\: unknown domain\\:', 'Acquia': 'The site you are looking for could not be found.|If you are an Acquia Cloud customer and expect to see your site at this address', 'Pantheon': 'The gods are wise, but do not know of the site which you seek.', 'Intercom': "This page is reserved for artistic dogs\\.|Uh oh\\. That page doesn\\'t exist</h1>", 'AWS/S3': 'The specified bucket does not exit', 'GetResponse': 'With GetResponse Landing Pages, lead generation has never been easier', 'Brightcove': '<p class=\\"bc-gallery-error-code\\">Error Code: 404</p>', 'Smartling': 'Domain is not configured', 'TeamWork': "Oops - We didn\\'t find your site.", 'ZenDesk': 'Help Center Closed', 'Jetbrains': 'is not a registered InCloud YouTrack.', 'Ghost': 'The thing you were looking for is no longer here\\, or never was', 'Github': "There isn\\'t a Github Pages site here\\.", 'Mashery': 'Unrecognized domain <strong>', 'Desk': "Sorry\\, We Couldn\\'t Find That Page", 'CloudFront': 'ERROR\\: The request could not be satisfied', 'Surge': 'project not found', 'S3Bucket': 'The specified bucket does not exist', 'Kajabi': "<h1>The page you were looking for doesn\\'t exist.</h1>", 'ActiveCampaign': 'alt=\\"LIGHTTPD - fly light.\\"', 'Helpscout': 'No settings were found for this company:', 'Aftership': 'Oops.</h2><p class=\\"text-muted text-tight\\">The page you\\\'re looking for doesn\\\'t exist.', 'Campaignmonitor': 'Double check the URL or <a href=\\"mailto:help@createsend.com', 'Wishpond': '<h1>https://www.wishpond.com/404?campaign=true', 'Bigcartel': '<h1>Oops! We couldn&#8217;t find that page.</h1>', 'Unbounce': 'The requested URL / was not found on this server|The requested URL was not found on this server', 'BitBucket': 'Repository not found', 'Aha': 'There is no portal here \\.\\.\\. sending you back to Aha!', 'Uservoice': 'This UserVoice subdomain is currently available!', 'StatuPage': 'You are being <a href=\\"https://www.statuspage.io\\">redirected', 'Simplebooklet': 'We can\\\'t find this <a href=\\"https://simplebooklet.com', 'Proposify': 'If you need immediate assistance, please contact <a href=\\"mailto:support@proposify.biz', 'Vend': "Looks like you\\'ve traveled too far into cyberspace.", 'Helpjuice': "We could not find what you\\'re looking for.", 'Tilda': 'Domain has been assigned', 'Surveygizmo': 'data-html-name', 'FeedPress': 'The feed has not been found\\.', 'Pingdom': 'pingdom'}

      def detect(self):
          vuln = ""
          not_vuln = 'Not Vulnerability Takeover'
          try:
             resp = requests.get(self.target)
             for a,b in self.__dat.items():
                 if re.search(b,resp.text,re.I) and re.search('[300-499]',str(resp.status_code),re.I):
                    vuln += a
                    break
                 else:
                    pass
             if vuln != "":
                return f'Vulnerability Takeover Found {vuln}'
             else:
                return not_vuln
          except ConnectionError:
             raise exceptions.air_ConnectionError('Internet Connection Error')
          except MissingSchema:
             raise exceptions.air_ErrorSchema('No Schema Available')
          except ConnectTimeout:
             raise exceptions.air_ConnectionTimeout('Internet Connection Timeout')      

class robot(object):

      def __init__(self,target):
          self.target = target

      def __repr__(self):
          return self.__req()

      def __req(self):
          try:
              r = requests.get(f'{self.target}/robots.txt',timeout=5)
              if r.status_code == 200:
                 return r.text
              else:
                 return 'No Robots.txt Found'
          except ConnectionError:
              raise exceptions.air_ConnectionError('Internet Connection Error')
          except MissingSchema:
              raise exceptions.air_ErrorSchema('No Schema Available')
          except ConnectTimeout:
              raise exceptions.air_ConnectionTimeout('Internet Connection Timeout') 

class whois_lookup:

      def __init__(self,host):
          self.host = host

      @property    
      def show_data(self):
          return whois.whois(self.host)

class email_extractor:

      __list = None

      def __init__(self,target):
          self.target = target
          self.__rex = '[\\w\\-][\\w\\-\\.]+@[\\w\\-][\\w\\-\\.]+[a-zA-Z]{1,4}'

      @property
      def search(self):
          try: 
              r = requests.get(self.target,timeout=5)
              _res = re.findall(self.__rex,r.text)
              if _res != []:
                 self.__list = _res
                 return self.__list
              else:
                 return 'No Email Found'
          except ConnectionError:
              raise exceptions.air_ConnectionError('Internet Connection Error')
          except MissingSchema:
              raise exceptions.air_ErrorSchema('No Schema Available')
          except ConnectTimeout:
              raise exceptions.air_ConnectionTimeout('Internet Connection Timeout')
