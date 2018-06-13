def messageFromBinaryCode(code):
    n = int(code, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
