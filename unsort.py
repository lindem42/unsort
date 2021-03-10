
# this algorithm divides the array into two sides, one of which will necessarily be longer than the other since the length of the array is odd
# the values will be reversed within each side, and then the two sides will be woven together
# whichever side is longer will begin the weaving sequence
# the longer side will be determined by dividing the length of the array by 2 and analyzing the values at the indices of array[length/2] and array[(length/2)+1]
# if the values at those indices are the same, then the second side will be longer
# if they are different, then the first side will be longer

def unsort(array):

  print("Original, sorted array:\n", array)
  length = len(array)

  if (length != 1):

    # determine which side should be longer
    if (array[int(length/2)] == array[int(length/2) + 1]):
      splitPoint = int(length/2)-1
      firstHalfLonger = False
    else:
      firstHalfLonger = True
      splitPoint = int(length/2)

    # method to swap order of two halves
    def reverseSide(start, end):
      while (start < end):
        temp = array[start]
        array[start] = array[end]
        array[end] = temp
        start += 1
        end -= 1

    # call swapHalf on the first half only if it contains more than one unique value
    if (array[0] != array[splitPoint]):
      reverseSide(0, splitPoint);
    # call swapHalf on the second half only if it contains more than one unique value
    if (array[splitPoint+1] != array[length - 1]):
      reverseSide(splitPoint+1, length - 1);

    print("Array with reversed sides:\n", array)

    array2 = [0] * length
    # weave second half into first half
    def weave(firstHalfIndex, secondHalfIndex):
      index = 0
      while (index < length):
          if (index % 2 == 0):
            array2[index] = array[firstHalfIndex]
            firstHalfIndex += 1
          else:
            array2[index] = array[secondHalfIndex]
            secondHalfIndex += 1
          index += 1

    if (firstHalfLonger):
      weave(0, splitPoint+1)
    else:
      weave(splitPoint+1, 0)

    print("Final, unsorted array:\n", array2)

  else:
    print("Array is length 1; nothing to unsort!")


# EXAMPLE [1,1,3]
# length = 3
# length/2 = 1
# array[1] = 1; array[1+1] = 3
# since the two values are different, the array is divided between index 1 and 2 (that is, the first side is longer, ending at index 1)
# side one: [1, 1]; side two: [3]
# no reversing needs to occur on either side, since the values within each side are the same
# begin weaving with the first value on the longer side:
# 3 (first value on the longer side), 1 (first value on the shorter side), 3 (last value on the longer side)
# final result: [1,3,1]
unsort([1,1,3])
print('\n')

# EXAMPLE: [1,1,2,2,2]
# length = 5
# length/2 = 2
# array[2] = 2; array[2+1] = 2
# since the two values are the same, the array is divided between index 1 and 2 (that is, the second side is longer,beginning at index 2)
# side one: [1,1]; side two: [2,2,2]
# no reversing needs to occur on either side, since the values within each side are the same
# begin weaving with the first value on the longer side:
# 2 (first value from longer side), 1 (first value from shorter side), 2 (next value from longer side), 1 (next value from shorter side) ... 2 (last value from longer side)
# final result: [2,1,2,1,2]
unsort([1,1,2,2,2])
print('\n')

# EXAMPLE: [1,1,2,2,3,3,3]
# length = 7
# length/2 = 3
# array[3] = 3; array[3+1] = 3
# since the two values are different, the array is divided between index 3 and 4 (that is, the first side is longer, ending at index 3)
# side one: [1, 1, 2, 2]; side two: [3, 3, 3]
# reverse side one: [2, 2, 1, 1]
# no reversing needs to occur in side two, since the values are all the same
# begin weaving with the first value on the longer side:
# 2 (first value from longer side), 3 (first value from shorter side), 2 (next value from longer side), 3 (next value from shorter side) ... 1 (last value from longer side)
# final result: [2,3,2,3,1,3,1]
unsort([1,1,2,2,3,3,3])
print('\n')

# EXAMPLE: [1,1,2,2,2,3,3,3,4,4,5,5,5,5,5,6,6,7,8,9,9,9,9]
# length = 23
# length/2: 11
# array[11]: 5; array[12]: 5
# since the two values are the same, the array is divided between index 10 and 11 (that is, the first side is shorter, ending at index 10)
# side one: [1,1,2,2,2,3,3,3,4,4,5]
# side two: [5,5,5,5,6,6,7,8,9,9,9,9]
# reverse side one: [5,4,4,3,3,3,2,2,2,1,1]
# reverse side two: [9,9,9,9,8,7,6,6,5,5,5,5]
# begin weaving with the first value on the longer side:
# 9 (first value from longer side), 5 (first value from shorter side), 9 (next value from longer side), 4 (next value from shorter side), ... 1 (last value from longer side)
# final result: [9,5,9,4,9,4,9,3,8,3,7,3,6,2,6,2,5,2,5,1,5,1,5]
unsort([1,1,2,2,2,3,3,3,4,4,5,5,5,5,5,6,6,7,8,9,9,9,9])
print('\n')

# here are some other tests; feel free to test with your own:)
unsort([1])
print('\n')
unsort([4,4,5,5,6,7,8,10,11])
print('\n')
unsort([5,6,6,7,9])
