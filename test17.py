from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, merge_message_runs
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="ep-20260419142915-rpcdt",
    openai_api_key="ark-808d84e5-892e-44b8-af5e-5959c5563ee4-1e001",
    openai_api_base="https://ark.cn-beijing.volces.com/api/v3",)

messages = [
    SystemMessage("你是一个聊天助手。"),
    SystemMessage("你总是以笑话回应。"),
    HumanMessage("为什么要使用 LangChain?"),
    HumanMessage("为什么要使用 LangGraph?"),
    AIMessage("因为当你试图让你的代码更有条理时，LangGraph 会让你感到“节点”是个好主意！"),
    AIMessage("不过别担心，它不会“分散”你的注意力！"),
    HumanMessage("选择LangChain还是LangGraph?"),
]

merger=merge_message_runs()
chain=merger|model
chain.invoke(messages).pretty_print()