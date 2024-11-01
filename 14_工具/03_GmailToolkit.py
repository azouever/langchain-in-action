import os

from dotenv import load_dotenv  # 用于加载环境变量
from langchain.agents import AgentType, initialize_agent
from langchain.agents.agent_toolkits import GmailToolkit
from langchain.chat_models import ChatOpenAI
from langchain.globals import set_debug, set_verbose
from langchain.tools.gmail.utils import build_resource_service, get_gmail_credentials

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量

os.environ["LANGCHAIN_TRACING_V2"] = "false"

# 导入与Gmail交互所需的工具包

# 初始化Gmail工具包
toolkit = GmailToolkit()

# 从gmail工具中导入一些有用的功能

# 获取Gmail API的凭证，并指定相关的权限范围
credentials = get_gmail_credentials(
    token_file="token.json",  # Token文件路径
    scopes=["https://mail.google.com/"],  # 具有完全的邮件访问权限
    client_secrets_file="credentials.json",  # 客户端的秘密文件路径
)
# 使用凭证构建API资源服务
api_resource = build_resource_service(credentials=credentials)
toolkit = GmailToolkit(api_resource=api_resource)

# 获取工具
tools = toolkit.get_tools()
print(tools)

# 导入与聊天模型相关的包

# 初始化聊天模型
llm = ChatOpenAI(temperature=0, model="gpt-4")

# 通过指定的工具和聊天模型初始化agent
agent = initialize_agent(
    tools=toolkit.get_tools(),
    llm=llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
)

# 使用agent运行一些查询或指令
result = agent.run("今天易速鲜花客服给我发邮件了么？最新的邮件是谁发给我的？")

# 打印结果
print(result)
