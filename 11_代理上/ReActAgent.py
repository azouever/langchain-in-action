import os

from dotenv import load_dotenv  # 用于加载环境变量
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.globals import set_debug, set_verbose
from langchain.llms import OpenAI

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量

os.environ["SERPAPI_API_KEY"] = "Your SerpAPI API Key"

# 加载所需的库

# 初始化大模型
llm = OpenAI(temperature=0)

# 设置工具
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# 初始化Agent
agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

# 跑起来
agent.run(
    "目前市场上玫瑰花的平均价格是多少？如果我在此基础上加价15%卖出，应该如何定价？"
)
