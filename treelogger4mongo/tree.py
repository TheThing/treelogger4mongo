from pymongo import Connection
from pymongo.errors import InvalidOperation

class Tree:
	def __init__(self, host="localhost", port="27017", dbname="treelog"):
		global TreeLogger
		TreeLogger = self
		self.host = host
		self.port = port
		self.dbname = dbname
		self.conn = Connection(self.host, self.port)
		self.db = self.conn[dbname]

	def debug(self, message):
		print inspect.stack()