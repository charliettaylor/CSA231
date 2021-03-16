'''
D takes a file path and considers current Directory
R takes file path and considers all childRen

A marks All as interesting X
N marks the Named file specified X
E marks specified Extension X
T files that contain Text X
< marks files that are less than specified bytes X
> marks files greater than specified bytes X
then prints all interesting file paths

F prints First line of text, else print NOT TEXT X
D makes a dup file called boo.jpg.dup
T Touches the file and changes last modified date to current time X
program ends
'''

from pathlib import Path
import pprint as pp


def get_file_path() -> list:
    directory = input()
    start = directory.startswith('D') or directory.startswith('R')

    while not directory.__contains__(' '):
        directory = input()
    
    exists = Path(directory.split()[-1]).exists()

    while not start or not exists:
        print('ERROR')
        directory = input()
        exists = Path(directory.split()[-1]).exists()
        start = directory.startswith('D') or directory.startswith('R')

    return directory.split()


def get_directory(dir: str):
    path = Path(dir[1])

    if dir[0] ==  'D':
        path = sorted(path.glob('*/.'))
    elif dir[0] == 'R':
        path = sorted(path.glob('**/*'))

    files = []
    for file in path:
        if file.is_file():
            files.append(file)
    return files

   
def mark_text_files(mark: list, subs: list) -> list:
    '''
    mark contains ['T', user text] where we want to mark files that contain
    the substring user text
    '''
    marked = []
    textInterest = mark[1]
    for file in subs:
        if file.read_text().__contains__(textInterest):
            marked.append(file)
    return marked


def mark_size_files(mark: list, subs: list) -> list:
    '''
    takes a list mark from user in format [> or <, size in bytes], and the
    subs previously selected
    '''
    marked = []
    size = mark[1]
    for file in subs:
        if mark[0] == '>':
            if file.stat().st_size > size:
                marked.append(file)
        else:
            if file.stat().st_size < size:
                marked.append(file)


def mark_file_name(mark: list, subs: list) -> list:
    '''
    takes list mark from user in format ['N', name] where name is the files
    that should be marked with that name
    '''
    marked = []
    name = mark[1]
    for file in subs:
        if file.name.__contains__(name):
            marked.append(file)
    return marked


def get_mark() -> list:
    '''
    gets user input for what files to mark and returns as a list of len 2
    '''
    mark = input()
    start = mark.startswith('<') or mark.startswith('N')\
         or mark.startswith('E') or mark.startswith('T')\
         or mark.startswith('>')

    while not start or not mark.__contains__(' ') or not len(mark.split()) == 2:
        if mark == 'A':
            break
        print('ERROR')
        mark = input()
        start = mark.startswith('<') or mark.startswith('N')\
             or mark.startswith('E') or mark.startswith('T')\
             or mark.startswith('>')

    return mark.split()

def mark_extensions(mark: list, subs: list):
    ext = mark[1]
    marked = []
    for sub in subs:
        if sub.suffix == ext:
            marked.append(sub)
    return marked


def mark_all(mark: list,  subs: list):
    return subs


def mark_files(mark: list, subs: list):
    mark_options = {
        'A' : mark_all,
        'N' : mark_file_name,
        'E' : mark_extensions,
        'T' : mark_text_files,
        '>' : mark_size_files,
        '<' : mark_size_files
    }
    mark_func = mark_options[mark[0]]
    return mark_func(mark, subs)

def get_action() -> list:
    '''
    gets user input for what files to mark and returns as a list of len 2
    '''
    action = input()
    start = action.startswith('F') or action.startswith('D')\
         or action.startswith('T')

    while not start and len(action) == 1:
        print('ERROR')
        action = input()
        start = action.startswith('F') or action.startswith('D')\
             or action.startswith('T')

    return action

def take_action(action: str, marked: list):
    actions = {
        'F' : first_line,
        'D' : dupe,
        'T' : touch
    }
    action = actions[action]
    action(marked)


def first_line(marked: list):
    for file in sorted(marked, key=lexo_sort):
        try:
            txt = file.read_text()
            if txt.__contains__('\n'):
                txt = txt.split('\n')
                print(txt[0])
            else:
                print(txt)
        except:
            print("NOT TEXT")


def dupe(marked: list):
    pass


def touch(marked: list):
    for file in marked:
        file.touch()


def lexo_sort(x):
    splits = x.__str__().split('\\')[4:]
    return len(splits), splits


def print_dir(dir: list):
    for file in sorted(dir, key=lexo_sort):
        print(file.__str__())


def main():
    dir = get_file_path() # gets user in for file path
    dir = get_directory(dir) # returns either curr dir or all subs
    print_dir(dir)
    mark = get_mark() # gets user in for what to mark
    marked = mark_files(mark, dir)
    print_dir(marked)
    action = get_action()
    take_action(action, marked)


if __name__ == "__main__":
    main()