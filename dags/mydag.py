from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    "start_date": datetime(2019, 7, 10),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG("mydag", default_args=default_args, schedule_interval=timedelta(1))

t1 = BashOperator(task_id="echo1", bash_command="echo 1", dag=dag)
t2 = BashOperator(task_id="echo2", bash_command="echo 2", dag=dag)
t3 = BashOperator(task_id="echo3", bash_command="echo 3", dag=dag)

t2.set_upstream(t1)
t3.set_upstream(t1)
