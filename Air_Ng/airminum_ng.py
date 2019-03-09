#-*- coding: utf-8 -*-
import sys

class PythonVersionNotSupport:

      def __init__(self,msg='Not Supported For python 2.x please use Python 3.x'):
          self.msg = msg
          
      def __str__(self):
          return self.msg
          
if sys.version[0] in '2':
   raise PythonVersionNotSupport()

from .lib1 import (
      geo_lookup,
      cms_detector,
      revIp,
      traceroute,
      subdomain
)
from .lib2 import (
     header_check,
     port_scanner,
     takeover,
     robot,
     whois_lookup,
     email_extractor     
)

class geoIplookup(geo_lookup):
      pass

class CMSdetector(cms_detector):
      pass

class reverseIplookup(revIp):
      pass

class Traceroute(traceroute):
      pass

class subdomainSearcher(subdomain):
      pass

class InformationHeaders(header_check):
      pass

class subdomainTakeverDetector(takeover):
      pass

class robotTxtDetector(robot):
      pass

class whoisLookup(whois_lookup):
      pass

class emailExtractor(email_extractor):
      pass


      
