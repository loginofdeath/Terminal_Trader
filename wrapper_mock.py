
import pandas as pd
import json
import requests

class Markit:       
    def __init__(self):
        self.lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json"
        self.quote_url  = "http://dev.markitondemand.com/Api/v2/Quote/json"
    @classmethod
    def company_search(self,company):
        url="http://dev.markitondemand.com/Api/v2/Lookup/json"+"?input="+company
        #x = requests.get(url)
        #page=x.content
        #page=str(page,'utf-8')
        #page=json.loads(page)
        #page=page[0]
        df=pd.read_json(url,orient='index')
        return (df)

        
       
    
    @classmethod
    def get_quote(self,company):
        url="http://dev.markitondemand.com/Api/v2/Quote/json"+"?symbol="+company
        x = requests.get(url)
        page=x.content
        page=str(page,'utf-8')
        page=json.loads(page)
        df=pd.Series(page)
        return (df)
