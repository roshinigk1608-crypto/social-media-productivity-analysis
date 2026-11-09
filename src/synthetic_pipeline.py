import pandas as pd

# Generate synthetic student data
data = {
    "student_id": [1, 2, 3, 4, 5],
    "social_media_hours": [2, 3, 5, 7, 8],
    "productivity_score": [9, 8, 7, 5, 4]
}

df = pd.DataFrame(data)

# Validate dataset
assert not df.empty
assert df["social_media_hours"].notna().all()
assert df["productivity_score"].between(1, 10).all()

# Save synthetic dataset
df.to_csv("synthetic_data.csv", index=False)

print("Synthetic pipeline test passed!")
print("Number of records:", len(df))
print(df.describe())
