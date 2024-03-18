import os
from pyftpdlib.handlers import FTPHandler
from server import FTP_DIR

class CustomHandler(FTPHandler):
    def on_login(self, username):
        self.banner = f"ftpd is ready, welcome {username}."
        userfolder_path = os.path.join(self.authorizer.user_table[username]["home"], username)
        if not os.path.exists(os.path.abspath(userfolder_path)):
            os.makedirs(userfolder_path)
