from getpass import getpass

import ftplib
from ftplib import FTP

class FTPHandler:
    def __init__(self):
        self.ftp = FTP()
        self.address = tuple(map(str,input("FTP server address: ").split(":")))
        self.username = str()
        self.password = str()
        if self.connect_server():
            while True:
                self.username = input("Username: ")
                self.password = getpass()
                is_login = self.login_server()
                if is_login is None:
                    print("Server closed connection")
                    break
                if is_login:
                    break


    def connect_server(self):
        try:
            self.ftp.connect(self.address[0], int(self.address[1]))
            print(self.ftp.getwelcome())
            return True
        except (ConnectionRefusedError, TimeoutError):
            return False
        except IndexError:
            print("Invalid Address")
            return False

    def login_server(self):
        try:
            self.ftp.login(self.username, self.password)
            print(self.ftp.getwelcome())
            return True
        except ftplib.error_perm as e:
            print(e)
            if "disconnecting" in str(e).lower():
                return None
            return False

    def __repr__(self):
        return self.ftp

        
