# -*- coding: utf-8 -*-

from urllib.parse import quote


def uri_encode(s):
    # python 3.7 之前，波浪线(~) 不作为保留字符，需要明确指定
    return quote(s, safe='~')


def uri_encode_except_slash(s):
    return quote(s, safe='/~')
