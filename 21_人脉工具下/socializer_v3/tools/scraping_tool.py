import json
import os
import time

import requests
from dotenv import load_dotenv  # 用于加载环境变量
from langchain.globals import set_debug, set_verbose

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量

os.environ["LANGCHAIN_TRACING_V2"] = "false"
# 导入所需的库

# 定义爬取微博用户信息的函数


def scrape_weibo(url: str):
    """爬取相关鲜花服务商的资料"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "Referer": "https://weibo.com",
    }
    cookies = {"cookie": """your cookie"""}
    response = requests.get(url, headers=headers, cookies=cookies)
    time.sleep(3)  # 加上3s 的延时防止被反爬
    return response.text


# 根据UID构建URL爬取信息


def get_data(id):
    url = "https://weibo.com/ajax/profile/detail?uid={}".format(id)
    html = scrape_weibo(url)
    response = json.loads(html)

    return response
