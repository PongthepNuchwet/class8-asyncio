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
    queue = asyncio.Queue(2)
    # start the consumer
    _ = asyncio.create_task(consumer(queue))
    # start the producer and wait for it to finish
    producers = [producer(queue) for _ in range(5)]

    await asyncio.gather(*producers)
    # wait for all items to be processed
    await queue.join()

# start the asyncio program
asyncio.run(main())

# Wed Aug 23 14:40:56 2023 Consumer: Running
# Wed Aug 23 14:40:56 2023 Producer: Running
# Wed Aug 23 14:40:56 2023 Producer: Running
# Wed Aug 23 14:40:56 2023 Producer: Running
# Wed Aug 23 14:40:56 2023 Producer: Running
# Wed Aug 23 14:40:56 2023 Producer: Running
# Wed Aug 23 14:40:56 2023 > got 0.09417540200686214
# Wed Aug 23 14:40:57 2023 > got 0.3420623884744082
# Wed Aug 23 14:40:57 2023 > got 0.4052456983178484
# Wed Aug 23 14:40:57 2023 > got 0.4318364422472504
# Wed Aug 23 14:40:58 2023 > got 0.3574992158026986
# Wed Aug 23 14:40:58 2023 > got 0.4329789347099251
# Wed Aug 23 14:40:59 2023 > got 0.49239476907090374
# Wed Aug 23 14:40:59 2023 > got 0.33045271968422807
# Wed Aug 23 14:41:00 2023 > got 0.3636170598390841
# Wed Aug 23 14:41:00 2023 > got 0.99820282788956
# Wed Aug 23 14:41:01 2023 > got 0.32949886865894107
# Wed Aug 23 14:41:01 2023 > got 0.03123851499442254
# Wed Aug 23 14:41:01 2023 > got 0.5433144954848662
# Wed Aug 23 14:41:02 2023 > got 0.7271985575518582
# Wed Aug 23 14:41:03 2023 > got 0.3037594197024084
# Wed Aug 23 14:41:03 2023 > got 0.9889683329137245
# Wed Aug 23 14:41:04 2023 > got 0.8960924267283653
# Wed Aug 23 14:41:05 2023 > got 0.7395411683852644
# Wed Aug 23 14:41:06 2023 > got 0.5012180500869045
# Wed Aug 23 14:41:06 2023 > got 0.6953314077075106
# Wed Aug 23 14:41:07 2023 > got 0.5967008959888018
# Wed Aug 23 14:41:07 2023 > got 0.17630951616865953
# Wed Aug 23 14:41:08 2023 > got 0.9321100275651582
# Wed Aug 23 14:41:09 2023 > got 0.36794890576076933
# Wed Aug 23 14:41:09 2023 > got 0.18265944600790107
# Wed Aug 23 14:41:09 2023 > got 0.3548270596646347
# Wed Aug 23 14:41:09 2023 > got 0.7626140057149501
# Wed Aug 23 14:41:10 2023 > got 0.8230033813420511
# Wed Aug 23 14:41:11 2023 > got 0.8937247344957122
# Wed Aug 23 14:41:12 2023 > got 0.33208305852065745
# Wed Aug 23 14:41:12 2023 > got 0.036189937731678334
# Wed Aug 23 14:41:12 2023 > got 0.4658617756631558
# Wed Aug 23 14:41:13 2023 > got 0.861120395460787
# Wed Aug 23 14:41:14 2023 > got 0.5129093473684271
# Wed Aug 23 14:41:14 2023 > got 0.8916385904960299
# Wed Aug 23 14:41:15 2023 > got 0.14413412498478528
# Wed Aug 23 14:41:15 2023 > got 0.07996063471381099
# Wed Aug 23 14:41:15 2023 > got 0.6613653513919862
# Wed Aug 23 14:41:16 2023 > got 0.16962554800432994
# Wed Aug 23 14:41:16 2023 > got 0.6544772386908548
# Wed Aug 23 14:41:17 2023 > got 0.8119507640837339
# Wed Aug 23 14:41:17 2023 Producer: Done
# Wed Aug 23 14:41:18 2023 > got 0.40678527997094305
# Wed Aug 23 14:41:18 2023 > got 0.08900406801695726
# Wed Aug 23 14:41:18 2023 > got 0.6884462507339517
# Wed Aug 23 14:41:18 2023 Producer: Done
# Wed Aug 23 14:41:19 2023 > got 0.7692575516316793
# Wed Aug 23 14:41:19 2023 Producer: Done
# Wed Aug 23 14:41:20 2023 > got 0.10186340161626684
# Wed Aug 23 14:41:20 2023 Producer: Done
# Wed Aug 23 14:41:20 2023 > got 0.5968926720806805
# Wed Aug 23 14:41:20 2023 > got 0.29628670834713156
# Wed Aug 23 14:41:20 2023 Producer: Done
# Wed Aug 23 14:41:21 2023 > got 0.5181612753191559
# Wed Aug 23 14:41:21 2023 > got 0.08611066711741688
