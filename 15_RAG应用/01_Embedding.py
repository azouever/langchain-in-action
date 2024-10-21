import os
from langchain.globals import set_debug, set_verbose
from dotenv import load_dotenv  # 用于加载环境变量

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量

os.environ["LANGCHAIN_TRACING_V2"] = "false"
import os
from langchain.globals import set_debug, set_verbose
from dotenv import load_dotenv  # 用于加载环境变量

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量

os.environ["LANGCHAIN_TRACING_V2"] = "false"
# 设置OpenAI的API密钥
import os
os.environ["OPENAI_API_KEY"] = 'Your OpenAI Key'

# 初始化Embedding类
from langchain.embeddings import OpenAIEmbeddings
embeddings_model = OpenAIEmbeddings()

# Embed文本
embeddings = embeddings_model.embed_documents(
    [
        "您好，有什么需要帮忙的吗？",
        "哦，你好！昨天我订的花几天送达",
        "请您提供一些订单号？",
        "12345678",
    ]
)
print(len(embeddings), len(embeddings[0]))

# Embed查询
embedded_query = embeddings_model.embed_query("刚才对话中的订单号是多少?")
print(embedded_query[:3])