

# 1000 bytes = 1 KiloBytes(KB)
# 1000000 bytes =1 megabytes(MB)
# 1000000000 bytes = 1 Gigabyte(GB)
# 1000000000000 bytes = 1 terabytes(TB)


bytes = int(input("Enter Bytes:"))

if bytes < 1000:
    print(bytes , "Bytes")
elif 1000 <= bytes < 1000000:
    kb = bytes / 1000
    print(bytes , "Bytes =", kb, "KB")
elif 1000000 <= bytes < 1000000000:
    mb = bytes / 1000000
    print(bytes , "Bytes =", mb, "MB")
elif 1000000000 <= bytes < 1000000000000:
    gb = bytes / 1000000000
    print(bytes , "Bytes =", gb, "GB")
elif bytes > 1000000000000:
    tb = bytes / 1000000000000
    print(bytes , "Bytes =", tb, "TB")
else:
    print("Your Number is Wrong.")

