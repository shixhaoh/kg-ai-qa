from typing import Iterator, List

from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
import asyncio

#组件1:聊天模型
model = ChatOpenAI(
    model="ep-20260419142915-rpcdt",
    openai_api_key="ark-808d84e5-892e-44b8-af5e-5959c5563ee4-1e001",
    openai_api_base="https://ark.cn-beijing.volces.com/api/v3",)
#组件2:定义解析器
parser = StrOutputParser()

#自定义生成器
def split_into_list(input:Iterator[str])->Iterator[List[str]]:
    buffer = ""
    for chunk in input:
        buffer += chunk
        #遇到叹号需要刷新
        while "!" in buffer:
            #找到叹号的位置
            stop_index = buffer.index("!")
            #yield用于创造生成器
            yield [buffer[:stop_index].strip()]
            buffer  = buffer[stop_index + 1:]
    #处理buffer最后几个字
    yield [buffer.strip()]
#定义链
chain= model|parser|split_into_list

#返回一个迭代器,产生的消息块

for chunk in chain.stream("写一段关于爱情的歌词,需要5句话,每句话使用英文叹号隔开"):
    # chunks.append(chunk)
    # chunk:AIMessageChunk
    print(chunk,end="|",flush=True)
# tmp_chunk = print(chunks[0] + chunks[1] + chunks[2] + chunks[3])
# print(tmp_chunk)

# print(model.invoke("写一段关于春天的作文,1000字").content)