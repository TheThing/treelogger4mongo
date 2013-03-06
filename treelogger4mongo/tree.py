import inspect
import sys
import traceback

from pymongo import Connection
from pymongo.errors import InvalidOperation

from .branch import Branch, LogLevel

class Tree:
    def __init__(self, host="localhost", port="27017", dbname="treelog", colname="entries"):
        global TreeLogger
        TreeLogger = self
        self.host = host
        self.port = port
        self.dbname = dbname
        self.colname = colname
        self.conn = Connection(self.host, self.port)
        self.db = self.conn[dbname]
        self.collection = self.db[self.colname]

    def log(self, lvl, message, parent=None, data=None):
        caller = self.get_top(inspect.stack())
        b = Branch(self, caller, lvl, message, parent, data)
        return b.save()

    def debug(self, message, data=None):
        return self.log(LogLevel.DEBUG, message, None, data)

    def info(self, message, data=None):
        return self.log(LogLevel.INFO, message, None, data)

    def warning(self, message, data=None):
        return self.log(LogLevel.WARNING, message, None, data)

    def error(self, message, data=None):
        return self.log(LogLevel.ERROR, message, None, data)

    def critical(self, message, data=None):
        return self.log(LogLevel.CRITICAL, message, None, data)

    def exception(self, message=None, exception=None, parent=None):
        etype, value, tb = sys.exc_info()
        if exception == None:
            exception = value
        if value == None:
            if exception == None:
                if message == None:
                    return
                self.error(message)
            if message == None:
                message = "%s: %s" % (exception.__class__.__name__, exception.message)
            return self.log(LogLevel.EXCEPTION,
                            message,
                            parent,
                            {'exception-type': exception.__class__.__name__,
                             'exception-message': exception.message})
        if message == None:
            message = "%s: %s" % (exception.__class__.__name__, exception.message)
        stack_list = traceback.format_tb(tb)
        print "====="
        print etype
        print value
        print tb
        print message
        print exception
        print "====="
        return self.log(LogLevel.EXCEPTION,
                        message,
                        parent,
                        {'exception-type': exception.__class__.__name__,
                         'exception-message': "%s" % exception,
                         'stacktrace': stack_list})


    def get_top(self, stack):
        for s in stack:
            if s[1].find("treelogger4mongo") < 0:
                return s

def debug(message, data=None):
    global TreeLogger
    return TreeLogger.debug(message, data)

def info(message, data=None):
    global TreeLogger
    return TreeLogger.info(message, data)

def warning(message, data=None):
    global TreeLogger
    return TreeLogger.warning(message, data)

def error(message, data=None):
    global TreeLogger
    return TreeLogger.error(message, data)

def critical(message, data=None):
    global TreeLogger
    return TreeLogger.critical(message, data)

def exception(message=None, exception=None):
    global TreeLogger
    return TreeLogger.exception(message, exception)