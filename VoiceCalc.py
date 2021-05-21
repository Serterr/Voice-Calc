from tkinter import *
from tkinter import ttk
from sphinxbase import *
from pocketsphinx import *
import speech_recognition as sr
import math

#listens for audio commands and performs mathematical equations based on input from the user
#format: Addition - add 32 to 59
#format: Subtraction - subtract 32 by 59
#format: Division - divide 32 by 59
#format: Multiplication - multiply 32 by 59
#format: Probability - probability 33.333 and 33.333
#format: Fibonnacci- Fibonnacci 6
def Calc():
    
    r = sr.Recognizer()
    listening=False;
    while(True):
        if(listening == False):
            listening = True;
            failedToCapture = False;
            with sr.Microphone() as source:
                print("Awaiting Instructions: ")
                audio = r.listen(source)
            try:
                words = r.recognize_google(audio)
            except sr.UnknownValueError:
                print("I didn't catch that; please try again!")
                failedToCapture = True
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                failedToCapture = True
            if(failedToCapture == False):
                splitwords = words.split()
                for x in range(len(splitwords)):
                    if splitwords[x] == "pi":
                        splitwords[x] = float(3.1415926)
                print("You said:" + words)
                if(splitwords[0] == "add"):
                    total = add(float(splitwords[1]), float(splitwords[3]))
                    print("Total is: ", total)
                elif(splitwords[0] == "subtract"):
                    total = subtract(float(splitwords[1]), float(splitwords[3]))
                    print("Total is: ", total)                
                elif(splitwords[0] == "divide"):
                    total = divide(float(splitwords[1]), float(splitwords[3]))
                    print("Total is: ", total)                
                elif(splitwords[0] == "multiply"):
                    total = multiply(float(splitwords[1]), float(splitwords[3]))
                    print("Total is: ", total)
                elif(splitwords[0] == "probability"):
                    total = probability("A&B", float(splitwords[1]), float(splitwords[3]))
                    print("Probability that both event A and event B occur is: ", total)
                    total = probability("A|B|A&B", float(splitwords[1]), float(splitwords[3]))
                    print("Probability that event A, event B, or both event A and event B occur is: ", total)
                    total = probability("(A|B)&!(A&B)", float(splitwords[1]), float(splitwords[3]))
                    print("Probability that event A or event B occur, but not both is: ", total)
                    total = probability("!A&!B", float(splitwords[1]), float(splitwords[3]))
                    print("Probability that neither event A nor event B occur is: ", total)
                    total = probability("A&!B", float(splitwords[1]), float(splitwords[3]))
                    print("Probability that event A occurs, but event B does not is: ", total)
                    total = probability("!A&B", float(splitwords[1]), float(splitwords[3]))
                    print("Probability that event B occurs, but event A does not is: ", total)
                elif(splitwords[0] == "root" or splitwords[0] == "Route"):
                    total = root(float(splitwords[1]), float(splitwords[3]))
                    print("The Nth root of ",splitwords[3], "where N = ",splitwords[1],"is equal to", total)
                elif(splitwords[0] == "power" or splitwords[0] == "exponent"):
                    total = realExponent(splitwords[1], splitwords[3])
                    print("The Nth power  of", splitwords[3], "where N = ", splitwords[1], "is equal to", total)
                elif(splitwords[0] == "Fibonacci"):
                    total = Fibonacci(float(splitwords[1]))
                    print("The Nth place of the Fibonacci sequence where N = ", splitwords[1], " is ", total)                
                elif(splitwords[0] == "exit" or splitwords[0] == "quit"):
                    print("Now exiting program. Thanks for using!")
                    return 0
            listening = False;
            
        

#adds num2 to num1
def add(num1, num2):
    return (num1 + num2)
#subtracts num2 from num1
def subtract(num1, num2):
    return (num1 - num2)
#multiplies num2 by num1
def multiply(num1, num2):
    return (num1 * num2)
#divides num1 by num2
def divide(num1,num2):
    return (num1/num2)
def probability(mode, num1, num2):
    num1 = num1*0.01
    num2 = num2*0.01
    if(mode == "A&B"):
        return(num1*num2)
    elif(mode =="A|B|A&B"):
        tempnum = num1*num2
        return(num1+num2-tempnum)
    elif(mode == "(A|B)&!(A&B)"):
        tempnum =num1*num2*2
        return(num1+num2-tempnum)
    elif(mode == "!A&!B"):
        tempnum = num1*num2
        tempnum = num1+num2-tempnum
        return(1-tempnum)
    elif(mode == "A&!B"):
        return(num1*(1-num2))
    elif(mode == "!A&B"):
        return(num2*(1-num1))

def root(root,num):
    if num>0:
        return(num**(1.0/float(root)))
    else:
        return(-(-num)**(1.0/float(root)))
    
    #Calculates the result of one number put to the power of another
def realExponent(power, num):
    return num**power

def Fibonacci(place):
    phi = (1+ math.sqrt(5))/2
    inversephi = (1- math.sqrt(5))/2
    tempnum = ((((phi**place) - (inversephi**place))/math.sqrt(5)))
    #complex number from pi conversion broke the builtin rounding function; below is the rounding being carried out manually
    tempnum=tempnum*1000
    tempnum=int(tempnum.real)
    return(tempnum/1000)
    
def percentage(num, percentage):
    percentage=percentage*0.01
    return num*percentage

def sinfunc(num):
    return math.sin(num)
    
def cosfunc(num):
    return math.cos(num)
    
def tanfunc(num):
    return math.tan(num)
    
    


#Calc()
x= RealExponent(1, 3)
print(x)