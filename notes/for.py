# for loops = execute a block of code a fixed number of times
# You can interage over a range, string sequence, etc.
# if you use continue if with continue condition you'll skip the counter and break you stop

# print 1 to 10
for x in range(1, 11):
    print(x) 

# skip 5
for x in range(1, 10):
    if x == 5:
        continue
    else:
        print(x)

# break at 5
for x in range(1, 10):
    if x == 5:
        break
    else:
        print(x)