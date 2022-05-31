from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
import requests
from sympy import content


class Stock(ABC):
    def _init_(self, number ):
        self.number = number #股票代號

    @abstractmethod

    def scrape(self):

        pass



#股票爬蟲
class GetStock(Stock):

    def scrape(self):
        response = requests.get(
         "https://tw.stock.yahoo.com/quote/"+self.number+".TW")

        soup = BeautifulSoup(response.content, "html.parser")

        #爬取股票資訊
        
        Volume = soup.find("span",{"class":"Fw(600) Fz(16px)--mobile Fz(14px) D(f) Ai(c) C($c-trend-up)"}).getText()
        
        Close = soup.find("span",{"class":"Jc(fe) Fz(20px) Lh(1.2) Fw(b) D(f) Ai(c) C($c-trend-up"}).getText()

        return content