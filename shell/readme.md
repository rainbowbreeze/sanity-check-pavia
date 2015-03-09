Deliberatamente 1.0

CONFIGURING THE ENVIRONMENT
from a scratch Ubuntu distro
 apt-get install python-pip
 sudo pip install virtualenv

 cd %projectdir%/shell
 virtualenb build_dir
 source build_dir/bin/activate
 pip install requests beautifulsoup4


TESTS
 pip install nose
 cd tests
 nosetests
 when creating dirs, creates python modules with __init__.py file, otherwise nose will not use them



