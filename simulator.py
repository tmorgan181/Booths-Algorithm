# Trenton Morgan, Karl Lodholz 2022

# This file implements a simulated Booth's algorithm and tracks the number of
# iterations and number of addition and subtraction operations that must be
# performed in both Booth's and extended Booth's in order to quantify their
# performances.


# Sets of acceptable binary characters for error checking
BIN_SET = {'0', '1'}
ZERO_SET = {'0'}
ONE_SET = {'1'}

# These constants define the minimum and maximum number of bits in any input.
MIN_INPUT_LEN: int = 4
MAX_INPUT_LEN: int = 12


def main() -> None:
	"""
	This driver takes in pairs of inputs either from a test dataset or stdin
	and performs Booth's and Extended Booth's algorithms on them while tracking
	the number of iterations and addition operations that are required to
	calculate the product.

	NOTE: Due to Python syntax requirements, all binary values are stored as
		  str type variables beginning with the "0b" prefix.

	Params:
		None

	Return:
		None
	"""

	# First, determine if the inputs are from stdin or test dataset and
	# retrieve them for the multiplier and multiplicand.
	valid_input: bool = False
	while not valid_input:

		from_stdin: str = input("Use stdin? (y/n) ")
		if from_stdin == "y" or from_stdin == "Y":
			
			# Get the inputs.
			multiplicand: str = input(
				"Input multiplicand (0s and 1s only, no prefix): ")
			multiplier: str = input(
				"Input multiplier (0s and 1s only, no prefix): ")

			# Check if the inputs are valid binary numbers.
			x: set = set(multiplicand).union(set(multiplier))
			if x == BIN_SET or x == ZERO_SET or x == ONE_SET:
				
				if (len(multiplicand) >= MIN_INPUT_LEN
				and len(multiplicand) <= MAX_INPUT_LEN
				and len(multiplier) >= MIN_INPUT_LEN
				and len(multiplier) <= MAX_INPUT_LEN):
				
					# All checks passed, inputs are good.
					print("Valid inputs given.")
					valid_input = True

				else:
					print("Invalid input(s) given.")
			else:
				print("Invalid input(s) given.")

		elif from_stdin == "n" or from_stdin == "N":
			
			# Preset values for now
			multiplicand = "0011"
			multiplier = "0010"

			valid_input = True

		else:
			print("Invalid input option given (need to implement dataset).")

	# Sanity check for inputs and product.
	multiplicand_temp = "0b" + multiplicand
	multiplier_temp = "0b" + multiplier
	print("Multiplicand:", multiplicand)
	print("Multiplier:", multiplier)
	product: str = bin(int(multiplicand_temp, 2) * int(multiplier_temp, 2))
	print("Product:", product[2:])

	# Now we have the inputs, we can run Booths and Extended Booths.
	default_result: str = Booths(multiplicand, multiplier)
	extended_result: str = Booths(multiplicand, multiplier, extended = True)

	print("Default Result:", default_result)
	print("Extended Result:", extended_result)

	return


def Booths(multiplicand: str, multiplier: str, extended: bool = False) -> str:
	"""
	This function executes Booth's or Booth's Extended Algorithm for two binary
	inputs while keeping track of the number of iterations and additions
	needed.

	Params:
		multiplicand: The first binary number in the operation.
		multiplier: The second binary number in the operation.
		extended: Switch to enable Extended Booth's when value is 1.

	Return:
		product: The calculated product as a binary string, or an empty string
			if an error occurs.
	"""
	
	# Extended Booth's requires the multiplicand and multiplier to be odd length???

	# Initialize the upper half of the double register for the product.
	dbl_reg_upper: str = ""
	for i in range(len(multiplier)):
		dbl_reg_upper += '0'
	print("Upper dbl:", dbl_reg_upper)

	# The final product is stored in the double register and extended by a '0'
	# bit to the right.
	product: str = dbl_reg_upper + multiplier + '0'
	print("Product:", product)
 
	# Now we are ready to execute Booth's or Extended Booth's.
	if not extended:
		pass
		# Default Booth's:

		# Repeat for the length of the multiplier.

	else:
		pass
		# Extended Booth's:

		# run extended

	return product


def Arithmetic_Shift_Right(bin_number: str) -> str:
	shifted_number: str = ""

	return shifted_number


# Start the main function on script execution.
if __name__ == "__main__":
	main()