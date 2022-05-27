import time

def getValues():
    val_input = input("Enter the sample values separated by spaces:\n")
    values = map(int, (val_input.split()))
    return values


def probabilities():
    values = getValues()
    print("Choose from the following calculations. You can choose multiple options separated by spaces:")
    print("1.) Sample Mean")
    print("2.) Sample Standard Deviation")
    print("3.) Sample Variance")
    print("4.) Sample Median")
    print("5.) Percentile Cutoff Value")
    print("6.) Percentiles")

    choices = input().split()


time.sleep(1)
print("Welcome to the CLI interface for the automated statistics calculator.")

print("You can choose from the following options: ")
print("1.) Probabilities")
print("2.) Sample Statistics")
print("3.) Population Estimates")

# choice = (input("\nWhich option would you like to choose?\nEnter your choices separated by spaces:\n")).split()
choice = input("\nWhich option would you like to choose?\nEnter your choices separated by spaces:\n")

if (choice == '1'):
    probablities()
elif (choice == '2'):
    statistics()
elif (choice == '3'):
    population()
else:
    print("Invalid option. Exiting now.")
