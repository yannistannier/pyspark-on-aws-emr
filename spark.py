import os
import sys



sc = SparkContext()


#Configuration for region without signature (like Franckfurt)
sc.setSystemProperty("com.amazonaws.services.s3.enableV4", "true")
sc._jsc.hadoopConfiguration().set("com.amazonaws.services.s3.enableV4", "true")
sc._jsc.hadoopConfiguration().set("mapreduce.fileoutputcommitter.algorithm.version", "2")
sc._jsc.hadoopConfiguration().set("speculation", "false")
sc._jsc.hadoopConfiguration().set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
sc._jsc.hadoopConfiguration().set("fs.s3a.fast.upload", "true")
sc._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "s3-eu-central-1.amazonaws.com")


dd = sys.argv[1]
df = sys.argv[1]
myRDD = sc.textFile("s3a://xxxx/"+dd+"/*")

# Script example ...
analyzed = myRDD.map(..)...
# Script example ...

analyzed.saveAsTextFile("s3a://xxxxx/"+df+"/")