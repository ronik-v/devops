from psutil import virtual_memory
from asyncio import run
from aiohttp import ClientSession
from datetime import datetime
from time import sleep
from socket import gethostname, gethostbyname
from sys import argv


async def alarm_request(memory_used: int, total: int) -> None:
	now = datetime.now()
	ip = gethostbyname(gethostname())
	_json = {
		'time': now.strftime("%Y-%m-%d %H:%M:%S"),
		'ip': ip,
		'free_memory': f'{total - memory_used}',
		'message': f'Alarm host use {memory_used} of {total}',
	}
	try:
		async with ClientSession() as session:
			async with session.post(url=API_URL, json=_json) as resp:
				resp_data = await resp.json()
				print(f'POST result = {resp_data}')
	except:
		raise Warning(f'Post request error\nCheck your url = {API_URL}')


async def memory_checker() -> None:
	memory = virtual_memory()
	total, used, free = memory.total, memory.used, memory.free
	print(f'Used memory = {used} | total mem = {total} | Share of use = {round(used / total, 2)}')
	if used >= int(PER_POSSIBLE_USE * total):
		await alarm_request(used, total)


async def main() -> None:
	try:
		while True:
			await memory_checker()
			sleep(30)
	except KeyboardInterrupt:
		print('Memory controller drop')
		exit(0)


if __name__ == '__main__':
	# percentage of possible memory usage without alarm
	PER_POSSIBLE_USE, API_URL = int(argv[1]), argv[2]
	if 1 <= PER_POSSIBLE_USE < 100:
		PER_POSSIBLE_USE = round(PER_POSSIBLE_USE / 100, 2)
	else:
		raise Exception('You are using an invalid usage percentage value...\nIt must be from 1 to 99')
	run(main())
