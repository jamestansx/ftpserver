import os

from ftplib import all_errors

from client.handlers import FTPHandler

def pwd(ftp):
    print(ftp.pwd())

def mkd(ftp):
    try:
        dir = input("Dir name: ")
        ftp.mkd(dir)
        return True
    except:
        return False

def rmd(ftp):
    try:
        dir = input("Dir name: ")
        ftp.rmd(dir)
        return True
    except:
        return False

def cwd(ftp):
    try:
        dir = input("Dir name: ")
        ftp.cwd(dir)
        return True
    except:
        return False
    
def ls(ftp):
    files = list()
    ftp.dir(files.append)
    for f in files:
        print(f)
        
def storlines(ftp):
    try:
        file = input("file name: ")
        with open(file, 'rb') as f:
            ftp.storlines(f'STOR {file}', f)
        print(f"Successfully transferred {file}")
        return True
    except:
        print('Error transferring. Local file may be incomplete or corrupt.')
        return False

def retrlines(ftp):
    try:
        file = input("file name: ")
        with open(file, 'w') as f:
            res = ftp.retrlines(f"RETR {file}", f.write)
            
            if res.startwith('226'):
                print(f"Successfully transferred {file}")
                return True
            else:
                print('Error transferring. Local file may be incomplete or corrupt.')
                return False
    except:
        return False


def connect():
    ftp = FTPHandler()
    return ftp

def disconnect(ftp):
    ftp.close()

def lsc():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        print(f)
