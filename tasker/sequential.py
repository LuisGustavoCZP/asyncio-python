import asyncio

async def main (data_list, callback):
    results = []
    for i in data_list:
        results.append(await asyncio.to_thread(callback, i))
    
    return results