# we will create a producer coroutine that will generate ten random numbers
# and put them on the queue. We will also create a consumer coroutine
# that will get numbers from the queue and report their values.

from random import random
import asyncio
import time

# coroutine to generate work
async def producer(queue):
    print(f"{time.ctime()} Producer: Running")
    # generate work
    for i in range(10):
        # generate work
        value = random()
        # block to simulate work
        await asyncio.sleep(value)
        # add to the queue
        await queue.put(value)
        print(f'{time.ctime()} Producer: put {value}')
    # send an all done signal
    await queue.put(None)
    print(f"{time.ctime()} Producer: Done")

# coroutine to consume work
async def consumer(queue):
    print(f"{time.ctime()} Consumer: Running")
    # consume work
    while True:

        # get a unit of work without blocking
        try:
            get_await = queue.get()
            # await the awaitable with a timeout
            item = await asyncio.wait_for(get_await,0.5)
        except asyncio.TimeoutError:
            print(f"{time.ctime()} Consumer: gave up waiting...")
            continue

        # check for stop signal
        if item is None:
            break
        # report
        print(f"{time.ctime()} > got {item}")
    # all done
    print(f"{time.ctime()} Consumer: Done")

# entry point corotine


async def main():
    # create the shared queue
    queue = asyncio.Queue()
    # run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))

# start the asyncio program
asyncio.run(main())


# Wed Aug 23 14:28:27 2023 Producer: Running
# Wed Aug 23 14:28:27 2023 Consumer: Running
# Wed Aug 23 14:28:28 2023 Producer: put 0.5005823992524218
# Wed Aug 23 14:28:28 2023 Consumer: gave up waiting...
# Wed Aug 23 14:28:28 2023 > got 0.5005823992524218
# Wed Aug 23 14:28:28 2023 Producer: put 0.12041877268742263
# Wed Aug 23 14:28:28 2023 > got 0.12041877268742263
# Wed Aug 23 14:28:29 2023 Consumer: gave up waiting...
# Wed Aug 23 14:28:29 2023 Producer: put 0.6728218068791444
# Wed Aug 23 14:28:29 2023 > got 0.6728218068791444
# Wed Aug 23 14:28:29 2023 Producer: put 0.5032103165782389
# Wed Aug 23 14:28:29 2023 Consumer: gave up waiting...
# Wed Aug 23 14:28:29 2023 > got 0.5032103165782389
# Wed Aug 23 14:28:30 2023 Consumer: gave up waiting...
# Wed Aug 23 14:28:30 2023 Producer: put 0.9062294267025764
# Wed Aug 23 14:28:30 2023 > got 0.9062294267025764
# Wed Aug 23 14:28:30 2023 Producer: put 0.215887147702422
# Wed Aug 23 14:28:30 2023 > got 0.215887147702422
# Wed Aug 23 14:28:31 2023 Producer: put 0.14080817027303527
# Wed Aug 23 14:28:31 2023 > got 0.14080817027303527
# Wed Aug 23 14:28:31 2023 Consumer: gave up waiting...
# Wed Aug 23 14:28:31 2023 Producer: put 0.5844580672962499
# Wed Aug 23 14:28:31 2023 > got 0.5844580672962499
# Wed Aug 23 14:28:32 2023 Consumer: gave up waiting...
# Wed Aug 23 14:28:32 2023 Producer: put 0.9114800048847561
# Wed Aug 23 14:28:32 2023 > got 0.9114800048847561
# Wed Aug 23 14:28:32 2023 Producer: put 0.2598306919136264
# Wed Aug 23 14:28:32 2023 Producer: Done
# Wed Aug 23 14:28:32 2023 > got 0.2598306919136264
# Wed Aug 23 14:28:32 2023 Consumer: Done