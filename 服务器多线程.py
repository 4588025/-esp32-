import sqlite3
import socket
import threading


# # 删除表格
# cursor.execute("DROP TABLE IF EXISTS managers")
# cursor.execute("DROP TABLE IF EXISTS students")





conn = sqlite3.connect("example.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS light ( id PRIMARY KEY NOT NULL, state1 TEXT)")


cursor.execute("CREATE TABLE IF NOT EXISTS temp (id TEXT, temp TEXT, time1 TEXT)")


cursor.execute("CREATE TABLE IF NOT EXISTS humi (id TEXT, humi TEXT, time1 TEXT)")

cursor.execute("CREATE TABLE IF NOT EXISTS dis (id TEXT, dis TEXT, time1 TEXT)")

conn.commit()
conn.close()


def handle_client(client, addr):
    print(f"New client connected: {addr}")
    while True:
        data = client.recv(1024).decode("utf-8")
        if not data:
            break
        print(data)
        response = data.upper()
        #client.send(response.encode("utf-8"))
    client.close()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('192.168.113.199', 8888))
    server.listen(128)
    print("Server is running on localhost:5000")

    while True:
        client, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.start()
        print(f"Thread {thread.name} started")


if __name__ == "__main__":
    main()
    pass