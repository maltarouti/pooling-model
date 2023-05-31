# Pooling Model
A very simple python API to apply short-pooling and long-pooling

# How to run?
* Install python in your machine
* Install Python libraries using `pip install -r requirements.txt`
* Run the program by using `python short_pooling.py` or `python long_pooling.py`
* Create a new job by executing this command `curl http://localhost:8000/create_new_job`
* Keep **pooling** using this command to check the status of the job till it reaches 100% `curl http://localhost:8000/check_status?job_id=job_id`
