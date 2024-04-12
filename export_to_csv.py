import sys
import re
import csv

regex = re.compile("\[([0-3][0-9]/[0-1][0-9]/2[0-1]), (\d*:\d\d:\d\d [AP]M)\] ([^:]*):(.*)")

if len(sys.argv) < 3:
	print("Usage: export_to_csv.py <exported chat file> <target CSV file>")
	quit()

ctr = 0;
with open(sys.argv[1], "r") as chat:
	out = open(sys.argv[2], 'w', newline='')
	outwriter = csv.writer(out)
	outwriter.writerow(["date","time","sender","text"])
	line = chat.readline()
	while line:
		data = regex.match(line)
		if data:
			date = data[1]
			time = data[2]
			person = data[3].strip().encode("ascii", "ignore").decode()
			if "changed the subject to" in person:
				line = chat.readline()
				continue
			text = data[4].strip()
			ctr += 1
			outwriter.writerow([date, time, person, text])
			if ctr % 1000 == 0:
				print(".", end="", flush=True)
			if ctr % 10000 == 0:
				print("")
		line = chat.readline()
