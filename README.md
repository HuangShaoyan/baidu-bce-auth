[![Build Status](https://travis-ci.org/HuangShaoyan/baidu-bce-auth.svg?branch=master)](https://travis-ci.org/HuangShaoyan/baidu-bce-auth)

# baidu-bce-auth

帮助你生成百度云 API 的鉴权认证字符串(Authorization header)

百度云 API 鉴权认证的文档：https://cloud.baidu.com/doc/Reference/s/njwvz1yfu

使用方法，以 requests 为例

```
ak = 'xxx'
sk = 'yyy'
path = 'zzz'
url = 'http://example.com'
params = {}

requests.get(
    url,
    params=params,
    headers={
        'Authorization': make_auth(   # <== 调用 make_auth，得到 Authorization 的内容
            ak=ak,
            sk=sk,
            method='GET',
            path=path,
            params=params,
            headers={
                'Host': 'example.com',
            },
        )
    }
)
```

完整的例子，可以参考：[tests/test_auth.py](tests/test_auth.py)
