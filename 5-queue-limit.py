# we will create a producer coroutine that will generate ten random numbers
# and put them on the queue. We will also create a consumer coroutine
# that will get numbers from the queue and report their values.

from random import random
import asyncio
import time

# coroutine to generate work


async def producer(queue,id):
    print(f"{time.ctime()} Producer: Running")
    # generate work
    for i in range(10):
        # generate work
        value = random()
        # block to simulate work
        await asyncio.sleep((id+1) * 0.1)
        # add to the queue
        await queue.put(value)
        # print(f'{time.ctime()} Producer: put {value}')
    print(f"{time.ctime()} Producer {id+1}: Done")

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
    queue = asyncio.Queue(2)
    # start the consumer
    _ = asyncio.create_task(consumer(queue))
    # start the producer and wait for it to finish
    producers = [producer(queue,i) for i in range(5)]

    await asyncio.gather(*producers)
    # wait for all items to be processed
    await queue.join()

# start the asyncio program
asyncio.run(main())


# Wed Aug 23 15:00:14 2023 Consumer: Running
# Wed Aug 23 15:00:14 2023 Producer: Running
# Wed Aug 23 15:00:14 2023 Producer: Running
# Wed Aug 23 15:00:14 2023 Producer: Running
# Wed Aug 23 15:00:14 2023 Producer: Running
# Wed Aug 23 15:00:14 2023 Producer: Running
# Wed Aug 23 15:00:14 2023 > got 0.258685248897251
# Wed Aug 23 15:00:15 2023 > got 0.5549122635910095
# Wed Aug 23 15:00:15 2023 > got 0.7285518126885728
# Wed Aug 23 15:00:16 2023 > got 0.34659844045662414
# Wed Aug 23 15:00:16 2023 > got 0.5731779308481642
# Wed Aug 23 15:00:17 2023 > got 0.4888030145748118
# Wed Aug 23 15:00:17 2023 > got 0.8727602367389058
# Wed Aug 23 15:00:18 2023 > got 0.8959191886006762
# Wed Aug 23 15:00:19 2023 > got 0.9748830705862149
# Wed Aug 23 15:00:20 2023 > got 0.18973940649421817
# Wed Aug 23 15:00:20 2023 > got 0.7145867490516197
# Wed Aug 23 15:00:21 2023 > got 0.04857068119170549
# Wed Aug 23 15:00:21 2023 > got 0.7767235909784673
# Wed Aug 23 15:00:22 2023 > got 0.09766759358604726
# Wed Aug 23 15:00:22 2023 > got 0.4862140634583001
# Wed Aug 23 15:00:22 2023 > got 0.40849348586969636
# Wed Aug 23 15:00:23 2023 > got 0.04391816923777736
# Wed Aug 23 15:00:23 2023 > got 0.5788493769952537
# Wed Aug 23 15:00:23 2023 > got 0.06978317185801453
# Wed Aug 23 15:00:24 2023 > got 0.6120384767397501
# Wed Aug 23 15:00:24 2023 > got 0.5442269171493297
# Wed Aug 23 15:00:25 2023 > got 0.061687478684670616
# Wed Aug 23 15:00:25 2023 > got 0.22617367794371657
# Wed Aug 23 15:00:25 2023 > got 0.3037287962491103
# Wed Aug 23 15:00:25 2023 > got 0.2484333548702078
# Wed Aug 23 15:00:26 2023 > got 0.9098650247822626
# Wed Aug 23 15:00:27 2023 > got 0.9599502147254857
# Wed Aug 23 15:00:28 2023 > got 0.49578360786167386
# Wed Aug 23 15:00:28 2023 > got 0.8685865048549809
# Wed Aug 23 15:00:29 2023 > got 0.9770977293009286
# Wed Aug 23 15:00:30 2023 > got 0.91921647123114
# Wed Aug 23 15:00:31 2023 > got 0.028898181650797827
# Wed Aug 23 15:00:31 2023 > got 0.08831856868033106
# Wed Aug 23 15:00:31 2023 > got 0.24218651960063753
# Wed Aug 23 15:00:31 2023 > got 0.04803791601654861
# Wed Aug 23 15:00:31 2023 > got 0.2768250101906967
# Wed Aug 23 15:00:32 2023 > got 0.33191447759086257
# Wed Aug 23 15:00:32 2023 Producer 1: Done
# Wed Aug 23 15:00:32 2023 > got 0.6653252218817094
# Wed Aug 23 15:00:33 2023 > got 0.48011626971331234
# Wed Aug 23 15:00:33 2023 > got 0.5810573779559701
# Wed Aug 23 15:00:33 2023 Producer 5: Done
# Wed Aug 23 15:00:34 2023 > got 0.042300231845943226
# Wed Aug 23 15:00:34 2023 > got 0.8120600676969553
# Wed Aug 23 15:00:35 2023 > got 0.1654100999031588
# Wed Aug 23 15:00:35 2023 Producer 2: Done
# Wed Aug 23 15:00:35 2023 > got 0.14895560344748893
# Wed Aug 23 15:00:35 2023 > got 0.28388677663564177
# Wed Aug 23 15:00:35 2023 > got 0.7216372601936817
# Wed Aug 23 15:00:36 2023 > got 0.5987476218749139
# Wed Aug 23 15:00:36 2023 Producer 4: Done
# Wed Aug 23 15:00:36 2023 > got 0.05725735810418697
# Wed Aug 23 15:00:36 2023 Producer 3: Done
# Wed Aug 23 15:00:37 2023 > got 0.8106191055036708
# Wed Aug 23 15:00:37 2023 > got 0.5338792684329929