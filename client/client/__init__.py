from client.commander import *

commands = dict(connect=connect, disconnect=disconnect, pwd=pwd, rmd=rmd, cwd=cwd, ls=ls, storlines=storlines, retrlines=retrlines, lsc=lsc, exit=exit)
ftp = None

def create_client():
    while True:
        try:
            command = input(">> ")
            try:
                if command in ['lsc', 'exit']:
                    commands[command]()
                    continue
                if "connect" == command:
                    ftp = commands[command]()
                    continue
                if ftp is None:
                    ftp = commands[command]()
                else:
                    commands[command](ftp.ftp)
            except KeyError:
                help()
            except UnboundLocalError:
                ftp = commands["connect"]()
        except KeyboardInterrupt:
            print("\nExiting...")
            exit(0)

def help():
    print("Usage: [Command] -> [Wrapper for ftplib]")
    for command in commands.keys():
        print(f"\t{command} -> {commands[command]}")
    print("Visit ftplib documentation to learn more about the wrapper")
