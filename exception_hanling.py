# Three keywords for error handling:
# 1. try:- this is the block of code to be attempted (may lead to an error)
# 2. except:- the block of code will be execute if there is an error in try block
# 3. finally:- a final block of code to be executed , regardless of an error

# example1
def add(n1, n2):
    return n1 + n2

print(add(10, 20))
number1 = 10
# number2 = input("enter value of number2")
# print(add(number1 + number2))
# error occurs in above case because number2 is string ..so concatnation of int and string is not possible and called type error
# whatever you write a code after  line13 its gonna be error, so overcome this we use exception handling

# to solve this do this way as below

# example2

try:
    # result = 10 + 10
    result = 10 + '10'
except:
    print("hey there looks like an error")
#     if there is an error occured this block will be executed
else:
    print("add went well")
    print(result)
#     else block is executed when there is no error

# example3

try:
    # f = open("testfile", 'w')
    f = open("testfile", 'r')
    f.write("write something here")
except TypeError:
    print("thre is an type error")
except OSError:
    print("hey there is an os error")
finally:
    print("i always run")


# erxample4

def ask_for_int():
    try:
        result = int(input("please provide number"))
    except:
        print("sorry, this is not an integer number")
    finally:
        print("i am always execute regardless of error occured")

ask_for_int()

# example5
# lets make above code asking for a interger number again and again if except occurs


def ask_for_int():
    while True:
        try:
            result = int(input("please provide number"))
        except:
            print("sorry, this is not an integer number")
            continue
        else:
            print("now you entered a integer number")
            break
        finally:
            print("i am always execute regardless of error occured")

ask_for_int()


