from bs4 import BeautifulSoup
import requests

def scrape(id):
    response = requests.get(
        "https://tw.stock.yahoo.com/quote/"+id+".TW")
    soup = BeautifulSoup(response.content, "html.parser")
    Volumes = soup.find_all(
        'li', {'class': 'price-detail-item H(32px) Mx(16px) D(f) Jc(sb) Ai(c) Bxz(bb) Px(0px) Py(4px) Bdbs(s) Bdbc($bd-primary-divider) Bdbw(1px)'})
    vec = ""
    for Volume in Volumes:
        vec2 = ""
        for df in Volume.select("span"):
            vec2 += df.text + "\t"
        vec += vec2 + "\n"
    return vec

