import os

from dotenv import load_dotenv  # 用于加载环境变量
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.globals import set_debug, set_verbose
from langchain.memory import ConversationBufferMemory
from langchain.prompts import (ChatPromptTemplate, HumanMessagePromptTemplate,
                               MessagesPlaceholder,
                               SystemMessagePromptTemplate)
from langchain.schema import HumanMessage, SystemMessage

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量

os.environ["LANGCHAIN_TRACING_V2"] = "false"


# 带记忆的聊天机器人类


class ChatbotWithMemory:
    def __init__(self):

        # 初始化LLM
        self.llm = ChatOpenAI()

        # 初始化Prompt
        self.prompt = ChatPromptTemplate(
            messages=[
                SystemMessagePromptTemplate.from_template(
                    "你是一个花卉行家。你通常的回答不超过30字。"
                ),
                MessagesPlaceholder(variable_name="chat_history"),
                HumanMessagePromptTemplate.from_template("{question}"),
            ]
        )

        # 初始化Memory
        self.memory = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True
        )

        # 初始化LLMChain with LLM, prompt and memory
        self.conversation = LLMChain(
            llm=self.llm, prompt=self.prompt, verbose=True, memory=self.memory
        )

    # 与机器人交互的函数
    def chat_loop(self):
        print("Chatbot 已启动! 输入'exit'来退出程序。")
        while True:
            user_input = input("你: ")
            if user_input.lower() == "exit":
                print("再见!")
                break

            response = self.conversation({"question": user_input})
            print(f"Chatbot: {response['text']}")


if __name__ == "__main__":
    # 启动Chatbot
    bot = ChatbotWithMemory()
    bot.chat_loop()
