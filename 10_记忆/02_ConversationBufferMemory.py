import os

from dotenv import load_dotenv  # 用于加载环境变量
from langchain import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory
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
# llm = OpenAI(temperature=0.5, model_name="text-davinci-003")
llm = OpenAI(temperature=0.5, model="gpt-3.5-turbo-instruct")


# 初始化对话链
conversation = ConversationChain(llm=llm, memory=ConversationBufferMemory())

# 第一天的对话
# 回合1
conversation("我姐姐明天要过生日，我需要一束生日花束。")
print("第一次对话后的记忆:", conversation.memory.buffer)

# 回合2
conversation("她喜欢粉色玫瑰，颜色是粉色的。")
print("第二次对话后的记忆:", conversation.memory.buffer)

# 回合3 （第二天的对话）
conversation("我又来了，还记得我昨天为什么要来买花吗？")
print("/n第三次对话后时提示:/n", conversation.prompt.template)
print("/n第三次对话后的记忆:/n", conversation.memory.buffer)
