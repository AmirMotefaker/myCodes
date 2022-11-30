# HTTP client

import urllib3

http = urllib3.PoolManager()
r = http.request('GET', 'http://httpbin.org/robots.txt')
print(r.status)
# 200
print(r.data)
# b'User-agent: *\nDisallow: /deny\n'
