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

    if intersections[0][2] == 'vr':
        intersections.pop(0)
    if intersections[-1][2] == '^g':
        intersections.pop(-1)

    return intersections


def draw_MACD(macd, signal, x0=0, x1=0):
    # Plotting lines
    if x0==0 and x1==0:
        plt.plot(macd, 'b', label="MACD")
        plt.plot(signal, 'r', label="SIGNAL")
    else:
        plt.plot(range(x0, x1), macd[x0 : x1], 'b', label="MACD")
        plt.plot(range(x0, x1), signal[x0 : x1], 'r', label="SIGNAL")

    # Plotting transaction points
    intersections = get_intersections(macd, signal)
    for point in intersections:
        if point[0]>=x0 and point[0]<=x1:
            plt.plot(point[0], point[1], point[2], markersize=8)
    plt.legend(loc='lower right')
    plt.show()


def simulate(intersections, close, start_money=1000):
    pretransaction_money = money = start_money
    amount_bought = 0
    transactions = [0,0] # [successful, failed]

    for point in intersections:
        if(point[0]>=52):
            # Buying
            if point[2]=='^g':
                pretransaction_money = money
                amount_bought = money / close[point[0]]
                money = 0
            # Selling
            else:
                money += amount_bought * close[point[0]]
                amount_bought = 0
                if(money > pretransaction_money):
                    transactions[0] +=1
                else:
                    transactions[1] +=1
                print(f"{point[0]}:\t{pretransaction_money:.2f} -> {money:.2f}")

    print(f"\nTotal transactions: {transactions[0] + transactions[1]}")
    print(f"Profitable transactions: {transactions[0]}")
    print(f"Failed transactions: {transactions[1]}")

    print(f"\nMoney before transactions: {start_money:.2f}")
    print(f"Money after transactions: {money:.2f}")
    print(f"Earnings: {money - start_money:.2f}")
    print(f"Profit [%]: {money / start_money * 100:.2f}")
    return money


def main():
    filename = "./data/GOLD-USD-1D.csv"
    close = read_data(filename)

    macd = MACD(close)
    signal = SIGNAL(macd)
    intersections = get_intersections(macd, signal)
    draw_MACD(macd, signal, 0, 200)
    simulate(intersections, close)

    #TODO Wallet graph for showcasing the simulation progress

main()