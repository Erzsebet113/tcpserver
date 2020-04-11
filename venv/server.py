import re
import socket
import logging

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()
print('Connection address:', addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print("received data:", data.decode())
    result = re.match(r'(\d{4})\s([A-Za-z]\d{1})\s((?:2[0-3]|[01][0-9]):[0-5][0-9]:[0-5][0-9].\d{3})\s(\d{2})(\[CR\])',
                      data.decode())
    logging.basicConfig(filename="data.log", level=logging.INFO)

    logging.info(result.group(0))

    if result.group(4) == '00':
        showData = (f"Спортсмен, нагрудный номер: {result.group(1)} прошел отсечку {result.group(2)} в {result.group(3)[:-2]}")
        conn.send(showData.encode())  # echo
conn.close()

conn, s.accept()