import argparse


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

    flags = arg_parse_creator()

    print('ADDRESS: {}'.format(flags.ipaddr))
    print('PORT: {}'.format(flags.port))
    print('REPEAT: {}'.format(flags.repeat))

if __name__ == '__main__':
    runCamera()
