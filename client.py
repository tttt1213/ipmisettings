# ソケットライブラリ取り込み
import socket

# サーバーIPとポート番号
IPADDR = "127.0.0.1"
PORT = 49152

# ソケット作成
sock = socket.socket(socket.AF_INET)
# サーバーへ接続
sock.connect((IPADDR, PORT))

# byte 形式でデータ送信
sock.send("hello".encode("utf-8"))
