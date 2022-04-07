# Trenton Morgan, Karl Lodholz 2022
# simulator.py

# This file implements a simulated Booth's algorithm and verifies the accuracy
# of the calculations. Additionally, it tracks the number of iterations and
# number of addition and subtraction operations that must be performed in both
# Booth's and extended Booth's in order to quantify their performances.


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
	
	Outputs:
		?

	Return:
		None
	"""

	# First, determine if the inputs are from stdin or test dataset and
	# retrieve them for the multiplier and multiplicand.
	valid_input: bool = False
	while not valid_input:

		from_stdin: str = input("Use stdin? (y/n) ")
		if from_stdin == "y" or from_stdin == "Y":
			
			multiplier: str = input(
				"Input multiplier (0s and 1s only, no prefix): ")
			multiplicand: str = input(
				"Input multiplicand (0s and 1s only, no prefix):")

			x: set = set(multiplicand).union(set(multiplier))
			if x == BIN_SET or x == ZERO_SET or x == ONE_SET:
				
				if (len(multiplicand) >= MIN_INPUT_LEN and
				len(multiplicand) <= MAX_INPUT_LEN and
				len(multiplier) >= MIN_INPUT_LEN and
				len(multiplier) <= MAX_INPUT_LEN):
				
					print("Valid inputs given.")
					valid_input = True
				else:
					print("Invalid input(s) given.")
			else:
				print("Invalid input(s) given.")
		else:
			print("Invalid input option given (need to implement dataset).")


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

	Outputs:
		The tracked number of iterations and additions.

	Return:
		product: The calculated product as a binary string.
	"""

	product: str = ""

	return product


# Start the main function on script execution.
if __name__ == "__main__":
	main()