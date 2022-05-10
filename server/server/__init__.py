DEFAULT_USER = "user"
DEFAULT_PASSWORD = "1234"

FTP_PORT = 21
FTP_ADDRESS = "0.0.0.0"
FTP_DIR = {"windows": "C:\\ftpserver", "others": "/home/ftpserver"}

import os
import sys


from .auth import BcryptAuthorizer
from .ftphandler import CustomHandler
from .threadserver import Threadftpserver


def create_server(username, password, address=FTP_ADDRESS, port=FTP_PORT, dir=None):

    authorizer = BcryptAuthorizer()
    
    if dir is not None:
        pass
    elif sys.platform == "win32":
        dir = os.path.join(FTP_DIR["windows"], username)
    else:
        dir = os.path.join(FTP_DIR["others"], username)

    if not os.path.exists(os.path.abspath(dir)):
        os.makedirs(dir)

    authorizer.add_user(username, authorizer.gen_hashed_passwd(password), dir, perm='elradfmwMT')
    authorizer.add_anonymous(os.getcwd())

    handler = CustomHandler 
    handler.authorizer = authorizer
    handler.banner = "ftpd is ready."
    address = (address, port)

    return Threadftpserver(address, handler)


if __name__ == '__main__':
    create_server(DEFAULT_USER, DEFAULT_PASSWORD)


