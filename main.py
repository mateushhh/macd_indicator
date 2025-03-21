date = []
close = []
data_length = 0

macd = []
signal = []

def read_data(filename):
    global data_length
    data_length = 0
    date.clear()
    close.clear()

    file = open(filename, 'r')
    for line in file:
        line = line.split("\t")
        date.append(line[0])
        close.append(float(line[4]))
        data_length += 1

def debug_data():
    for i in range(0, data_length):
        print(i+1,":\t", date[i],"\t",close[i])

def EMA(n, i, data, depth=0):
    alfa = 2/(n+1)

    if i == 0:
        return data[0]
    elif i < n:
        return sum(data[0:i+1]) / (i+1)
    else:
        if depth == n:
            return alfa*data[i]
        return alfa*data[i] + (1-alfa) * EMA(n, i-1, data, depth+1)

# MACD values from the first 26 days shouldn't be analyzed as it is highly unstable
def MACD(i):
    return EMA(12,i, close) - EMA(26, i, close)

def SIGNAL(i):
    return EMA(9, i, macd)

def calculate_MACD():
    macd.clear()
    for i in range(0, data_length):
        macd.append(MACD(i))

def calculate_SIGNAL():
    signal.clear()
    for i in range(0, data_length):
        signal.append(SIGNAL(i))

def main():
    filename = "./data/GOLD-USD-1D.csv"
    read_data(filename)
    #debug_data()

    calculate_MACD()
    calculate_SIGNAL()

    #print(macd)
    #print(signal)

main()