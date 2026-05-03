import aiohttp
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.runnables import Runnable, RunnableWithMessageHistory
from langchain_core.stores import InMemoryStore
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="ep-20260419142915-rpcdt",
    openai_api_key="ark-808d84e5-892e-44b8-af5e-5959c5563ee4-1e001",
    openai_api_base="https://ark.cn-beijing.volces.com/api/v3",)

# model.invoke("我是小明你好").pretty_print()
# model.invoke("我是谁").pretty_print()

#模型本身没有记忆功能
# messages = [
#     HumanMessage(content="我是小明你好!"),
#     AIMessage(content="你好小明很高兴认识你今天有什么想聊的呢"),#将ai消息保留下来就可以进行多轮对话
#     HumanMessage(content="你知道我是谁么")
# ]
# model.invoke(messages).pretty_print()

store = {}
#根据会话id查询会话里的消息列表
def get_session_history(session_id:str)->BaseChatMessageHistory:
    if session_id not in store:
        #InMemoryChatMessageHistory()帮助我们将AIMessage.HumanMessage等消息自动添加进来
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

#包装了model让model具备存储历史消息的能力
with_history_Message_model = RunnableWithMessageHistory(model,get_session_history)

#model:Runnable实例
#invoke:config:配置Runnable实例
config={"configurable":{"session_id":"1"}}
with_history_Message_model.invoke(
    [HumanMessage(content="我是小明,你好")],
    config=config,
).pretty_print()

with_history_Message_model.invoke(
    [HumanMessage(content="你知道我是谁么")],
    config=config,
).pretty_print()