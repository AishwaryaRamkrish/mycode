#!/usr/bin/env python3

def main():
    proto = ["ssh", "http", "https"]
    protoa = ["ssh", "http", "https"]
    print(proto)
    proto.append("dns") # this line will add "dns" to the end of our list
    protoa.append("dns") # this line will add "dns" to the end of our list
    print(proto)
    proto2 = [ 22, 80, 443, 53 ] # a list of common ports
    proto.extend(proto2) # pass proto2 as an argument to the extend method
    print(proto)
    protoa.append(proto2) # pass proto2 as an argument to the append method
    print(protoa)

    proto.insert(2, "name") # Inserting the string "name" at position 2 in the list
    print(proto)
    

    proto.remove("name") # To remove the item "name" from the list
    print(proto)

    protob = [1, 4, 2, 7, 5]
    print(protob)
    protob.clear()  # Removes all the elements in the list
    print(proto)

    proto.pop()  # pops/removes the last element in the list
    print(proto)

    proto.index("ssh")
    print(proto)

    proto.extend(["ssh", "http", "ssh"])
    print(proto)

    print(proto.count("https"))

    proto.reverse()
    print(proto)

    print(proto.copy())

    print(proto.count("ssh"))




if __name__ == "__main__":
    main()
