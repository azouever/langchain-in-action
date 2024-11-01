import os

from dotenv import load_dotenv  # 用于加载环境变量
from langchain.globals import set_debug, set_verbose

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量

os.environ["LANGCHAIN_TRACING_V2"] = "false"
"""欢迎来到LangChain实战课
https://time.geekbang.org/column/intro/100617601
作者 黄佳"""

from operator import itemgetter

from langchain.chains import LLMChain, SequentialChain
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAI

# 导入所需要的库


# 第一个LLMChain：生成鲜花的介绍
llm = OpenAI(temperature=0.7)
template = """
你是一个植物学家。给定花的名称和类型，你需要为这种花写一个200字左右的介绍。
花名: {name}
颜色: {color}
植物学家: 这是关于上述花的介绍:"""
prompt_template = PromptTemplate(input_variables=["name", "color"], template=template)
# introduction_chain = LLMChain(
#     llm=llm, prompt=prompt_template, output_key="introduction"
# )

introduction_chain = prompt_template | llm | {"introduction": RunnablePassthrough()}


# 第二个LLMChain：根据鲜花的介绍写出鲜花的评论
template = """
你是一位鲜花评论家。给定一种花的介绍，你需要为这种花写一篇200字左右的评论。
鲜花介绍:
{introduction}
花评人对上述花的评论:"""
prompt_template1 = PromptTemplate(input_variables=["introduction"], template=template)
# review_chain = LLMChain(llm=llm, prompt=prompt_template, output_key="review")

review_chain = prompt_template1 | llm | {"review": RunnablePassthrough()}


# 第三个LLMChain：根据鲜花的介绍和评论写出一篇自媒体的文案
template = """
你是一家花店的社交媒体经理。给定一种花的介绍和评论，你需要为这种花写一篇社交媒体的帖子，300字左右。
鲜花介绍:
{introduction}
花评人对上述花的评论:
{review}
社交媒体帖子:
"""
prompt_template2 = PromptTemplate(
    input_variables=["introduction", "review"], template=template
)
# social_post_chain = LLMChain(
# llm=llm, prompt=prompt_template, output_key="social_post_text"
# )

social_post_chain = prompt_template2 | llm | {"social_post_text": RunnablePassthrough()}


combined_chain = (
    introduction_chain
    | {"review": review_chain, "introduction": itemgetter("introduction")}
    | social_post_chain
)

# 总的链：按顺序运行三个链
# overall_chain = SequentialChain(
#     chains=[introduction_chain, review_chain, social_post_chain],
#     input_variables=["name", "color"],
#     output_variables=["introduction", "review", "social_post_text"],
#     verbose=True,
# )


# 运行链并打印结果
result = combined_chain.invoke({"name": "玫瑰", "color": "黑色"})
print(result)
