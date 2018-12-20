import re
import requests

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'zh-CN,zh;q=0.9',
           'Connection': 'keep-alive',
           'Host': 'aweme.snssdk.com',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/67.0.3396.99 Safari/537.36'}


def get_location(url):
    html = requests.get(url, headers=headers, allow_redirects=False)
    location_url = html.headers['Location'];
    print(html.headers)
    print(location_url)
    return location_url


def get_url(url):
    html = requests.get(url, allow_redirects=False)
    download_url = html.headers['Location'];
    print(download_url)
    text = requests.get(download_url, headers=headers).text
    pat = re.compile('playAddr:(.*?)cover', re.S)
    result = pat.findall(text)[0]
    return result
