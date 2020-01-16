python3 ../setup.py develop
sphinx-apidoc -F -f -H "cimpy" -o "../documentation-build" "../"
python3 set_inheritance_diagram.py
cd ../documentation-build
make html
