# BigDataProg
This is a simple Word count program using Pyspark in which we are counting occurances of each word and saving it as a text file in a specified directory.
type of file -- text file from which we are reading the data
In text file, per line input is considered as a record
we are creating a sparksession and then loading a text file from a location into a RDD.
Using flatMap, Map and reduceByKey methods, we are counting the number of occurances of each word in the file
FlatMap --  It is used to make the multiple line records to a single record.
Map -- It is used to map anything per word, in this case, we are mapping 1 to each word(initiating count from 1)
reduceByKey -- it is used to add all the values of same keys across the data.
