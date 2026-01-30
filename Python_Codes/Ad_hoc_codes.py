from pyspark.sql import functions as F
df = spark.table("workspace.salesdb.dim_customers")
df.display()


df = spark.sql("""
    SELECT * FROM workspace.salesdb.dim_customers
    """)
from pyspark.sql import functions as F
df = spark.table("workspace.salesdb.dim_customers")
df.display()


df = spark.sql("""
    SELECT * FROM workspace.salesdb.dim_customers
    """)
