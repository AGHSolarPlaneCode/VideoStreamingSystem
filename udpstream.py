import socket

class VideoController:
    def __init__(self):
        self.frameid = 0
        self.frame_buffer = bytes()
        self.transmitter = None
        self.running = False

    def write(self, s):
        self.transmitter.send_data(self.transmitter.datagram_creator(s))

    def set_transmision_method(self, sender):
        self.transmitter = sender

class UDPVideoTransmitter:
    def __init__(self, ip, port, repeat):
        self.ipaddress = ip
        self.port = port
        self.repeat = repeat
        self.payload = 1000
        # socket init
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def datagram_creator(self, rdata):

        packet_length = self.payload
        packet_repeat = 2 if self.repeat else 1
        datagrams = list()
        msg = bytes(rdata)
        for n in range(0, packet_repeat):
            for i in range(0, int(len(msg) / packet_length) + 1):
                if packet_length * i + packet_length > len(msg):
                    if len(msg) != i * packet_length:
                        datagrams.append(int.to_bytes(i * packet_length, 4, 'big') + msg[i * packet_length:len(msg)])
                else:
                    datagrams.append(int.to_bytes(i * packet_length, 4, 'big') + msg[i * packet_length:packet_length* i + packet_length])
        return datagrams

    def send_data(self, datagrams):

        for datagram in datagrams:
            self.socket.sendto(datagram, (self.ipaddress, self.port))
