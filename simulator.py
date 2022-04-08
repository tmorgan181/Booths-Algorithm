# # Trenton Morgan, Karl Lodholz 2022

# # This file implements a simulated Booth's algorithm and tracks the number of
# # iterations and number of addition and subtraction operations that must be
# # performed in both Booth's and extended Booth's in order to quantify their
# # performances.


# # Sets of acceptable binary characters for error checking
# BIN_SET = {'0', '1'}
# ZERO_SET = {'0'}
# ONE_SET = {'1'}

# # These constants define the minimum and maximum number of bits in any input.
# MIN_INPUT_LEN: int = 4
# MAX_INPUT_LEN: int = 12


# def main() -> None:
# 	"""
# 	This driver takes in pairs of inputs either from a test dataset or stdin
# 	and performs Booth's and Extended Booth's algorithms on them while tracking
# 	the number of iterations and addition operations that are required to
# 	calculate the product.

# 	NOTE: Due to Python syntax requirements, all binary values are stored as
# 		  str type variables beginning with the "0b" prefix.

# 	Params:
# 		None

# 	Return:
# 		None
# 	"""

# 	# First, determine if the inputs are from stdin or test dataset and
# 	# retrieve them for the multiplier and multiplicand.
# 	valid_input: bool = False
# 	while not valid_input:

# 		from_stdin: str = input("Use stdin? (y/n) ")
# 		if from_stdin == "y" or from_stdin == "Y":
			
# 			# Get the inputs.
# 			multiplicand: str = input(
# 				"Input multiplicand (0s and 1s only, no prefix): ")
# 			multiplier: str = input(
# 				"Input multiplier (0s and 1s only, no prefix): ")

# 			# Check if the inputs are valid binary numbers.
# 			x: set = set(multiplicand).union(set(multiplier))
# 			if x == BIN_SET or x == ZERO_SET or x == ONE_SET:
				
# 				if (len(multiplicand) >= MIN_INPUT_LEN
# 				and len(multiplicand) <= MAX_INPUT_LEN
# 				and len(multiplier) >= MIN_INPUT_LEN
# 				and len(multiplier) <= MAX_INPUT_LEN):
				
# 					# All checks passed, inputs are good.
# 					print("Valid inputs given.")
# 					valid_input = True

# 				else:
# 					print("Invalid input(s) given.")
# 			else:
# 				print("Invalid input(s) given.")

# 		elif from_stdin == "n" or from_stdin == "N":
			
# 			# Preset values for now
# 			multiplicand = "0011"
# 			multiplier = "0010"

# 			valid_input = True

# 		else:
# 			print("Invalid input option given (need to implement dataset).")

# 	# Sanity check for inputs and product.
# 	multiplicand_temp = "0b" + multiplicand
# 	multiplier_temp = "0b" + multiplier
# 	print("Multiplicand:", multiplicand)
# 	print("Multiplier:", multiplier)
# 	product: str = bin(int(multiplicand_temp, 2) * int(multiplier_temp, 2))
# 	print("Product:", product[2:])

# 	# Now we have the inputs, we can run Booths and Extended Booths.
# 	default_result: str = Booths(multiplicand, multiplier)
# 	extended_result: str = Booths(multiplicand, multiplier, extended = True)

# 	print("Default Result:", default_result)
# 	print("Extended Result:", extended_result)

# 	return


# def Booths(multiplicand: str, multiplier: str, extended: bool = False) -> str:
# 	"""
# 	This function executes Booth's or Booth's Extended Algorithm for two binary
# 	inputs while keeping track of the number of iterations and additions
# 	needed.

# 	Params:
# 		multiplicand: The first binary number in the operation.
# 		multiplier: The second binary number in the operation.
# 		extended: Switch to enable Extended Booth's when value is 1.

# 	Return:
# 		product: The calculated product as a binary string, or an empty string
# 			if an error occurs.
# 	"""
	
# 	# Extended Booth's requires the multiplicand and multiplier to be odd length???

# 	# Initialize the upper half of the double register for the product.
# 	dbl_reg_upper: str = ""
# 	for i in range(len(multiplier)):
# 		dbl_reg_upper += '0'
# 	print("Upper dbl:", dbl_reg_upper)

