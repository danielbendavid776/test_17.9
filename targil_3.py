def camel_to_hyphen(text):
    '''
    returns a string from camel case to hyphen case
    :param text: string
    :return: str from camel case to hyphen case with
    '''
    result = str()
    for c in text:
        if c.isupper():
            result += '-' + c.lower()
        else:
            result += c
    return result
print(camel_to_hyphen('helloPython'))
print(camel_to_hyphen('myVariableName'))
print(camel_to_hyphen('python'))
print(camel_to_hyphen('aBigTest'))

