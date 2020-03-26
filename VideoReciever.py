import socket
import sys
import subprocess


def deserialize_msg(msg):
    return (int.from_bytes(msg[0:4], "big"),  # frame_id
            int.from_bytes(msg[4:8], 'big'),  # payload_first_index
            int.from_bytes(msg[8:12], 'big'),  # payload_length
            int.from_bytes(msg[4:8], 'big') + int.from_bytes(msg[8:12], 'big'),  # payload_last_index
            msg[16:payload_length + 16])  # payload (h264)


receiver_address = ('192.168.3.10', 8880)
player_cmd_line_string = ['vlc', '--demux', 'h264', '--h264-fps', '30', '-']
video_player = subprocess.Popen(player_cmd_line_string, stdin=subprocess.PIPE)

try:
    receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver_socket.bind(receiver_address)
except socket.error as msg:
    print('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

frame_buff_1 = bytearray()  # buffer for even frames
frame_buff_2 = bytearray()  # buffer for odd frames
current_frame: int = 0

while True:
    received_msg, source_address = receiver_socket.recvfrom(1016)

    frame_id, payload_first_index, payload_length, payload_last_index, payload = deserialize_msg(received_msg)

    if frame_id >= current_frame + 2:
        if current_frame % 2 == 0:
            player.stdin.write(frame_buff_1)
            frame_low.clear()
        if current_frame % 2 == 1:
            player.stdin.write(frame_buff_2)
            frame_high.clear()
        current_frame = frame_id - 1

    if current_frame % 2 == 1:
        if current_frame == frame_id:
            frame_buff_2[payload_first_index:payload_last_index] = payload
        elif frame_id > actual_frame:
            frame_buff_1[payload_first_index:payload_last_index] = payload
    if actual_frame % 2 == 0:
        if current_frame == frame_id:
            frame_buff_1[payload_first_index:payload_last_index] = payload
        elif frame_id > actual_frame:
            frame_buff_2[payload_first_index:payload_last_index] = payload
