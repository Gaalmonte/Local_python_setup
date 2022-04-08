def hello():
    print('Hello!')

hello()

def pack(fname1,fname2,fname3):
    return (fname1, fname2, fname3)

print(pack("Monday","Thursday", "Saturday"))

def eat_lunch(list):
    if len(list) == 0:
        print("My lunchbox is empty")
    else:
        for i in range(len(list)):
            if i == 0:
                print(f"First I eat {list[0]}")
            else:
                print(f"Next I eat {list[i]}")

eat_lunch(["steak", "rice", "beans", "orange"])