from matplotlib import pyplot as plt

x_noop = []
y_noop = []
x_sstf = []
y_sstf = []

order_noop = 1
order_sstf = 1
last_sector_noop = None
last_sector_sstf = None
noop_sectors = 0
sstf_sectors = 0
end_noop = False
end_sstf = False

# Read the result.txt file and store the data in the x and y arrays for each algorithm
with open("result2.txt") as file_in:
    lines = []
    # Read the file line by line
    for line in file_in:
        # If the sector limit is reached, stop reading the file
        if end_noop and end_sstf:
            break
        # Separates the sector limits for each algorithm
        elif order_noop > 1000:
            end_noop = True
            if order_sstf > 1000:
                end_sstf = True
        # Get the sector number
        sector = int(line.split()[3])
        # Treats data for NOOP
        if "add" in line and not end_noop:
            x_noop.append(sector)
            y_noop.append(order_noop)
            # Calculates the total sectors traversed by NOOP
            if last_sector_noop is not None:
                noop_sectors += abs(sector - last_sector_noop)
            last_sector_noop = sector
            order_noop += 1
        # Treats data for SSTF
        if "dsp" in line and not end_sstf:
            x_sstf.append(sector)
            y_sstf.append(order_sstf)
            # Calculates the total sectors traversed by SSTF
            if last_sector_sstf is not None:
                sstf_sectors += abs(sector - last_sector_sstf)
            last_sector_sstf = sector
            order_sstf += 1



# Plot the data
plt.clf()
plt.figure(figsize=(5, 15))
plt.plot(x_noop, y_noop, label="NOOP", color="mediumslateblue")
plt.plot(x_sstf, y_sstf, label="SSTF", color="red")
plt.legend()
plt.xlabel("Sector")
plt.ylabel("Order")
plt.title("SSTF vs NOOP")
plt.savefig("plot2.png")


# Print the total sectors traversed for NOOP
print("Total sectors traversed by NOOP:", noop_sectors)
# Print the total sectors traversed for SSTF
print("Total sectors traversed by SSTF:", sstf_sectors)
