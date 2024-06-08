import csv
with open('data/test.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    with open('data/test_with_id.csv', mode="w", newline='') as write_csv:
        writer = csv.writer(write_csv)
        curr_id = 0
        for row in reader:
            if(curr_id == 0):
                row.insert(0, "id")
            else:
                row.insert(0, curr_id)
            writer.writerow(row)
            curr_id += 1