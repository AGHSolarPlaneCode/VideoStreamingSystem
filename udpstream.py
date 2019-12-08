import socket

class VideoController:
    def __init__(self):
        self.frameid = 0
        self.frame_buffer = bytes()
        self.transmitter = None
        self.running = False

    def write(self, s):
        print('Get frame')

    def set_transmision_method(self, sender):
        self.transmitter = sender

class UDPVideoTransmitter:
    def __init__(self, ip, port, repeat):
        self.ipaddress = ip
        self.port = port
        self.repeat = repeat
        # socket init
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #self.socket.bind((ip, port))  # uncomment with appropriate address

    def datagram_creator(self, rdata):
        print('Prepare datagram list ( > MTU) ')
        PACKET_LENGTH = self.payload
        PACKET_REPEAT = 2 if self.repeat else 1
        datagrams = list()
        msg = bytes(data)
        for n in range(0, PACKET_REPEAT):
            for i in range(0, int(len(msg) / PACKET_LENGTH) + 1):
                if PACKET_LENGTH * i + PACKET_LENGTH > len(msg):
                    if len(msg) != i * PACKET_LENGTH:
                        datagrams.append(int.to_bytes(i * PACKET_LENGTH, 4, 'big') + msg[i * PACKET_LENGTH:len(msg)])
                else:
                    datagrams.append(int.to_bytes(i * PACKET_LENGTH, 4, 'big') + msg[i * PACKET_LENGTH:PACKET_LENGTH * i + PACKET_LENGTH])

        return datagrams

    def send_data(self, datagrams):
        for datagram in datagrams:
            print(datagram)