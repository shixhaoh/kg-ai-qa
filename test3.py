from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage

#1.基本用法
# gpt_model = init_chat_model(
#     model="ep-20260419142915-rpcdt",
#     model_provider="openai",
#     openai_api_key="ark-808d84e5-892e-44b8-af5e-5959c5563ee4-1e001",
#     openai_api_base="https://ark.cn-beijing.volces.com/api/v3",
# )
# print(f"gpt_model={gpt_model.invoke("你是谁")}")

#2.定义可配置的模型(模型模拟器)
# config_model = init_chat_model(temperature=0.3)
# messages = [
#     SystemMessage(content="请帮我进行翻译,由英文翻译成中文"),
#     HumanMessage(content="hi!")
# ]
# #.invoke()的config参数才真正意义上定义了模型
# print(config_model.invoke(messages,
#   config=
#   {"configurable":
#       {"model": "ep-20260419142915-rpcdt"}}).content
#       )
#
# print(f"gpt_model={config_model.invoke("你是谁")}")


#3.可配置的模型(默认参数)
#原本输出
#精简版本
model = init_chat_model(model="ep-20260419142915-rpcdt",
    model_provider="openai",
    openai_api_key="ark-808d84e5-892e-44b8-af5e-5959c5563ee4-1e001",
    openai_api_base="https://ark.cn-beijing.volces.com/api/v3",
    max_tokens=1024,
    temperature=0.3,
    configurable_fields=("max_tokens","temperature",),
    config_prefix="first"
)
messages = [
    SystemMessage(content="请你补全一段故事,100字数以内"),
    HumanMessage(content="一只猫正在__?")
]
result=model.invoke(messages,
             config={
                "configurable":{
                "first_max_tokens":10,
                "first_temperature":1.0,
                }
             }
)
print(result.content)