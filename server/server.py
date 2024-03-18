import argparse
from server import create_server

parser = argparse.ArgumentParser(description="Create FTP Server")
parser.add_argument("username", type=str, nargs='?', default="user", help="Username")
parser.add_argument("password", type=str, nargs='?', default="1234", help="password")
args = parser.parse_args()


server = create_server(args.username, args.password)
try:
    server._run_server()
except KeyboardInterrupt:
    server.stop()

