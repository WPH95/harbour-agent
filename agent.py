from flask import Flask, jsonify, request
app = Flask(__name__)
import docker
import json
c = docker.Client(base_url='unix://var/run/docker.sock',version='1.9',timeout=10)
@app.route('/', methods=['GET', 'POST'])
def docker_exec():
    key = request.args.get('key', '')
    if key!='nijueduixiangbuchulai':
        return "503!!!you not have permit"
    _exec = request.form.get('exec', 'data = c.info()')
    exec _exec
    return jsonify(results=data)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=12345)
