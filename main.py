import matplotlib.pyplot as plt

def read_data(filename):
    close = []

    file = open(filename, 'r')
    for line in file:
        line = line.split("\t")
        close.append(float(line[4]))
    return close

def debug_data(data):
    for i in range(0, len(data)):
        print(i+1,":\t", data[i])

# EMA values from the first 2N days shouldn't be analyzed as they can be unstable
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

def get_intersections(macd, signal):
    intersections = []
    for i in range(1, len(macd)):
        # Sell Signal - MACD crossing SIGNAL from the top
        if(macd[i-1] > signal[i-1]):
            if(macd[i] < signal[i]):
                intersections.append([i, macd[i], 'vr'])

        # Buy Signal - MACD crossing SIGNAL from the top
        elif (macd[i - 1] < signal[i - 1]):
            if (macd[i] > signal[i]):
                intersections.append([i, macd[i], '^g'])

    return intersections


def draw_MACD(macd, signal, x0=0, x1=0):
    # Plotting lines
    if x0==0 and x1==0:
        plt.plot(macd, 'b')
        plt.plot(signal, 'r')
    plt.plot(range(x0, x1), macd[x0 : x1], 'b')
    plt.plot(range(x0, x1), signal[x0 : x1], 'r')

    # Plotting transaction points
    intersections = get_intersections(macd, signal)
    for point in intersections:
        if point[0]>=x0 and point[0]<=x1:
            plt.plot(point[0], point[1], point[2], markersize=8)
    plt.show()


def main():
    filename = "./data/GOLD-USD-1D.csv"
    close = read_data(filename)

    macd = MACD(close)
    signal = SIGNAL(macd)
    intersections = get_intersections(macd, signal)

    draw_MACD(macd, signal, 0,356)
    plt.show()


main()