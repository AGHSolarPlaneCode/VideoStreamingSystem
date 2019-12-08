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

    def send_data(self, datagrams):
        print('Send data to server')