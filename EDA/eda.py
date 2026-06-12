import pandas as pd

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"

columns = [
    "pregnancies",
    "glucose",
    "blood_pressure",
    "skin_thickness",
    "insulin",
    "bmi",
    "diabetes_pedigree",
    "age",
    "outcome"
]

suspicious_columns = [
   "glucose",
   "blood_pressure",
   "skin_thickness",
   "insulin",
   "bmi" 
]

df = pd.read_csv(url, names=columns)

print("=== SHAPE (rows, columns) ===")
print(df.shape)

print("\n=== FIRST 5 ROWS ===")
print(df.head())

print("\n=== DATA TYPES ===")
print(df.dtypes)

print("\n=== BASIC STATISTICS ===")
print(df.describe())

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

print("\n=== LABEL DISTRIBUTION ===")
print(df["outcome"].value_counts())

print("\n === SUSPICIOUS ZEROS (hidden missing values) ===")
for col in suspicious_columns:
    zero_count = (df[col] == 0).sum()
    percentage = (zero_count / len(df)) * 100
    print(f"{col:<20} zeros: {zero_count} ({percentage:.1f}%)")

