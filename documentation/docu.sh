python3 ../setup.py develop
sphinx-apidoc -F -H "cimpy" --separate -o "../documentation" "../" "../setup.py"
python3 set_inheritance_diagram.py
cd ../documentation
make html
