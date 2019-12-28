import udpstream as udp

x = udp.UDPVideoTransmitter(None, None, False)
x.payload = 1000
datagrams = x.video_datagram_creator((0, int.to_bytes(12345678900987654321, 10000, 'big')))
datagrams1 =(x.video_datagram_creator((1, int.to_bytes(1234567890098765432, 10000, 'big'))))
datagrams2 = (x.video_datagram_creator((2, int.to_bytes(123456789009876543, 10000, 'big'))))
datagrams3 = (x.video_datagram_creator((3, int.to_bytes(12345678900987654, 10000, 'big'))))
datagrams = datagrams + datagrams1 + datagrams2 + datagrams3
#

print(len(datagrams))
actual_frame = 0
frame_high = bytearray()
frame_low = bytearray()
for d in datagrams:

    if int.from_bytes(d[0:4], 'big') >= actual_frame + 2:
        if actual_frame % 2 == 0:
            print("Frame_low is rdy")
            print(frame_low == int.to_bytes(12345678900987654321, 10000, 'big'))
            frame_low.clear()
        if actual_frame % 2 == 1:
            print("Frame_high is rdy")
            print(frame_high == int.to_bytes(1234567890098765432, 10000, 'big'))
            frame_high.clear()
        actual_frame += 1
    if actual_frame % 2 == 1:
        if actual_frame == int.from_bytes(d[0:4], "big"):
            frame_high[int.from_bytes(d[4:8], 'big') : int.from_bytes(d[4:8], 'big') + int.from_bytes(d[8:12], 'big')] = d[16:1016]
        elif int.from_bytes(d[0:4], "big") > actual_frame:
            frame_low[int.from_bytes(d[4:8], 'big') : int.from_bytes(d[4:8], 'big') + int.from_bytes(d[8:12], 'big')] = d[16:1016]
    if actual_frame % 2 == 0:
        if actual_frame == int.from_bytes(d[0:4], "big"):
            frame_low[int.from_bytes(d[4:8], 'big') : int.from_bytes(d[4:8], 'big') + int.from_bytes(d[8:12], 'big')] = d[16:1016]
        elif int.from_bytes(d[0:4], "big") > actual_frame:
            frame_high[int.from_bytes(d[4:8], 'big'): int.from_bytes(d[4:8], 'big') + int.from_bytes(d[8:12], 'big')] = d[16:1016]