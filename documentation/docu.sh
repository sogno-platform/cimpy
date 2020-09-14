python3 ../setup.py develop
sphinx-apidoc -F -H "cimpy" -o "../documentation" "../"
python3 set_inheritance_diagram.py
cd ../documentation
make html
