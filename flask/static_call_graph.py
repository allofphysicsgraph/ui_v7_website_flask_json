#!/usr/bin/env python3

import glob
import re

list_of_py_files = glob.glob('*.py')

py_dict = {}
for py_file in list_of_py_files:
    #print(py_file)
    with open(py_file) as fil:
        py_content = fil.readlines()
    py_dict[py_file] = py_content

py_code_dict = {}
for py_file, list_of_lines in py_dict.items():
    #print(py_file)
    py_code_dict[py_file] = []
    inside_multiline_comment = False
    for this_line in list_of_lines:
        line_without_trailing_spaces = this_line.rstrip()
        if line_without_trailing_spaces == '':
            #print('empty line')
            pass
        else: # line is not empty
#            print('this_line = ', this_line)
            line_without_comments = re.sub('#.*', '', this_line).rstrip()
#            print('line_without_comments = ',line_without_comments)
            if line_without_comments == '':
                #print('line is only comment:', this_line)
                pass
            else: # line has content
                if this_line.strip().startswith('"""') and not inside_multiline_comment:
                    inside_multiline_comment = True
                elif this_line.strip().startswith('"""') and inside_multiline_comment:
                    inside_multiline_comment = False
                if inside_multiline_comment:
                    #print('inside multiline comment: ',this_line)
                    pass
                else:
                    if not this_line.strip() == '"""':
                        #print(this_line.rstrip())
                        py_code_dict[py_file].append(line_without_comments.rstrip())

# py_code_dict now contains all the code sans comments
dict_of_functions_per_file = {}
for py_file, list_of_lines in py_code_dict.items():
    dict_of_functions_per_file[py_file] = []
    for this_line in list_of_lines:
        if this_line.startswith('def '):
            #print(re.sub('\(.*', '', this_line.replace('def ','')))
            dict_of_functions_per_file[py_file].append(re.sub('\(.*', '', this_line.replace('def ','')))

print('==== functions per file ====')
for py_file, func_list in dict_of_functions_per_file.items():
    print(py_file, func_list)

dict_of_imports_per_file = {}
for py_file, list_of_lines in py_code_dict.items():
    dict_of_imports_per_file[py_file] = []
    for this_line in list_of_lines:
        if this_line.startswith('import') and ' as ' not in this_line:
            name_of_file = this_line.replace('import ','').rstrip()
            if name_of_file+'.py' in list_of_py_files:
                import_alias = this_line.replace('import ','')
                tup = (name_of_file, import_alias)
                dict_of_imports_per_file[py_file].append(tup)
            else:
                print(name_of_file + ' is not local')
        elif this_line.startswith('import') and ' as ' in this_line:
            name_of_file = this_line.replace('import ','').split(' as ')[0].strip()
            if name_of_file + '.py' in list_of_py_files:
                import_alias = this_line.replace('import ','').split(' as ')[1].strip()
                tup = (name_of_file, import_alias)
                dict_of_imports_per_file[py_file].append(tup)
            else: 
                print(name_of_file + ' is not local')

print('==== imports per file ====')
for py_file, import_tuples in dict_of_imports_per_file.items():
    print(py_file, import_tuples)

# EOF
