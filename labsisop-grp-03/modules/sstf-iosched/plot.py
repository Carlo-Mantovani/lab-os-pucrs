from matplotlib import pyplot as plt

x_fifo = []
y_fifo = []
x_sstf = []
y_sstf = []

ycount = 1
last_sector_fifo = None
last_sector_sstf = None
fifo_sectors = 0
sstf_sectors = 0

with open("out.txt") as file_in:
    lines = []
    for line in file_in:
        if ycount == 500:
            break
        if "add" in line:
            sector = int(line[line.find("R ") + 2:])
            x_fifo.append(sector)
            y_fifo.append(ycount)
            if last_sector_fifo is not None:
                fifo_sectors += abs(sector - last_sector_fifo)
            last_sector_fifo = sector
            ycount += 1

plt.xlabel('sectors')
plt.ylabel('order')
plt.figure(figsize=(5, 15))
plt.plot(x_fifo, y_fifo)
plt.savefig("outfifo2.png")

# Print the total sectors traversed for FIFO
print("Total sectors traversed by FIFO:", fifo_sectors)

# Reset counters for SSTF
ycount = 1

with open("out.txt") as file_in:
    lines = []
    for line in file_in:
        if ycount == 500:
            break
        if "dsp" in line:
            sector = int(line[line.find("R ") + 2:])
            x_sstf.append(sector)
            y_sstf.append(ycount)
            if last_sector_sstf is not None:
                sstf_sectors += abs(sector - last_sector_sstf)
            last_sector_sstf = sector
            ycount += 1

plt.clf()
plt.xlabel('sectors')
plt.ylabel('order')
plt.plot(x_sstf, y_sstf)
plt.savefig("outsstf2.png")

# Print the total sectors traversed for SSTF
print("Total sectors traversed by SSTF:", sstf_sectors)
