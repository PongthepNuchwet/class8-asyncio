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
            item = queue.get_nowait()
        except asyncio.QueueEmpty:
            print(f"{time.ctime()} Consumer: got nothing , waiting a while...")
            await asyncio.sleep(0.5)
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


# Wed Aug 23 14:28:02 2023 Producer: Running
# Wed Aug 23 14:28:02 2023 Consumer: Running
# Wed Aug 23 14:28:02 2023 Consumer: got nothing , waiting a while...
# Wed Aug 23 14:28:02 2023 Consumer: got nothing , waiting a while...
# Wed Aug 23 14:28:03 2023 Producer: put 0.7547659974024341
# Wed Aug 23 14:28:03 2023 > got 0.7547659974024341
# Wed Aug 23 14:28:03 2023 Consumer: got nothing , waiting a while...
# Wed Aug 23 14:28:03 2023 Consumer: got nothing , waiting a while...
# Wed Aug 23 14:28:04 2023 Producer: put 0.9199624265239977
# Wed Aug 23 14:28:04 2023 > got 0.9199624265239977
# Wed Aug 23 14:28:04 2023 Consumer: got nothing , waiting a while...
# Wed Aug 23 14:28:04 2023 Producer: put 0.5587854493228992
# Wed Aug 23 14:28:04 2023 > got 0.5587854493228992
# Wed Aug 23 14:28:04 2023 Consumer: got nothing , waiting a while...
# Wed Aug 23 14:28:04 2023 Producer: put 0.315855872345411
# Wed Aug 23 14:28:04 2023 Producer: put 0.013429867027581532
# Wed Aug 23 14:28:05 2023 > got 0.315855872345411
# Wed Aug 23 14:28:05 2023 > got 0.013429867027581532
# Wed Aug 23 14:28:05 2023 Consumer: got nothing , waiting a while...
# Wed Aug 23 14:28:05 2023 Producer: put 0.8607283965051301
# Wed Aug 23 14:28:05 2023 > got 0.8607283965051301
# Wed Aug 23 14:28:05 2023 Consumer: got nothing , waiting a while...
# Wed Aug 23 14:28:06 2023 Producer: put 0.5006047698752678
# Wed Aug 23 14:28:06 2023 > got 0.5006047698752678
# Wed Aug 23 14:28:06 2023 Consumer: got nothing , waiting a while...
# Wed Aug 23 14:28:06 2023 Producer: put 0.1046092200338038
# Wed Aug 23 14:28:06 2023 > got 0.1046092200338038
# Wed Aug 23 14:28:06 2023 Consumer: got nothing , waiting a while...
# Wed Aug 23 14:28:07 2023 Producer: put 0.647129550329618
# Wed Aug 23 14:28:07 2023 > got 0.647129550329618
# Wed Aug 23 14:28:07 2023 Consumer: got nothing , waiting a while...
# Wed Aug 23 14:28:07 2023 Producer: put 0.5425082292659985
# Wed Aug 23 14:28:07 2023 Producer: Done
# Wed Aug 23 14:28:08 2023 > got 0.5425082292659985
# Wed Aug 23 14:28:08 2023 Consumer: Done