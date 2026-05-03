from langchain_openai import ChatOpenAI
import asyncio

model = ChatOpenAI(
    model="ep-20260419142915-rpcdt",
    openai_api_key="ark-808d84e5-892e-44b8-af5e-5959c5563ee4-1e001",
    openai_api_base="https://ark.cn-beijing.volces.com/api/v3",)

#返回一个迭代器,产生的消息块

# chunks=[]
# for chunk in model.stream("写一段关于春天的作文,1000字"):
#     chunks.append(chunk)
    #chunk:AIMessageChunk
    #print(chunk.content,end="|",flush=True)
# tmp_chunk = print(chunks[0] + chunks[1] + chunks[2] + chunks[3])
# print(tmp_chunk)

# print(model.invoke("写一段关于春天的作文,1000字").content)



#异步流式输出
async def async_stream():
    print("====开始异步调用====")
    async for chunk in model.astream("写一段关于春天的作文,1000字"):
        print(chunk.content,end="|",flush=True)
asyncio.run(async_stream())