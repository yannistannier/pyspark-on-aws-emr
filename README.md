## PySpark en AWS EMR


### Install python dependencies :

Create requirements.txt file with all depencies and upload to S3 Bucket.


Create depencies.sh file :
```
#!/bin/bash
sudo pip-3.4 install -r https://s3.amazonaws.com/bucket/requirements.txt
``` 

Use EMR’s bootstrap


### Configure EMR with python :

Create configuration.js
```
[
    {
        "Classification": "spark-env",
        "Properties": {},
        "Configurations": [
            {
                "Classification": "export",
                "Properties": {
                    "PYSPARK_PYTHON": "python34"
                },
                "Configurations": []
            }
        ]
    }
]
``` 



### Create cluster with configuration 

Example : 
```
aws emr create-cluster [..config..] --region eu-central-1 --configurations file://configurations.json --bootstrap-action Path="s3://bucket/dependencies.sh"
``` 


### Add step : 

![alt text](https://i1.wp.com/blog.sqreen.io/wp-content/uploads/2017/05/word-image-4.png)


### Acces log 

Go SSH on instance : 
```
ssh -i xxxp.em hadoop@xxxxxx.eu-central-1.compute.amazonaws.com
``` 


Display logs :
```
yarn logs -applicationId <applicationID>
``` 


