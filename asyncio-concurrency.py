import asyncio

async def task_one():
    print("Task One: Start")
    await asyncio.sleep(2)
    print("Task One: End")

async def task_two():
    print("Task Two: Start")
    await asyncio.sleep(1)
    print("Task Two: End")

async def main():
    await asyncio.gather(task_one(), task_two())

asyncio.run(main())
