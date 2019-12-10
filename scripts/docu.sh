sphinx-apidoc -F -f -H "cimpy" -o "../documentation" "../"
python3 set_inheritance_diagram.py
cd ../documentation
make html
