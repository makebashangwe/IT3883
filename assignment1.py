# Program Name: Assignment1.py (use the name the program is saved as)
# Course: IT3883/Section W01
# Student Name: Makeba W.
# Assignment Number: 1
# Due Date: 06/12/2026
# Purpose: This program asks if the user wants to append data to a list, display the list, or clear it. There is also the option to quit.
# None, this uses pretty basic Python knowledge. I enjoyed the memory exercise. My cat may have helped me; she danced on my keyboard during the for loop.


input_buffer = []

option = ""

print(
    "\nOption 1: Append data to Input Buffer\n"
    "Option 2:Clear the Input Buffer \n"
    "Option 3:Display the Input Buffer\n"
    "Option4: Quit")

while True:
    try:
        option = input("Please enter an option: ")
        option = int(option)
        match option:
            case 1:
                user_input = input("Please enter a string to add to the list: ")
                input_buffer.append(user_input)
            case 2:
                input_buffer.clear()
            case 3:
                if len(input_buffer)>0:
                    for text in input_buffer:
                        print(text)
                else:
                    print("List is empty.")
            case 4:
                break
            case _:
                print("Invalid option.")

    except (ValueError):
        print("Please enter a valid option.")

print("Goodbye.")
