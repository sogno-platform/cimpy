import setuptools

setuptools.setup(
   name = 'cimpy',
   version = '1.0.0',
   description = 'Python package for import, modification and export of CIM grid data',
   author = 'Institute for Automation of Complex Power Systems',
   author_email = 'acs-software@eonerc.rwth-aachen.de',
   include_package_data=True,
   license = 'MPL-2.0',
   packages = setuptools.find_packages(),
   install_requires = [
       'lxml',
       'xmltodict',
       'chevron',
   ]
)
