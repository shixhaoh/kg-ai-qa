from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, trim_messages
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="ep-20260419142915-rpcdt",
    openai_api_key="ark-808d84e5-892e-44b8-af5e-5959c5563ee4-1e001",
    openai_api_base="https://ark.cn-beijing.volces.com/api/v3",
    disable_token_counting=True,)

messages = [
    SystemMessage(content="you're a good assistant"),
    HumanMessage(content="hi! I'm bob"),
    AIMessage(content="hi!"),   
    HumanMessage(content="I like vanilla ice cream"),
    AIMessage(content="nice"),
    HumanMessage(content="whats 2 + 2"),
    AIMessage(content="4"),
    HumanMessage(content="thanks"),
    AIMessage(content="no problem!"),
    HumanMessage(content="having fun?"),
    AIMessage(content="yes!"),
    HumanMessage(content="What's my name?"),
]

#trim
#使用trim_message减少发送给模型的消息数量
trimmer = trim_messages(
    max_tokens= 65,#修剪消息的最大令牌数,根据你想要的谈话长度来调整
    strategy = "last",#修剪策略:
                      #"last"(默认):保留最后的消息
                      #"first":保留最早的消息
    token_counter = model,#传入一个函数或语言模型(因为语言模型有消息令牌计数方法)
    include_system=True,#如果想始终保留初始消息可以使用这个方法
    allow_partial=False,#是否允许拆分消息内容
    start_on="human",#如果需要确保我们的第一条消息(不包括系统消息)始终是特定类型,可以指定start_on
)

chain=trimmer|model

print(chain.invoke(messages))