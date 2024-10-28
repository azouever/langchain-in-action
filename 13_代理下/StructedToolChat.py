import asyncio
import os

from dotenv import load_dotenv  # 用于加载环境变量
from langchain.agents import AgentType, initialize_agent
from langchain.agents.agent_toolkits import PlayWrightBrowserToolkit
from langchain.chat_models import ChatOpenAI
from langchain.globals import set_debug, set_verbose
from langchain.tools.playwright.utils import create_async_playwright_browser

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量

os.environ["LANGCHAIN_TRACING_V2"] = "false"
"""欢迎来到LangChain实战课
https://time.geekbang.org/column/intro/100617601
作者 黄佳"""


async_browser = create_async_playwright_browser()
toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=async_browser)
tools = toolkit.get_tools()
print(tools)


# LLM不稳定，对于这个任务，可能要多跑几次才能得到正确结果
llm = ChatOpenAI(temperature=0.5)

agent_chain = initialize_agent(
    tools,
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)


async def main():
    response = await agent_chain.arun("What are the headers on python.langchain.com?")
    print(response)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
