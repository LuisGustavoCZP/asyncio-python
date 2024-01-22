import asyncio
import concurrent.futures
import configs

async def main (data_list, callback):
    pool = concurrent.futures.ThreadPoolExecutor(configs.max_threads)
    loop = asyncio.get_event_loop()
    resultProcess = []

    # def append_result (task):
    #     results.append(task.result())

    # async with asyncio.TaskGroup() as tg:
    #     for i in data_list:
    #         task = tg.create_task(asyncio.threads.to_thread(callback, i))
    #         task.add_done_callback(append_result)
        
    async def process_result (i):
        with pool:
            process = await loop.run_in_executor(pool, callback, i)
        return process
    
    for i in data_list:
        resultProcess.append(process_result(i)) 

    return await asyncio.gather(*resultProcess, return_exceptions=True)