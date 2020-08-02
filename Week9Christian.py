'''This week we will create a program that performs file processing activities.
Your program this week will use the OS library in order to validate that a directory exists before creating a file in that directory.
Your program will prompt the user for the directory they would like to save the file in as well as the name of the file.
The program should then prompt the user for their name, address, and phone number.
Your program will write this data to a comma separated line in a file and store the file in the directory specified by the user. '''


fname = input('Hello, what is your first name? ')
lname = input('What is your last name? ')
full_name = fname + ' ' + lname
user_directory = input("Hello " + full_name + ', where would you like to save this data to? An example format is' + r" 'C:\Users\Chris\OneDrive\Desktop\' . Make sure to include the '\' at the end. ")
user_file = input('What is the name of the file you would like to save the data in? (if no file exists a new one will be created) ')
address = input('What is your address? ')
number = input('What is your phone number? ')
new_data = ('New data entered bellow')
log_file = ("\n" + full_name + ', ' + address +', ' + number)
f = open(user_directory + user_file + '.txt', "a")
f.write(log_file)
f.close()

#advanced alternative started bellow.
'''
class Directory:

    def __init__(self, name, address, number):
        self.name = full_name
        self.address = address
        self.number = number

        print('Added to Directory: {},{},{}'.format(self.name, self.address, self.number))
        @property
        def address(self):
            return address

        @property
        def number(self):
            return number

        @property
        def name(self):
            return name

user_1 = Directory(name, address, number)
'''
