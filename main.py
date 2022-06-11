def add_space(string):
    if '<' in string:
        string = string.replace('<', '&nbsp;<')
    if '>' in string:
        string = string.replace('>', '>&nbsp;')
    return string


a = '''I'm at the <b> end </b> of my <a> wits</a>'''

print(add_space(a))
