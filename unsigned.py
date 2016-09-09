def convert_to_32(i,n):
    return format(i, 'b').zfill(n)

def decimal(number):
    return ~number & 0xFFFFFFFF

def main():

    times = int(raw_input())
    for i in range(times):
        number1 = int(raw_input()) 
        n_decimal = decimal(number1)
        print n_decimal


if __name__ == '__main__':
    main()
