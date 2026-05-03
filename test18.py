from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder

from langchain_openai import ChatOpenAI

#1.定义OpenAi模型

model = ChatOpenAI(
    model="ep-20260419142915-rpcdt",
    openai_api_key="ark-808d84e5-892e-44b8-af5e-5959c5563ee4-1e001",
    openai_api_base="https://ark.cn-beijing.volces.com/api/v3",)
#定义文本提示词模板,Runnable实例
#方式一:
# prompt=PromptTemplate(
#     template="介绍{city}的历史",
#     input_variables=["city"],
# )

# #方式二
# prompt_template=PromptTemplate.from_template("将文本从{language_from}翻译为{language_to}")
# #调用:实例化模板
# print(prompt_template.invoke({"language_from": "英文", "language_to": "中文"}))


#处理聊天消息的模板
# chat_prompt_template=ChatPromptTemplate(
#     [
#         ("system","将文本从{language_from}翻译为{language_to}只输出翻译结果不要多余的废话"),
#         ("user","你是专业的翻译助手你要翻译这句话{text}")
#         #("ai","{}")
#     ]
# )

# messages=chat_prompt_template.invoke(
#     {"language_from": "英文",
#      "language_to": "中文",
#      "text": "hi,what your name"}
# )

# model.invoke(messages).pretty_print()
# chain=chat_prompt_template|model
# print(chain.invoke(
#     {"language_from": "英文",
#      "language_to": "中文",
#      "text": "hi,what your name"}
# ))



chat_prompt_template=ChatPromptTemplate(
    [
        ("system","将文本从{language_from}翻译为{language_to}只输出翻译结果不要多余的废话"),
        MessagesPlaceholder("msgs"),#消息占位符
        ("user","你是专业的翻译助手你要翻译这句话{text}")
        #("ai","{}")
    ]
)

messages_placeholder=[
    HumanMessage(content="hi,what your name"),
    AIMessage(content="你好,你叫什么名字")
]

chain=chat_prompt_template|model
chain.invoke(
    {
    "language_from": "英文",
    "language_to": "中文",
    "text": "hi,what your age",
    "msgs":messages_placeholder}
).pretty_print()