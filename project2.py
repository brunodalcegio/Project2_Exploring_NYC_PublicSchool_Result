# Re-run this cell 
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Start coding here...

# Which NYC schools have the best math results?
# The best math results are at least 80% of the *maximum possible score of 800* for math.
filter1 = schools[schools['average_math'] >= 640    ]
best_math_schools = filter1[['school_name', 'average_math']].sort_values(by= "average_math", ascending=False) 
print(best_math_schools)

# What are the top 10 performing schools based on the combined SAT scores?
schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]
top_10_schools = schools[["school_name", "total_SAT"]].sort_values(by= "total_SAT", ascending=False).head(10)
print(top_10_schools)

# Which single borough has the largest standard deviation in the combined SAT score?
filter2 = schools.groupby("borough")["total_SAT"].agg(["count", "mean", "std"]).round(2)

# This line below filters by descending value, but keeps several rows saved, unlike the next line.
# largest_std_dev = filtro2.sort_values(by="std", ascending=False)
# this line returns the max value of column std o filtro2 df. 
largest_std_dev = filter2[filter2["std"] == filter2["std"].max()]

largest_std_dev = largest_std_dev.rename(
    columns = {
        "count": "num_schools",
        "mean": "average_SAT",
        "std": "std_SAT"}
)

print(largest_std_dev.reset_index())
