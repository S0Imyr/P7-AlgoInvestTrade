def display_cell_length(message, length):
    if len(str(message)) > length:
        return str(message)[:length]
    else:
        return str(message) + " " * (length - len(str(message)))


if __name__ == '__main__':
    pass
