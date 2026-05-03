from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from openai import max_retries, BaseModel
from pydantic import Field

from Langchain.test6 import model_with_tools

model = ChatOpenAI(
    model="ep-20260419142915-rpcdt",
    openai_api_key="ark-808d84e5-892e-44b8-af5e-5959c5563ee4-1e001",
    openai_api_base="https://ark.cn-beijing.volces.com/api/v3",)

#定义工具
tool = TavilySearch(max_result=4)

#绑定工具
model_with_tools = model.bind_tools([tool])

#定义消息列表
messages = [
    HumanMessage("北京今天的天气怎么样?")
]
ai_message = model.invoke(messages)
messages.append(ai_message)
for tool_call in ai_message.tool_calls:
    tool_message = tool.invoke(tool_call)
    messages.append(tool_message)

class SearchResult(BaseModel):
    """这是一个结构化搜索对象"""
    query:str=Field(description="搜索查询")
    findings:str=Field(description="查询结果摘要")

model_with_search=model.with_structured_output(SearchResult)
print(model_with_search.invoke(messages))