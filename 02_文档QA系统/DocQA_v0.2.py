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
"""欢迎来到LangChain实战课 测试
https://time.geekbang.org/column/intro/100617601
作者 黄佳"""

import logging  # 导入Logging工具
import os

# os.environ["OPENAI_API_KEY"] = '你的OpenAI API Key'
from dotenv import load_dotenv  # 用于加载环境变量
from flask import Flask, render_template, request
from langchain.chains import RetrievalQA  # RetrievalQA链
from langchain.retrievers.multi_query import (
    MultiQueryRetriever,
)  # MultiQueryRetriever工具
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import Docx2txtLoader, PyPDFLoader, TextLoader
from langchain_community.vectorstores import Qdrant
from langchain_openai import ChatOpenAI  # ChatOpenAI模型
from langchain_openai import OpenAIEmbeddings

load_dotenv()  # 加载 .env 文件中的环境变量

# 1.Load 导入Document Loaders

# 加载Documents
base_dir = "02_文档QA系统/OneFlower"  # 文档的存放目录
documents = []
for file in os.listdir(base_dir):
    # 构建完整的文件路径
    file_path = os.path.join(base_dir, file)
    if file.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
        documents.extend(loader.load())
    elif file.endswith(".docx"):
        loader = Docx2txtLoader(file_path)
        documents.extend(loader.load())
    elif file.endswith(".txt"):
        loader = TextLoader(file_path)
        documents.extend(loader.load())

# 2.Split 将Documents切分成块以便后续进行嵌入和向量存储

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200, chunk_overlap=10)
chunked_documents = text_splitter.split_documents(documents)

# 3.Store 将分割嵌入并存储在矢量数据库Qdrant中

vectorstore = Qdrant.from_documents(
    documents=chunked_documents,  # 以分块的文档
    embedding=OpenAIEmbeddings(),  # 用OpenAI的Embedding Model做嵌入
    location=":memory:",  # in-memory 存储
    collection_name="my_documents",
)  # 指定collection_name

# 4. Retrieval 准备模型和Retrieval链


# 设置Logging
logging.basicConfig()
logging.getLogger("langchain.retrievers.multi_query").setLevel(logging.INFO)

# 实例化一个大模型工具 - OpenAI的GPT-3.5
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

# 实例化一个MultiQueryRetriever
retriever_from_llm = MultiQueryRetriever.from_llm(
    retriever=vectorstore.as_retriever(), llm=llm
)

# 实例化一个RetrievalQA链
qa_chain = RetrievalQA.from_chain_type(llm, retriever=retriever_from_llm)

# 5. Output 问答系统的UI实现

app = Flask(__name__)  # Flask APP


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # 接收用户输入作为问题
        question = request.form.get("question")

        # RetrievalQA链 - 读入问题，生成答案
        result = qa_chain({"query": question})

        # 把大模型的回答结果返回网页进行渲染
        return render_template("index.html", result=result)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
