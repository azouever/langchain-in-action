import asyncio

from dotenv import load_dotenv  # 用于加载环境变量
from langchain.globals import set_debug, set_verbose
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量

model = ChatOpenAI(model="gpt-3.5-turbo")


# Define a new graph
workflow = StateGraph(state_schema=MessagesState)


# Define the function that calls the model
def call_model(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": response}


# Define the (single) node in the graph
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

# Add memory
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)


config = {"configurable": {"thread_id": "abc123"}}


query = "Hi! I'm Bob."

input_messages = [HumanMessage(query)]
output = app.invoke({"messages": input_messages}, config)
output["messages"][-1].pretty_print()  # output contains all messages in state


query = "What's my name?"

input_messages = [HumanMessage(query)]
output = app.invoke({"messages": input_messages}, config)
output["messages"][-1].pretty_print()


config = {"configurable": {"thread_id": "abc234"}}

input_messages = [HumanMessage(query)]
output = app.invoke({"messages": input_messages}, config)
output["messages"][-1].pretty_print()


config = {"configurable": {"thread_id": "abc123"}}

input_messages = [HumanMessage(query)]
output = app.invoke({"messages": input_messages}, config)
output["messages"][-1].pretty_print()


# 假设以下组件是从相关库中导入的
# from some_library import MessagesState, StateGraph, MemorySaver, START, model


async def call_model(state: MessagesState):
    try:
        response = await model.ainvoke(state["messages"])
        return {"messages": response}
    except Exception as e:
        # 处理调用模型时的异常
        print(f"Error invoking model: {e}")
        return {"messages": []}


def create_workflow():
    workflow = StateGraph(state_schema=MessagesState)
    workflow.add_node("model", call_model)
    workflow.add_edge(START, "model")
    return workflow.compile(checkpointer=MemorySaver())


async def main(input_messages, config):
    app = create_workflow()
    try:
        output = await app.ainvoke({"messages": input_messages}, config)
        # 检查 output["messages"] 是否为空，避免索引错误
        if output["messages"]:
            output["messages"][-1].pretty_print()
        else:
            print("No messages returned from the model.")
    except Exception as e:
        # 处理工作流执行时的异常
        print(f"Error during workflow execution: {e}")


# 假设 input_messages 和 config 是预定义的
asyncio.run(main(input_messages, config))
