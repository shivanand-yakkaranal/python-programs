"""
content="Python is awesome"

print(content)

print(len(content))

print("Python" in content)

print("Hello" in content)

print("Demo" not in content)

for strarr in content:
    print(strarr)

if "Demo" in content:
    print(f"Demo found in {content}")
else:
    print(f"Demo not found in '{content}'")
"""
class DemoString(object):
    def __init__(self,paramstr):
        self.param=paramstr
    def stringLength(self):
        print(f"{self.param} length ={len(self.param)}")
    def isPolindrome(self,stringParam):
        print(self.param)
        if stringParam==stringParam[::-1]:
            print(f"{stringParam} is polindrome")
        else:
            print(f"{stringParam} is not polindrome")
    def allstringmethods(self,sampleString):
        print(f"'{sampleString}'.capitalize() =>",sampleString.capitalize())
        print(f"'{sampleString}'.casefold() =>",sampleString.casefold())
        print(f"'{sampleString}'.center(20) =>",sampleString.center(20))
        print(f"'{sampleString}'.cout(\"Python\") =>",sampleString.count("Python"))
        txt = "My name is Ståle"
        x = txt.encode()
        print(txt,x)
        txt = "My name is Ståle"
        print(txt.encode(encoding="ascii",errors="backslashreplace"))
        print(txt.encode(encoding="ascii",errors="ignore"))
        print(txt.encode(encoding="ascii",errors="namereplace"))
        print(txt.encode(encoding="ascii",errors="replace"))
        print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

        txt = "Hello, welcome to my world."
        x = txt.endswith(".")
        print(x)

        txt = "H\te\tl\tl\to"
        x =  txt.expandtabs(2)
        print(x)

        txt = "Hello, welcome to my world."
        x = txt.find("welcome")
        print(x)

        txt = "Hello, welcome to my world."
        print(txt.find("o"))
        print(txt.index("o"))

        txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
        print(txt1)
        txt2 = "My name is {0}, I'm {1}".format("John",36)
        print(txt2)
        txt3 = "My name is {}, I'm {}".format("John",36)
        print(txt3)

        txt1 = "Company12"
        txt2 = "Company 12"
        x1 = txt1.isalnum()
        x2 = txt2.isalnum()
        print(x1,x2)

#Initialize the object
demoStrObj= DemoString("Demo")
#demoStrObj.isPolindrome("malayalam")
#demoStrObj.stringLength()
demoStrObj.allstringmethods("Hello Python,Django is Python framework.")
