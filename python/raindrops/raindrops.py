def convert(number):
    stuff = []
    divisibleby = [(3, "Pling"), (5, "Plang"), (7, "Plong")]
    for test in divisibleby:
        if number % test[0] == 0:
            stuff.append(test[1])
    return ''.join(stuff) if stuff else str(number)
