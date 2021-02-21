## Setup - create virtualenv and activate it
    cd celery-redis
    
    # create virtual env
    pipenv install --python 3.8
    
    # activate virtuelenv 
    pipenv shell
    Note that its created in /Users/sheelava/.local/share/virtualenvs/celery-redis-kb0Bn8Kl/bin/python. Add to project interpreter.
    
## Install celery and redis (message broker or a queue where we will add/store tasks)
    
    (do pip install -r requirements.txt)
    pip install -U celery[redis]
    
    pip list
    
    brew install redis
    
## Code with celery and redis

    Create a Celery app by providing (refer to celery_config.py)
            1) it a name  
            2) A broker URL where task can be sent 
            3) code that should be copied by workers (or set of code for each worker)
            
    [Main Application] ----celery----> [write tasks to redis]
    [Celery workers] <----read---- [tasks inside redis]
    

## Run withoutCelery

    python hit_urls_without_celery.py
    (It took overall 11, 7, 32.95052218437195 seconds for 3 runs)
    
## Setup terminals for celery and redis 

    Terminal-1: Start redis server
            redis-server 
            
    Terminal-2: Start 5 celery workers
            celery -A celery_config worker -l info -c 5
            
    Terminal-3: Execute hit_urls.py from celery
            python hit_urls_with_celery.py
            (It took overall < 5 seconds for 3 runs)
            
## Points to note:
    
    1) when putting the task on queue, celery uses the app name (i.e first parm passed to Celery() constructor 
        in celery_config.py)
    2) when starting celery, it gets started with module name (i.e celery_config)