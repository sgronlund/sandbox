# Writeup / Notes
## Apache Airflow
### Official Tutorial
- create your DAG definition file, add all code needed
- run using interpreter -> if no exceptions then all should work! (this can be very incorrectly be seen as compiling the config)
    - if succesful just place it in your DAGs folder and you should be able to e.g. test the tasks, this also goes for any code called by your DAG i.e. shell files
- validate
    - airflow db migrate
    - airflow dags list 
    - airflow tasks list YOUR_DAG_NAME
        - air flow tasks list YOUR_DAG_NAME --tree
    - airflow tasks test YOUR_DAG_NAME TASK_TO_TEST DATE is used for testing particular tasks within your DAG
    - airflow dags test YOUR_DAGE_NAME tests the whole DAG :)
- view progress? -> airflow webserver
    - needs an user -> airflow users create ....
- airflow scheduler needs to be running 
- both the scheduler and webserver can be ran as daemons using -D OR you can run everything via airflow standalone
- all tests pass -> backfill
    - queues up X jobs in a span
#### Default Arguments for a DAG
- sla, essentially allows you to set a run-time "limit" for jobs so that an alert is raised if it runs longer than X 
#### Webserver
- IN audit log you can see where the tasks are started from i.e. cli_dag_test means that a user as started the tasks via airflow dags test DAG_NAME
## Links
- https://airflow.apache.org/docs/apache-airflow/stable/tutorial/fundamentals.html
- https://github.com/apache/airflow#installing-from-pypi
- https://airflow.apache.org/docs/apache-airflow/stable/faq.html
- https://airflow.apache.org/docs/apache-airflow/stable/howto/set-config.html#configuring-local-settings
- https://airflow.apache.org/docs/apache-airflow/2.4.3/security/webserver.html
