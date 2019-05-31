print("Enter two numbers: lowest and highest")

start = input("Enter the lowest number: ")
end = input("Enter the highest number: ")

start = int(start)
end = int(end)

f = open("output.txt","w")

for i in range(start, end + 1):
    print(i, file=f)
end

print("Done!")