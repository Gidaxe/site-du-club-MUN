def add_space(string):
    if '<' in string:
        string = string.replace('<', '&nbsp;<')
    if '>' in string:
        string = string.replace('>', '>&nbsp;')
    return string
