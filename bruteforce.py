import csv


def import_shares_data():
    names = []
    prices = []
    profits = []
    with open('dataForceBrute.csv', newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=';')
        for row in data:
            if row[0] != 'name':
                names.append(row[0])
            if row[1] != 'price':
                prices.append(float(row[1]))
            if row[2] != 'profit':
                profits.append(float(row[2]))
    return names, prices, profits


if __name__ == '__main__':
    names, prices, profits = import_shares_data()
    print(names)
    print(prices)
    print(profits)