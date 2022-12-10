try:
    with open('../data/test.txt',mode='r') as f:
        print(f.readline())
except:
    print("file not found")
else:
    print("Completed read ")