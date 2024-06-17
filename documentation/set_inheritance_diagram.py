from os import remove
import os
from tempfile import mkstemp
from shutil import move

directory = os.path.abspath(os.path.join("..", "documentation"))

# if 'conf.py' in os.listdir(directory):
#     conf_file = os.path.abspath(os.path.join(directory, 'conf.py'))
#     real_conf_file = os.path.abspath('real_conf.py')
#     remove(conf_file)
#     copy(real_conf_file, conf_file)
#
# if 'index.rst' in os.listdir(directory):
#     index_file = os.path.abspath(os.path.join(directory, 'index.rst'))
#     real_index_file = os.path.abspath('real_index.rst')
#     remove(index_file)
#     copy(real_index_file, index_file)


for file in os.listdir(directory):
    if file.endswith(".rst"):
        file_path = os.path.abspath(file)
        fh, abs_path = mkstemp()
        found_inheritance = False
        with open(fh, "w") as new_file:
            with open(os.path.join(directory, file)) as old_file:
                for line in old_file:
                    if "undoc-members" in line:
                        continue
                    else:
                        if "automodule" in line:
                            name = line.split("::")[1]
                        if "show-inheritance" in line:
                            new_file.write("\nInheritance Diagram:\n")
                            new_file.write('""""""""""""""""""""\n')
                            new_file.write(".. inheritance-diagram:: " + name)
                            new_file.write("    :parts: 1\n")
                            new_file.write("")
                            new_file.write("")
                            found_inheritance = True
                        else:
                            new_file.write(line)

        if found_inheritance:
            remove(os.path.join(directory, file))
            move(abs_path, os.path.join(directory, file))
