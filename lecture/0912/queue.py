# queue
queue=[]
def add(item):
  queue.append(item)

def remove():
  if len(queue) != 0:
    item =queue.pop(0)
    return item

add('book')
add('pen')
add('lunch')

print(queue)
remove()
print(queue)
