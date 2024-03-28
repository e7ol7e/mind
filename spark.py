from pyspark.sql import SparkSession
from pyspark.sql.functions import lit

def get_product_category_pairs_with_no_category(products_df, categories_df):
    # Переименование колонок для корректного объединения
    products_renamed = products_df.withColumnRenamed("id", "product_id").withColumnRenamed("name", "product_name")
    categories_renamed = categories_df.withColumnRenamed("id", "category_id").withColumnRenamed("name", "category_name")
    
    # Объединение данных по категориям
    product_category_pairs = products_renamed.join(categories_renamed, products_renamed.product_id == categories_renamed.category_id, "left") \
        .select(products_renamed.product_name, categories_renamed.category_name)
    
    # Выбор продуктов без категорий
    products_with_no_category = products_renamed.join(categories_renamed, products_renamed.product_id == categories_renamed.category_id, "left_anti") \
        .select(products_renamed.product_name, lit(None).alias("category_name"))
    
    # Объедидение результатов
    result = product_category_pairs.union(products_with_no_category)
    
    return result

if __name__ == "__main__":
    spark = SparkSession.builder.appName("ProductCategoryPairs").getOrCreate()

    # Пример данных
    products_data = [("product1", 1), ("product2", 2), ("product3", 3)]
    categories_data = [("category1", 1), ("category2", 2)]

    products_df = spark.createDataFrame(products_data, ["name", "id"])
    categories_df = spark.createDataFrame(categories_data, ["name", "id"])

    result_df = get_product_category_pairs_with_no_category(products_df, categories_df)
    result_df.show()

    spark.stop()
