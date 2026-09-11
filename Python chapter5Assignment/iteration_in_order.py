iteration_in_order =[[0,0,0],
[0,0,0]]

index = 1
for row in range(len(iteration_in_order)):
    for column in range(len(iteration_in_order[row])):
        index +=1
        
for column in range(len(iteration_in_order[row])):
    print (column, end= ' ')
print()
    
for row in range(len(iteration_in_order)):
      print (row, end= ' ')
      
print()

for column in range(len(iteration_in_order[row])):
    print (row, end= ' ')
