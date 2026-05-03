from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from langchain_deepseek import ChatDeepSeek
from langchain_openai import ChatOpenAI

#1.定义OpenAi模型

model = ChatOpenAI(
    model="ep-20260419142915-rpcdt",
    openai_api_key="ark-808d84e5-892e-44b8-af5e-5959c5563ee4-1e001",
    openai_api_base="https://ark.cn-beijing.volces.com/api/v3",
    # temperature=0.5,#采样温度,温度越高ai回复内容越天马行空一般范围0-2
    # max_tokens=10,#文本的基本单位,1token约等于4字符或0.75单词,对于中文1个汉字约等于1.5-2token
    # timeout=None,#超时时间
    # max_retries=10,#最大重试次数
    # organization="",#指定openai组织

)
#2.定义消息

messages = [
    SystemMessage(content="请补全一段故事,10字数以内"),
    HumanMessage(content="一只猫正在__?")
]
print(model.invoke(messages))

#3.调用大模型
result=model.invoke(messages)

#4.定义输出解析器组件
parser=StrOutputParser()
#5.开始定义链
chain = model | parser

print(chain.invoke(messages))