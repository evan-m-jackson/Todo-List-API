# ToDo List API

## Setup

The first thing is to clone the repository:

        $ git clone https://github.com/evan-m-jackson/Todo-List-API.git
        $ cd Todo-List-API

Then create a virtual environment and activate it:

        $ pip install virtualenv
        $ virtualenv myenv
        $ source myenv/bin/activate

Next install dependencies:
    
        (env)$ pip install -r requirements.txt

Once dependencies are installed, navigate to the todo folder and run the server (Note server is running on port 8000):
    
        (env)$ cd todo
        (env)$ python manage.py runserver
