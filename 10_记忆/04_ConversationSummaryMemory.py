import os

from dotenv import load_dotenv  # 用于加载环境变量
from langchain import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationSummaryMemory
from langchain.globals import set_debug, set_verbose

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量

os.environ["LANGCHAIN_TRACING_V2"] = "false"

# 导入所需的库

# 初始化大语言模型

llm = OpenAI(temperature=0.5, model="gpt-3.5-turbo-instruct")

# 初始化对话链
conversation = ConversationChain(llm=llm, memory=ConversationSummaryMemory(llm=llm))

# 第一天的对话
# 回合1
result = conversation("我姐姐明天要过生日，我需要一束生日花束。")
print(result)
# 回合2
result = conversation("她喜欢粉色玫瑰，颜色是粉色的。")
# print("\n第二次对话后的记忆:\n", conversation.memory.buffer)
print(result)

# 第二天的对话
# 回合3
result = conversation("我又来了，还记得我昨天为什么要来买花吗？")
print(result)
