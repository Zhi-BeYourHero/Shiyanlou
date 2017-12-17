with open('/etc/protocols') as file:
    count=0
    for line in file:
        count+=1
    print(count)

