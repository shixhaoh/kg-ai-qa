#同步IO
# #1.烧水
# #2.发消息
# import time
#
#
# def boil_water():
#     print("开始烧水...")
#     time.sleep(5)
#     print("烧水完成")
#
# def send_message():
#     print("开始发消息")
#     time.sleep(2)
#     print("发消息完成")
#
# def main():
#     #1.烧水
#     boil_water()
#     #2.发消息
#     send_message()
#
# if __name__ == "__main__":
#     main()

#异步IO
#1.烧水
#2.发消息
import asyncio
#协程
async def boil_water_async():
    print("开始烧水...")
    await asyncio.sleep(5)#等待这个操作完成期间可以做别的事情
    print("烧水完成")
#协程
async def send_message_async():
    print("开始发消息")
    await asyncio.sleep(2)
    print("发消息完成")

#协程调度
#事件循环
async def main():
    #1.烧水(任务)
    task1 = asyncio.create_task(boil_water_async())
    #2.发消息(任务)
    task2 = asyncio.create_task(send_message_async())

    await task1
    await task2

asyncio.run(main())



