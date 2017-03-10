#Process,step one, Normal function
def main_function():
    greeting='Hello world'
    def sub_function():
        print('First function: '+greeting)
    return sub_function()
#run the main_function
main_function()

#Process,step two Calling with instance
def main_function():
    greeting='Hello world'
    def sub_function():
        print('Second function '+greeting)
    return sub_function
#Call the instance
fun1=main_function()
fun1()
fun1()

#process, step Three, Cut the middle man and assign the msg
#directly to sub_function print
def main_function(msg):
    def sub_function():
        print('Third function '+msg)
    return sub_function
#Call the instance
Hello_world=main_function('Hello world')
Greeting=main_function('Greeting')
Hello_world()
Greeting()
