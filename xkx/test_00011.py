from dotenv import load_dotenv  # 用于加载环境变量
from langchain.globals import set_debug, set_verbose
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量


model = ChatOpenAI(model="gpt-3.5-turbo")

parser = StrOutputParser()


result = model.invoke(
    [
        HumanMessage(content="Hi! I'm Bob"),
        AIMessage(content="Hello Bob! How can I assist you today?"),
        HumanMessage(content="What's my name?"),
    ]
)


print("-------------------")
print(result)

print("-------------------")
print(parser.invoke(result))

# ref : https://python.langchain.com/docs/tutorials/chatbot/#quickstart