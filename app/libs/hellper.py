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
    {pageUrl: "http://vm.tiktok.com/JQ6Qat/", flatform: 18}
    获取解析结果
    :return:
    """
    data = {"pageUrl": str(short_url), "flatform": "18"}
    if 'tiktok' in str(short_url):
        referer = "http://www.tutujiexi.com/"
        data["flatform"] = "18"
    elif 'douyin' in str(short_url):
        referer = "http://www.tutujiexi.com/douyin.html"
        data["flatform"] = "1"
    elif 'kuaishou' in str(short_url)\
            or "baise.m." in str(short_url)\
            or "gifshow" in str(short_url)\
            or "chenzhongtech" in str(short_url)\
            or "kspkg.com" in str(short_url) \
            or "yxixy.com" in str(short_url):
        referer = "http://www.tutujiexi.com/kuaishou.html"
        data["flatform"] = "2"
    elif 'huoshan' in str(short_url)\
            or "aiyayoubin.cn" in str(short_url) \
            or "hotsoon" in str(short_url) \
            or "smzhuhe.com" in str(short_url):
        referer = "http://www.tutujiexi.com/huoshan.html"
        data["flatform"] = "3"
    elif 'meipai.com' in str(short_url):
        referer = "http://www.tutujiexi.com/meipai.html"
        data["flatform"] = "4"
    elif 'immomo' in str(short_url):
        referer = "http://www.tutujiexi.com/momo.html"
        data["flatform"] = "5"
    elif 'xiaoying.tv' in str(short_url):
        referer = "http://www.tutujiexi.com/xiaoying.html"
        data["flatform"] = "6"
    elif 'weishi' in str(short_url):
        referer = "http://www.tutujiexi.com/weishi.html"
        data["flatform"] = "7"
    elif 'weibo' in str(short_url)\
            or "t.cn" in str(short_url):
        referer = "http://www.tutujiexi.com/weibo.html"
        data["flatform"] = "8"
    elif 'miaopai' in str(short_url):
        referer = "http://www.tutujiexi.com/miaopai.html"
        data["flatform"] = "9"
    elif 'music.163.com' in str(short_url):
        referer = "http://www.tutujiexi.com/yunyinyue.html"
        data["flatform"] = "10"
    elif 'xiaokaxiu' in str(short_url):
        referer = "http://www.tutujiexi.com/xiaokaxiu.html"
        data["flatform"] = "11"
    elif 'hulushequ' in str(short_url):
        referer = "http://www.tutujiexi.com/pipixia.html"
        data["flatform"] = "12"
    elif 'doupai.cc' in str(short_url):
        referer = "http://www.tutujiexi.com"
        data["flatform"] = "13"
    elif '.toutiao' in str(short_url)\
            or "365yg.com" in str(short_url):
        referer = "http://www.tutujiexi.com/toutiao.html"
        data["flatform"] = "14"
    elif 'krcom' in str(short_url):
        referer = "http://www.tutujiexi.com/krcom.html"
        data["flatform"] = "15"
    elif 'nani' in str(short_url):
        referer = "http://www.tutujiexi.com/nani.html"
        data["flatform"] = "16"
    elif 'instagram' in str(short_url):
        referer = "http://www.tutujiexi.com/instagram.html"
        data["flatform"] = "17"
    elif 'quanmin' in str(short_url):
        referer = "http://www.tutujiexi.com/quanmin.html"
        data["flatform"] = "19"
    elif 'bcjzjg.com' in str(short_url)\
            or "dongnantang.com.cn" in str(short_url) \
            or "whmzhjy.com" in str(short_url) \
            or "qukantoutiao.net" in str(short_url) \
            or "sh-piano.com" in str(short_url):
        referer = "http://www.tutujiexi.com/quduopai.html"
        data["flatform"] = "20"
    elif 'kg.qq.com' in str(short_url)\
            or "kg1.qq.com" in str(short_url) \
            or "kg2.qq.com" in str(short_url) \
            or "kg3.qq.com" in str(short_url) \
            or "kg4.qq.com" in str(short_url) \
            or "kg5.qq.com" in str(short_url):
        referer = "http://kge.tutujiexi.com"
        data["flatform"] = "21"
    else:
        return {"error": "该平台暂不支持"}

    tutu_header['Referer'] = referer
    print(data)
    r = requests.post(current_app.config['TUTU_URL'], data=json.dumps(data), headers=tutu_header).json()
    if r["data"] is None:
        return json.dumps({"error": "该平台暂不支持"})
    print(type(r['data']))
    result = {"title": r["data"]["title"], "pic_url": r["data"]["coverUrls"][0], "video_url": r["data"]["videoUrls"][0]}
    return json.dumps(result)

