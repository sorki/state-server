import time
import logging
import threading

class State(object):
    def __init__(self):
        self.__state_dict = {}

    def set(self, name, value):
        self.__state_dict[name] = value

    def get(self, name):
        if name in self.__state_dict:
            return self.__state_dict[name]
        else:
            return None

    def dump(self):
        return self.__state_dict

class TimedState(State):
    def __init__(self, file_path):
        super(TimedState, self).__init__()

        self.semaphore = threading.Semaphore()

        try:
            self.file = open(file_path, 'w')
        except IOError as e:
            logging.error('Unable to open "%s" for writing,'
                ' timed output disabled. Exception: "%s"', file_path, e)
            self.file = None

    def _log(self, event):
        if not self.file:
            return

        msg = '%s %s\n' % (time.time(), event)

        self.semaphore.acquire()
        self.file.write(msg)
        self.semaphore.release()

    def set(self, name, value):
        self._log('SET:%s=%s' % (name, value))
        return super(TimedState, self).set(name, value)

    def get(self, name):
        self._log('GET:%s' % name)
        return super(TimedState, self).get(name)

    def __del__(self):
        if self.file:
            self.file.close()
