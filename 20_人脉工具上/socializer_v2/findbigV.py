import os
import re

from agents.weibo_agent import lookup_V
from dotenv import load_dotenv  # 用于加载环境变量
from langchain.globals import set_debug, set_verbose
from tools.general_tool import remove_non_chinese_fields
from tools.scraping_tool import get_data

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量

os.environ["LANGCHAIN_TRACING_V2"] = "false"

os.environ["SERPAPI_API_KEY"] = "your key"

# 导入所取的库


if __name__ == "__main__":

    # 拿到UID
    response_UID = lookup_V(flower_type="牡丹")

    # 抽取UID里面的数字
    UID = re.findall(r"\d+", response_UID)[0]
    print("这位鲜花大V的微博ID是", UID)

    # 根据UID爬取大V信息
    person_info = get_data(UID)
    print(person_info)

    # 移除无用的信息
    remove_non_chinese_fields(person_info)
    print(person_info)
