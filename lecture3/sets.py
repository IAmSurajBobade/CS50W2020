# Create an empty set
myset = set()

myset.add(1)
myset.add(3)
myset.add(2)
# 3 is not added
myset.add(3)
myset.add(4)

myset.remove(4)
print(myset)
print(f"my set has {len(myset)} elements")
