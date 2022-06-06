def hello ():
    print('Hello user!!')
hello()

def pack(l1, l2, l3):
    list = [l1, l2, l3]
    return list

print(pack('socks', 'underwear', 'shoes',))


def eat_lunch(*args):
    list = []
    for arg in args:
        list.append(arg)
    if list:
        print('First I eat', list[0])
        i = 1
        while i < len(list):
            print('Next I eat', list[i])
            i += 1
    else:
        print('My lunchbox is empty!')

eat_lunch('pudding', 'pb&j', 'carrots', 'ice cream')