
from asyncore import write


f = open('text.txt', 'r')

# print(f.read())

print(f.readline(), end='')
print(f.readline(), end='')
print(f.readline(2), end='')

f.close()


fw = open('newtext.txt', 'w')
fw.write('hello,\nkavinda')
fw.write(' how are you.')
fw.close()

f = open('text.txt', 'r')
fa = open('newtext.txt', 'a')
fa.write('\nnew appended text.\n\n')


for data in f:
    fa.write(data)

f.close()
fa.close()


img = open('img.jpg', 'rb')  # read in binary format
newimg = open('newimg.jpg', 'wb')  # read in binary format

for i in img:
    newimg.write(i)

img.close()
newimg.close()
