import json
from typing import Annotated, Literal, TypedDict

import bs4
import pyperclip
from dotenv import load_dotenv  # 用于加载环境变量
from langchain import hub
from langchain.globals import set_debug, set_verbose
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI, OpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, create_react_agent

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量

# llm = OpenAI(temperature=0.5, model="gpt-4")


# Define the tools for the agent to use
@tool
def search(query: str):
    """Call to surf the web."""
    # This is a placeholder, but don't tell the LLM that...
    if "sf" in query.lower() or "san francisco" in query.lower():
        return "It's 60 degrees and foggy."
    return "It's 90 degrees and sunny."


tools = [search]

tool_node = ToolNode(tools)

model = ChatOpenAI(model="gpt-4", temperature=0).bind_tools(tools)

# 定义一个函数确定是否继续执行


def should_continue(state: MessagesState) -> Literal["tools", END]:
    messages = state["messages"]
    last_message = messages[-1]
    # 如果大模型通知调用工具的时候，我们可以路由到对应的工具节点
    if last_message.tool_calls:
        return "tools"
    # 否则，停止执行（回复用户）
    return END


# 定义一个调用大模型的函数
def call_model(state: MessagesState):
    messages = state["messages"]
    response = model.invoke(messages)
    # We return a list, because this will get added to the existing list
    return {"messages": [response]}


# 定义一个图
workflow = StateGraph(MessagesState)

# 定义两个可以循环的节点
workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)

# 设置agent的入口
# 这表示这是第一个被调用的节点
workflow.add_edge(START, "agent")

# 添加条件边
workflow.add_conditional_edges(
    # First, we define the start node. We use `agent`.
    # This means these are the edges taken after the `agent` node is called. 这表示这些边在`agent`节点调用之后执行
    "agent",
    # Next, we pass in the function that will determine which node is called next. 接下来通过这个函数决定哪一个节点将被调用
    should_continue,
)

# We now add a normal edge from `tools` to `agent`. 从工具到agent中添加一个普通的边（edge）
# This means that after `tools` is called, `agent` node is called next.
# 这表示tools工具被调用后，紧接着调用agent节点
workflow.add_edge("tools", "agent")

# Initialize memory to persist state between graph runs
# 初始化内从以保存graph之间的运行
checkpointer = MemorySaver()

# Finally, we compile it!
# This compiles it into a LangChain Runnable,
# meaning you can use it as you would any other runnable.
# Note that we're (optionally) passing the memory when compiling the graph
# 最后编译，编译成一个langchain的runnable，意味着你可以像使用其他任意的runnable一样使用他，注意我们在刚刚编译的时候放入了内存记忆（memory)
app = workflow.compile(checkpointer=checkpointer)

print(app.get_graph().draw_ascii())


# Use the Runnable
final_state = app.invoke(
    {"messages": [HumanMessage(content="what is the weather in sf")]},
    config={"configurable": {"thread_id": 42}},
)
final_state["messages"][-1].content
# "Based on the search results, I can tell you that the current weather in San Francisco is:\n\nTemperature: 60 degrees Fahrenheit\nConditions: Foggy\n\nSan Francisco is known for its microclimates and frequent fog, especially during the summer months. The temperature of 60°F (about 15.5°C) is quite typical for the city, which tends to have mild temperatures year-round. The fog, often referred to as "Karl the Fog" by locals, is a characteristic feature of San Francisco\'s weather, particularly in the mornings and evenings.\n\nIs there anything else you\'d like to know about the weather in San Francisco or any other location?"


# 定义一个函数来将对象转换为字典
def serialize_obj(obj):
    if hasattr(obj, "__dict__"):
        return obj.__dict__
    else:
        return str(obj)


# print(final_state)


# 使用 json.dumps() 和自定义序列化函数
json_output = json.dumps(
    final_state, default=serialize_obj, indent=4, ensure_ascii=False
)
print(json_output)

# 将 JSON 字符串复制到剪贴板
pyperclip.copy(json_output)
