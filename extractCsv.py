import csv

with open("ONSPD_FEB_2025_UK_WR.csv", newline="") as csvInfile,open("result.csv", "w", newline="") as csvOutfile:

    reader = csv.DictReader(csvInfile)
    fieldnames = ["postcode", "latitude", "longitude"]
    writer = csv.DictWriter(csvOutfile, fieldnames=fieldnames)
    fieldnames = ["postcode", "latitude", "longitude"]
    writer.writeheader()
    
    count = 0
    for row in reader:
        print(f'Postcode: {row["pcd"]}   latitude: {row["lat"]}   longitude {row["long"]}')
        
        writer.writerow({"postcode": row["pcd"], "latitude": row["lat"], "longitude": row["long"]})
        count = count + 1
        if count == 10:
            break


    


