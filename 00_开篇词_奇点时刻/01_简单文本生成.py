import os
from langchain.globals import set_debug, set_verbose
from dotenv import load_dotenv  # 用于加载环境变量

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量

os.environ["LANGCHAIN_TRACING_V2"] = "false"
import os
from langchain.globals import set_debug, set_verbose
from dotenv import load_dotenv  # 用于加载环境变量

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量

os.environ["LANGCHAIN_TRACING_V2"] = "false"
"""欢迎来到LangChain实战课
https://time.geekbang.org/column/intro/100617601
作者 黄佳"""

from langchain_openai import OpenAI
from dotenv import load_dotenv  # 用于加载环境变量

load_dotenv()  # 加载 .env 文件中的环境变量

# import os
# os.environ["OPENAI_API_KEY"] = '你的Open AI API Key'
# from langchain.llms import OpenAI

# llm = OpenAI(model_name="text-davinci-003",max_tokens=200)
llm = OpenAI(model="gpt-3.5-turbo-instruct", max_tokens=200)
# text = llm("请给我写一句情人节红玫瑰的中文宣传语")
text = llm.invoke("请给我写一句情人节红玫瑰的中文宣传语")
print(text)


# define input text
# input_text = "请给我写一句情人节红玫瑰的中文宣传语"

# stream resp
# for chunk in llm.stream(input_text):
# print(chunk)
# print(chunk, end="|")
