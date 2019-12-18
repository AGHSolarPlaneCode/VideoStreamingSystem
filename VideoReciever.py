import socket
import sys

ADDRESS = ('localhost', 8889)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sendSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error as msg:
    print('Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
try:
    sendSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error as msg:
    print('Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

try:
    s.bind(ADDRESS)
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()


frame_high = bytes()
frame_low = bytes()
actual_frame: int = 0

while True:
    d, address = s.recvfrom(1016)
    if int.from_bytes(d[0:4], 'big') >= actual_frame + 2:
        if actual_frame % 2 == 1:
            sendSocket.sendto(frame_high, ('localhost', 7787))
            frame_high = bytes()
        elif actual_frame % 2 == 0:
            sendSocket.sendto(frame_low, ('localhost', 7787))
            frame_low = bytes()
        actual_frame += 1

    if actual_frame % 2 == 1:
        if actual_frame == int.from_bytes(d[0:4], "big"):
            frame_high[int.from_bytes(d[4:8], 'big'), int.from_bytes(d[4:8], 'big') + int.from_bytes(d[8:12], 'big')] = d[16:1016]
        elif int.from_bytes(d[0:4], "big") > actual_frame:
            frame_low[int.from_bytes(d[4:8], 'big'), int.from_bytes(d[4:8], 'big') + int.from_bytes(d[8:12], 'big')] = d[16:1016]
    if actual_frame % 2 == 0:
        if actual_frame == int.from_bytes(d[0:4], "big"):
            frame_low[int.from_bytes(d[4:8], 'big'), int.from_bytes(d[4:8], 'big') + int.from_bytes(d[8:12], 'big')] = d[16:1016]
        elif int.from_bytes(d[0:4], "big") > actual_frame:
            frame_high[int.from_bytes(d[4:8], 'big'), int.from_bytes(d[4:8], 'big') + int.from_bytes(d[8:12], 'big')] = d[16:1016]

