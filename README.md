# Airflow data pipeline to automate ETL
	ETL-E-verified-Employer is linked as a submodule to this automation project. 

## Installation (Raspberry pi setup)

	1. Setup Airflow home directory
		export AIRFLOW_HOME = /path/to/my_airflow_directory

 	2. Install py package 
		pip install apache-airflow
	
	3. Initialize SQLite DB
		airflow db init
	
	4. Execute
		airflow webserver -p 8080 & airflow scheduler
