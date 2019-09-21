class Employee:
	def __init__(self, name, empID, emailID):
		self.__name = name
		self.__empID = empID
		self.__emailID = emailID

	def getName(self):
		return self.__name

	def getEmpID(self):
		return self.__empID

	def getEmailID(self):
		return self.__emailID

class InfosysDirectory:
	def __init__(self, empList):
		self.__empList = empList

	def lookup(self, keyName):
		resultList = []
		for emp in self.__empList:
			if keyName in emp.getName():
				resultList.append(emp)
		self.display(resultList)
		return resultList

	def display(self, lst):
		print('Search Results...')
		for emp in lst:
			print("{} {} {}".format(emp.getName(), emp.getEmpID(), emp.getEmailID()))

emp1 = Employee('Anurag', 1, 'anu@gmail.com')
emp2 = Employee('Tanu', 1, 'tanu@gmail.com')
emp3 = Employee('Smruti', 1, 'smruti@gmail.com')
emp4 = Employee('Mayuree', 1, 'mayuree@gmail.com')

empList = [emp1, emp2, emp3, emp4]
infyDir = InfosysDirectory(empList)
infyDir.lookup('Smruti')

