from typing import List, Literal

from dotenv import load_dotenv  # 用于加载环境变量
from langchain.globals import set_debug, set_verbose
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
    trim_messages,
)
from langchain_core.messages.base import BaseMessage
from langchain_core.runnables import RunnableLambda
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.graph import END, MessageGraph
from langgraph.prebuilt import ToolNode

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量

model = ChatOpenAI(model="gpt-3.5-turbo")


# ref:https://python.langchain.com/docs/tutorials/chatbot/#managing-conversation-history
trimmer = trim_messages(
    max_tokens=165,
    strategy="last",
    token_counter=model,
    include_system=True,
    allow_partial=False,
    start_on="human",
)

messages = [
    SystemMessage(content="you're a good assistant"),
    HumanMessage(content="hi! I'm bob"),
    AIMessage(content="hi!"),
    HumanMessage(content="I like vanilla ice cream"),
    AIMessage(content="nice"),
    HumanMessage(content="whats 2 + 2"),
    AIMessage(content="4"),
    HumanMessage(content="thanks"),
    AIMessage(content="no problem!"),
    HumanMessage(content="having fun?"),
    AIMessage(content="yes!"),
]

msgObj = trimmer.invoke(messages)

print(msgObj)
