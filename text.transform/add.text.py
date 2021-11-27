
filename = './man-ln'

front_meta = """
title: How to add front meta to all markdown files
Date: Wed 27 Oct 2021 06:19:48 PM CST
Tags: Howto


"""

#with open(filename, 'r+') as f:
f = open(filename, 'r+')

print(type(f))

t = f.read()

#f.close()
f.seek(0)


print(len(t))

ta = front_meta + t


f.write(ta)

f.flush()
f.close()




