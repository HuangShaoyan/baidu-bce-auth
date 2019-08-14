# -*- coding: utf-8 -*-

import hashlib
import hmac
from datetime import datetime

from .utils import uri_encode, uri_encode_except_slash

BCE_PREFIX = 'x-bce-'


def make_auth(ak, sk, method, path, params, headers):
    canonical_uri = uri_encode_except_slash(path)
    canonical_query_string = _to_canonical_query_string(params)
    canonical_headers = _to_canonical_headers(headers)
    canonical_request = f'{method}\n{canonical_uri}\n{canonical_query_string}\n{canonical_headers}'  # noqa

    timestamp = _to_timestamp()

    auth_string_prefix = f'bce-auth-v1/{ak}/{timestamp}/1800'

    signing_key = hmac.new(
        sk.encode('utf-8'),
        auth_string_prefix.encode('utf-8'),
        hashlib.sha256).hexdigest()

    signature = hmac.new(
        signing_key.encode('utf-8'),
        canonical_request.encode('utf-8'),
        hashlib.sha256).hexdigest()

    return f'bce-auth-v1/{ak}/{timestamp}/1800//{signature}'


def _to_canonical_query_string(params):
    param_list = []
    for k, v in params.items():
        new_k = uri_encode(k)
        if v:
            new_v = uri_encode(str(v))
        else:
            new_v = ''
        param_list.append(f'{new_k}={new_v}')
    return '&'.join(sorted(param_list))


def _to_canonical_headers(headers, headers_to_sign=None):
    headers = headers or {}

    if headers_to_sign is None or len(headers_to_sign) == 0:
        headers_to_sign = {
            'host',
            'content-md5',
            'content-length',
            'content-type',
        }

    result = []
    for k, v in headers.items():
        k_lower = k.strip().lower()

        if k_lower.startswith(BCE_PREFIX) or k_lower in headers_to_sign:
            new_k = uri_encode(k_lower)
            new_v = uri_encode(str(v).strip())
            result.append(f'{new_k}:{new_v}')

    return '\n'.join(sorted(result))


def _to_timestamp():
    t = datetime.utcnow().isoformat(timespec='seconds')
    return f'{t}Z'
