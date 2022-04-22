def mergeSort(array):
    if len(array) > 1:
      mid = len(array) // 2
      leftSection = array[:mid]
      rightSection = array[mid:]

      mergeSort(leftSection)
      mergeSort(rightSection)

      i = 0
      j = 0
      k = 0

      while i < len(leftSection) and j < len(rightSection):
        if leftSection[i] < rightSection[j]:
          array[k] = leftSection[i]
          i += 1
        else:
          array[k] = rightSection[j]
          j += 1
        k += 1
      while i < len(leftSection):
        array[k] = leftSection[i]
        i += 1
        k += 1
      while j < len(rightSection):
        array[k] = rightSection[j]
        j += 1
        k += 1
    return array