import socket
import logging
import asyncore

from state_server.core import state
from state_server.core import handler

class StateServer(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

        self.connection_id = 0
        self.state_obj = state.State()

    def handle_accept(self):
        pair = self.accept()
        if pair is None:
            pass
        else:
            sock, addr = pair
            logging.debug('Incoming connection #%d from %s' %
                 (self.connection_id, repr(addr)))

            self.connection_id += 1
            hand = handler.QueryHandler(sock)
            hand.state_obj = self.state_obj

