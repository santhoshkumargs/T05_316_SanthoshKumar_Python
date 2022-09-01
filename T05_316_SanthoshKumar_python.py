# INTRODUCTION OF PYTHON:
#
#      * Python is a general purpose intrepreted high level language.
#      * It is developed by guido vann rossem in 1991.
#
# WHY PYTHON IS POPULAR IN NOW A DAYS?
#
#      * Python is great effort in web development,data analytics,machine learning,data science and data engineering.
#      * Many top software companies depend upon a python including facebook,google,instagram and netflix etc...
#
# Features of python?
#
#      * Easy to code.
#      * Easy to write.
#      * It is intrepreted.
#
# Advantages of python?
#
#      * It is portable.
#      * It is object oriented programming language.
#      * It is scripted language.
#      * High level intrepreted languages.
#      * Dynamic languages.
#      * It is portable.
#
# Disadvantages of Python?
#
#      * User friendly data structures.
#      * python is a time consuming language.it has a low execution speed
#      * there are many issues with the design of the language, which only gets displayed during run time.
#
# What is .py vs .pyc files?
#
#      *.py files contain the source code of a program.
#      *.pyc file contains the bytecode of your program.
#
# How compilation will happen internally. Explain in detail?
#
#      * The source code in python is saved as a . py file which is then compiled into a format known as byte code, byte code is then converted to machine code.
#      * After the compilation, the code is stored in . pyc files and is regenerated when the source is updated.
#
# Why Python is Dynamically typed programming Language. Explain?
#
#      * Python don't have any problem even if we don't declare the type of variable. It states the kind of variable in the runtime of the program.
#      * Python also take cares of the memory management which is crucial in programming.
#
# VARIABLES
#
#      * variables contains for storing a data values
#      * for examples:
# x = 10
# y = "santhosh"
# print(x)
# print(y)
#
# What is casting?
#
#       * If you want to specify the data type of a variable, this can be done with casting.
#       * For examples:
# x = str(3)
# y = int(3)
# z = float(3)
#
# what is Strings?
#
#       * String variables can be declared either by using single or double quotes.
#       *For examples:
# x = "Santhosh"
# x = 'Santhosh'
#
# Explain in detail for crud operations?
#
#      * The abbreviation CRUD expands to Create, Read, Update and Delete. These four are fundamental operations in a database.
#      * In the sample database, we will create it, and do some operations.
#
# TOKENS IN PYTHON?
#      * A token is the smallest individual unit in python program.all statements and instructions in a program are built with not tokens.
#      * There are five types of token,
#         --> literals
#         --> operators
#         --> keywords
#         --> identifiers
#         __> constants
#
# WHAT IS GARBAGE COLLECTION HOW IT WORKS?
#
#      * Python deletes unwanted objects automatically to free the memory space.
#      * The process by which periodically frees and reclaims the blocks of memory that no longer are in use is called garbage collection.
#
# WHAT IS MEMORY MANAGEMENT IN PYTHON?
#
#      * Memory management in Python involves a private heap containing all Python objects and data structures.
#      * The management of this private heap is ensured internally by the Python memory manager.
#
# Assigning value to multiple variables. Explaion?
#      * Python allows you to assign values to multiples variables in one line.
#      * For Examples:
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)
#
# IDE:
#      * IDE means integrated development environment.
# IDE SHORTCUTS:
#      TEXT EDITING:
# key          |       description
#
# tab                  indent or block indent
# shift+tab            block un-indent
# control+c            copy
# control+v            paste
# control+a            select all
# control+z            undo
# control+x            cut
# control+/            comment
# control+f            find
# control+k            find next
# shift+control+k      find previous
# control+backspace    remove word left
# control+=            smaller font
#
#      SELECTION
#
# SHIFT+DOWN ARROW    highlight down
# SHIFT+UP ARROW      highlight up
# SHIFT+LEFT ARROW    select left
# SHIFT+RIGHT ARROW   select right
#
#     TERMINAL
#
# ALT+S               switch to terminal or file
# CONTROL+C           abort command or program
#
#    NAVIGATION
#
# CONTROL+W        close pane
# SHIFT+CONTROL      privious pane
# CONTROL+]          goto right tab
# CONTROL+[          goto left  tab
#
# OPERATORS:
#
#        * Operators are used to perform operations on variables and values.
#
# Python divides the operators in the following groups:
#
#        * Arithmetic operators
#        * Assignment operators
#        * Comparison operators
#        * Logical operators
#        * Identity operators
#        * Membership operators
#        * Bitwise operators
#
# ARITHMETIC OPERATORS:
#
#        * Arithmetic operators are used with numeric values to perform common mathematical operations:
#        * For examples:
#          addition       (x+y)
#          subtraction    (x-y)
#          multiplication (x*y)
#          division       (x/y)
#          modulus        (x%y)
#          exponentiation (x**y)
#          floor division (x//y)
#
# ASSIGNMENT OPERATORS:
#
#       * Assignment operators are used to assign values to variables
#       * For examples:
#         x = 5
#         x += 3
#         x -= 3
#         x *= 3
#
# COMPARISON OPERATORS:
#
#       * Comparison operators are used to compare two values.
#       * For Examples:
#         x == y
#         x != y
#         x > y
#         x < y
#
# LOGICAL OPERATORS:
#
#       * Logical operators are used to combine conditional statements.
#       * For examples:
#         AND   x<5 and x>10
#         OR    x<5 or  x>10
#         NOT   NOT(x<5 and x>10)
#
# IDENTITY OPERATORS:
#
#        * Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.
#        * For example:
#          is     (x is y)
#          is not x is not y
#
# MEMBERSHIP OPERATORS:
#
#        * Membership operators are used to test if a sequence is presented in an object.
#        * For example:
#          in         x in y
#          not in     x not in y
#
# DATA TYPES:
#
#        *Variables can store data of different types, and different types can do different things.
#        *They are int,float,complex,bool,strings.
#        *int-(1,2,3,4,5)
#        *float-(2.5,6.5)
#        *complex-(ai+bj)
#        *bool-(true or false)
#        *strings-('santhosh')
#
# DATA STRUCTURES:
#
#         * Data Structures allows you to organize your data in such a way that enables you to store collections of data, relate them and perform operations on them accordingly.
#         * There are four types of data structure
#         * list,tuple,set,dictionary
#
# LIST:
#
#            * Lists are used to store multiple items in a single variable.
#            * Lists are mutable,ordered,and allow duplicate values.
#            * for example:
#              list = ["apple", "banana", "cherry", "apple", "cherry"]
#              print(list)t
#
# TUPLE:
#
#            * Tuples are used to store multiple items in a single variable.
#            * Tuples are immutable,ordered, and allow duplicate values.
#            * For Example:
#              tuple = ("apple", "banana", "cherry", "apple", "cherry")
#              print(tuple)
#
# SET:
#
#             * Sets are used to store multiple items in a single variable.
#             * Sets are unordered and not allow duplicate values.
#             * For Example:
#               set = {"apple", "banana", "cherry", "apple"}
#               print(set)
#
# DICTIONARY:
#
#             * Dictionaries are used to store data values in key:value pairs.
#             * A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#             * For Example:
#               dict = {"brand": "Ford","model": "Mustang","year": 1964}
#               print(dict)
#
# kEYWORDS:
#
#            * Keywords in Python are reserved words that can not be used as a variable name, function name, or any other identifier.
#            * There are 33 keywords in python,they are and,as,assert,break,pass,continue,class,def,del,elif,else,if,global,import,finally,for,from,pass,return, true
#              false,try,with,yield,lambda,with,none
#              
#