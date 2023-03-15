# -*- coding: utf-8 -*-
from flask import Flask
import plivo
import requests
import json


app = Flask(__name__)

@app.route('/send_sms/', methods=['GET','POST'])
def outbound_sms():
    client = plivo.RestClient("Auth_ID","Auth_token")
    response = client.messages.create(
                                  src='11111111111',
                                  dst='To_number',
                                  text='You are receiving a call')
    print(response)

@app.route('/send_sms2/', methods=['GET','POST'])
def outbound_sms1():
    client = plivo.RestClient("Auth_ID","Auth_token")
    response1 = client.messages.create(
                                  src='11111111111',
                                  dst='To_number',
                                  text='You missed a call please check logs')
    print(response1)

@app.route('/dadjoke/' , methods=['GET','POST'])
def dad_joke():
    headers = {'Accept':'text/plain'}
    r = requests.get('https://icanhazdadjoke.com/',headers=headers)
    return(r.text)

if __name__ == "__main__":
    app.run(debug=True)