# 	# The final product is stored in the double register and extended by a '0'
# 	# bit to the right.
# 	product: str = dbl_reg_upper + multiplier + '0'
# 	print("Product:", product)
 
# 	# Now we are ready to execute Booth's or Extended Booth's.
# 	if not extended:
# 		pass
# 		# Default Booth's:

# 		# Repeat for the length of the multiplier.

# 	else:
# 		pass
# 		# Extended Booth's:

# 		# run extended

# 	return product


# def Arithmetic_Shift_Right(bin_number: str) -> str:
# 	shifted_number: str = ""

# 	return shifted_number


# # Start the main function on script execution.
# if __name__ == "__main__":
# 	main()

#Import libraries
import copy #Imported to deep copy lists
import matplotlib.pyplot as plt #Imported to auto generate graphs

#Function to run Arithmetic Shift Right method
def addAndShift(num1, num2):
    #Output
    print("Arithmetic Shift Right: ", bin_to_str(num1), " ", bin_to_str(num2))

    #Counter for the number of additions performed and number of iterations
    add_ctr = 0
    iter_ctr = len(num1)

    #Transform into a double register
    for i in range(len(num2)):
        num1.insert(0,0)
       
    #Loop through once for each entry in our original num1 input
    for i in range(iter_ctr):
        #Check if the rightmost bit is a 1
        if num1[-1] == 1:
            #If this is true then we perform a Arithmetic Shift Right
            print(bin_to_str(num1), '\t', num1[-1], "add & shift")

            #Increment the counter of the number of additions performed
            add_ctr += 1

            #Add num2 to the upper bits of num1, and leave the latter half as is
            num1 = add_Nums(num1[:len(num2)],num2)+num1[len(num2):]

            #Then shift right by removing the right most bit
            num1.pop()

            #And add 0s back to the left until we reach our original size
            if len(num1) != iter_ctr + len(num2):
                num1.insert(0,0)

        else:
            #If the rightmost bit is a 0, then we shift right
            print(bin_to_str(num1), '\t', num1[-1], "shift")
            num1.pop()
            num1.insert(0,0)
           
    #Return the list, num of iterations, and num of additions
    return num1, iter_ctr, add_ctr

#Function to run Booths algorithm
def booths(num1, num2):
    #Output
    print("Booths algorithm: ", bin_to_str(num1), " ", bin_to_str(num2))

    #Counters for the number of additions and subtractions performed
    add_ctr = 0
    sub_ctr = 0
    #Counter for the number of iterations needed
    iter_ctr = len(num1)

    #Turn the multiplier into a double register
    for i in range(len(num2)):
        num1.insert(0,0)
    num1.append(0)

    #Loop through once for each entry in our original num1 input and check the last 2 bits
    for i in range(iter_ctr):
        #If 01 then we add and shift
        if num1[-2:] == [0,1]:
            print(bin_to_str(num1), '\t', bin_to_str(num1[-2:]), "add & shift")

            #Increment the counter of the number of additions performed
            add_ctr += 1

            #Add num2 to the upper bits of num1
            num1 = add_Nums(num1[:len(num2)],num2)[-len(num2):]+num1[len(num2):]

            #Then shift right by removing the right most bit
            num1.pop()
            num1.insert(0,num1[0])

        #If 10 then we subtract and shift
        elif num1[-2:] == [1,0]:
            print(bin_to_str(num1), '\t', bin_to_str(num1[-2:]), "subtract & shift")

            #Increment the counter of the number of subtractions performed
            sub_ctr += 1

            #Add the complement of num2
            num1 = add_Nums(num1[:len(num2)],complement(num2))[-len(num2):]+num1[len(num2):]

            #Then shift right by removing the right most bit
            num1.pop()
            num1.insert(0,num1[0])

        #If 00 or 11 then we shift right
        else:
            print(bin_to_str(num1), '\t', bin_to_str(num1[-2:]), "shift")
            num1.pop()
            num1.insert(0,num1[0])        

    #Remove extra bit at the end
    num1.pop()
   
    #Return the list, num of iterations, and num of additions
    return num1, iter_ctr, add_ctr+sub_ctr

#Function to add bits
def add_Bits(bit1, bit2, carry_bit):
    #The sum is equal to the XOR of all bits
    sum_Bit = bit1 ^ bit2 ^ carry_bit
    #And the carry out is (a XOR b AND c) OR (a AND b)
    carry_Out = (bit1^bit2) & carry_bit | bit1 & bit2
    return sum_Bit, carry_Out

