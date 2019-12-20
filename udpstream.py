import socket

class VideoController:
    def __init__(self):
        self.frame_id = 0
        self.transmitter = None

    def write(self, s):
        datagrams = self.transmitter.video_datagram_creator((self.frame_id, s))
        self.transmitter.video_send_data(datagrams)
        self.frame_id += 1

    def set_transmision_method(self, sender):
        self.transmitter = sender

class UDPVideoTransmitter:
    def __init__(self, ip, port, repeat):
        self.dest_address = (ip, port)
        self.repeat = repeat
        self.payload = 1000
        # socket init
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def video_datagram_creator(self, r_data):
        packet_length = self.payload
        datagrams = list()
        frame_id = r_data[0]
        msg = bytes(r_data[1])
        for i in range(0, int(len(msg) / packet_length) + 1):
            if packet_length * i + packet_length > len(msg):
                if len(msg) != i * packet_length:
                    datagrams.append(
                                    int.to_bytes(frame_id, 4, 'big') +
                                    int.to_bytes(i * packet_length, 4, 'big') +
                                    int.to_bytes(len(msg) - i*packet_length, 4, 'big') +
                                    int.to_bytes(len(msg), 4, 'big') +
                                    msg[i * packet_length:len(msg)])
            else:
                datagrams.append(
                                int.to_bytes(frame_id, 4, 'big') +
                                int.to_bytes(i * packet_length, 4, 'big') +
                                int.to_bytes(packet_length, 4, 'big') +
                                int.to_bytes(len(msg), 4, 'big') +
                                msg[i * packet_length:packet_length * i + packet_length])
        return datagrams

    def video_send_data(self, datagrams):
        packet_repeat = 2 if self.repeat else 1
        for datagram in datagrams:
            for n in range(0, packet_repeat):
                self.socket.sendto(datagram, self.dest_address)

    def __del__(self):
        self.socket.close()