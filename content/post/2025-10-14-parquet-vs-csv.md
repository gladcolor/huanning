---
title: Parquet format may be faster than CSV
date: '2025-10-14T20:33:31-05:00'
summary: I use CSV file for a long time to process a lot of tabular data. However, one of my recent project need to extract
  rows from a large parquet table. After a few testing, I found that DuckDB can speed up my work by about 5 times. I recommend
  to try Parquet and DuckDB if […]
original: https://gladcolor.wordpress.com/2025/10/14/parquet-format-may-be-faster-than-csv/
wordpress_id: 58
aliases:
- /post/parquet-format-may-be-faster-than-csv/
---

I use CSV file for a long time to process a lot of tabular data. However, one of my recent project need to extract rows from a large parquet table. After a few testing, I found that DuckDB can speed up my work by about 5 times. I recommend to try Parquet and DuckDB if you need a fast processing.
