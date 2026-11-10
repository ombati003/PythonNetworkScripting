
'''
Author: Lameck Gekonde
Date: 10th November 2026
Program: List of IP Addresses

Description: This program allows a user to enter IP addresses,
stores them in a list, displays the list, and gives
the user an opportunity to add more addresses.
'''

def main():
    # Create an empty list to store IP addresses
    addresses = []

    # Ask the user how many IP addresses they want to enter
    NumberOfAddresses = int(input("Enter the maximum number of IP addresses to add: "))

    # Loop to allow the user to enter the specified number of addresses
    for i in range(NumberOfAddresses):
        AddAddresses = input("Enter IP address: ")

        # Add the IP address to the list
        addresses.append(AddAddresses)

    # Display the list of IP addresses
    print("\nYour IP Address List:")
    for address in addresses:
        print(address)

    # Ask the user if they want to add more IP addresses
    choice = input("\nWould you like to add another IP address? (yes/no): ")

    # Continue adding addresses while the user chooses yes
    while choice.lower() == "yes":
        AddAddresses = input("Enter another IP address: ")

        # Add the new address to the existing list
        addresses.append(AddAddresses)

        # Display the updated list
        print("\nUpdated IP Address List:")
        for address in addresses:
            print(address)

        # Ask again if the user wants to continue
        choice = input("\nWould you like to add another IP address? (yes/no): ")

    # Display the final list
    print("\nFinal IP Address List:")
    print(addresses)


# Call the main function
main()
