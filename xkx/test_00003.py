from dotenv import load_dotenv  # 用于加载环境变量
from langchain.globals import set_debug, set_verbose
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量


model = ChatOpenAI(model="gpt-4o")

messages = [
    SystemMessage(content="Translate the following from English into Chinese"),
    HumanMessage(content="hi!"),
]
parser = StrOutputParser()

chain = model | parser

content = chain.invoke(messages)

print("-------")

print(content)
