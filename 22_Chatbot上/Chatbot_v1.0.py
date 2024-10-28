import os

from dotenv import load_dotenv  # 用于加载环境变量
from langchain.chat_models import ChatOpenAI
from langchain.globals import set_debug, set_verbose
from langchain.schema import HumanMessage, SystemMessage

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量

os.environ["LANGCHAIN_TRACING_V2"] = "false"

# 导入所需的库和模块

# 创建一个聊天模型的实例
chat = ChatOpenAI()

# 创建一个消息列表
messages = [
    SystemMessage(content="你是一个花卉行家。"),
    HumanMessage(content="朋友喜欢淡雅的颜色，她的婚礼我选择什么花？"),
]

# 使用聊天模型获取响应
response = chat(messages)
print(response)
