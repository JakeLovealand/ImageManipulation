def groups_of_3(values):
   result = []
   counter = 0
   for val in values:
      if counter % 3 == 0:
         result.append([])
      result[counter//3].append(values[counter])
      counter += 1
   return result  
