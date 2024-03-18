import os

from bcrypt import gensalt, hashpw, checkpw
from pyftpdlib.authorizers import DummyAuthorizer, AuthenticationFailed


class BcryptAuthorizer(DummyAuthorizer):

    def validate_authentication(self, username, password, handler):
        if username != "anonymous":
            try:
                if not checkpw(password.encode(), self.user_table[username]['pwd'].encode()):
                    raise AuthenticationFailed
            except KeyError:
                raise AuthenticationFailed

    @staticmethod
    def gen_hashed_passwd(password, rounds=5):
        passwd = hashpw(password.encode(), gensalt(rounds))
        return passwd.decode()

