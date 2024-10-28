from dotenv import load_dotenv  # 用于加载环境变量
from langchain.globals import set_debug, set_verbose
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量

system_template = "Translate the following into {language}:"

prompt_template = ChatPromptTemplate([
    ("system", system_template),
    ("user", "{text}"),
])


# 这里把发送给大模型的内容统称为prompt

prompt = prompt_template.invoke({"language": "Chinese", "text": "chain"})





print("-------")

print(prompt.to_messages())
