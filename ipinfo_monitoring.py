#!/usr/bin/python3
import unicodedata
import requests
import subprocess
import json

PLUGIN_VERSION=1
HEARTBEAT=True

class ipinfo:

    def __init__(self):
        self.maindata={}
        self.maindata['plugin_version'] = PLUGIN_VERSION
        self.maindata['heartbeat_required']=HEARTBEAT

    def metricCollector(self):
        try:
            result=requests.get("http://ipinfo.io")
            self.maindata.update(dict(result.json()))

            #removing accents from city
            nfkd_form = unicodedata.normalize('NFKD', self.maindata['city'])
            only_ascii = nfkd_form.encode('ASCII', 'ignore')

            self.maindata['city']=only_ascii.decode('utf-8')
            self.maindata['postal']= f"Postal({self.maindata['postal']})"
        except Exception as e:
            self.maindata['msg']=str(e)
            self.maindata['status']=0
        return self.maindata
                



        
    


ip_data=ipinfo()
result=ip_data.metricCollector()
print(json.dumps(result,indent=True))