#Function to add two binary numbers and return a list of int
def add_Nums(num1, num2):
    #Initialize a list to hold the sum
    sum_result=[]
    #Initialize a single bit to hold the result and carry
    result = 0
    carry_bit = 0

    #Loop through the two numbers from right to left
    for i in range(len(num1))[::-1]:
        #Add the bits and insert into the sum
        result, carry_bit = add_Bits(num1[i],num2[i],carry_bit)
        sum_result.insert(0,result)
       
    #Append the carry to the result if it exists
    if carry_bit:
        sum_result.insert(0,carry_bit)
   
    #Return the sum
    return sum_result

#Function to get the complement of a number
def complement(num):
    #Create a copy of the binary number
    comp = copy.deepcopy(num)
   
    #Initialize a counter to the last index of the number
    ctr = len(comp)-1

    #Loop from the right of the number
    while(ctr>=0 and comp[ctr] != 1):
        ctr-=1

    #Skip the first 1
    ctr-=1

    #Check for remaining numbers
    if ctr>=0:
        while(ctr>=0):
            #Invert the bit
            if comp[ctr] == 1:
                comp[ctr] = 0
            else:
                comp[ctr] = 1
           
            ctr-=1

    #If the only 1 was the left most bit, extend by a 0 to the left
    else:
        comp.insert(0,0)
       
    return comp
   
#Function to turn the binary number into a string
def bin_to_str(bin):
    #Take the input list, cast each integer as a character,
    output = "".join(list(map(str, bin)))
    return output
   
#Main function
#Variables
val_Add = []
booths_Vals = []
n = []
sum_Add = 0
sum_Booths = 0

#Two lists using the given test data
multipliers  =  ['1110','0101','111111','101110','111011','00011111','11010111','01010101','01110111','01111000',
	'0101010101','1100111011','1001101110','010101010101','001111100111','101010101010','111001110000']
multiplicands = ['1111','0101','111111','110111','100011','01010101','01010101','11010111','00110011','01110111',
	'0101010101','1001110000','0101111010','010101010101','000011111111','101010101010','000011111111']

#Loop for each multiplier
for i in range(len(multipliers)):
    #Create a list for the multipliers
    add_multiplier = [0] + list(map(int, multipliers[i]))
    booths_multiplier = [0] + list(map(int, multipliers[i]))
   
    #Repeat for the multiplicands
    add_multiplicand = [0] + list(map(int, multiplicands[i]))
    booths_multiplicand = [0] + list(map(int, multiplicands[i]))
   
    #Call Arithmetic Shift Right on add_multiplier and add_multiplicand
    add_Result, add_Iterations, add_count = addAndShift(add_multiplier, add_multiplicand)

    #Print the result
    print("Arithmetic Shift Right result:", bin_to_str(add_Result[2:]), '\n')
   
    #Call booths on booths_multiplier and booths_multiplicand
    booths_Result, booths_Iterations, booths_count = booths(booths_multiplier,booths_multiplicand)

    #Print the result obtained from Booths
    print("Booths algo result:", bin_to_str(booths_Result[2:]), '\n')

    #Print the full results
    print("Arithmetic Shift Right:\tIterations: ", add_Iterations, "\tAdditions: ", add_count)
    print("Booths Algorithm:\tIterations: ", booths_Iterations, "\tAdditions: ", booths_count, "\n\n")

    #Add these to the running averages for the graph
    sum_Add += add_count
    sum_Booths += booths_count

    #Update the graph as the length changes every 5 intervals
    if (i+1)%5 == 0:
        #Add the average to the val_Add and boothVals series
        val_Add.append(sum_Add/5)
        booths_Vals.append(sum_Booths/5)

        #And add the input length at which those values occurred to the n series
        n.append(len(multipliers[i]))

        #Then reset the counters to restart with the next set.
        sum_Add=0
        sum_Booths=0

#Plot lines for the two algorithms
plt.plot(n,val_Add, label = "Arithmetic Shift Right")
plt.plot(n,booths_Vals, label = "Booths Algorithm")

#Lable axis
plt.xlabel("Length of number")
plt.ylabel("Average number of additions")

#Print graphs
plt.legend()
plt.show() 
