def check_encoding(string):
    allowed = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
               'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
               'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
               'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь',
               'э', 'ю', 'я', '.', '-'}
    if set(string).difference(allowed):
        if set(string.encode('cp1251', 'ignore').decode('UTF-8', 'ignore')).difference(allowed):
            print('String contains non-allowed symbols or is in wrong codepage.')
            return None
        else:
            print('That\'s CP1251!')
            return string.encode('cp1251', 'ignore').decode('UTF-8', 'ignore')
    else:
        print('That\'s UTF-8!')
        return string


dn = input('Waiting for Cyrillic domain address to convert:\n')
dn = check_encoding(dn)
if dn:
    print(dn)
    try:
        result = dn.encode('idna')
    except UnicodeEncodeError as E:
        print('IDNA encoding error: ', E)
    else:
        print(result.decode('ascii'))
