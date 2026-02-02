# Reading files from CSV
df = (
    spark.read.option("header", "true")
    .option("inferSchema", "true")
    .csv("/Volumes/workspace/bronze/source_system/source_crm/prd_info.csv")
)
df.display()
df = (
    spark.read.option("header", "true")
    .option("inferSchema", "true")
    .csv("/Volumes/workspace/bronze/source_system/source_crm/sales_details.csv")
)
df.display()
# Writing to Bronze Layer
df.write.mode("overwrite").saveAsTable("bronze.crm_prd_info")
df.write.mode("overwrite").saveAsTable("bronze.crm_sales_details")
df = (
    spark.read.option("header", "true")
    .option("inferSchema", "true")
    .csv("/Volumes/workspace/bronze/source_system/source_crm/sales_details.csv")
)
df.display()
# Writing to Bronze Layer
df.write.mode("overwrite").saveAsTable("bronze.crm_prd_info")
df.write.mode("overwrite").saveAsTable("bronze.crm_sales_details")
