import asyncio
from typing import Sequence

from dotenv import load_dotenv  # 用于加载环境变量
from IPython.display import Image, display
from langchain.globals import set_debug, set_verbose
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langgraph.graph.message import add_messages
from typing_extensions import Annotated, TypedDict

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量

model = ChatOpenAI(model="gpt-3.5-turbo")


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability in {language}.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)


class State(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    language: str


workflow = StateGraph(state_schema=State)


def call_model(state: State):
    chain = prompt | model
    response = chain.invoke(state)
    return {"messages": [response]}


workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

memory = MemorySaver()
app = workflow.compile(checkpointer=memory)


config = {"configurable": {"thread_id": "abc456"}}
query = "Hi! I'm Bob."
language = "Chinese"

input_messages = [HumanMessage(query)]
output = app.invoke(
    {"messages": input_messages, "language": language},
    config,
)
output["messages"][-1].pretty_print()


try:
    # display(Image(app.get_graph().print_ascii()))
    app.get_graph().print_ascii()
except Exception as e:
    print(f"An error occurred: {e}")
    # This requires some extra dependencies and is optional
    pass
