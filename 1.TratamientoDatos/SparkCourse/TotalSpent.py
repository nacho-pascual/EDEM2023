from pyspark.sql import SparkSession
from pyspark.sql import functions as func
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

spark = SparkSession.builder.appName("TotalSpent").getOrCreate()

schema = StructType([ \
                     StructField("clientID", StringType(), True), \
                     StructField("productID", StringType(), True), \
                     StructField("€", FloatType(), True)])

# // Read the file as dataframe
total_spent = spark.read.schema(schema).csv("file:/Users/nachopascualrodriguez/Desktop/SparkCourse/customer-orders.csv")
total_spent.printSchema()


# Aggregate to find minimum temperature for every station

total_spent_bycustomer= total_spent.groupBy("clientID").agg(func.round(func.sum("€"), 2)
  .alias("Total_spent_perclient")).sort("clientID")

total_spent_bycustomer_sorted = total_spent_bycustomer.sort("Total_spent_perclient",ascending=False)

total_spent_bycustomer_sorted.show()

total_spent_bycustomer_sorted.show(total_spent_bycustomer_sorted.count())


spark.stop()