from mergesort import mergeSort # pragma: no cover

  # Get user input; put into array  
def userInput(): # pragma: no cover
  inputArray = []
  n = int(input("Enter size of array: "))
  if n < 2:
    print("The size must be at least 2.")
    return userInput()
  for i in range(0,n):
    element = int(input("Element: "))
    inputArray.append(element)
  return inputArray

def main(): # pragma: no cover
  r = userInput()
  mergeSort(r)
  print(r)

if __name__ == '__main__': # pragma: no cover
  main() 