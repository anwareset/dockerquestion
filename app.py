from flask import Flask, request, redirect, url_for, make_response, session, jsonify
from flask_session import Session
from redis import Redis

app = Flask(__name__)

app.secret_key = 'BAD_SECRET_KEY'
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = True
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_REDIS'] = Redis(host="redis", port=6379)
app.config.from_object(__name__)
Session(app)

@app.route('/')
def hello():
    if 'count' in session:
        session['count'] = session.get('count') + 1
    else:
        session['count'] = 1
    return jsonify({'ip': request.remote_addr},{'visit': '{0}' . format(session.get( 'count' ))}), 200

if __name__ == "__main__":
    app.run(host= "0.0.0.0", debug=False)
