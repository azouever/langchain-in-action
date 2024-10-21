import os
from langchain.globals import set_debug, set_verbose
from dotenv import load_dotenv  # 用于加载环境变量

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量

os.environ["LANGCHAIN_TRACING_V2"] = "false"
'''欢迎来到LangChain实战课
https://time.geekbang.org/column/intro/100617601
作者 黄佳'''

import json
import os
from langchain_openai import ChatOpenAI
from langchain.schema import (
    HumanMessage,
    SystemMessage
)
from dotenv import load_dotenv  # 用于加载环境变量
load_dotenv()  # 加载 .env 文件中的环境变量


# os.environ["OPENAI_API_KEY"] = '你的OpenAI API Key'
llm = ChatOpenAI(model="gpt-4o",
                 temperature=0.8,
                 max_tokens=1000,
                 stream_options={"include_usage": True}
                 )
messages = [
    SystemMessage(content="你是一个很棒的智能助手"),
    HumanMessage(content="给我讲个笑话吧")
]

for chunk in llm.stream(messages):
    print(chunk)


# print(response)


# 格式化打印 response 的内容
# def print_response(response):
#     print("Content:")
#     print(response.content)
#     print("\nAdditional Kwargs:")
#     print(json.dumps(response.additional_kwargs, indent=4, ensure_ascii=False))
#     print("\nResponse Metadata:")
#     print(json.dumps(response.response_metadata, indent=4, ensure_ascii=False))
#     print("\nID:")
#     print(response.id)
#     print("\nUsage Metadata:")
#     print(json.dumps(response.usage_metadata, indent=4, ensure_ascii=False))
#
#
# print_response(response)
