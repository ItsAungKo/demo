for x in range(3):
    name = input("Enter Student Name : ")
    mark = input("Enter Student Mark : ")

    if mark >= "90":
        print("A") 
    elif mark >= "80":
        print("B")
    elif mark >= "70":
        print("C")
    elif mark >= "60":
        print("D")
    else:
        print("F")