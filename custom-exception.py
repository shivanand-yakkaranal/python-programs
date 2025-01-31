class MyCustomError(Exception):
	def __init__(self, message,error_code):
		self.message=message
		super().__init__(self.message)
		self.error_code=error_code
		
	def __str__(self):
		return f"{self.message} (Error code: {self.error_code})"
	

def divide(a,b):
	if b==0:
		raise MyCustomError("Division by zero is not allowed",400)
	return a/b

try:
	result=divide(2,0)
except MyCustomError as e:
	print(f"Caught an error: {e}")
	