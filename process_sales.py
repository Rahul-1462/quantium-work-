import csv

files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

with open("data.csv", "w", newline="") as out_file:
    writer = csv.writer(out_file)
    writer.writerow(["sales", "date", "region"])

    for file in files:
        with open(file, newline="") as f:
            reader = csv.DictReader(f)

            for row in reader:
                if row["product"] != "pink morsel":
                    continue

                quantity = int(row["quantity"])
                price = float(row["price"].replace("$", ""))
                sales = quantity * price

                writer.writerow([sales, row["date"], row["region"]])
