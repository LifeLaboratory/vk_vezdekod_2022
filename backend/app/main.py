# -*- coding: utf-8 -*-
from flask import request, jsonify, make_response
from source.processor import Processor
from flask import Flask
from source.helper import main

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/list', methods=['GET'])
@app.route('/list/<limit>', methods=['GET'])
@app.route('/list/<limit>/<offset>', methods=['GET'])
def list_image(limit=25, offset=0):
    images = Processor().get_all_user({'limit': limit, 'offset': offset})
    return jsonify(images)


@app.route('/get/<id_image>', methods=['GET'])
def get_image(id_image):
    images = Processor().get_image(id_image)
    return jsonify(images)


@app.route('/like/<id_image>', methods=['GET'])
def like_image(id_image):
    images = Processor().set_likes(id_image)
    return jsonify(images)


@app.route('/priority/<id_image>', methods=['GET'])
def priority_image(id_image):
    images = Processor().set_priority_image(id_image)
    return jsonify(images)


@app.route('/statistic', methods=['GET'])
def statistic():
    images = Processor().get_statistics()
    return jsonify(images)


if __name__ == "__main__":
    main()
    app.run(host='0.0.0.0', debug=False, port=13452)
