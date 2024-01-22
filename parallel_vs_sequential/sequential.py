import time
from tasker import sequential

async def main(data_list, callback):
    print(f"\nStarting Sequential Processing")
    start_timestamp = time.time()
    results = await sequential.main(data_list, callback)
    #print(f"Result is {results}\n at {time.time() - start_timestamp}")
    return time.time() - start_timestamp