  <h1 align="center">
    Django Personal Site Project
    https://mhas1381.pythonanywhere.com/
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
```
### Project Model Schema :
this is the model schema have been used in this project:
![drawSQL-export-2021-08-23_23_26](https://s24.picofile.com/file/8452681742/130503854_cefc63a6_1466_4164_825a_9f313d521059.png)
