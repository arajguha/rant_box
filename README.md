### RantBox

#### Steps to run locally 

>Note:  Using Anaconda for virtual environment creation. Feel free to use virtualenv or something like that.

- Download [Anaconda ](https://docs.anaconda.com/anaconda/user-guide/getting-started/)  

> [Anaconda Cheatsheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

- Open Anaconda prompt
- Use command `conda create --name RantBox python=3.8` This will create a new virtual environment and also install pip and other useful packages in the environment.
- Next use command `conda activate RantBox`to activate the envrionment
- Navigate to the project root directory
- Run `pip install -r requirements.txt` to install the python packages used in the project.
> Note: `pip install <package>` or `conda install <package>` can be used to seperately install packages if needed.

**Note:**  Django needs a secret key. Inside the .env file set  a value for 				DJANGO_SECRET_KEY .
> DJANGO_SECRET_KEY='put_your_secret_key_here'

**Location of .env file: /project-root/rant_box/**

The secret key can be generated locally or from [here](https://miniwebtool.com/django-secret-key-generator/) 

After the installations are complete,  run the database migrations. But before that the DB needs to be configured.

#### Log Directory
Add a directory in the project root and name it "log".

#### Steps for using DB locally
PostgreSQL is used. It can be installed from [here](https://www.postgresql.org/). 
For quick local setup, use sqlite DB. 

Following are the steps to change the DB to sqlite DB which will run in memory.

In settings.py in the root directory change the Database settings. The current DB settings is:  
	
	
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.postgresql_psycopg2',
			'NAME': os.getenv('DB_TABLE'),
			'HOST': os.getenv('DB_HOST'),
			'PORT': os.getenv('DB_PORT'),
			'USER': os.getenv('DB_USER'),
			'PASSWORD': os.getenv('DB_PASSWORD')
		}

	}
 

Change it to :

	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': BASE_DIR / 'db.sqlite3',
		}
	}
 
Next run Database migrations with the following commands
- `python manage.py makemigrations`
- ` python manage.py migrate`


After database migrations are complete. Create a new superuser for the django admin panel.

- Run `python manage.py createsuperuser` and enter username, password as asked.

Finally, 
Run `python manage.py runserver` to start the development server on default port(8000)
> To start the dev server on a custom port
>  use `python manage.py runserver <port_no>`




