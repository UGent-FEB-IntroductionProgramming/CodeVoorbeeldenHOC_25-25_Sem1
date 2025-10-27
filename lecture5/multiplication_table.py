print("Multiplication Table")
print("-" * 20)
print("\t",end="")
for i in range(1,10):
    print(i, end=" ")

print()
for i in range(1,10):
    print(i, end="\t")
    for j in range(1,10):
        print(i*j, end=" ")
    print()