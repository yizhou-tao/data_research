import polars as pl

df = pl.read_csv("/Users/zealot/yizhou/git/data_research/com/silq/canclled_reason.csv")

ctx = pl.SQLContext()
ctx.register("churn", df)

result = ctx.execute("""
SELECT
    *
FROM churn
limit 5
""").collect()

print(result)

result = ctx.execute("""
SELECT
    Reason,
    COUNT(*) AS cnt
FROM churn
GROUP BY Reason
ORDER BY cnt DESC
""").collect()

print(result)