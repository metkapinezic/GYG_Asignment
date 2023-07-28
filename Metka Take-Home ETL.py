# Databricks notebook source
# MAGIC %sql
# MAGIC -- creating an empty table where i want to store the clean data 
# MAGIC
# MAGIC CREATE OR REPLACE TABLE main.clean.films_dataset (
# MAGIC     id INT PRIMARY KEY,
# MAGIC     title STRING,
# MAGIC     director STRING,
# MAGIC     release_year INT,
# MAGIC     genre STRING,
# MAGIC     rating FLOAT,
# MAGIC     gross FLOAT,
# MAGIC     streaming_service STRING
# MAGIC );

# COMMAND ----------

# MAGIC %sql
# MAGIC -- generating unique ids
# MAGIC
# MAGIC CREATE OR REPLACE TEMPORARY VIEW imdb_raw_with_id AS
# MAGIC SELECT *, monotonically_increasing_id() AS unique_id
# MAGIC FROM main.raw.imdb_raw;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC -- inserting clean data into an empty table
# MAGIC
# MAGIC INSERT INTO main.clean.films_dataset 
# MAGIC SELECT
# MAGIC     ROW_NUMBER() OVER (ORDER BY im.unique_id) AS id,
# MAGIC     im.title,
# MAGIC     im.director,
# MAGIC     REGEXP_REPLACE(im.release_year, '[^0-9]', '') AS release_year_int,
# MAGIC     im.genre,
# MAGIC     im.rating,
# MAGIC     CAST(
# MAGIC         CASE
# MAGIC             WHEN gross LIKE '%$%M' THEN REPLACE(REPLACE(gross, '$', ''), 'M', '')::FLOAT * 1000000
# MAGIC             ELSE gross::FLOAT
# MAGIC         END
# MAGIC     AS FLOAT) AS gross_numeric,
# MAGIC     CASE
# MAGIC         WHEN ap.show_id IS NOT NULL AND nf.show_id IS NOT NULL THEN 'Amazon Prime, Netflix'
# MAGIC         WHEN ap.show_id IS NOT NULL THEN 'Amazon Prime'
# MAGIC         WHEN nf.show_id IS NOT NULL THEN 'Netflix'
# MAGIC         ELSE 'null'
# MAGIC     END AS streaming_service
# MAGIC FROM
# MAGIC     imdb_raw_with_id AS im
# MAGIC LEFT JOIN
# MAGIC     main.raw.amazon_prime_titles AS ap ON im.title = ap.title
# MAGIC LEFT JOIN
# MAGIC     main.raw.netflix_titles AS nf ON im.title = nf.title;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM main.clean.films_dataset 
