#-*- coding: utf-8 -*-
class air_Exception(Exception):

      def __init__(self,msg=' air-ng Exception'):
          self._msg = msg
          
      def __str__(self):
          return self._msg
          
class air_ConnectionError(air_Exception):

      def __init__(self,msg='Internet Connection Error'):
          super().__init__(msg)

      def __str__(self):
          return self._msg
      

class air_ErrorSchema(air_Exception):

      def __init__(self,msg='No Scheme is Used'):
          super().__init__(msg)

      def __str__(self):
          return self._msg

class air_ConnectionTimeout(air_Exception):

      def __init__(self,msg="Internet Connection Timeout"):
          super().__init__(msg)

      def __str__(self):
          return self._msg
      