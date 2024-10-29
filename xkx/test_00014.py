from typing import List, Literal

from langchain_core.messages import HumanMessage
from langchain_core.messages.base import BaseMessage
from langchain_core.runnables import RunnableLambda
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.graph import END, MessageGraph
from langgraph.prebuilt import ToolNode

from langchain.globals import set_debug, set_verbose
from dotenv import load_dotenv  # 用于加载环境变量

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量


@tool
def multiply(first_number: int, second_number: int):
    """Multiplies two numbers together."""
    return first_number * second_number


def fn_pprint_A(obj):
    print("------pA-----")
    print(obj)
    print("-------------")
    return obj


pprint_A = RunnableLambda(fn_pprint_A)


def fn_pprint_B(obj):
    print("------pB-----")
    print(obj)
    print("-------------")
    return obj


pprint_B = RunnableLambda(fn_pprint_B)

model = ChatOpenAI()
model_with_tools = model.bind_tools([multiply])

tool_node = ToolNode([multiply])

builder = MessageGraph()

builder.add_node("oracle", model_with_tools)
builder.add_node("multiply", tool_node)
builder.add_node("pprint_A", pprint_A)
builder.add_node("pprint_B", pprint_B)


builder.add_edge("multiply", "pprint_A")
builder.add_edge("pprint_A", "pprint_B")
builder.add_edge("pprint_B", END)

builder.set_entry_point("oracle")


def router(state: List[BaseMessage]) -> Literal["multiply", "__end__"]:
    tool_calls = state[-1].additional_kwargs.get("tool_calls", [])
    if len(tool_calls):
        return "multiply"
    else:
        return "__end__"


builder.add_conditional_edges("oracle", router)

runnable = builder.compile()

# runnable.invoke(HumanMessage("What is 123 * 456?"))

runnable.get_graph().print_ascii()
