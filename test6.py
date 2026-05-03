from typing import Annotated

from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI


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

@tool
def multiply(
    a:Annotated[int,...,"第一个整数"],
    b:Annotated[int,...,"第二个整数"],
)->int:
    """两数相乘
    Args:
        a:第一个整数
        b:第二个整数
    """
    return a*b

model = ChatOpenAI(
    model="ep-20260419142915-rpcdt",
    openai_api_key="ark-808d84e5-892e-44b8-af5e-5959c5563ee4-1e001",
    openai_api_base="https://ark.cn-beijing.volces.com/api/v3",)


#绑定工具
tools = [add, multiply]
# model_with_tools = model.bind_tools(tools)
#强制选择工具
model_with_tools = model.bind_tools(tools,tool_choice="any")

#调用工具
# print(model_with_tools.invoke("2乘3等于几"))
# print(model_with_tools.invoke("你是谁"))


#定义消息列表,添加要传递给聊天模型的消息
message = [
    HumanMessage("2乘3等于几?6+6等于多少?")
]

ai_msg = model_with_tools.invoke(message)
message.append(ai_msg)

#构造ToolMessage,并添加到消息列表
for tool_calls in ai_msg.tool_calls:
    selected_tool = {"add":add,"multiply":multiply}[tool_calls["name"].lower()]
    tool_msg = selected_tool.invoke(tool_calls)
    message.append(tool_msg)

print(message)
print(model.invoke(message).content)
# print(multiply.invoke(ai_msg.tool_calls[0]))