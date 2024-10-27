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

# 导入所需库
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI


# 设置提示模板
prompt = PromptTemplate(
    input_variables=["flower", "season"], template="{flower}在{season}的花语是?"
)

# 初始化大模型
llm = OpenAI(temperature=0)

# 初始化链
llm_chain = prompt | llm

# 调用链
response = llm_chain.invoke({"flower": "玫瑰", "season": "夏季"})
print(response)

# predict方法
# result = llm_chain.predict_and_parse(flower="玫瑰", season="夏季")
# print(result)

# apply方法允许您针对输入列表运行链
input_list = [
    {"flower": "玫瑰", "season": "夏季"},
    {"flower": "百合", "season": "春季"},
    {"flower": "郁金香", "season": "秋季"},
]
result = llm_chain.batch(input_list)
print(result)

# generate方法
# result = llm_chain.generate(input_list)
# print(result)
