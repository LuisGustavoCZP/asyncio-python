import asyncio
import time

def blocking_io(value):
    print(f"start {value} blocking_io at {time.strftime('%X')}")
    with open(f"texto{value}.txt", "r") as arquivo:
        print(f"completed {value} blocking_io at {time.strftime('%X')}")
        return arquivo.read()

async def main():
    print(f"started main at {time.strftime('%X')}")

    results = []

    async with asyncio.TaskGroup() as tg:
        for i in [0, 1, 2, 3]:
            task = tg.create_task(asyncio.to_thread(blocking_io, i))
            task.add_done_callback(lambda task: results.append(task.result()))
    
    # for i in [0, 1, 2, 3]:
    #     results.append(await asyncio.to_thread(blocking_io, i))
    
    print(f"Result is {results} at {time.strftime('%X')}")


asyncio.run(main())