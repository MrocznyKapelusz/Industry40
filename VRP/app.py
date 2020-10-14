import csv






def main():
    with open('data/PL.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        # for row in spamreader:
        #     print(', '.join(row))
        data = list(spamreader)
        print(str(data))

if __name__ == "__main__":
    main()