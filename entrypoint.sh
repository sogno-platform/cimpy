#!/bin/sh

if [ -n "${GITHUB_WORKSPACE}" ];
then
    cd documentation
    ./docu.sh --release
    cp -a ${GITHUB_WORKSPACE}/documentation/_build/html ${GITHUB_WORKSPACE}/built_documentation
fi
