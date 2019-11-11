#!/usr/bin/python3

def main():
    mylist = []

    mylist.append("192.168.102.55")

    ## append works by opening up a slot at the END of the list and inserting the value
    mylist.append("10.10.0.1")
    print(mylist)

    myotherlist = []

    ## extend works by ITERATING across the value passed, and opening up that may slots at the end of the list
    myotherlist.extend("abcdefg")
    # myotherlist == ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(myotherlist)

    mylastlist = ["192.168.0.1", "8.8.8.8"]

    mylastlist.extend(["9.9.9.9", "4.4.4.4"])
    # mylastlist = ["192.168.0.1", "8.8.8.8", "9.9.9.9", "4.4.4.4"]

    print(mylastlist)


if __name__ == "__main__":
    main()
