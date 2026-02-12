def process_data(data=[]):
    result = 0

    for i in range(len(data)):
        result += data[i]

    unused_variable = 100

    print("The result is: %s" % result)

    return result


process_data([10, 20, 30])
