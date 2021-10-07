import csv
import sys

def main():

    # Ensure correct usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit()

    # Open csv file and convert to dict
    with open(sys.argv[1], "r") as cfile:
        reader = csv.DictReader(cfile)
        dict_list = list(reader)
    # Open sequences file and convert to list
    with open(sys.argv[2], "r") as file:
        sequence = file.read()
    # For each STR, compute longest run of consecutive repeats in      sequence
    max_counts = []
    for i in range(1, len(reader.fieldnames)):
        STR = reader.fieldnames
        STR_count = 0
        Count = 0
        

    # Loop through sequence to find STR
        j=0
        while(j<len(sequence)):

        # If match found, start counting repeats
            if sequence[j:(j + len(STR))] == STR:
                STR_count+=1
                j+=len(STR)  # incrementing i with the length of STR so that
            else:
                STR_count=0
                j+=1

            if STR_count> Count:
                Count = STR_count

        max_counts.append(Count)
        

    # Compare against data
    for i in range(len(dict_list)):
        match = 0
        for j in range(1, len(reader.fieldnames)):
            if int(max_counts[j-1]) == int( dict_list[i] [ reader.fieldnames[j] ] ):
                match+=1
        if match == (len(reader.fieldnames) - 1):
            print(dict_list[i]['name'])
            exit(0)
               
    print("No match")

if __name__ == "__main__":
    main()
