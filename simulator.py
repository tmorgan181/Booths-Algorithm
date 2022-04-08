# # Trenton Morgan, Karl Lodholz 2022

# This file implements a simulated Booth's algorithm and tracks the number of
# iterations and number of addition and subtraction operations that must be
# performed in both Booth's and extended Booth's in order to quantify their
# performances.

#Import libraries
import copy #Imported to deep copy lists
import matplotlib.pyplot as plt #Imported to auto generate graphs


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


#Function to run Extended Booths algorithm
def extended_booths(num1, num2):
    #Output
    print("Extended Booths algorithm: ", bin_to_str(num1), " ", bin_to_str(num2))

    #Counters for the number of additions and subtractions performed
    add_ctr = 0
    sub_ctr = 0
    #Counter for the number of iterations needed
    iter_ctr = int(len(num1) / 2)

    #Turn the multiplier into a double register with extended '0' to the right
    for i in range(len(num2)):
        num1.insert(0,0)
    num1.append(0)

    #Loop through once for every two bits in num1 and check the last 3 bits
    for i in range(iter_ctr):
        # If 001 or 010 then we add multiplicand
        if num1[-3:] == [0,0,1] or num1[-3:] == [0,1,0]:
            print(bin_to_str(num1), '\t', bin_to_str(num1[-3:]), "add & shift")

            #Increment the counter of the number of additions performed
            add_ctr += 1

            #Add num2 to the upper bits of num1
            num1 = add_Nums(num1[:len(num2)],num2)[-len(num2):]+num1[len(num2):]

        # If 011 we add 2* multiplicand
        elif num1[-3:] == [0,1,1]:
            print(bin_to_str(num1), '\t', bin_to_str(num1[-3:]), "add 2* & shift")

            #Increment the counter of the number of additions performed
            add_ctr += 2

            #Add num2 to the upper bits of num1 twice
            num1 = add_Nums(num1[:len(num2)],num2)[-len(num2):]+num1[len(num2):]
            num1 = add_Nums(num1[:len(num2)],num2)[-len(num2):]+num1[len(num2):]

        # If 100 we subtract 2* multiplicand
        elif num1[-3:] == [1,0,0]:
            print(bin_to_str(num1), '\t', bin_to_str(num1[-3:]), "subtract 2* & shift")

            #Increment the counter of the number of subtractions performed
            sub_ctr += 2

            #Add the complement of num2 twice
            num1 = add_Nums(num1[:len(num2)],complement(num2))[-len(num2):]+num1[len(num2):]
            num1 = add_Nums(num1[:len(num2)],complement(num2))[-len(num2):]+num1[len(num2):]

        # If 101 or 110 we subtract multiplicand
        elif num1[-3:] == [1,0,1] or num1[-3:] == [1,1,0]:
            print(bin_to_str(num1), '\t', bin_to_str(num1[-3:]), "subtract & shift")

            #Increment the counter of the number of subtractions performed
            sub_ctr += 1

            #Add the complement of num2
            num1 = add_Nums(num1[:len(num2)],complement(num2))[-len(num2):]+num1[len(num2):]

        # If 000 or 111 we just shift
        else:
            print(bin_to_str(num1), '\t', bin_to_str(num1[-3:]), "shift")
        
        # After taking an action, arithmetic shift right two bit positions
        num1.pop()
        num1.pop()
        num1.insert(0,num1[0])
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
def main():
    # Tracker variables
    booths_addition_counts = []
    ext_addition_counts = []
    
    booths_iteration_counts = []
    ext_iteration_counts = []
    
    multiplier_lengths = []

    booths_Vals = []
    ext_Vals = []
    n = []
    sum_Ext = 0
    sum_Booths = 0

    #Two lists using the given test data
    multipliers  =  ['1110','0101','111111','101110','111011','00011111','11010111','01010101','01110111','01111000',
        '0101010101','1100111011','1001101110','010101010101','001111100111','101010101010','111001110000']
    multiplicands = ['1111','0101','111111','110111','100011','01010101','01010101','11010111','00110011','01110111',
        '0101010101','1001110000','0101111010','010101010101','000011111111','101010101010','000011111111']

    #Loop for each multiplier
    for i in range(len(multipliers)):
        #Create a list of binary bits for the multiplier and multiplicand
        multiplier = list(map(int, multipliers[i]))
        multiplicand = list(map(int, multiplicands[i]))

        multiplier_lengths.append(len(multiplier))

        #Call booths on multiplier and multiplicand
        booths_Result, booths_Iterations, booths_count = booths(multiplier, multiplicand)
        booths_addition_counts.append(booths_count)
        booths_iteration_counts.append(booths_Iterations)

        #Print the result obtained from Booths
        print("Booths Algorithm result:", bin_to_str(booths_Result[2:]), '\n')

        #Call extended Booths on multiplier and multiplicand
        multiplier = list(map(int, multipliers[i]))
        multiplicand = list(map(int, multiplicands[i]))
        ext_Result, ext_Iterations, ext_count = extended_booths(multiplier, multiplicand)
        ext_addition_counts.append(ext_count)
        ext_iteration_counts.append(ext_Iterations)

        #Print the result
        print("Extended Booths result:", bin_to_str(ext_Result[2:]), '\n')

        #Print the full results
        print("Booths Algorithm:\tIterations: ", booths_Iterations, "\tAdditions: ", booths_count)
        print("Extended Booths:\tIterations: ", ext_Iterations, "\tAdditions: ", ext_count, "\n\n")

        #Add these to the running averages for the graph
        sum_Booths += booths_count
        sum_Ext += ext_count

    # Debug outputs
    print("Lengths:", multiplier_lengths)
    print("Booths additions:", booths_addition_counts)
    print("Booths iterations:", booths_iteration_counts)
    print("Ext additions:", ext_addition_counts)
    print("Ext iterations:", ext_iteration_counts)

    # Get the unique length values
    unique_multiplier_lengths = list(set(multiplier_lengths))

    # Calculate the average additions and iterations for each input length and each algorithm
    avg_booths_additions = []
    avg_booths_iterations = []
    avg_ext_additions = []
    avg_ext_iterations = []

    for l1 in unique_multiplier_lengths:
        indexes_to_avg = []
        index = -1
        for l2 in multiplier_lengths:
            index += 1
            if l1 == l2:
                indexes_to_avg.append(index)

        z = 0
        booths_add_sum = 0
        booths_iter_sum = 0
        ext_add_sum = 0
        ext_iter_sum = 0

        for i in indexes_to_avg:
            z += 1
            booths_add_sum += booths_addition_counts[i]
            booths_iter_sum += booths_iteration_counts[i]

            ext_add_sum += ext_addition_counts[i]
            ext_iter_sum += ext_iteration_counts[i]

        avg_booths_additions.append(round(booths_add_sum / z, 1))
        avg_booths_iterations.append(round(booths_iter_sum / z, 1))

        avg_ext_additions.append(round(ext_add_sum / z, 1))
        avg_ext_iterations.append(round(ext_iter_sum / z, 1))

    # Debug outputs
    # print("\nUnique lengths:", unique_multiplier_lengths)
    # print("Avg Booths adds:", avg_booths_additions)
    # print("Avg Booths iter:", avg_booths_iterations)
    # print("Avg ext adds:", avg_ext_additions)
    # print("Avg ext iters:", avg_ext_iterations)

    #Plot average addition lines for the two algorithms
    plt.plot(unique_multiplier_lengths, avg_booths_additions, label = "Booths Algorithm")
    plt.plot(unique_multiplier_lengths ,avg_ext_additions, label = "Extended Booths")

    #Lable axis
    plt.xlabel("Length of number")
    plt.ylabel("Average number of additions")

    #Print graphs
    plt.legend()
    plt.show()

    # Plot average iterations
    plt.plot(unique_multiplier_lengths, avg_booths_iterations, label = "Booths Algorithm")
    plt.plot(unique_multiplier_lengths ,avg_ext_iterations, label = "Extended Booths")

    #Lable axis
    plt.xlabel("Length of number")
    plt.ylabel("Average number of iterations")

    #Print graphs
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()