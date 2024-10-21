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

# import os
# os.environ["OPENAI_API_KEY"] = '你的OpenAI API Key'
from langchain_openai import OpenAI
from dotenv import load_dotenv  # 用于加载环境变量
load_dotenv()  # 加载 .env 文件中的环境变量


llm = OpenAI(
    model="gpt-3.5-turbo-instruct",
    temperature=0.8,
    max_tokens=60,)
response = llm.invoke("请给我的花店起个名")
print(response)
