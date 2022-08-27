def get_positions(n):
    sequence = {}
    persons = [0, 0, 0]
    sequence[0] = (persons[0], persons[1], persons[2])
    for i in range(1,n+1):
        if  persons == [2, 2, 2]:
            persons = [0, 0, 0]
            sequence[i] = (persons[0], persons[1], persons[2])
        else:
            if persons[0] <2:
                persons[0] += 1
                sequence[i] = (persons[0], persons[1], persons[2])
            elif persons[1] <2:
                persons[0] = 0
                persons[1] += 1
                sequence[i] = (persons[0], persons[1], persons[2])
            elif persons[2] < 2:
                persons[0] = 0
                persons[1] = 0
                persons[2] += 1
                sequence[i] = (persons[0], persons[1], persons[2])

    return sequence[n]

#n = int(input("Enter the number of steps: "))

print(get_positions(998))

