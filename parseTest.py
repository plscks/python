# A simple program to try to understand argparse
# written by plscks
import argparse

def parse():
    parser = argparse.ArgumentParser(description='Discord bot')
    parser.add_argument('-t', '--token', help='Your bot\'s token', action='store', dest='token')
    parser.add_argument('-n', '--name', help='Your bot\'s name', action='store', dest='name')
    args = parser.parse_args()
    vars = args.token + ' ' + args.name
    return vars

if __name__ == '__main__':
    token = parse()
    print(token)
