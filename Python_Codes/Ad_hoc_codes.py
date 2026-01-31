# Reading files from CSV
df = (
    spark.read.option("header", "true")
    .option("inferSchema", "true")
    .csv("/Volumes/workspace/bronze/source_system/source_crm/prd_info.csv")
)
df.display()
