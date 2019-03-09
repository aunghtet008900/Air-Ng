<img src="Air.png" width="325" height="328" alt="Air-Ng logo">

<img src="https://img.shields.io/badge/Pypi-19.0.3-blue.svg" alt="pypi">

<img src="https://img.shields.io/badge/build-passing-brightgreen.svg" alt="build passing">
    


##### Description

<br>*Air-Ng* dependencies on Python library, (and command line utilities), Reconnaissance, Information Collection Network and so on</br>

#### Features
<br>*Access information Reconnaissance - Network Gathering* </br><br>

* [*Geo Ip Lookup*](#Geo-Ip-Lookup)
* [*CMS detector*](#Cms-Detector)
* [*Reverse Ip Lookup*](#Reverse-Ip-Lookup)
* [*Traceroute*](#Traceroute)
* [*Subdomain Searcher*](#Subdomain-Searcher)
* [*Information Headers*](#Information-Headers)
* [*Subdomain Takeover Detector*](#Subdomain-Takeover-Detector)
* [*robot.txt Detector*](#Robot.txt-Detector)
* [*Whois Lookup*](#Whois-Lookup)
* [*Email Extractor*](#Email-Extractor)

### Installation
```
# with pip

apt install python
pip3 install Air-Ng

# with Git

apt install git
git clone https://github.com/jaxBCD/Air-Ng.git
cd Air-Ng
python setup.py install

```
# Getting Started

<br>Let's start. How to use it</br>

##### Geo Ip Lookup

<br>Search for a location from an IP address or host</br>
```python
>>> import Air_Ng as air
>>> x = air.geoIplookup('www.google.com')
>>> x.city
'Ashburn'
>>> x.country
'United States'
>>> x.countryCode
'US'
>>> x.host
'www.google.com'
>>> x.info_name
'AS15169 Google LLC'
>>> x.isp
'Google LLC'
>>> x.lat
39.0438
>>> x.lon
-77.4874
>>> x.org
'Google LLC'
>>> x.query
'2404:6800:4003:c04::67'
>>> x.region
'VA'
>>> x.regionName
'Central Singapore Community Development Council'
>>> x.status
'success'
>>> x.timezone
'Asia/Singapore'
>>> x.zip
''
>>> x.show_all()
{'as': 'AS15169 Google LLC', 'city': 'Singapore', 'country': 'Singapore', 'countryCode': 'SG', 'isp': 'Google LLC', 'lat': 1.27623, 'lon': 103.8, 'org': 'Google LLC', 'query': '172.217.194.147', 'region': '01', 'regionName': 'Central Singapore', 'status': 'success', 'timezone': 'Asia/Singapore', 'zip': ''}
>>>
```

##### Cms Detector

<br> detect type cms a web application </br>
```python
>>> import Air_Ng as air
>>> x = air.CMSdetector('www.domain.co.li')
>>> x.data
{'code': 200, 'msg': 'Success', 'id': 1, 'name': 'WordPress', 'confidence': 'high', 'version': '4.8', 'cms_url': 'https://whatcms.org/c/WordPress'}
>>>
```
##### Reverse Ip Lookup

<br>map an IP Address to a sub domain</br>
```python
>>> import Air_Ng as air
>>> x = air.reverseIplookup('www.domain.co.li')
>>> x.show_list_Ip
['domain.co.li', 'domain.col.mek', 'domain.example', 'domain.bo.ol']

```
##### Traceroute

<br>Traceroute to show the route the packet has passed to reach the destination</br>

```python
>>> import Air_Ng as air
>>> air.traceroute('www.google.com')
Start: 2019-03-09T07:17:27+0000
HOST: web01                          Loss%   Snt   Last   Avg  Best  Wrst StDev
  1.|-- 2600:3c00::e6c7:22ff:fe10:9cc1  0.0%     3    4.4   2.3   0.8   4.4   1.8
  2.|-- 2600:3c00:2222:18::1            0.0%     3    0.5   4.1   0.5  11.1   6.1
  3.|-- 2600:3c00:2222:10::1            0.0%     3    2.3   2.7   1.1   4.8   1.9
  4.|-- de-cix.dfw.google.com           0.0%     3    1.9   1.5   1.3   1.9   0.4
  5.|-- 2001:4860:0:11e4::1             0.0%     3    2.4   2.3   2.1   2.4   0.2
  6.|-- 2001:4860:0:1::1a91             0.0%     3    2.7   2.6   2.2   2.8   0.3
  7.|-- dfw28s22-in-x04.1e100.net       0.0%     3    1.6   1.5   1.2   1.6   0.2

```

##### Subdomain Searcher

<br>look for a Host subdomain</br>
```python
>>> import Air_Ng as air
>>> x = air.subdomainSearcher('google.com')
>>> x.list
['google-proxy-64-233-172-0.google.com',...
```
##### Information Headers

<br> Show Headers Information</br>

```python
>>> import Air_Ng as air
>>> x = air.InformationHeaders('https://www.google.com')
>>> x.check
{'Date': 'Sat, 09 Mar 2019 07:28:26 GMT', 
'Expires': '-1', 
'Cache-Control': 'private, max-age=0', 
'Content-Type': 'text/html; charset=ISO-8859-1', 
'P3P': 'CP="This is not a P3P policy! See g.co/p3phelp for more info."', 
'Content-Encoding': 'gzip', 
'Server': 'gws', 
'X-XSS-Protection': '1; mode=block', 
'X-Frame-Options': 'SAMEORIGIN', 
'Set-Cookie': '1P_JAR=2019-03-09-07; expires=Mon, 08-Apr-2019 07:28:26 GMT; path=/; domain=.google.com, NID=162=fC8hFTAmi_uWHcfT29c3wGUEwl2WtK5Yltd293lbzWogVu9Hf4Aj_7pGrWQ2fO7gF69RZgdagFFQZY1WOhuDOmYbAqSyS-cu7ff5u4u72s1FtRlhG9zyXJwrMV6xDCo4pAgdiEtEonthzLGmqpgCTz3huG0hJveykMMOjDrv_iA; expires=Sun, 08-Sep-2019 07:28:26 GMT; path=/; domain=.google.com; HttpOnly', 'Alt-Svc': 'quic=":443"; ma=2592000; v="46,44,43,39"', 'Transfer-Encoding': 'chunked', 
'status': '200', 
'sha256_page': 'ac3de0d749dc7e803f3ee4bd60ac6993c92c1057be3b211ae27e0fc9c82c3b7f'}
```

##### Subdomain Takeover Detector

<br>detect the takeover Subdomain</br>

```python
>>> import Air_Ng as air
>>> x = air.subdomainTakeoverDetector('https://www.domain.co.li')
>>> x.detect()
'Vulnerability Takeover Found Cargo'
>>>
```

##### Robot.txt Detector

<br> Detect Robot.txt file </br>

```python
>>> import Air_Ng as air
>>> x = air.robotTxtDetector('https://www.domain.col.mek')
>>> x
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php
```

##### Whois Lookup

<br>looking for registered users or\n recipients of Internet resource rights</br>

```python
>>> import airminum_ng as air
>>> x = air.whoisLookup('www.google.com')
>>> x.show_data
{'domain_name': ['GOOGLE.COM', 'google.com'], 
'registrar': 'MarkMonitor, Inc.', 
'whois_server': 'whois.markmonitor.com', 'referral_url': None,...
```
##### Email Extractor

<br> extract email that is on a target web </br>

```python
>>> import airminum_ng as air
>>> x = air.emailExtractor('https://www.domain.example')
>>> x.search
['your@email.com', 'domain@example',...

```
