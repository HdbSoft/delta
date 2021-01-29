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
		if self.tables[name] == None or type(name) != str:
			return 1
		else:
			self.table = name

	def create_table(self, name):
		if not name or type(name) != str:
			return 1
		else:
			self.tables[name] = {}

	def set(self, name, value):
		if not name or type(name) != str:
			return 1
		else:
			self.tables[self.table][name] = value

	def select(self, name):
		output = None
		try:
			output = self.tables[self.table][name]
		except KeyError:
			print (f'deltaDB: in table {self.table}, property {name} does not exist')
			return
		return output
