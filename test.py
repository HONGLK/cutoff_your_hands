from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

res = requests.get("https://detail.tmall.com/item.htm?spm=a312a.7700824.w4011-15691211890.32.41945742dYJIMW&id=616642818126&rn=fc058cd0d627f99c2350c0e5ae086c58&abbucket=4&sku_properties=134942334:28316", headers=headers)
print(res.text)