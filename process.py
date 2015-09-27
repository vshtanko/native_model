#видоизмененная функция для обработки одиночного файла датасета
#добавлена возможность легко добавлять доп функции извлечения фич



#импорт всех функций для фичеэкстракшна
import feature_extraction 
from inspect import getmembers, isfunction
fe_funcs = getmembers(feature_extraction, isfunction)

import os
import re




def process(filepath, extract_text = False):
    values = {}
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as infile:
        text = infile.read()

    #if filename in train_keys:
    #    values['sponsored'] = train_keys[filename]
    values['file'] = filename
    values['lines'] = text.count('\n')
    values['spaces'] = text.count(' ')
    values['tabs'] = text.count('\t')
    values['braces'] = text.count('{')
    values['brackets'] = text.count('[')
    values['words'] = len(re.split('\s+', text))
    values['length'] = len(text)


    #более сложные фичи
    soup = BeautifulSoup(text, 'html.parser')
    
    for func in fe_funcs:
        values[func[0]] = func[1](soup)

    if extract_text == True:
        text = soup.get_text()
        (root, ext) = os.path.splitext(filename)
        with open(root+'.nlp', 'w') as fout:
            fout.write(text)


    return values
