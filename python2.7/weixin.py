#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


def requestWX():
    r = requests.get('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx543ed3903a242eb6&secret=972d0295533d95069c14338296e1bff7')
    print(r.text)

if __name__ == "__main__":
    requestWX()
