import socket
import logging
import asyncore

OK_MSG = '_ok'
NA_MSG = '_na'

class QueryHandler(asyncore.dispatcher_with_send):
    def handle_cmd(self, varname, value=None):
        logging.debug('Query- varname: %s, value: %s' % (varname, value))
        current_val = self.state_obj.get(varname)

        if value is None:
            if current_val is None:
                return NA_MSG
            else:
                return current_val
        else:
            self.state_obj.set(varname, value)
            return OK_MSG


    def handle_read(self):
        try:
            data = self.recv(4096)
        except socket.error:
            return
        inputs = data.strip().split('\n')
        logging.debug('Inputs: %s' % inputs)
        for inp in inputs:
            if len(inp) == 0:
                continue
            cmd = inp.split(' ')
            result = self.handle_cmd(*cmd)
            try:
                self.send("%s\n" % result)
            except socket.error:
                return


