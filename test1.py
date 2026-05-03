from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from langchain_deepseek import ChatDeepSeek
from langchain_openai import ChatOpenAI
from pyexpat.errors import messages

#1.定义OpenAi模型
#这样写默认系统环境中读取OPENAI_API_KEY
# model = ChatOpenAI(model="gpt-4o-mini")
model = ChatDeepSeek(model="deepseek-chat")
#2.定义消息
#用户消息HumanMessage
#系统提示消息 通常作为第一条消息传入
#AI消息 AIMessage
messages = [
    SystemMessage(content="请帮我进行翻译,由英文翻译成中文"),
    HumanMessage(content="hi!")
]

#3.调用大模型
result=model.invoke(messages)
# print(result)

#链式体现在哪里??

#4.定义输出解析器组件
parser=StrOutputParser()
# print(parser.invoke(result))

#5.开始定义链
#执行链
#因此上述操作不用手动执行
#方式一管道符
chain = model | parser

#方式二
#chain=RunnableSequence(first=model,second=parser)

#方式三
# chain=model.pipe(parser)

print(chain.invoke(messages))