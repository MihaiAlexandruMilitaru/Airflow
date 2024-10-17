import os

from pyspark.sql import SparkSession

pathDataFolder = os.getenv("DATA_FOLDER")

def count_accidents():
    spark = SparkSession.builder.appName("CountAccidents").getOrCreate()
    df = spark.read.csv(f"{pathDataFolder}/monroe-county-crash.csv", header=True, inferSchema=True, sep=",")
    count = df.count()
    print(f"Number of accidents: {count}")

    f = open(f"{pathDataFolder}/accidents.txt", "w")
    f.write("Number of accidents: " + str(count))
    f.close()

    spark.stop()

count_accidents()