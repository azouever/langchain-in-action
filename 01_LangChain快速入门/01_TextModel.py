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

from openai import OpenAI
from dotenv import load_dotenv  # 用于加载环境变量
load_dotenv()  # 加载 .env 文件中的环境变量

# import os
# os.environ["OPENAI_API_KEY"] = '你的OpenAI API Key'

# import openai
# # openai.api_key = '你的OpenAI API Key'

# response = openai.Completion.create(
#   model="text-davinci-003",
#   temperature=0.5,
#   max_tokens=100,
#   prompt="请给我的花店起个名")

# print(response.choices[0].text.strip())

client = OpenAI()

response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    temperature=0.5,
    max_tokens=100,
    prompt="请给我的花店起个名")

print(response)
print(response.choices[0].text.strip())
