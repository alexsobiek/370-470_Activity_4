from mergesort import mergeSort

def main():
    r = userInput()
    mergeSort(r)
    print(r)

def userInput():
    inputArray = []
    n = int(input("Enter size of array: "))
    if n < 2:
      print("The size must be at least 2.")
      return userInput()
    for i in range(0,n):
      element = int(input())
      inputArray.append(element)
    return inputArray

main()