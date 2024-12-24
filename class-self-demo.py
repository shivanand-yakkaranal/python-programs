class Check(object):
    def __init__(self,val):
        self.checktheval=val
    def testdemo(self,param):
         print("In test",self.checktheval)
from Testclass import demo
#obj = Check(300)
#obj.testdemo("DEMO")
demo("Accessing from the class-self-demo.py")
#print("Address of class object = ",id(obj))