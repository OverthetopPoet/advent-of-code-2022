class File:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = int(size)
        self.parent = parent

    def get_size(self):
        return self.size


class Folder:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = {}

    def get_size(self):
        if self.size == None:
            self.calculate_size()
        return self.size

    def calculate_size(self):
        self.size = 0
        for child in self.children.values():
            self.size += child.get_size()

    def add_child(self, name, size, type):
        if type == 'dir':
            self.children.update({name: Folder(name, None, self)})

        if type == 'file':
            self.children.update({name: File(name, size, self)})

    def get_child(self, name):
        return self.children[name]

    def get_children(self):
        child_list = []
        for child in self.children.keys():
            child_list.append(child)
        return child_list

    def get_subdirectories(self):
        subdirectories = []
        child_list = []
        for child in self.children.keys():
            child_list.append(self.children[child])
        for child in child_list:
            if type(child) == Folder:
                subdirectories.append(child)
                subdirectories.extend(child.get_subdirectories())

        return subdirectories

    def get_name(self):
        return self.name


def create_file_system(terminal_output):
    # read_state='file_navigation' #alternate state=list directory

    current_file_structure = '/'
    file_system = Folder('/', None, None)

    for output in terminal_output:
        output = output.replace('\n', '')
        # print(current_file_structure+'>'+output)
        if output.startswith('$ cd'):
            if output == '$ cd ..':
                if current_file_structure != '/':
                    current_file_structure = current_file_structure[:-1]
                while not current_file_structure.endswith('/'):
                    current_file_structure = current_file_structure[:-1]

            elif output == '$ cd /':
                current_file_structure = '/'
            else:
                new_dir = output.split(' ')[2]
                current_file_structure = current_file_structure+new_dir+'/'
        elif output.startswith('dir '):
            # add directory to file system
            split_dirs = current_file_structure.split('/')
            current_dir = file_system
            for dir in split_dirs:
                if dir != '':
                    current_dir = current_dir.get_child(dir)
            current_dir.add_child(output[4:], None, 'dir')
            pass
        elif '$ ls' not in output:
            # add file to filesystem
            split_dirs = current_file_structure.split('/')
            current_dir = file_system
            for dir in split_dirs:
                if dir != '':
                    current_dir = current_dir.get_child(dir)
            current_dir.add_child(output.split(' ')[1], output.split(' ')[0], 'file')
    return file_system


f = open('input.txt')
terminal_output = f.readlines()
f.close()


file_system = create_file_system(terminal_output)

file_system.get_size()
total_dir_size = 0

subdirectories = file_system.get_subdirectories()
for subdirectory in subdirectories:
    dir_size = subdirectory.get_size()
    if dir_size <= 100000:
        total_dir_size += dir_size
dir_size = file_system.get_size()
if dir_size <= 100000:
    total_dir_size += dir_size
print("The total size of all directories with a size <= 100000 is: "+str(total_dir_size))

minimum_folder_size = dir_size
smallest_folder_name = file_system.get_name()

total_needed_space = 30000000
file_system_size = 70000000
occupied_size = dir_size
free_size = file_system_size-occupied_size
minimum_needed_size = total_needed_space-free_size

for subdirectory in subdirectories:
    dir_size = subdirectory.get_size()
    if dir_size < minimum_folder_size and dir_size >= minimum_needed_size:
        minimum_folder_size = dir_size
        smallest_folder_name = subdirectory.get_name()

print('In order to free up enough space you need to delete directory ' +
      smallest_folder_name+' with a size of: '+str(minimum_folder_size))
