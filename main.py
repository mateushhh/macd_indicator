import matplotlib.pyplot as plt

def read_data(filename):
    global data_length
    close = []

    file = open(filename, 'r')
    for line in file:
        line = line.split("\t")
        close.append(float(line[4]))
    return close

def debug_data(data):
    for i in range(0, len(data)):
        print(i+1,":\t", data[i])

def EMA(n, data):
    ema = []
    alfa = 2/(n+1)

    for i in range(0, len(data)):
        if(i==0):
            ema.append(data[i])
        #elif(i<=n):
        #    ema.append(sum(data[0:i])/i)
        else:
            ema.append(alfa * data[i] + (1 - alfa) * ema[i-1])
    return ema


# MACD values from the first 2N days (2*26=52) shouldn't be analyzed as they can be unstable
def MACD(close):
    macd = []
    ema12 = EMA(12, close)
    ema26 = EMA(26, close)

    for i in range(0, len(close)):
        macd.append(ema12[i] - ema26[i])
    return macd

def SIGNAL(macd):
    signal = EMA(9, macd)
    return signal

def main():
    filename = "./data/GOLD-USD-1D.csv"
    close = read_data(filename)
    #debug_data(close)


    #ema26 = EMA(26, close)
    #print(ema26)
    #plt.plot(range(0, 500), ema26[0:500])
    #plt.plot(range(0, 500), close[0:500])


    macd = MACD(close)
    signal = SIGNAL(macd)
    #print(macd)
    #print(signal)
    plt.plot(range(50, 150), macd[50: 150])
    plt.plot(range(50, 150), signal[50: 150])
    plt.show()

main()