import os

from dotenv import load_dotenv  # 用于加载环境变量
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.globals import set_debug, set_verbose
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量

os.environ["LANGCHAIN_TRACING_V2"] = "false"

# 导入文档加载器模块，并使用TextLoader来加载文本文件
loader = TextLoader("./OneFlower/易速鲜花花语大全.txt", encoding="utf8")

# 使用VectorstoreIndexCreator来从加载器创建索引
index = VectorstoreIndexCreator().from_loaders([loader])

# 定义查询字符串, 使用创建的索引执行查询
query = "玫瑰花的花语是什么？"
result = index.query(query)
print(result)  # 打印查询结果


# 替换成你所需要的工具
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
embeddings = OpenAIEmbeddings()
index_creator = VectorstoreIndexCreator(
    vectorstore_cls=Chroma,
    embedding=OpenAIEmbeddings(),
    text_splitter=CharacterTextSplitter(chunk_size=1000, chunk_overlap=0),
)
