count = 0          # Initialize a counter 'count' to keep track of the number of inputs.
sum = 0.0          # Initialize 'sum' to store the cumulative sum of the numbers entered.
number = 1         # Set 'number' to 1 to enter the while loop; this will hold each input number.

# Start loop to collect numbers until the user enters 0
while number != 0:
    number = int(input())   # Take an integer input from the user and assign it to 'number'.
    sum = sum + number      # Add the current 'number' to 'sum' for cumulative total.
    count += 1              # Increment 'count' by 1 to track how many numbers were entered.

# Check if any numbers were entered before calculating average
if count == 0: 
    print("Input some numbers")   # If 'count' is zero, prompt the user to input some numbers.
else:
    # Display the average and sum, adjusting 'count' by subtracting 1 (because the last input is 0).
    print("Average and Sum of the above numbers are:", sum / (count-1), sum)