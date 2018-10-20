# Sleep sort - in asyncio Python 3.6
import asyncio


async def dosleep(i):
    await asyncio.sleep(i)
    print(i)


loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(
        *[dosleep(i) for i in [8, 4, 1, 3, 7]]
    )
)
loop.close()
