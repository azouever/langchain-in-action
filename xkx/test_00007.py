from dotenv import load_dotenv  # 用于加载环境变量
from langchain.globals import set_debug, set_verbose
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量

system_template = "Translate the following into {language}:"

prompt_template = ChatPromptTemplate(
    [
        ("system", system_template),
        ("user", "{text}"),
    ]
)

model = ChatOpenAI(model="gpt-4")

parser = StrOutputParser()


chain = prompt_template | model | parser


content = chain.invoke({"language": "Chinese", "text": "chain"})

print("--------------------------------------------------------")
print(content)
