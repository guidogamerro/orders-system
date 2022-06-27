def entry_str(message,error):

    data = input(message)

    while data == "":

        print(error)

        data = input(message)

    return data