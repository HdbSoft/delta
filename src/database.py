# DELTA DATA PROCESSING FRAMEWORK:
# NoSQL database engine with data in JSON
# format

class deltaDB:
	def __init__(self):
		self.tables = {
			'main': {}
		}
		self.table = 'main'

	def set_table(self, name):
		if self.tables[name] == None:
			return 1
		else:
			self.table = name

	def create_table(self, name):
		self.tables[name] = {}
