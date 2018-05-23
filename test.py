"""
This is the "front door" of your application which gets submitted
to Spark and serves as the starting point. If you needed to
implement a command-line inteface, for example, you'd invoke the
setup from here.
"""

from pyspark import SparkContext,SparkConf
from pyspark.sql import HiveContext

if __name__ == '__main__':
    
    sc = SparkContext()
    sqlContext = HiveContext(sc)
    my_dataframe = sqlContext.sql("SELECT * FROM default.web_logs LIMIT 20")
    #my_dataframe = sqlContext.sql("show databases")
    my_dataframe.show()
