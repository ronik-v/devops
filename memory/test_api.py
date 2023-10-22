from flask import Flask, request
api = Flask(__name__)


@api.route('/api', methods=['POST'])
def index():
	if request.method == 'POST':
		host_data = request.get_json()
		print('type = ', type(host_data))
		print(host_data)
	return {'status': 200}


if __name__ == '__main__':
	api.run(debug=False, port=8000)
