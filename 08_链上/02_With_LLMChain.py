import os

from dotenv import load_dotenv  # 用于加载环境变量
from langchain.globals import set_debug, set_verbose

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量

os.environ["LANGCHAIN_TRACING_V2"] = "false"
"""欢迎来到LangChain实战课
https://time.geekbang.org/column/intro/100617601
作者 黄佳"""
# 导入所需的库
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

# 原始字符串模板
template = "{flower}的花语是?"
# 创建模型实例
llm = OpenAI(temperature=0)
prompt = PromptTemplate.from_template(template)
# 创建LLMChain
# llm_chain = LLMChain(llm=llm, prompt=PromptTemplate.from_template(template))
llm_chain = prompt | llm
# 调用LLMChain，返回结果
result = llm_chain.invoke("玫瑰")
print(result)
