import os

from dotenv import load_dotenv  # 用于加载环境变量
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from langchain.globals import set_debug, set_verbose
from langchain.llms import OpenAI
from langchain.utilities import SQLDatabase

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量

os.environ["LANGCHAIN_TRACING_V2"] = "false"

# 连接到FlowerShop数据库
db = SQLDatabase.from_uri("sqlite:///FlowerShop.db")
llm = OpenAI(temperature=0, verbose=True)

# 创建SQL Agent
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=SQLDatabaseToolkit(db=db, llm=llm),
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

# 使用Agent执行SQL查询
questions = [
    "哪种鲜花的存货数量最少？",
    "平均销售价格是多少？",
]

for question in questions:
    response = agent_executor.run(question)
    print(response)
