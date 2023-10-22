from matplotlib import pyplot as plt

x_fifo = []
y_fifo = []
x_sstf = []
y_sstf = []

order_fifo = 1
order_sstf = 1
last_sector_fifo = None
last_sector_sstf = None
fifo_sectors = 0
sstf_sectors = 0
end_fifo = False
end_sstf = False

# Read the result.txt file and store the data in the x and y arrays for each algorithm
with open("result.txt") as file_in:
    lines = []
    # Read the file line by line
    for line in file_in:
        # If the sector limit is reached, stop reading the file
        if end_fifo and end_sstf:
            break
        # Separates the sector limits for each algorithm
        elif order_fifo > 1000:
            end_fifo = True
            if order_sstf > 1000:
                end_sstf = True
        # Get the sector number
        sector = int(line.split()[3])
        # Treats data for FIFO
        if "add" in line and not end_fifo:
            x_fifo.append(sector)
            y_fifo.append(order_fifo)
            # Calculates the total sectors traversed by FIFO
            if last_sector_fifo is not None:
                fifo_sectors += abs(sector - last_sector_fifo)
            last_sector_fifo = sector
            order_fifo += 1
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
plt.plot(x_fifo, y_fifo, label="FIFO", color="mediumslateblue")
plt.plot(x_sstf, y_sstf, label="SSTF", color="red")
plt.legend()
plt.xlabel("Sector")
plt.ylabel("Order")
plt.title("SSTF vs FIFO")
plt.savefig("plot.png")


# Print the total sectors traversed for FIFO
print("Total sectors traversed by FIFO:", fifo_sectors)
# Print the total sectors traversed for SSTF
print("Total sectors traversed by SSTF:", sstf_sectors)
