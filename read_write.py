

def main():

    # create a file

    tabbed_folder = open("myfile.txt", "w")
    print("First line in the file", file=tabbed_folder)
    print("Second line", file=tabbed_folder)
    tabbed_folder.close()


    # option 2

    with open("myfile02.txt", "w") as glossy_folder:
        print("First line in file 2!", file = glossy_folder)
        print("Second line in file2 !", file = glossy_folder)
  
    







if __name__ == "__main__":
    main()
