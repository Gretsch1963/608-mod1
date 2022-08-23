# Fig. 2.2: calc_max_johnhickman.py
"""Find the maximum of three values."""

number1 = int(input('Enter first integer: '))
number2 = int(input('Enter second integer: '))
number3 = int(input('Enter third integer: '))

maximum = number1

if number2 > maximum:
    maximum = number2

if number3 > maximum:
    maximum = number3

print('Maximum value is', maximum)

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and    JOHN HICKMAN    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
