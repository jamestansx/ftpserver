import threading

from pyftpdlib.servers import ThreadedFTPServer

class Threadftpserver(ThreadedFTPServer):
    def __init__(self, addr, handler):
        ThreadedFTPServer.__init__(self, addr, handler)

        self.max_cons = 256
        self.max_cons_per_ip = 5

    def _run_server(self):
        self.serve_forever()

    def start(self):
        srv = threading.Thread(target=self._run_server)
        srv.daemon = True
        srv.start()

    def stop(self):
        self.close_all()


        


