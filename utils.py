def partition(array, low, high):
  pivot = array[high]
  i = low - 1
 
  for j in range(low, high):
    if array[j]['rating'] <= pivot['rating']: # or array[j]['review'] <= pivot['review']:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
 
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1

def quicksort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quicksort(array, low, pi - 1)
    quicksort(array, pi + 1, high)


def print_table(array, max = 10):
  URL = "https://www.park4night.com"

  print("╭----------------------------------------------------------------------------------------------╮")
  print("|   URL:                                      | Rating | Review | type  | label                |")
  print("|----------------------------------------------------------------------------------------------|")
  for e in array[:max]: 
    url_place = URL + e['url']
    rating = str(e['rating'])
    review = str(e['review'])
    type_code = str(e['type']['code'])
    type_label = str(e['type']['label'])
    type_label = (type_label[:20]) if len(type_label) > 20 else type_label

    print('|' , end=' ')
    print(f'{url_place:<43}', end = ' | ')
    print(f'{rating:<6}', end = ' | ')
    print(f'{review:<6}', end = ' | ')
    print(f'{type_code:<5}', end = ' | ')
    print(f'{type_label:<20}', end = ' |\n')
    print("|----------------------------------------------------------------------------------------------|")


  print("╰----------------------------------------------------------------------------------------------╯")

