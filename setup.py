from distutils.core import setup
import os

NAME = 'state-server'
VERSION = '0.1'


# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

srcdir = 'state_server'

for dirpath, dirnames, filenames in os.walk(srcdir):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[(len(srcdir)+1):] # Strip "$srcdir/" or "$srcdir\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))


f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
long_description = f.read().strip()
f.close()




setup(name=NAME,
        version=VERSION,
        description='State server',
        long_description=long_description,
        author='Richard Marko',
        author_email='rissko@gmail.com',
        license='BSD',
        package_dir={'state_server': 'state_server'},
        packages=packages,
        scripts=['state_server/state_server'],
        package_data={'state_server': data_files},

        classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Science/Research',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python'],
    )

