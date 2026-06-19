from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secure_chat_secret_key_123'
# Cho phép kết nối từ mọi nguồn (CORS)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

# Lắng nghe sự kiện khi có tin nhắn gửi lên từ một Client
@socketio.on('message_from_client')
def handle_message(data):
    print(f"Server nhận dữ liệu (đã mã hóa): {data}")
    # Phát ngược lại tin nhắn đó cho TẤT CẢ các bên đang kết nối (Broadcast)
    emit('message_from_server', data, broadcast=True, include_self=False)

if __name__ == '__main__':
    # Chạy server Socket tại cổng 5000
    socketio.run(app, debug=True, port=5000)