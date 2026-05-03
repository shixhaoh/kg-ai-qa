from typing import Optional, List

from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from pydantic import Field
from pydantic.v1.schema import json_scheme

model = ChatOpenAI(
    model="ep-20260419142915-rpcdt",
    openai_api_key="ark-808d84e5-892e-44b8-af5e-5959c5563ee4-1e001",
    openai_api_base="https://ark.cn-beijing.volces.com/api/v3",)

#Pydanic对象
# class Joke(BaseModel):
#     """给用户讲的一个笑话"""
#     setup:str=Field(description="这个笑话的开头")
#     punchline:str=Field(description="这个笑话的妙语")
#     rating:Optional[int]=Field(default=None,description="从1-10分,给这个笑话评分")
# # print(model.invoke("给我讲一个关于唱歌笑话").content)
#
# class Data(BaseModel):
#     """
#     获取关于笑话的数据列表
#     """
#     jokes:List[Joke]
#
# model_with_structured=model.with_structured_output(Data)
# print(model_with_structured.invoke("分别给我讲一个关于唱歌和跳舞的笑话"))


#JSON schema
json_scheme = {
    "title":"joke",
    "description":"给用户讲一个笑话",
    "type":"object",
    "properties":{
        "setup":{
            "type":"object",
            "description":"这个笑话的开头",
        },
        "punchline":{
            "type":"object",
            "description":"这个笑话的妙语"
        },
        "rating":{
            "type":"object",
            "description":"从1-10分,给这个笑话评分",
            "default":None,
        },
    },
    "required":["setup","punchline"],

}
model_with_structured=model.with_structured_output(json_scheme)
# print(model_with_structured.invoke("分别给我讲一个关于唱歌和跳舞的笑话"))
print(model_with_structured.invoke("你是谁?"))