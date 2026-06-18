from flask import Flask, request
from flask_socketio import SocketIO, emit, disconnect

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Lưu trữ tất cả kết nối: { socket_id: { username, public_key } }
all_users = {}
# Lưu trữ tối đa 2 kết nối đang chat đôi: { socket_id: { username, public_key } }
online_users = {}

@socketio.on('connect')
def handle_connect():
    print(f"\n[INFO] Client connected: {request.sid}")

@socketio.on('disconnect')
def handle_disconnect():
    username = None
    if request.sid in all_users:
        username = all_users[request.sid]['username']
        del all_users[request.sid]
        
    if request.sid in online_users:
        print(f"[INFO] Client chat doi disconnected: {username}")
        del online_users[request.sid]
        
        if username:
            emit('user_left', username, broadcast=True)
            
        # Tự động chọn người dùng tiếp theo trong hàng chờ để đưa vào chat đôi
        for sid, user_info in all_users.items():
            if sid not in online_users:
                online_users[sid] = user_info
                print(f"[DH EXCHANGE] Tu dong dua user {user_info['username']} vao chat doi")
                if len(online_users) == 2:
                    emit('all_public_keys', list(online_users.values()), broadcast=True)
                break

@socketio.on('share_public_key')
def handle_share_key(data):
    all_users[request.sid] = {
        'username': data['username'],
        'public_key': data['public_key']
    }
    
    # Nếu chưa đủ 2 người trong chat đôi, thêm vào
    if len(online_users) < 2 and request.sid not in online_users:
        online_users[request.sid] = all_users[request.sid]
        print(f"[DH EXCHANGE] Nhan key tu: {data['username']} (Hien tai: {len(online_users)}/2 user chat doi)")
        
        if len(online_users) == 2:
            print("[DH EXCHANGE] Da du 2 nguoi hop le. Tien hanh kích hoat hoan doi khoa doi...")
            emit('all_public_keys', list(online_users.values()), broadcast=True)
    else:
        print(f"[DH EXCHANGE] Bo qua key tu {data['username']} (nguoi thu 3+) trong chat doi")
        emit('spectator_status', {'message': 'Bạn là người thứ 3 tham gia. Bạn không thể tham gia chat đôi nhưng có thể trò chuyện ở phòng chung!'}, room=request.sid)

@socketio.on('send_secure_message')
def handle_secure_message(data):
    emit('receive_secure_message', data, broadcast=True, include_self=False)

if __name__ == "__main__":
    print("[SERVER] Socket Server dang chay o port 5000...")
    socketio.run(app, port=5000, debug=True, allow_unsafe_werkzeug=True)