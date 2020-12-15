class SortedArray:
  # Using Binary Search for implementation of this class

  def __init__(self):
    self.array = []

  def search(self, number):
    low = 0
    high = len(self.array)-1
    mid = 0
    while low <= high:
      mid = (low+high)//2
      if self.array[mid] < number: 
          low = mid + 1
  
      elif self.array[mid] > number: 
          high = mid - 1
      else: 
          return (True, mid)
    else:
      return (False, mid)

  def insert(self, number):
    found, index = self.search(number)
    if len(self.array) == 0:
      self.array.insert(0, number)
    elif found:
      self.array.insert(index, number)
    else:
      if number < self.array[index]:
        self.array.insert(index, number)
      else:
        self.array.insert(index+1, number)

  def show(self):
    print(self.array)

