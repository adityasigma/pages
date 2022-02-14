# CRUD Application
CRUD Application is python program in which u can perform POST, DELETE, GET, PUT action on user model using homepage and you can see logs related to your actions which you performed using Homepage and NOT Django-admin panel.

## Installation


First Create Virtual environment in python 3.8 using following command in powershell if use windows operating system and Terminal if use Linux or MacOS .


```bash
pip3 install virtualenv
python3 -m venv myenv
```

Change directory where your virtual environment is placed and use this command to activate virtual environment.

For Windows:

```bash
.\myenv\Scripts\activate
```
For Linux and MacOS:

```bash
source myenv/bin/activate
```

Change directory to Project folder and use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt file make sure u install this file inside python virtual environment.

```bash
pip install -r requirements.txt
```

## Usage

inside Project directory which contain manage.py file use this command in terminal/powershell to run localhost server make sure your virtual environment is on.


```python
python manage.py runserver
```

open your chrome or Firefox browser and go on to [localhost](http://localhost:8000) on 8000 port and you can perform CRUD operations on users using POST, DELETE, GET, PUT tabs  given on homepage and to see logs related to CRUD operations from homepage click on log tab. 


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
