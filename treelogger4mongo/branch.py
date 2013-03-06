import datetime
import getpass
import threading

class LogLevel:
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3
    CRITICAL = 4
    EXCEPTION = 5

    def get_friendly_name(lvl):
        for p in dir(LogLevel):
            if not p.startswith("_"):
                if getattr(LogLevel, p) == lvl:
                    return p

class Branch:
    def __init__(self, tree, caller, lvl, message, parent=None, data=None):
        self._id = None
        self.tree = tree
        self.caller = caller
        self.lvl = lvl
        self.message = message
        self.data = data
        self.parent = parent._id if parent != None else parent
        pass

    def save(self):
        self._id = self.tree.collection.insert(self.to_dict())
        return self

    def debug(self, message, data=None):
        return self.tree.log(LogLevel.DEBUG, message, self, data)

    def info(self, message, data=None):
        return self.tree.log(LogLevel.INFO, message, self, data)

    def warning(self, message, data=None):
        return self.tree.log(LogLevel.WARNING, message, self, data)

    def error(self, message, data=None):
        return self.tree.log(LogLevel.ERROR, message, self, data)

    def critical(self, message, data=None):
        return self.tree.log(LogLevel.CRITICAL, message, self, data)

    def exception(self, message=None, exception=None):
        return self.tree.exception(message, exception, self)

    def to_dict(self):
        return {
            'time': datetime.datetime.now(),
            'thread_ident': threading.current_thread().ident,
            'user': getpass.getuser(),
            'level': self.lvl,
            'level-text': LogLevel.get_friendly_name(self.lvl)
            'parent': self.parent,
            'call_file': self.caller[1],
            'call_function': self.caller[3],
            'message': self.message,
            'data': self.data,
        }