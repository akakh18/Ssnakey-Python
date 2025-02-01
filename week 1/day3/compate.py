import time

if __name__ == '__main__':
    list_collection = []
    for i in range(100000000):
        list_collection.append(i)

    print("List collection: ")
    start_time = time.time()
    if 45310831 in list_collection:
        print("Yes")
    else:
        print("No")
    print("--- %s seconds ---" % (time.time() - start_time))


    set_collection = set(list_collection)

    print("Set collection: ")
    start_time = time.time()
    if 45310831 in set_collection:
        print("Yes")
    else:
        print("No")
    print("--- %s seconds ---" % (time.time() - start_time))
