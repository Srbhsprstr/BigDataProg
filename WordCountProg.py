from pyspark.sql import SparkSession


spark = SparkSession.builder.master("local")\
    .appName("WordCountProg")\
    .config("spark.some.config.option","some-value")\
    .getOrCreate()

sc = spark.sparkContext

worddf = sc.textFile("/home/srbhsprstr/Downloads/textfile.txt")
finaldf = worddf.flatMap(lambda x:x.split(' ')).map(lambda x:(x,1)).reduceByKey(lambda x,y:(x+y))
# print(finaldf.collect())
finaldf.saveAsTextFile("/home/srbhsprstr/Downloads/wordcountprogoutput")




