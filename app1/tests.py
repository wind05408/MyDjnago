from django.test import TestCase

# Create your tests here.

def test(param):
    print("test",param)

def printNum():
    lower = int(input("输入区间最小值: "))
    upper = int(input("输入区间最大值: "))

    for num in range(lower,upper+1):
        if num>1:
            for i in range(2,num):
                if(num%i)==0:
                    break
            else:print(num);

if __name__=='__main__':
    printNum()
    # test(" haha git")
