import macmouse
import argparse

parser = argparse.ArgumentParser(
                    prog = 'Mouse Mover for MacOS',
                    description = 'This script moves the mouse cursor to a user-specified absolute path.')


parser.add_argument('-x', required=True)
parser.add_argument('-y', required=True)

args = parser.parse_args()

macmouse.move(args.x, args.y, absolute=True, duration=0, steps_per_second=0)
