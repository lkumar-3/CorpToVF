"""
Docstring for main
"""

def callFucntionTest(args, kwargs):
    print("this is testing")
    print(args, kwargs)
    return "ok"


# call the fuction automatically
if __name__ == "__main__":
    callFucntionTest(args=10, kwargs={'id':10})