from server import create_server

server = create_server("user", "1234")
try:
    server._run_server()
except KeyboardInterrupt:
    server.stop()

