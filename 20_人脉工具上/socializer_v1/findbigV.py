import os
import re

from agents.weibo_agent import lookup_V
from dotenv import load_dotenv  # 用于加载环境变量
from langchain.globals import set_debug, set_verbose

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量

os.environ["LANGCHAIN_TRACING_V2"] = "false"

os.environ["SERPAPI_API_KEY"] = "Your Key"

# 导入所取的库


if __name__ == "__main__":

    # 拿到UID
    response_UID = lookup_V(flower_type="牡丹")

    # 抽取UID里面的数字
    UID = re.findall(r"\d+", response_UID)[0]
    print("这位鲜花大V的微博ID是", UID)
