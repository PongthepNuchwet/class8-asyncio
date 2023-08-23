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
        # print(f'{time.ctime()} Producer: put {value}')
    print(f"{time.ctime()} Producer: Done")

# coroutine to consume work


async def consumer(queue):
    print(f"{time.ctime()} Consumer: Running")
    # consume work
    while True:

        # get a unit of work without blocking

        item = await queue.get()
        # report
        print(f"{time.ctime()} > got {item}")

        # check for stop signal
        if item:
            await asyncio.sleep(item)

        queue.task_done()


# entry point corotine
async def main():
    # create the shared queue
    queue = asyncio.Queue()
    # start the consumer
    _ = asyncio.create_task(consumer(queue))
    # start the producer and wait for it to finish
    await asyncio.create_task(producer(queue))
    # wait for all items to be processed
    await queue.join()

# start the asyncio program
asyncio.run(main())

# Wed Aug 23 14:38:29 2023 Consumer: Running
# Wed Aug 23 14:38:29 2023 Producer: Running
# Wed Aug 23 14:38:30 2023 > got 0.9271930633259894
# Wed Aug 23 14:38:31 2023 > got 0.641953217158021
# Wed Aug 23 14:38:32 2023 > got 0.8706615534169184
# Wed Aug 23 14:38:33 2023 > got 0.5357065668464032
# Wed Aug 23 14:38:33 2023 > got 0.9628973929546193
# Wed Aug 23 14:38:34 2023 > got 0.5492758835534498
# Wed Aug 23 14:38:35 2023 > got 0.2569636280652018
# Wed Aug 23 14:38:35 2023 > got 0.6961301146954427
# Wed Aug 23 14:38:36 2023 > got 0.8804428788352309
# Wed Aug 23 14:38:37 2023 Producer: Done
# Wed Aug 23 14:38:37 2023 > got 0.9792386440674326