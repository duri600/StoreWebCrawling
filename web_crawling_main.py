#-*- coding: utf-8 -*-

import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
from requests import get

def product_qty_crawling(url):
    extract_str = "°³"
    html = get(url)
    bsObject = BeautifulSoup(html.content.decode('euc-kr', 'replace'), "html.parser")
    cnt = bsObject.select_one('#lInfoBody > div.lInfoBody.lInfoRow.lSelected > table > tbody > tr.lInfoQty > td').get_text()
    cnt = ''.join(x for x in cnt if x not in extract_str)
    cnt = int(''.join(list(filter(str.isdigit, cnt))))

    usable = bsObject.select_one('#lInfoView > div.lInfoViewSubWrap > form > table > tbody > tr > td.lInfoViewSubTd2 > div.lInfoViewImgUse > div:nth-child(1) > b').get_text()

    return cnt, usable

url1 = 'http://domeggook.com/10612944'

count, usable = product_qty_crawling(url1)

print(count)
print(usable)

# html = urlopen("http://domeggook.com/10612944")
# bsObject = BeautifulSoup(html, "html.parser")
#
# html2 = urlopen("http://domeggook.com/10620103")
# bsObject2 = BeautifulSoup(html2, "html.parser")
#
# cnt1 = bsObject.select_one('#lInfoBody > div.lInfoBody.lInfoRow.lSelected > table > tbody > tr.lInfoQty > td').get_text()
#
# cnt2 = bsObject2.select_one('#lInfoBody > div.lInfoBody.lInfoRow.lSelected > table > tbody > tr.lInfoQty > td').get_text()
#
# extract_str = "°³"
# cnt1 = ''.join( x for x in cnt1 if x not in extract_str)
# cnt1 = int(''.join(list(filter(str.isdigit, cnt1))))
# cnt2 = ''.join( x for x in cnt2 if x not in extract_str)
# cnt2 = int(''.join(list(filter(str.isdigit, cnt2))))
#
# print(cnt1)
# print(cnt2)

