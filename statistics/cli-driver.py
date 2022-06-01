import time
import stats

def getValues():
    val_input = input("Enter the sample values separated by spaces:\n")
    values = val_input.split()
    return [float(i) for i in values]

# option 1
def probabilities():
    print("TODO")


# option 2
def statistics():
    values = getValues()
    print(stats.getSampleMean(values))
    print("Choose from the following calculations. You can choose multiple options separated by spaces:")
    print("1.) Sample Mean")
    print("2.) Sample Standard Deviation")
    print("3.) Sample Variance")
    print("4.) Sample Median")
    print("5.) Percentile Cutoff Value")
    print("6.) Percentile")

    choices = input().split()
    print_string = ""
    print(values)
    if ('5' in choices):
        p = input("Enter the desired percentile cutoff: ")
    if ('6' in choices):
        cutoff = input("Enter a value to determine its percentile: ")

    for x in choices:
        if (x == 1):
            print_string = (print_string + "Sample Mean: " + stats.getSampleMean(values) + "\n")
        elif (x == 2):
            print_string = (print_string + "Sample SD " + stats.getSampleSD(values) + "\n")
        elif (x == 3):
            print_string = (print_string + "Sample Variance: " + stats.getSampleVariance(values) + "\n")
        elif (x == 4):
            print_string = (print_string + "Sample Median: " + stats.getSampleSD(values) + "\n")
        elif (x == 5):
            print_string = (print_string + "Cutoff for " + p + " percentile: " + stats.getPercentileCutoff(values,p) + "\n")
        elif (x == 6):
            print_string = (print_string + "Percentile for " + cutoff + "cutoff value: " + stats.getPercentile(values, cutoff) + "\n")

    print("Results:\n" + print_string)
    time.sleep(2)

# option 3
def onePopulation():
    values = getValues()


def multiPopulation():
    print("TODO")


time.sleep(.5)
print("Welcome to the CLI interface for the automated statistics calculator.")

print("You can choose from the following options: ")
print("1.) Probabilities")
print("2.) Sample Statistics")
print("3.) Single Population Estimates")
print("4.) Multiple Population Estimates")


# choice = (input("\nWhich option would you like to choose?\nEnter your choices separated by spaces:\n")).split()
choice = input("\nWhich option would you like to choose?\nEnter your choices separated by spaces:\n")

if (choice == '1'):
    probabilities()
elif (choice == '2'):
    statistics()
elif (choice == '3'):
    onePopulation()
elif (choice == '4'):
    multiPopulation()
else:
    print("Invalid option. Exiting now.")
