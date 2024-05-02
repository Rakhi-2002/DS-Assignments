import threading
import datetime
import socket
import time

def send_time(slave_client):
    while True:
        slave_client.send(str(datetime.datetime.now()).encode())
        print("Time sent successfully")
        time.sleep(5)

def receive_time(slave_client):
    while True:
        synchronized_time = datetime.datetime.strptime(slave_client.recv(1024).decode(), "%Y-%m-%d %H:%M:%S.%f")
        print("Synchronized time at the client is:", synchronized_time)

def initiate_slave_client(port=8080):
    slave_client = socket.socket()
    slave_client.connect(('127.0.0.1', port))
    print("Starting to receive time from server")
    threading.Thread(target=send_time, args=(slave_client,)).start()
    print("Starting to receive synchronized time from server")
    threading.Thread(target=receive_time, args=(slave_client,)).start()

if __name__ == '__main__':
    initiate_slave_client(port=8080)