from flask import Flask
from flask import request, make_response, jsonify
from flask_cors import CORS
import datetime, base64, requests, json
from Crypto.Hash import CMAC
from Crypto.Cipher import AES

app = Flask(__name__)

def toggleLock():
	# 各種パラメータ
	uuid = ''
	secret_key = ''
	api_key = ''

	# ヘッダーの設定
	headers = {'x-api-key': api_key}

	# cmd
	cmd = 88 # 施錠する場合は「82」、解錠する場合は「83」

	# history
	history = 'WEB API' # とりあえず「WEB API」と名付ける
	base64_history = base64.b64encode(bytes(history, 'utf-8')).decode()

	# sign
	cmac = CMAC.new(bytes.fromhex(secret_key), ciphermod=AES)
	ts = int(datetime.datetime.now().timestamp())
	message = ts.to_bytes(4, byteorder='little')
	message = message.hex()[2:8]
	cmac = CMAC.new(bytes.fromhex(secret_key), ciphermod=AES)
	cmac.update(bytes.fromhex(message))
	sign = cmac.hexdigest()

	# API
	url = f'https://app.candyhouse.co/api/sesame2/{uuid}/cmd'
	body = {
		'cmd': cmd,
		'history': base64_history,
		'sign': sign
	}
	res = requests.post(url, json.dumps(body), headers=headers)

@app.route("/", methods=['GET'])
def hello():
	toggleLock()
	return "ok"

if __name__ == "__main__":
		app.debug = True
		app.run(host='127.0.0.1', port=5000)
