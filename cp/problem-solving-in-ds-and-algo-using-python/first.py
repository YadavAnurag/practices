class HelloWorld(object):
	@classmethod
	def main(a, args):
		print("hello world", args)

if __name__ == "__main__":
	import sys
	HelloWorld.main(sys.argv)