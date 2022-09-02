# DECISION MAKING:
#        * There comes a point in your life where you need to decide what steps should be taken and based on that you decide your next decisions.
#        * In programming, we often have this similar situation where we need to decide which block of code should be executed based on a condition.
# Python has the following decision-making statements:
#          * if statements
#          * if-else statements
#          * if-elif ladder
#          * Nested statements
#
# PYTHON IF STATEMENTS:
#          * if statement is the most simple form of decision-making statement.
#          * It takes an expression and checks if the expression evaluates to True then the block of code in if statement will be executed.
#          * If the expression evaluates to False, then the block of code is skipped.
#SYNTAX:
#  if (expression):
#    statement 1
#    statement 2
#    .
#    statement n
#
# EXAMPLE:
#
# a = 20 ; b = 20
# if ( a == b ):
#   print( “a and b are equal”)
# print(“If block ended)
# OUTPUT:
# a and b are equal
# if block ended
#
# PYTHON IF-ELSE STATEMENTS:
#           * From the name itself, we get the clue that the if-else statement checks the expression and executes the if block when the expression is True otherwise it will execute the else block of code.
#           * The else block should be right after if block and it is executed when the expression is False.
#SYNTAX:
# if( expression ):
#   Statement
# else:
#   Statement
#
#  EXAMPLE:
#
# number1 = 20
# number2 = 30
# if(number1 >= number2 ):
#   print(“number 1 is greater than number 2”)
# else:
#   print(“number 2 is greater than number 1”)
# OUTPUT:
# number 2 is greater than number 1
#
# PYTHON IF-ELIF STATEMENT
#           * In Python, we have an elif keyword to chain multiple conditions one after another. With elif ladder, we can make complex decision-making statements.
#           * The elif statement helps you to check multiple expressions and it executes the code as soon as one of the conditions evaluates to True.
# SYNTAX:
# if( expression1 ):
#   statement
# elif (expression2 ) :
#   statement
# elif(expression3 ):
#   statement
# else:
#   statement
#
# EXAMPLE:
#
# print(“Select your ride:”)
# print(“1. Bike”)
# print(“2. Car”)
# print(“3. SUV”)
#
# choice = int( input() )
#
# if( choice == 1 ):
#   print( “You have selected Bike” )
# elif( choice == 2 ):
# elif( choice == 3 ):
#   print( “You have selected SUV” )
# else:
#   print(“Wrong choice!“)
# OUTPUT:
# Select your ride:
# 1. Bike
# 2. Car
# 3. SUV
# 3
# You have selected SUV
#
# PYTHON NESTED-IF STATEMENT
#           * In very simple words, Nested if statements is an if statement inside another if statement.
#           * Python allows us to stack any number of#   print( “You have selected Car” ) if statements inside the block of another if statements.
#           * They are useful when we need to make a series of decisions.
#
#SYNTAX:
# if (expression):
#   if(expression):
#     Statement of nested if
#   else:
#     Statement of nested if else
#   Statement of outer if
# Statement outside if block
#
# EXAMPLE:
#num1 = int( input())
# num2 = int( input())
#
# if( num1>= num2):
#     if(num1 == num2):
#         print(f'{num1} and {num2} are equal')
#     else:
#         print(f'{num1} is greater than {num2}')
# else:
#     print(f'{num1} is smaller than {num2}')
# OUTPUT:
# 10
# 20
# 10 is smaller than 20
#
# LOOPS:
#        * Programming languages provide us with the concept of loops which helps us execute some task n number of times where n can be any whole number.
#        * In Python loops, we will study For loop, while loop, nested loops and loop control statements.
#
# PYTHON FOR IN LOOP
#          * For loop in Python is used to iterate over a sequence of items like list, tuple, set, dictionary, string or any other iterable objects.
#
# EXAMPLE:
#for item in [1,2,3,4]:
# print( item)
# Output:
# 1
# 2
# 3
# 4
#
# PYTHON WHILE LOOP
#           * The while loop in Python executes a block of code until the specified condition becomes False.
#
# EXAMPLE:
# count = 0
# while( count< 10):
#   print(count)
#   count = count + 2
# OUTPUT:
# 0
# 2
# 4
# 6
# 8
#
#  PYTHON NESTED LOOP
#           * We can nest a loop inside another loop which simply means that a loop within a loop. Let’s see this with an example.
#
# EXAMPLE:
# for num1 in range(3):
#     for num2 in range(5, 8):
#         print(num1, ",", num2)
#  OUTPUT
# 0 , 5
# 0 , 6
# 0 , 7
# 1 , 5
# 1 , 6
# 1 , 7
# 2 , 5
# 2 , 6
# 2 , 7
#
#
# PYTHON CONTROL STATEMENTS:
#            *Python allows us to control the flow of the execution of the program in a certain manner. For this we use the continue, break and pass keywords.
#
# BREAK STATEMENTS:
#            *The break statement inside a loop is used to exit out of the loop. Sometimes in a program, we need to exit the loop when a certain condition is fulfilled.
# EXAMPLE:
# num = 0
# while( num <10 ):
#     num +=1
#     if(num==5): break
#     print( num )
#
# print("Loop ended")
# OUTPUT:
# 1
# 2
# 3
# 4
# Loop ended
#
# CONTINUE STATEMENTS:
#          * The continue statement is used to skip the next statements in the loop.
#          * When the program reaches the continue statement, the program skips the statements after continue and the flow reaches the next iteration of the loop.
#  EXAMPLE:
# num = 0
# while( num <10 ):
#     num +=1
#     if(num==5): continue
#     print( num )
#
# print("Loop ended")
#
# OUTPUT:
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10
# Loop ended
#
# PASS STATEMENTS:
#             * The pass is a null statement and the Python interpreter returns a no-operation (NOP) after reading the pass statement.
#             * Nothing happens when the pass statement is executed. It is used as a placeholder when implementing new methods or we can use them in exception handling.