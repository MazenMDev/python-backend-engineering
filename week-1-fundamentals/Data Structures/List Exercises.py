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