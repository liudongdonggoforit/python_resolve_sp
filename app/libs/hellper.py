import re
import requests
from app.libs.headers import common_headers, tutu_header
from flask import current_app
import json


def get_location(url):
    html = requests.get(url, headers=common_headers, allow_redirects=False)
    location_url = html.headers['Location'];
    print(html.headers)
    print(location_url)
    return location_url


def get_url(url):
    html = requests.get(url, allow_redirects=False)
    download_url = html.headers['Location'];
    print(download_url)
    text = requests.get(download_url, headers=common_headers).text
    pat = re.compile('playAddr:(.*?)cover', re.S)
    result = pat.findall(text)[0]
    return result


def get_tutu(short_url):
    """
    {sourceUrl: "http://vm.tiktok.com/JQ6Qat/", flatform: 18}
    获取解析结果
    :return:
    """
    data = {"sourceUrl": str(short_url), "flatform": "18"}
    if 'tiktok' in str(short_url):
        referer = "http://www.tutujiexi.com/tiktok.html"
        data["flatform"] = "18"
    elif 'douyin' in str(short_url):
        referer = "http://www.tutujiexi.com/douyin.html"
        data["flatform"] = "1"
    elif 'tiktok' in str(short_url):
        referer = "http://www.tutujiexi.com/douyin.html"
        data["flatform"] = "2"
    elif 'tiktok' in str(short_url):
        referer = "http://www.tutujiexi.com/tiktok.html"
        data["flatform"] = "18"
    elif 'tiktok' in str(short_url):
        referer = "http://www.tutujiexi.com/tiktok.html"
        data["flatform"] = "18"
    elif 'tiktok' in str(short_url):
        referer = "http://www.tutujiexi.com/tiktok.html"
        data["flatform"] = "18"
    tutu_header['Referer'] = referer
    print(data)
    r = requests.post(current_app.config['TUTU_URL'], data=json.dumps(data), headers=tutu_header).text
    return r

