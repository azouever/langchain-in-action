import os

from dotenv import load_dotenv  # 用于加载环境变量
from langchain import OpenAI, SerpAPIWrapper
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.globals import set_debug, set_verbose

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量

os.environ["LANGCHAIN_TRACING_V2"] = "false"


"""欢迎来到LangChain实战课
https://time.geekbang.org/column/intro/100617601
作者 黄佳"""
# 设置OpenAI和SERPAPI的API密钥
os.environ["SERPAPI_API_KEY"] = "Your Key"


llm = OpenAI(temperature=0)
search = SerpAPIWrapper()
tools = [
    Tool(
        name="Intermediate Answer",
        func=search.run,
        description="useful for when you need to ask with search",
    )
]

self_ask_with_search = initialize_agent(
    tools, llm, agent=AgentType.SELF_ASK_WITH_SEARCH, verbose=True
)
self_ask_with_search.run("使用玫瑰作为国花的国家的首都是哪里?")
