# short-pooling
A very simple python API to apply short-pooling

# How to run?
* Install python in your machine
* Install Python libraries using `pip install -r requirements.txt`
* Run the program by using `python main.py`
* Create a new job by executing this command `curl http://localhost:8000/create_new_job`
* Keep **pooling** using this command to check the status of it `curl http://localhost:8000/check_status?job_id=job_id`