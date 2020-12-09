if [ "$1" = "--release" ] || [ "$1" == "" ]; then
    python3 ../setup.py develop
    sphinx-apidoc -F -H "cimpy" --separate -o "../documentation" "../" "../setup.py"
    python3 set_inheritance_diagram.py
    if [ "$1" = "--release" ] ; then
        make html
    else
        make text
    fi
else
    echo "Usage: $0 [--release]"
fi
