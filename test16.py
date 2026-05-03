from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, filter_messages
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="ep-20260419142915-rpcdt",
    openai_api_key="ark-808d84e5-892e-44b8-af5e-5959c5563ee4-1e001",
    openai_api_base="https://ark.cn-beijing.volces.com/api/v3",)

messages=[
    SystemMessage(content="你是一个聊天机器人",id="1"),
    HumanMessage(content="示例输入",id="2"),
    AIMessage(content="示例输出",id="3"),
    HumanMessage(content="真实输入",id="4"),
    AIMessage(content="真实输出",id="5"),
]

#按照类型筛选
print(filter_messages(include_types="human").invoke(messages))

#按照id筛选
print(filter_messages(messages, exclude_ids=["3"]))

#按照id+类型筛选
print(filter_messages(messages, exclude_ids=["3"], include_types=[HumanMessage, AIMessage]))