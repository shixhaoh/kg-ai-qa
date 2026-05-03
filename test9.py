from typing import Optional

from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


model = ChatOpenAI(
    model="ep-20260419142915-rpcdt",
    openai_api_key="ark-808d84e5-892e-44b8-af5e-5959c5563ee4-1e001",
    openai_api_base="https://ark.cn-beijing.volces.com/api/v3",)

class Person(BaseModel):
    """一个人的信息"""
    name: Optional[str]=Field(default=None,description="这个人的名字")
    hair_color: Optional[str]=Field(default=None,description="如果知道这个人头发的颜色")
    skin_color: Optional[str]=Field(default=None,description="如果知道这个人头发的发色")
    height_in_meters: Optional[str]=Field(default=None,description="以米为单位的高度,如果输入的是英尺转化为米")

structure_model = model.with_structured_output(Person)

messages = [
    SystemMessage(content="你是一个提取专家,从文本中提取相关信息,如果你不知道要提取属性的值,属性值返回null"),
    HumanMessage(content="史密斯身高6英尺,金发.")
]

result = structure_model.invoke(messages)
print(result)