from dotenv import load_dotenv  # 用于加载环境变量
from langchain.globals import set_debug, set_verbose
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量


# Import relevant functionality

# Create the agent
memory = MemorySaver()
model = ChatOpenAI(model="gpt-3.5-turbo")

# need a tavily api key ref: https://python.langchain.com/docs/tutorials/agents/#tavily
search = TavilySearchResults(max_results=2)
tools = [search]
agent_executor = create_react_agent(model, tools, checkpointer=memory)

# Use the agent
config = {"configurable": {"thread_id": "abc123"}}
for chunk in agent_executor.stream(
    {"messages": [HumanMessage(content="hi im bob! and i live in sf")]}, config
):
    print(chunk)
    print("----")

for chunk in agent_executor.stream(
    {"messages": [HumanMessage(content="whats the weather where I live?")]}, config
):
    print(chunk)
    print("----")
