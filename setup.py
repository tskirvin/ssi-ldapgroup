from setuptools import setup
import glob, re, os

## get documentation from README.md
with open("README.md", "r") as fh:
    long_description = fh.read()

## get version from spec file
with open('ssi-ldapgroup.spec', 'r') as fh:
    for line in fh:
        m = re.search("^Version:\s+(.*)\s*$", line)
        if m:
            version = m.group(1)
            break

## get list of files to install
pyfiles = glob.glob(os.path.join('*', '*.py'))
pyfiles = [pyfile[:-3] for pyfile in pyfiles]

scripts = glob.glob(os.path.join('usr/bin/*'))

setup(
    author_email='tskirvin@fnal.gov',
    author='Tim Skirvin',
    description='tools to add/remove users from LDAP groups',
    license='Perl Artistic',
    install_requires=['ldap_groups==2.5.2', 'PyYAML>=3.11'],
    keywords=['ldap_group'],
    long_description_content_type='text/markdown',
    long_description=long_description,
    maintainer_email='tskirvin@fnal.gov',
    maintainer='Tim Skirvin',
    name='ssi-ldapgroup',
    package_dir={'ldapgroup': 'ldapgroup'},
    py_modules=pyfiles,
    scripts=scripts,
    url='https://github.com/tskirvin/ssi-ldapgroup.git',
    version=version
)
