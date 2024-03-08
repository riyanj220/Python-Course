# import asyncio


# async def main():
#     print("start")
#     await asyncio.sleep(1)
#     print("end")


# asyncio.run(main())
# _____________________________________________________________________

# import time


# def task1():
#     print("task1 started")
#     time.sleep(3)
#     print("task1 ended")


# def task2():
#     print("task2 started")
#     time.sleep(2)
#     print("task2 ended")


# def main():
#     task1()
#     task2()
#     print("all task are called")


# main()

# ____________________________________________________________

import asyncio


# async def task1():
#     print("task1 started")
#     await asyncio.sleep(3)
#     print("task1 ended")


# async def task2():
#     print("task2 started")
#     await asyncio.sleep(2)
#     print("task2 ended")


# async def main():
#     await asyncio.gather(task1(), task2())
#     print("all task are called")


# asyncio.run(main())

# ____________________________________________________________________


import requests

URL = "https://instagram.com/favicon.ico"
response = requests.get(URL)

open("instagram.ico", "wb").write(response.content)


async def func1():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)

    open("instagram2.ico", "wb").write(response.content)
    print("func1")
    return "riyan"


async def func2():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)

    open("instagram3.ico", "wb").write(response.content)
    print("func2")
    return "riya"


async def func3():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)

    open("instagram.ico", "wb").write(response.content)
    print("func3")
    return "riy"


async def main():
    l = await asyncio.gather(func1(), func2(), func3())
    print(l)


asyncio.run(main())

# ___________________________________________________________________
