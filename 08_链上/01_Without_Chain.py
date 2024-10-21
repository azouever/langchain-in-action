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

# ----第一步 创建提示
# 导入LangChain中的提示模板
from langchain_core.prompts import PromptTemplate

# 原始字符串模板
template = "{flower}的花语是?"
# 创建LangChain模板
prompt_temp = PromptTemplate.from_template(template)
# 根据模板创建提示
prompt = prompt_temp.format(flower="玫瑰")
# 打印提示的内容
print(prompt)

# ----第二步 创建并调用模型
# 导入LangChain中的OpenAI模型接口
from langchain_openai import OpenAI

# 创建模型实例
model = OpenAI(temperature=0)
# 传入提示，调用模型，返回结果
result = model.invoke(prompt)
print(result)
