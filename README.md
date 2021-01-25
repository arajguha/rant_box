### RantBox

#### Steps to run locally 

>Note:  Using Anaconda for virtual environment creation. Feel free to use virtualenv or something like that.

- Download [Anaconda ](https://docs.anaconda.com/anaconda/user-guide/getting-started/)  
- Open Anaconda prompt
- Use command `conda create --name RantBox py=3.8` This will create a new virtual environment and also install pip and other useful packages in the environment.
- Next use command `conda activate RantBox`to activate the envrionment
- Navigate to the project root directory
- Run `pip install -r requirements.txt` to install the python packages used in the project.
> Note: `pip install <package>` or `conda install <package>` can be used to seperately install packages if needed.

After the installations are complete, run the following commands.
- `python manage.py makemigrations`
- ` python manage.py migrate`

> The above two commands will run the database migration.

After database migrations are complete. Create a new superuser for the django admin panel.

- Run `python manage.py createsuperuser` and enter username, password as asked.
-  Finally run `python manage.py runserver` to start the development server on default port(8000)
> To start the dev server on a custom port
>  use `python manage.py runserver <port_no>`

Now that the development server has started, open up a browser and enter the url
http://localhost:port/admin  and enter the superuser credentials to enter the admin panel.


