import os

from dotenv import load_dotenv  # 用于加载环境变量
from langchain_openai import OpenAI
from langchain.chains import ConversationChain
from langchain.globals import set_debug, set_verbose

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量


os.environ["LANGCHAIN_TRACING_V2"] = "false"
"""欢迎来到LangChain实战课
https://time.geekbang.org/column/intro/100617601
作者 黄佳"""
# 导入所需的库

# 初始化大语言模型
llm = OpenAI(temperature=0.5, model_name="text-davinci-003")

# 初始化对话链
conv_chain = ConversationChain(llm=llm)

# 打印对话的模板
print(conv_chain.prompt.template)
