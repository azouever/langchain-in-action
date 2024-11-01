import os

from dotenv import load_dotenv  # 用于加载环境变量
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.globals import set_debug, set_verbose
from langchain.prompts import PromptTemplate
from tools.search_tool import get_UID

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量

os.environ["LANGCHAIN_TRACING_V2"] = "false"

# 导入一个搜索UID的工具

# 导入所需的库

# 通过LangChain代理找到UID的函数


def lookup_V(flower_type: str):
    # 初始化大模型
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    # 寻找UID的模板
    template = """given the {flower} I want you to get a related 微博 UID.
                  Your answer should contain only a UID.
                  The URL always starts with https://weibo.com/u/
                  for example, if https://weibo.com/u/1669879400 is her 微博, then 1669879400 is her UID
                  This is only the example don't give me this, but the actual UID"""
    # 完整的提示模板
    prompt_template = PromptTemplate(input_variables=["flower"], template=template)

    # 代理的工具
    tools = [
        Tool(
            name="Crawl Google for 微博 page",
            func=get_UID,
            description="useful for when you need get the 微博 UID",
        )
    ]

    # 初始化代理
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )

    # 返回找到的UID
    ID = agent.run(prompt_template.format_prompt(flower=flower_type))

    return ID
