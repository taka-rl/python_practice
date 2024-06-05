'''
Exercise 3: Slice list into 3 equal chunks and reverse each chunk
Given:

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
Expected Outcome:

Chunk  1 [11, 45, 8]
After reversing it  [8, 45, 11]
Chunk  2 [23, 14, 12]
After reversing it  [12, 14, 23]
Chunk  3 [78, 45, 89]
After reversing it  [89, 45, 78]
'''

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
chunk1, chunk2, chunk3 = [], [], []
revChunk1, revChunk2, revChunk3 = [], [], []

l = 3
chunk1 = sample_list[0:l*1:1]
chunk2 = sample_list[3:l*2:1]
chunk3 = sample_list[6:l*3:1]
revChunk1 = sample_list[l*1 - 1::-1]
revChunk2 = sample_list[l*2 - 1:2:-1]
revChunk3 = sample_list[l*3 - 1:5:-1]

'''
length = len(sample_list)
for i in range(0, length, 1):
    if i < 3:
        chunk1.append(sample_list[i])
    elif 3 <= i < 6:
        chunk2.append(sample_list[i])
    elif 6 <= i:
        chunk3.append(sample_list[i])
    else:
        continue
'''
print("Chunk1,", chunk1)
print("After reversing it", revChunk1)

print("Chunk2,", chunk2)
print("After reversing it", revChunk2)

print("Chunk3,", chunk3)
print("After reversing it", revChunk3)


# sample answer
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("Original list", sample_list)

length = len(sample_list)
chunk_size = int(length / 3)
start = 0
end = chunk_size

# run loop 3 times
for i in range(3):
    # get indexes
    indexes = slice(start, end)
    print(type(indexes))
    ind = (start, end)
    print(type(ind))
    
    # get chunk
    list_chunk = sample_list[indexes]
    print("Chunk", i, list_chunk)
    
    # reverse chunk
    print("After reversing it", list(reversed(list_chunk)))
    
    start = end
    end += chunk_size
    
'''
https://note.nkmk.me/python-slice-usage/
slice() can creat a slice object like this → [start:end:step]
in this program, indexes = slice(start, end) is shown below.
indexes[start, end, none]
where start is 0, end = chunk_size at the begining of the program.
chunk_size = int(length / 3)
start = 0
end = chunk_size

'''
