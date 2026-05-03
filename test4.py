from typing import Annotated

from openai.types.chat.chat_completion_message import Annotation
from pydantic import BaseModel, Field
from langchain_core.tools import tool


#定义工具
#方式一
#函数名.字符串文档.类型提示都需要定义,实际上这些信息都是传递给工具schema
# @tool
# def add(a:int,b:int)->int:
#     """两数相加
#
#     Args:
#         a:第一个整数
#         b:第二个整数
#     """
#     return a+b

#方式二
# class AddInput(BaseModel):
#     """两数相加"""
#     a:int=Field(...,description="第一个整数")
#     b:int=Field(...,description="第二个整数")
#
#
# @tool(args_schema=AddInput)
# def add(a:int,b:int)->int:
#     return a+b

#方式三
@tool
def add(a:Annotated[int,...,"第一个整数"],
        b:Annotated[int,...,"第二个整数"],
    )->int:
    """两数相加

    Args:
        a:第一个整数
        b:第二个整数
    """
    return a+b
print(add.invoke({"a": 2, "b": 3}))
print(add.name)
print(add.description)
print(add.args)

#工具名称,工具描述,工具参数

