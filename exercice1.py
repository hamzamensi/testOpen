import sys

def serialize(tab=[]):
    if not isinstance(tab, list):
        raise TypeError('Il faut un tableau')
    str1 = ' '
    return str1.join(tab)

def deserialize(chr=''):
    if not isinstance(chr, str):
        raise TypeError('Il faut une chaine de caracteres')
    if chr == '':
        return []
    return chr.split(' ')

if __name__ == '__main__':
    tab = sys.argv[1:]
    print(deserialize(serialize(tab)))
