# ECOR 1042 Lab 6 - Individual submission for text_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Prasidhaan Anandavimalan"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101260157"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-114"

#==========================================#
# Place your script for your text_UI after this line
import load_data
import sort
import histogram
import curve_fit


def displayUI():
    print("The available commands are:")
    print("L)oad Data")
    print("S)ort Data")
    print("C)urve Fit")
    print("H)istogram")
    print("E)xit")
    choice = input("Please type your command: ")
    
    if choice.upper() == "E":
        exit()
        
    elif choice.upper() == "L":
        done = False
        while not done:    
            filename = input("Please enter the name of the file: ")
            try:
                f = open(filename)
                done = True
            except OSError as e:
                print("Invalid input.")
        
        filter = input("Please enter the attribute to use as a filter: ")
        while (not isValidAttribute(filter, ['school', 'age', 'failures', 'health'])):
            print("Invalid input.")
            filter = input("Please enter the attribute to use as a filter: ")
            
        value = 0 
        if not filter.upper() == "ALL":
            value = input("Please enter the value of the attribute: ")
            
        data = load_data.load_data(filename, (filter, value))
        
        print("Data loaded")
        loaded = True
        return displayUI()
        
    elif choice.upper() == "S":
        if not loaded:
            print("File not loaded. Please, load a file first.")
            return displayUI()
        
        print("Please enter the attribute you want to use for sorting: ")
        print("'Age' 'StudyTime' 'Failures' 'G_Avg'")
        attribute = input(": ")
        
        while (not isValidAttribute(attribute, ['studytime', 'age', 'failures', 'g_avg'])):
            print("Invalid input.")            
            print("Please enter the attribute you want to use for sorting: ")
            print("'Age' 'StudyTime' 'Failures' 'G_Avg'")
            attribute = input(": ")
        
        order = input("Ascending (A) or Descending (D) order: ")
        
        while (not isValidAttribute(attribute, ['a', 'd'])):
            print("Invalid input.")            
            order = input("Ascending (A) or Descending (D) order: ")
        
        data = sort.sort_by_key(data, order, attribute)
        
        if (input("Data Sorted. Do you want to display the data? (Y or N): ").upper() == 'Y'):
            print(data)
        
        return displayUI()
        
    elif choice.upper() == "C":
        if not loaded:
            print("File not loaded. Please, load a file first.")
            return displayUI()
        
        attribute = input("Please enter the attribute you want to use to find the best fit for G_Avg: ")

        while (not isValidAttribute(filter, ['age', 'failures', 'health', 'absences'])):
            print("Invalid input.")
            attribute = input("Please enter the attribute you want to use to find the best fit for G_Avg: ")
        
        order = input("Please enter the order of the polynomial to be fitted: ")
        
        while (not order.isdigit()):
            print("Invalid input.")
            order = input("Please enter the order of the polynomial to be fitted: ")
            
        curve_fit.curve_fit(data, attribute, order)
        
        return displayUI()
        
    elif choice.upper() == "H":
        if not loaded:
            print("File not loaded. Please, load a file first.")
            displayUI()
            return
        
        attribute = input("Please enter the attribute you want to use for plotting: ")
        
        while (not isValidAttribute(filter, ['age', 'failures', 'health', 'absences', 'studytime'])):
            print("Invalid input.")
            attribute = input("Please enter the attribute you want to use for plotting: ")
        
        histogram.histogram(data, string)
        
        return displayUI()
        
    else:
        print()
        print("Invalid command.")
        print()
        return displayUI()

def isValidAttribute(input, list):
    if input.lower() in list:
        return True
    return False

loaded = False
data = []
displayUI()
