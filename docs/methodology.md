# Methodology
## ftp server
### dependencies

server: [pyftpdlib](https://github.com/giampaolo/pyftpdlib)
client: [ftplib](https://docs.python.org/3/library/ftplib.html)

### process

1. clone the source code:
`$ git clone https://github.com/jamestansx/ftpserver.git && cd ftpserver`

1. create a virtual environment:
`$ virtualenv venv`

1. activate the virtual env:%
`$ ./venv/Scripts/activate`

1. install all the dependencies:
`$ pip install -r requirements.txt`

#### server side

cd into `server` directory:
`$ cd server`

run:
`$ python server.py`

#### client side

cd into `client` directory:
`$ cd client`

run:
`$ python client.py`

