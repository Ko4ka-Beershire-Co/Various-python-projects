import glob

read_files = glob.glob("*.ass")

with open("BIG_FILE.ass", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
