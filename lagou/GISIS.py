import requests

url = 'https://gisis.imo.org/Public/MCI/Browse.aspx?Form=Incident&Action=View&IncidentID=10953'

headers = {
    'Host': 'gisis.imo.org',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'https://gisis.imo.org/Public/MCI/Search.aspx',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': '_ga=GA1.2.2057353594.1546088042; _gid=GA1.2.1796171618.1546088042; ASP.NET_SessionId=11c5hr1hpa52m1otda4sxdfj; IMOWEBACC=DE255E786697B368F2830FC128161CBA8E790562ECF838CF75CF108DA313BE02A1C39BB345B12556EF20A74FC1F2C9A4BDF617B897448EA7FB2093E175B4F90A0D19AC6AE1E6C5ADA2CFEFF9E54C52DEDB90BB4B18EC19B46A941B2D7342CECFED350DF033F06D3180F9A602C0C01BB58B1F131F556FDAEBAC3BF9CE5D91CC02414F0435; __utma=188917437.2057353594.1546088042.1546091084.1546091084.1; __utmc=188917437; __utmz=188917437.1546091084.1.1.utmcsr=webaccounts.imo.org|utmccn=(referral)|utmcmd=referral|utmcct=/Common/WebLogin.aspx; __utmt=1; __utmb=188917437.11.10.1546091084',
}

response = requests.get(url, headers=headers)
with open('gisis.html', 'w', encoding='utf-8') as f:
    f.write(response.text)