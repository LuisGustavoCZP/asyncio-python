import asyncio
import requests
import time
from reader import read_csv
from . import parallel_process, parallel_thread, sequential

def get_request(value):
    print(f"start {value} blocking_network at {time.strftime('%X')}")
    result = requests.get(value).json()
    print(f"completed {value} blocking_network at {time.strftime('%X')}")
    return result

def read_file(value):
    print(f"start {value} blocking_io at {time.strftime('%X')}")
    result = read_csv(value)
    print(f"completed {value} blocking_io at {time.strftime('%X')}")
    return result

async def execute():

    data_list = [
        #"datasets/demographic_data.csv",
        "datasets/airports.csv",
        "datasets/airports.csv",
        "datasets/airports.csv",
        "datasets/airports.csv",
        "datasets/airports.csv",
        "datasets/airports.csv",
        "datasets/airports.csv",
        "datasets/airports.csv",
    ]

    url_list = [
        "https://rickandmortyapi.com/api/character",
        "https://rickandmortyapi.com/api/location",
        "https://rickandmortyapi.com/api/episode",
    ]
    
    print("\n Test Network Bounds:")
    parallel_process_deltatime = await parallel_process.main(url_list, get_request)
    parallel_thread_deltatime = await parallel_thread.main(url_list, get_request)
    sequential_deltatime = await sequential.main(url_list, get_request)
    print(f"\nParallel Process Time: {parallel_process_deltatime}\nParallel Thread Time: {parallel_thread_deltatime}\nSequential Time: {sequential_deltatime}")

    print("\n Test IO Bounds:")
    parallel_process_deltatime = await parallel_process.main(data_list, read_file)
    parallel_thread_deltatime = await parallel_thread.main(data_list, read_file)
    sequential_deltatime = await sequential.main(data_list, read_file)
    print(f"\nParallel Process Time: {parallel_process_deltatime}\nParallel Thread Time: {parallel_thread_deltatime}\nSequential Time: {sequential_deltatime}")

def main ():
    asyncio.run(execute())