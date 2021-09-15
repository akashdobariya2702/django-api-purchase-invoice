pip3 install --upgrade virtualenv
virtualenv -p python3 ace_env
source ace_env/bin/activate
pip3 install -r requirements.txt
python3 manage.py runserver
