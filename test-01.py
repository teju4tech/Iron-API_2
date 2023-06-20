def calculate(amount, percent):
	return (amount * percent) / 100

def calculate_income_tax(total_income:
						float) -> float:

	if total_income <= 250000:
		return 0
	elif total_income <= 500000:
		return calculate(total_income -
						250000, 5)
	elif total_income <= 750000:
		return calculate(total_income -
						500000, 10) + 12500
	elif total_income <= 1000000:
		return calculate(total_income -
						750000, 15) + 37500
	elif total_income <= 1250000:
		return calculate(total_income -
						1000000, 20) + 75000
	elif total_income <= 1500000:
		return calculate(total_income -
						1250000, 25) + 125000
	else:
		return calculate(total_income -
						1500000, 30) + 187500


if __name__ == '__main__':
	total_income = float(input("What's your \
					annual income?\n>>> "))
	tax = calculate_income_tax(total_income)
	print(f"Total tax applicable at \
					₹{total_income} is ₹{tax}")
