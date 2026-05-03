from typing import Optional, Union

from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

model = ChatOpenAI(
    model="ep-20260419142915-rpcdt",
    openai_api_key="ark-808d84e5-892e-44b8-af5e-5959c5563ee4-1e001",
    openai_api_base="https://ark.cn-beijing.volces.com/api/v3",)

class Joke(BaseModel):
    """给用户讲的一个笑话"""
    setup:str=Field(description="这个笑话的开头")
    punchline:str=Field(description="这个笑话的妙语")
    rating:Optional[int]=Field(default=None,description="从1-10分,给这个笑话评分")
class Response(BaseModel):
    """用以对话的方式回应"""
    response:str=Field(description="用于对用户查询的对话的响应")

class FinalResponse(BaseModel):
    """最终回复,选择合适的输出结构"""
    final_output:Union[Joke,Response]

model_with_structured=model.with_structured_output(FinalResponse)
print(model_with_structured.invoke("讲一个关于跳舞的笑话"))
print(model_with_structured.invoke("你是谁?"))