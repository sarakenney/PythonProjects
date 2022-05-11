# unique list exercise

#first set up a program to capture a list from the user

def main():
    """This program collects user input to create a list of unique values"""
    num_list = []    #sets up an empty list
    playing = True   #sets playing to true
    print(main.__doc__)    #prints the docstring of main
    
    #set up loop to repeatedly get user input of an int and append to num_list
    while (playing == True):
        num = int(input("Enter a number. Enter 0 to stop at any time: "))
        if (num == 0):
            playing = False
        else:
            num_list.append(num)
 

    #define function that takes a list as a parameter
    def unique_list(l):
        """Returns a list of unique values from given list l"""
        
        x = []  #create an empty list
        for a in l:   #iterates over the given list
            if a not in x:   #checks if value in our created list
                x.append(a)    #if value not in empty list add it

        return x

    print("Here are the unique values in your list: ", unique_list(num_list))  #initiates function with num_list

if __name__ == "__main__":
    main()
    
