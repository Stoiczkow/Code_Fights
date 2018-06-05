def findEmailDomain(address):
    reversed_addres = address[::-1]
    index_of_at = reversed_addres.index('@')
    reversed_domain = reversed_addres[:index_of_at]
    return reversed_domain[::-1]