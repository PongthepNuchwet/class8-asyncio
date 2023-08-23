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
        # get a unit of work
        item = await queue.get()
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


# Wed Aug 23 14:27:33 2023 Producer: Running
# Wed Aug 23 14:27:33 2023 Consumer: Running
# Wed Aug 23 14:27:34 2023 Producer: put 0.8475005222669835
# Wed Aug 23 14:27:34 2023 > got 0.8475005222669835
# Wed Aug 23 14:27:34 2023 Producer: put 0.11850263173276876
# Wed Aug 23 14:27:34 2023 > got 0.11850263173276876
# Wed Aug 23 14:27:35 2023 Producer: put 0.18465793760891946
# Wed Aug 23 14:27:35 2023 > got 0.18465793760891946
# Wed Aug 23 14:27:35 2023 Producer: put 0.30017855667927495
# Wed Aug 23 14:27:35 2023 > got 0.30017855667927495
# Wed Aug 23 14:27:35 2023 Producer: put 0.19540596427404477
# Wed Aug 23 14:27:35 2023 > got 0.19540596427404477
# Wed Aug 23 14:27:36 2023 Producer: put 0.48196829917047024
# Wed Aug 23 14:27:36 2023 > got 0.48196829917047024
# Wed Aug 23 14:27:36 2023 Producer: put 0.2121282704307147
# Wed Aug 23 14:27:36 2023 > got 0.2121282704307147
# Wed Aug 23 14:27:36 2023 Producer: put 0.6642197116774426
# Wed Aug 23 14:27:36 2023 > got 0.6642197116774426
# Wed Aug 23 14:27:37 2023 Producer: put 0.9571552860283901
# Wed Aug 23 14:27:37 2023 > got 0.9571552860283901
# Wed Aug 23 14:27:38 2023 Producer: put 0.28640574277489006
# Wed Aug 23 14:27:38 2023 Producer: Done
# Wed Aug 23 14:27:38 2023 > got 0.28640574277489006
# Wed Aug 23 14:27:38 2023 Consumer: Done