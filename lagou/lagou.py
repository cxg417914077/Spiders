import sqlite3, os, requests, random, time
from fake_useragent import UserAgent

ua = UserAgent()

position_path = 'lagou.sqlite'
if os.path.exists(position_path):
    os.remove(position_path)
conn = sqlite3.connect(position_path)
sql = '''
    create table position(
   id integer primary key autoincrement not null,
   companyFullName text not null,
   companyShortName text not null,
   companySize text not null,
   financeStage text not null,
   district text not null,
   positionName text not null,
   workYear text not null,
   education text not null,
   salary text not null,
   positionAdvantage text not null
);
'''
cur = conn.cursor()
cur.execute(sql)
conn.commit()


def get_json(url, num, proxies):
    '从网页获取JSON,使用POST请求,加上头部信息'
    my_headers = {
        'User-Agent': ua.random,
        'Host': 'www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_python?px=new&city=%E5%8C%97%E4%BA%AC',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': 'WEBTJ-ID=20181229085752-167f777a67e0-040b56af7709d1-b781636-1049088-167f777a67f588; _ga=GA1.2.1065870372.1546045073; _gid=GA1.2.1109387087.1546045073; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1546045073; user_trace_token=20181229085754-c6580a12-0b04-11e9-ad85-5254005c3644; LGUID=20181229085754-c6580e42-0b04-11e9-ad85-5254005c3644; X_HTTP_TOKEN=cf90bd453cd9e6575cb0cfb7185ab6b2; sajssdk_2015_cross_new_user=1; JSESSIONID=ABAAABAAADEAAFI5958542B1506C3F01C01F7CDABBF37E1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22167f777f49c177-0c129fd0c9e24f-b781636-1049088-167f777f49d39c%22%2C%22%24device_id%22%3A%22167f777f49c177-0c129fd0c9e24f-b781636-1049088-167f777f49d39c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _putrc=F4C9CE88A8816FE6123F89F2B170EADC; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B71436; hasDeliver=0; index_location_city=%E5%8C%97%E4%BA%AC; TG-TRACK-CODE=search_code; _gat=1; LGSID=20181229110154-18a50380-0b16-11e9-ad85-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_python%3Fpx%3Dnew%26city%3D%25E5%258C%2597%25E4%25BA%25AC; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_python%3Fpx%3Dnew%26yx%3D10k-15k%26city%3D%25E5%258C%2597%25E4%25BA%25AC; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; gate_login_token=ed416bfebf9f5662f49e85e077287d43ab8932d705e4e1aaf54a3d8f286e3eec; LGRID=20181229110237-326a0796-0b16-11e9-ad85-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1546052557; SEARCH_ID=7250c81b8bcc485cbcb0cb4a23d9aad4',
    }

    my_data = {
        'first': 'true',
        'pn': num,
        'kd': 'python'}

    proxies = {'http': proxies}

    res = requests.post(url, headers=my_headers, data=my_data, proxies=proxies)
    res.raise_for_status()
    res.encoding = 'utf-8'
    # 得到包含职位信息的字典
    page = res.json()
    return page


def get_connect(page):
    position_list = page['content']['positionResult']['result']
    for position in position_list:
        companyFullName = position['companyFullName']
        companyShortName = position['companyShortName']
        companySize = position['companySize']
        financeStage = position['financeStage']
        district = position['district']
        positionName = position['positionName']
        workYear = position['workYear']
        education = position['education']
        salary = position['salary']
        positionAdvantage = position['positionAdvantage']


        sql1 = '''
                 insert into position(companyFullName,companyShortName,companySize,financeStage,district,positionName,workYear,education,salary,positionAdvantage) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');
                  ''' % (
        companyFullName, companyShortName, companySize, financeStage, district, positionName, workYear, education,
        salary, positionAdvantage)

        cur.execute(sql1)
        conn.commit()


if __name__ == '__main__':
    f = open('ip.txt', 'r', encoding='utf-8')
    proxies = random.choice(f.read().split('\n'))
    url = 'https://www.lagou.com/jobs/positionAjax.json?px=new&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
    for i in range(30):
        page = get_json(url, i + 1, proxies)
        get_connect(page)
        time.sleep(3)
    f.close()
