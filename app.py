def kuku(maxdan):
    for i in range(1, maxdan + 1):
        for j in range(1, 10):
            print(f"{i}x{j}={i*j}", end="\t")
        print()  # 改行される


maxdan = int(input("何段まで:"))
kuku(maxdan)
