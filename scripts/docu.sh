sphinx-apidoc -F -f -H "cimpy" -o "./" "../"
python3 set_inheritance_diagram.py
make html
