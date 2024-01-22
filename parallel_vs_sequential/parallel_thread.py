import time
from tasker import parallel_thread

async def main(data_list, callback):
    print(f"\nStarting Parallel Processing")
    start_timestamp = time.time()
    await parallel_thread.main(data_list, callback)
    # for i in results:
    #     print(f"\n{i}\n")
    return time.time() - start_timestamp
    