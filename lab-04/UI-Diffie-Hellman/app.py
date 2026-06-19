from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dh_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

# Lắng nghe khi có một Client gửi khóa công khai Diffie-Hellman của họ lên
@socketio.on('share_dh_public_key')
def handle_dh_key(data):
    print(f"Server trung chuyển DH Public Key từ: {data['sender']}")
    # Gửi public key này cho client còn lại
    emit('receive_dh_public_key', data, broadcast=True, include_self=False)

# Lắng nghe và trung chuyển tin nhắn mã hóa AES
@socketio.on('message_from_client')
def handle_message(data):
    emit('message_from_server', data, broadcast=True, include_self=False)

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)