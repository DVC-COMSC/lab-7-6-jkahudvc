
def getInput():
    nums = list(input("Please enter as many integers as you can: ").split())
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    return nums


def makeReverse(numbers):
    l = len(numbers)
    for i in range(0,int(l/2)):
        numbers[i],numbers[l-1-i] = numbers[l-1-i], numbers[i]
    return numbers
        


def main():
    numbers = getInput()
    ret = makeReverse(numbers)
    print(f'The result values are: {ret}')


if __name__ == '__main__':
    main()
