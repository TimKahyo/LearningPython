import csv

# Create a dummy 'csv_file.txt' and write some test data
with open("csv_file.txt", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Phone", "Role"])
    writer.writerow(["John Doe", "555-1234", "Manager"])
    writer.writerow(["Jane Smith", "555-5678", "Developer"])

# Read from 'csv_file.txt'
with open("csv_file.txt", "r") as f:
    csv_f = csv.reader(f)
    # Skip header
    next(csv_f)
    for row in csv_f:
        name, phone, role = row
        print("Name: {}, Phone: {}, Role: {},".format(name, phone, role))

# Writing 'hosts.csv' (this part is okay)
hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]
with open("hosts.csv", "w", newline="") as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)

# Create a dummy 'software.csv' for reading
with open("software.csv", "w", newline="") as software_csv:
    writer = csv.DictWriter(software_csv, fieldnames=["name", "users"])
    writer.writeheader()
    writer.writerow({"name": "Office Suite", "users": "100"})
    writer.writerow({"name": "Antivirus", "users": "50"})

# Reading from 'software.csv'
with open("software.csv", "r") as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(("{} has {} users").format(row["name"], row["users"]))

# Writing 'by_department.csv' (this part is okay)
users = [
    {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
    {
        "name": "Lio Nelson",
        "username": "lion",
        "department": "User Experience Research",
    },
    {"name": "Charlie Grey", "username": "greyc", "department": "Development"},
]
keys = ["name", "username", "department"]

with open("by_department.csv", "w", newline="") as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
