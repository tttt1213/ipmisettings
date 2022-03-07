import socket

host = "192.168.10.238"
port = 8629 #適当なPORTを指定してあげます
massage = ('192.168.20.95 NA read')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #オブジェクトの作成をします
client.connect((host, port)) #これでサーバーに接続します
client.send(massage.encode()) #適当なデータを送信します（届く側にわかるように）
response = client.recv(512) #レシーブは適当な2の累乗にします（大きすぎるとダメ）

print(response test)