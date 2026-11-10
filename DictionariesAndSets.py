
'''
Author: Lameck Gekonde
Date: 10th November 2026

Program: IP Addresses and Router Names

Description:
This program uses a dictionary to store IP addresses
and router names. It allows the user to add and remove
IP addresses using Python append() and remove() methods.
'''

# Function 1: Display IP addresses in numeric order
def display_routers(routers, addresses):

    print("\nIP Addresses and Router Names:")

    # Sort IP addresses in numerical order
    for ip in sorted(addresses, key=lambda x: tuple(map(int, x.split('.')))):
        print(ip, ":", routers[ip])


# Function 2: Add an IP address
def add_router(routers, addresses):

    # Ask the user to enter an IP address
    ip = input("\nEnter the IP address to add: ")

    # Check if the IP address already exists
    if ip in addresses:
        print("This IP address already exists.")

    else:
        # Ask the user for the router name
        name = input("Enter the router name: ")

        # Add the IP address using append()
        addresses.append(ip)

        # Add the IP address and router name to the dictionary
        routers[ip] = name

        print("IP address successfully added!")


# Function 3: Remove an IP address
def remove_router(routers, addresses):

    # Ask the user which IP address to remove
    ip = input("\nEnter the IP address to remove: ")

    # Check if the IP address exists
    if ip in addresses:

        # Remove the IP address using remove()
        addresses.remove(ip)

        # Remove the IP address from the dictionary
        del routers[ip]

        print("IP address successfully removed!")

    else:
        print("IP address not found.")


# Main function
def main():

    # Create a dictionary containing four IP addresses and router names
    routers = {
        "192.168.169.20": "Router1",
        "192.168.169.21": "Router2",
        "192.168.169.22": "Router3",
        "192.168.169.23": "Router4"
    }

    # Create a list containing the IP addresses
    addresses = [
        "192.168.169.20",
        "192.168.169.21",
        "192.168.169.22",
        "192.168.169.23"
    ]

    # Display the original IP address list
    display_routers(routers, addresses)

    # Create a menu for managing IP addresses
    while True:

        print("\n--- Router Management Menu ---")
        print("1. Display IP addresses")
        print("2. Add IP address")
        print("3. Remove IP address")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_routers(routers, addresses)

        elif choice == "2":
            add_router(routers, addresses)

        elif choice == "3":
            remove_router(routers, addresses)

        elif choice == "4":
            print("\nFinal IP Address List:")
            display_routers(routers, addresses)
            print("\nThank you for using the program!")
            break

        else:
            print("Invalid choice. Please try again.")


# Call the main function
main()
