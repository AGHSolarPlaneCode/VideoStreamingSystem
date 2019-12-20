import argparse
import udpstream as udps
import time

from setup import *

def arg_parse_creator():
    parser = argparse.ArgumentParser(description='UDPVideoStreaming')

    parser.add_argument('-ip', '--ipaddr',
                        help='Server destination address',
                        type=str,
                        required=True)
    parser.add_argument('-p', '--port',
                        help='Port number',
                        type=int,
                        required=True)

    parser.add_argument('-r', '--repeat',
                        help='Double frame mode',
                        type=bool,
                        required=False)

    return parser.parse_args()

def runCamera():

    print('UDP VIDEO STREAM')
    # print('ADDRESS: {}'.format(flags.ipaddr))
    # print('PORT: {}'.format(flags.port))
    # print('REPEAT: {}'.format(flags.repeat))

    flags = arg_parse_creator()

    udp_transmition = udps.UDPVideoTransmitter(ip=flags.ipaddr,
                                               port=flags.port,
                                               repeat=flags.repeat)

    vid_controller = udps.VideoController()

    vid_controller.set_transmision_method(udp_transmition)

    with picamera.PiCamera() as camera:
        camera.resolution = (RES_WIDTH, RES_HEIGHT)
        camera.framerate = FRAME_RATE

        try:
            camera.start_preview()
            time.sleep(2)
            camera.start_recording(vid_controller,
                                       format=CODEC_FORM)

        finally:
            camera.stop_recording()

if __name__ == '__main__':
    runCamera()
