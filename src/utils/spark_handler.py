import os
from functools import cache

from dotenv import load_dotenv
from pyspark import SparkConf
from pyspark.sql import SparkSession


@cache
def get_spark_session():
    load_dotenv()
    AWS_ENDPOINT_URL = "https://s3.bhs.io.cloud.ovh.net"
    AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
    AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")

    conf = SparkConf().setAppName("Spark Places").setMaster("local[*]")
    conf.set("spark.sql.adaptive.enabled", "true")
    conf.set("spark.sql.parquet.filterPushdown", "true")
    conf.set("spark.driver.memory", "30g")
    conf.set("spark.executor.memory", "30g")
    conf.set("spark.executor.pyspark.memory", "30g")
    conf.set("spark.memory.offHeap.enabled", "true")
    conf.set("spark.memory.offHeap.size", "30g")
    conf.set("spark.driver.maxResultSize", "5g")
    conf.set("spark.hadoop.fs.s3a.access.key", AWS_ACCESS_KEY)
    conf.set("spark.hadoop.fs.s3a.secret.key", AWS_SECRET_KEY)
    conf.set("spark.hadoop.fs.s3a.endpoint", AWS_ENDPOINT_URL)
    conf.set("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
    conf.set(
        "spark.hadoop.fs.s3a.aws.credentials.provider",
        "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider",
    )
    conf.set(
        "spark.jars.packages",
        "org.apache.hadoop:hadoop-aws:3.2.2",
    )
    conf.set("spark.sql.parquet.enableVectorizedReader", "false")
    conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")
    conf.set("spark.sql.repl.eagerEval.enabled", "true")
    conf.set("spark.sql.repl.eagerEval.truncate", 100)

    spark = SparkSession.builder.config(conf=conf).getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    return spark