import asyncio
import concurrent.futures
import configs

async def main (data_list, callback):

    pool = concurrent.futures.ProcessPoolExecutor(configs.max_process)
    loop = asyncio.get_event_loop()
    resultProcess = []

    async def process_result (i):
        with pool:
            process = await loop.run_in_executor(pool, callback, i)
        return process
    
    for i in data_list:
        resultProcess.append(process_result(i)) 

    results = await asyncio.gather(*resultProcess, return_exceptions=True)

    return results

async def main2 (data_list, callback):

    loop = asyncio.get_event_loop()
    results = []

    def append_result (task):
        results.append(task.result())

    async def process_result (i):
        with concurrent.futures.ProcessPoolExecutor(4) as pool:
            process = await loop.run_in_executor(pool, callback, i)
        return process

    async with asyncio.TaskGroup() as tg:
        for i in data_list:
            task = tg.create_task(process_result(i))
            task.add_done_callback(append_result)

    return results

    results = []

    def append_result (task):
        results.append(task.result())

    async with asyncio.TaskGroup() as tg:
        for i in data_list:
            task = tg.create_task(asyncio.threads.to_thread(callback, i))
            task.add_done_callback(append_result)
    
    return results