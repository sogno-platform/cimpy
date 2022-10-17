FROM fedora:29

LABEL \
	org.label-schema.schema-version = "1.0" \
	org.label-schema.name = "cimpy" \
	org.label-schema.license = "Mozilla Public License Version 2.0" \
	org.label-schema.vendor = "Institute for Automation of Complex Power Systems, RWTH Aachen University" \
	org.label-schema.author.name = "Jan Dinkelbach" \
	org.label-schema.author.email = "acs-software@eonerc.rwth-aachen.de" \
	org.label-schema.vcs-url = "https://git.rwth-aachen.de/acs/public/cim/cimpy"


RUN dnf -y update

RUN dnf -y install \
	make \
	python3-pip \
	graphviz-devel

RUN dnf --refresh -y install \
	python3-devel

RUN pip3 install sphinx_rtd_theme

RUN pip3 install sphinx

RUN pip3 install pytest

RUN pip3 install pytest-check

ADD . /cimpy

WORKDIR /cimpy

RUN python3 setup.py install
