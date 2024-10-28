import os

from dotenv import load_dotenv  # 用于加载环境变量
from langchain.globals import set_debug, set_verbose

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量

os.environ["LANGCHAIN_TRACING_V2"] = "false"


def compute(x, y, callback):
    result = x + y
    callback(result)


def print_result(value):
    print(f"The result is: {value}")


def square_result(value):
    print(f"The squared result is: {value**2}")


# 使用print_result作为回调
compute(3, 4, print_result)  # 输出: The result is: 7

# 使用square_result作为回调
compute(3, 4, square_result)  # 输出: The squared result is: 49
