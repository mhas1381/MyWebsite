  <h1 align="center">
    Django Personal Site Project
  </h1>
  <p align="center">The full project for Django fundemental education for my self</p>
  ## Download & Setup Instructions :

After downloading the project, make sure to create a virtual enviroment and  install [project's requirements.](https://github.com/mhas1381/MyWebsite/blob/main/requirements.txt)

Clone the project. This will download the GitHub respository files onto your local machine.

```Shell
git clone https://github.com/alibigdeli/mysite.git
```
installing virtual enviroment and activating:
```Shell
pip install virtualenv
```
Windows setup:
```Shell
#creating the enviroment
python -m venv venv

#activating the enviroment
venv\Scripts\activate

#deactivating enviroment
deactivate
```
Linux and Mac setup:
```Shell
#creating the enviroment
python -m venv venv

#activating the enviroment
source venv/bin/activate

#deactivating enviroment
deactivate
```

then installing the requirements:

```Shell
pip install -r requirements.txt
```
### Running the Project
in order to run the project you need to use either ways below

default and development settings
```Shell
python manage.py runserver 
#or
python manage.py runserver 0.0.0.0:8000 --settings=mysite.setting.dev
```
production settings
```Shell
python manage.py runserver 0.0.0.0:8000 --settings=mysite.setting.prod

