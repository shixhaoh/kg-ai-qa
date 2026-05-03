from typing import List, Tuple

from langchain_core.messages import HumanMessage
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field


#方式一
# def add(a:int,b:int)->int:
#     """两数相加
#     """
#     return a+b
#
# add_tool = StructuredTool.from_function(func=add)

#方式三:
class AddInput(BaseModel):
    a:int=Field(description="第一个整数")
    b:int=Field(description="第二个整数")

def add(a:int,b:int)->Tuple[str,List[int]]:
    nums=[a,b]
    content = f"{nums}相加结果是{a+b}"
    return content,nums
add_tool = StructuredTool.from_function(func=add,
                                        name="ADD",#工具名
                                        description="两数相加",#工具描述
                                        args_schema=AddInput,#工具参数
                                        response_format="content_and_artifact")



#模拟大模型调用方式
print(add_tool.invoke(
    {"name": "ADD",
     "args": {"a": 1, "b": 2},
     "type": "tool_call",  #必填
     "id": "111",  #必填,用来将工具调用请求和结果关联起来
     }
))
# print(add_tool.invoke({"a": 1, "b": 2}))