#-*- coding: utf-8 -*-

import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
from requests import get

def product_qty_crawling(url):
    extract_str = "°³"
    html = get(url)
    bsObject = BeautifulSoup(html.content.decode('euc-kr', 'replace'), "html.parser")

    # prod_exist = bsObject.select_one('#lEmpty > h3').get_text()
    # if prod_exist == "상품을 찾을 수 없습니다.":
    #     return 0, 0, 'None'

    if(bsObject.select_one('#lInfoBody > div.lInfoBody.lInfoRow.lSelected > table > tbody > tr.lInfoQty > td') == None):
        print("상품 없음")
        return 0, 0, 'None'

    cnt = bsObject.select_one('#lInfoBody > div.lInfoBody.lInfoRow.lSelected > table > tbody > tr.lInfoQty > td').get_text()
    cnt = ''.join(x for x in cnt if x not in extract_str)
    cnt = int(''.join(list(filter(str.isdigit, cnt))))

    cost_a = bsObject.select_one('#lInfoBody > div.lInfoBody.lInfoRow.lSelected > table > tbody > tr.lInfoAmt > td > div > div.lItemPrice')
    if cost_a != None:
        cost = bsObject.select_one('#lInfoBody > div.lInfoBody.lInfoRow.lSelected > table > tbody > tr.lInfoAmt > td > div > div.lItemPrice').get_text()
    else:
        cost = 'Have to Check'

    usable = bsObject.select_one('#lInfoView > div.lInfoViewSubWrap > form > table > tbody > tr > td.lInfoViewSubTd2 > div.lInfoViewImgUse > div:nth-child(1) > b').get_text()

    return cnt, cost, usable

# Start!
csv_name = 'Product_20211101_210226.csv'
PL_csv = pd.read_csv(csv_name)
key = '판매자바코드'
name_key = '상품명'
our_qty_key = '재고수량'
our_cost_key = '할인가(PC)'
url_list = PL_csv[key]
name_list = PL_csv[name_key]
our_qty_list = PL_csv[our_qty_key]
our_cost_list = PL_csv[our_cost_key]

for idx in range(url_list.size):
    pd_cnt, cost, pd_usable = product_qty_crawling(url_list[idx])
    print("#" + name_list[idx])
    print('재고 : ' + str(pd_cnt))
    print('현재가격 : ' + str(cost))
    print('사용여부 : ' + pd_usable)

    if pd_usable != '사용허용':
        print(name_list[idx])
        print("이미지 허용 불가!")

    if pd_cnt == 0:
        print("재고 부족")



    # if cost == our_cost_list[idx]:
    #     continue
    # else:
    #     print(name_list[idx])


key_new = 'a'

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

