import base64
import re

from app.web import web
from flask import render_template, jsonify
from app.libs.hellper import get_location, get_url


@web.route("/")
def index():
    return render_template("index.html")


@web.route('/<url>')
def resolve_url(url):
    playAddr = get_url(base64.b64decode(url)).replace(",", "").replace('"', "")
    print(playAddr)
    pat = re.compile('video_id=(.*?)&', re.S)
    filename = pat.findall(playAddr)[0] + ".mp4"

    # download_video(playAddr, filename)
    video_url = get_location(playAddr)
    print(video_url)
    down_url = "http://118.25.217.21:1001/download/videos/" + filename
    return jsonify({'playAddr': playAddr, 'url': down_url})
