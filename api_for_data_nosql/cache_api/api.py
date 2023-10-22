from flask import Flask, request, json
from redis import StrictRedis
from typing import Any, Awaitable

# initialization of main components
api = Flask(__name__)
_redis = StrictRedis(
	host='127.0.0.1',
	port=6379,
	charset='utf-8',
	decode_responses=True
)


@api.route('/api/get', methods=['GET'])
def get_value() -> dict[str, Awaitable | int | Any] | dict[str, str | int] | None:
	if request.args.get('key'):
		try:
			value = _redis.get(request.args.get('key'))
			return {'status': 200, 'value': value}
		except:
			return {'status': 404, 'value': ''}


@api.route('/api/insert', methods=['POST'])
def insert_value() -> dict[str, int] | None:
	# take json... format = {'key': some_key, 'value': some_value}
	insert_data = request.get_json()
	if insert_data['key'] != '' and insert_data['value'] != '':
		try:
			new = _redis.set(insert_data['key'], insert_data['value'])
			return {'status': 200}
		except:
			return {'status': 404}


@api.route('/api/update', methods=['PUT'])
def update_value() -> dict[str, int] | None:
	# use redis "GETSET"
	# take json... format = {'key': some_key, 'value': some_new_value}
	update_data = json.loads(request.data)
	if update_data and update_data.get('key') != '' and update_data.get('value') != '':
		try:
			new = _redis.getset(update_data.get('key'), update_data.get('value'))
			return {'status': 200}
		except:
			return {'status': 404}


if __name__ == '__main__':
	api.run(debug=False, port=8080)
