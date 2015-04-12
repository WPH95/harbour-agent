from flask import Flask, jsonify, request
app = Flask(__name__)
import docker
import json
c = docker.Client(base_url='unix://var/run/docker.sock',version='1.17',timeout=10)
_stats = c.stats('work_wiki_1')
@app.route('/', methods=['GET', 'POST'])
def docker_exec():
    key = request.args.get('key', '')
    if key!='nijueduixiangbuchulai':
        return "503!!!you not have permit"
    _exec = 'data = c.' + request.form.get('exec', 'info()')
    app.logger.debug(_exec)
    exec _exec
    return jsonify(results=data)

@app.route('/stats', methods=['GET', 'POST'])
def docker_stats():
    key = request.args.get('key', '')
    if key!='nijueduixiangbuchulai':
        return "503!!!you not have permit"
    id = request.args.get('id', '')
    _exec = "stats = c.stats('{0}')".format(id)
    exec _exec
    for t in stats:
        data = t
        break
    return data

@app.route('/containers', methods=['GET', 'POST'])
def docker_containers():
    key = request.args.get('key', '')
    if key!='nijueduixiangbuchulai':
        return "503!!!you not have permit"
    containers = c.containers()
    data = []
    for container in containers:
        data.append(c.inspect_container(container['Id']))
    return jsonify(results=data)


@app.route('/images', methods=['GET', 'POST'])
def docker_images():
    key = request.args.get('key', '')
    if key!='nijueduixiangbuchulai':
        return "503!!!you not have permit"
    images = c.images()
    data = []
    for image in images:
        data.append(c.inspect_image(image['Id']))
    return jsonify(results=data)



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=12345)
