##! /usr/bin/env python
# encoding:utf-8
from get_password import get_password
from chrome_login  import chrome_login


#IPADDRESS input
IPADDRESS= input("input ip address: ")

#get PASSWORD using IP address
PASSWORD = get_password(IPADDRESS)

#login IPMI via web
chrome_login(IPADDRESS,PASSWORD)
