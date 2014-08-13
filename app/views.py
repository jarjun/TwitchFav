from flask import render_template
from app import app
import requests

@app.route('/')
def default():
	return render_template("rootpage.html")

@app.route('/<name>')
def index(name):
	p = {"limit": 50}
	r = requests.get("https://api.twitch.tv/kraken/users/"+name+"/follows/channels", params = p)
	r = r.json()
	channellist = []
	for key in r["follows"]:
		streamname = key["channel"]["name"]
		stream = requests.get("https://api.twitch.tv/kraken/streams/" + streamname)
		stream = stream.json()
		if stream["stream"] != None:
			channellist.append((stream["stream"]["viewers"], streamname))

	channellist = sorted(channellist)
	fin = channellist[-1][1]
	return render_template("stream.html", top = fin)

@app.route('/<name>/<pos>')
def indexpos(name,pos):
	p = {"limit": 50}
	r = requests.get("https://api.twitch.tv/kraken/users/"+name+"/follows/channels", params = p)
	r = r.json()
	channellist = []
	for key in r["follows"]:
		streamname = key["channel"]["name"]
		stream = requests.get("https://api.twitch.tv/kraken/streams/" + streamname)
		stream = stream.json()
		if stream["stream"] != None:
			channellist.append((stream["stream"]["viewers"], streamname))

	channellist = sorted(channellist)
	fin = channellist[-int(pos)][1]
	return render_template("stream.html", top = fin)