# non pythonic way
# class A:
# 	def m(self):
# 		print('m of A is called')

# class B(A):
# 	def _m(self):
# 		print('m of B is called')
# 	def m(self):
# 		self._m()
# 		A.m(self)

# class C(A):
# 	def _m(self):
# 		print('m of C is called')
# 	def m(self):
# 		self._m()
# 		A.m(self)

# class D(B,C):
# 	def m(self):
# 		print('m of D is called')
# 		B._m(self)
# 		C._m(self)
# 		A.m(self)



# pythonic way
class A:
	def m(self):
		print('m of A is called')

class B(A):
	def m(self):
		print('m of B is called')
		super().m()

class C(A):
	def m(self):
		print('m of C is called')
		super().m()

class D(B,C):
	def m(self):
		print('m of D is called')
		super().m()


x = D()
x.m()