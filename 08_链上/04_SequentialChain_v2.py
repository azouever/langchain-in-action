import os

from dotenv import load_dotenv  # 用于加载环境变量
from langchain.chains import LLMChain, SequentialChain
from langchain.globals import set_debug, set_verbose
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAI

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量

os.environ["LANGCHAIN_TRACING_V2"] = "false"
"""欢迎来到LangChain实战课
https://time.geekbang.org/column/intro/100617601
作者 黄佳"""


# 导入所需要的库


# 第一个LLMChain：生成鲜花的介绍
llm = OpenAI(temperature=0.7)
template = """
你是一个植物学家。给定花的名称和类型，你需要为这种花写一个200字左右的介绍。
花名: {name}
颜色: {color}
植物学家: 这是关于上述花的介绍:"""
prompt_template = PromptTemplate(input_variables=["name", "color"], template=template)
# introduction_chain = LLMChain(
#     llm=llm, prompt=prompt_template, output_key="introduction"
# )

introduction_chain = prompt_template | llm | {"introduction": RunnablePassthrough()}


# 运行链并打印结果
result = introduction_chain.invoke({"name": "玫瑰", "color": "黑色"})


print("================")
print(result)
