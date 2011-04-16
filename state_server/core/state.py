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
