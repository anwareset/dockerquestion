from flask import Flask, request, jsonify
from redis import Redis

app = Flask(__name__)
redis = Redis(host= "redis", port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return jsonify({'ip': request.remote_addr},{'visit': '{0}' . format (redis.get( 'hits' ))}), 200

if __name__ == "__main__":
    app.run(host= "0.0.0.0", debug=False)
