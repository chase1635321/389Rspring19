
#!/usr/bin/env python3

import sys
from struct import pack, unpack
import time

MAGIC = 0x8badf00d
VERSION = 1

with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

print("=" * 80)

magic, version = unpack("<LL", data[0:8])
(timestamp,) = unpack("<L", data[8:12])
(author,) = unpack("<8s", data[12:20])
(section,) = unpack("<L", data[20:24])

if magic != MAGIC or version != VERSION:
    exit()

print("Magic: " + str(hex(magic)))
print("Version: " + str(version))
print("Time: " + str(timestamp))
print("Author: " + str(author))
print("Section: " + str(section))

print("=" * 80)

o = 24
for i in range(section):
    s, l = unpack("<LL", data[o:o + 8])
    (val,) = unpack("<{}s".format(l), data[o:o + l])

    print("Type: " + str(s) + " Length: " + str(l))

    o += 8

    if s == 1:
        print("Ascii:" + str(val))
    elif s == 2:
        print("UTF-8: " + str(val))
    elif s == 3:
        (message,) = unpack("<{}s".format(l/4), data[o:o + l/4])
        print("Words: " + str(message))
    elif s == 4:
        for i in range(0, l, 8):
            (message, ) = unpack("<8s", data[o+i, o+i+9])
            print("Dwords: " + str(message))
    elif s == 5:
         for i in range(0, l, 8):
            (message, ) = unpack("<8s", data[o+i, o+i+8])
            print("Doubles: " + str(message))
    elif s == 6:
        (lat, lon) = unpack("<dd", data[o:o+l])
        print("Coor: " + str(lat) + ", " + str(lon))
    elif s == 7:
        (message,) = unpack("<d", data[o:o+l])
        print("Ref: " + str(message))
    elif s == 8 or s == 9 or s == 10:
        header = b"\x89\x50\x4E\x47\x0d\x0a\x1a\x0a"
        with open(str("file" + str(s) + ".output"), "wb") as f:
            f.write(header)
            f.write(data[o:o + l])

        print("Saved file as file" + str(s) + ".output")
    else:
        print("Error")

    o += l
    print("-" * 80)
