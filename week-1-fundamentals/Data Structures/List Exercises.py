def sum_list(numbers):
  total = 0
  for num in numbers:
    total += num
  return total

def find_max(numbers):
  if not numbers:
    return None
  
  current_max = float('-inf')
  for num in numbers:
    if(num > current_max): current_max = num
  return current_max

def remove_duplicates(items):
  seen = set()
  result = []
  for item in items:
      if item not in seen:   
          result.append(item)
          seen.add(item)

  return result           


def reverse_list(items):
  new_items = []
  for item in items:
    new_items.insert(0, item)

  return new_items

def count_occurrences(items, target):
  count = 0
  for item in items:
    if target == item: count += 1
  return count

def get_evens(numbers) :
  result = []
  for num in numbers:
    if num % 2 == 0:
      result.append(num)
  return result


def alternate_merge(list1, list2):
  result = []
  for item1, item2 in zip(list1, list2):
    result.append(item1)
    result.append(item2)

  longer_start = len(min([list1, list2], key=len))
  result.extend(list1[longer_start:])
  result.extend(list2[longer_start:])
  return result

def chunk_list(items, chunck_size):
  result = []
  i = 0
  while i < len(items):
    chunk = items[i : i + chunck_size]
    result.append(chunk)
    i += chunck_size

  return result

def find_pairs_sum(numbers, target):
  seen = set()
  pairs = []

  for num in numbers:
    complement = target - num 
    if complement in seen: 
      pairs.append((complement, num)) 
    seen.add(num)
  return pairs  


def rotate_list(items, n):
  result = []
  for i in range(n):
    result.append(items[len(items) - n + i])
  for i in range(len(items) - n):
    result.append(items[i])
  return result

print(find_pairs_sum([1,2,3,4,5,6], 7))
print("="*50)
print(sum_list([1,2,3,4,5]))
print(remove_duplicates([1, 2, 3, 2, 1, 4]))
print(remove_duplicates(["a", 'b', 'a', 'c']))
print(get_evens([1, 2, 3, 4, 5]))
print(alternate_merge([1,2,3], ['a','b','c']))
print(rotate_list([1,2,3,4,5], 2))


##################################################################################

def find_second_largest(numbers):
  seen = set()
  for num in numbers:
    seen.add(num)
  if len(seen) < 2: return None

  current_max = float("-inf")
  second_max = float("-inf")
  for num in numbers:
    if num > current_max: current_max = num
  for num in numbers:
    if num < current_max and num > second_max: second_max = num

  return second_max

print("="*100)
print(find_second_largest([1,2,3,4,5,6,7]))

def flatten_list(nested):
  result = []
  for item in nested:
    if isinstance(item, list):
      result.extend(flatten_list(item))
    else:
      result.append(item)
  return result

print("HERE WE GO")
print(flatten_list([[1, 2], [3, 4]]))          
print(flatten_list([1, [2, [3, 4]], 5]))       


def find_missing_number(numbers):
  n = max(numbers)
  total = int(n*(n+1)/2)
  current_total = 0
  for num in numbers:
    current_total += num
  missing_number = total - current_total
  return missing_number

print(find_missing_number([1,2,4,5,6]))

def merge_sorted_lists(list1, list2):
  result = []
  i = j = 0

  while i < len(list1) and j < len(list2):
    if list1[i] <= list2[j]:
      result.append(list1[i])
      i+=1
    else:
      result.append(list2[j])
      j+=1  

  result.extend(list1[i:])
  result.extend(list2[j:])

  return result

print(merge_sorted_lists([1,3,5,7,8], [2,4]))

def is_palindrome(items):
  check = True
  for i in range(len(items)):
    if (items[i] == items[len(items) - 1 - i]):
      print(f"({items[i]}, {items[len(items) - 1 - i]})")
    else: check = False
  return check

print("*"*10)
print(is_palindrome([1,2,3,2,1]))

def move_zeros_to_end(numbers):
  zero_count = 0
  i = 0
  while i < len(numbers):
    if numbers[i] == 0:
      numbers.pop(i)
      zero_count += 1
    else:
      i += 1

  for _ in range(zero_count):
    numbers.append(0)

  return numbers

print(move_zeros_to_end([0, 1, 0, 3, 12]))
print(move_zeros_to_end([1, 2, 3]))
print(move_zeros_to_end([0, 0, 1]))


def longest_increasing_sequence(numbers):
  if not numbers:
    return 0  
  
  max_length = 1
  current_length = 1

  for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
      current_length += 1
      max_length = max(max_length, current_length)
    else:
      current_length = 1

  return max_length

print(longest_increasing_sequence([1, 2, 3, 1, 2, 3, 4, 5]))

def remove_all(items, value):
  while value in items:
    items.remove(value)

  return items  

print("&"*100)
print(remove_all([1,2,3,2,4,2], 2))
print("&"*100)



def find_intersection(list1, list2):
  both = set()
  for item1 in list1:
    if item1 in list2:
      both.add(item1)
  return list(both)

print(find_intersection([1, 2, 3, 4], [3, 4, 5, 6]))
print(find_intersection([1,2,2,3], [2,2,3,4]))
print(find_intersection([1,2], [3,4]))

def rotate_left(items, k):
  # if k > len(items) - 1 or k < 0:
  #   k = k % len(items)

  # result = []
  # for i in range(len(items)):
  #   if i >= k:
  #     result.append(items[i])

  # for i in range(len(items)):
  #   if i < k:
  #     result.append(items[i])

  if not items:
    return items
  k = k % len(items)
  return items[k:] + items[:k]

  

print(rotate_left([1,2,3,4,5], 2))
print(rotate_left([1,2,3], 0))
print(rotate_left([1,2,3,], 5))
print(rotate_left([1,2,3], -1))