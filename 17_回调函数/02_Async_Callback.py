import asyncio
import os

from dotenv import load_dotenv  # 用于加载环境变量
from langchain.globals import set_debug, set_verbose

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量

os.environ["LANGCHAIN_TRACING_V2"] = "false"


async def compute(x, y, callback):
    print("Starting compute...")
    await asyncio.sleep(0.5)  # 模拟异步操作
    result = x + y
    # callback(result)
    print("Finished compute...")


def print_result(value):
    print(f"The result is: {value}")


async def another_task():
    print("Starting another task...")
    await asyncio.sleep(1)
    print("Finished another task...")


async def main():
    print("Main starts...")
    task1 = asyncio.create_task(compute(3, 4, print_result))
    task2 = asyncio.create_task(another_task())

    await task1
    await task2
    print("Main ends...")


asyncio.run(main())
