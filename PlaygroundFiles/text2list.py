
def text2list(filename):

#asks for the file name

#opens the file for reading
    list_file = open(filename,'r')
#reads the files inputs into varriable as string
    list_characers = list_file.read()

    print(list_characers)

    length = len(list_characers)
    new_list = []

    for i in range(0,length - 1 ):
#converts the string to an integer list
        if list_characers[i] != ',':
            new_list.append(int(list_characers[i]))

    return new_list;

#prints it out for testing
def main():
    filename = input("Please enter your file name: ")
    new_list = text2list(filename)
    for i in range(0, len(new_list)):
        if i < len(new_list) - 1:
            print(new_list[i],',', sep = '',end = '' )
        else:
            print(new_list[i])

    return;

main()