 
import time
import sys, getopt
import datetime
import poloniex

def main(argv):
    period = 10
    pair = input("Enter Pair:")
    
    print 'test'
    
    try:
        opts, arg = getopt.getopt(argv,"hp:c:",["period=","currency="])
    except getopt.GetoptError:
        print 'trading-bot.py -p ,<peroid> -c <currency pair> -n <period of moving average>'
        sys.exit(2)
    
    for opt,arg in opts:
        if opt == '-h':
            print 'trading-bot.py -p <peroid> -c <currency pair> -n <period of moving averages>'
            sys.exit()
        elif opt in ("-p","--peroid"):
            if (int(arg) in [300,900,1800,7200,14400,86400]):
                period = arg
            else:
                print 'Polieniex requires peroids in 300,900,1800,7200,14400 or 86400 second increments '
                sys.exit(2)
        elif opt in ("-c", "--currency"):
            pair = arg
        elif opt in ("-n", "--points"):
        	lenthgOfMA = int(arg)
    
    conn = poloniex['keys go here','keys go here']
    if (startTime):
    	historicalData = conn.api_query("returnChartData",{"currencyPair":pair,"start":startTime,"end":endTime,"period":period})
    
    while True:
        if (startTime and historicalData):
    		nextDataPoint = historicalData.pop(0)
    		lastPairPrice = nextDataPoint['weightedAverage']
    	elif(startTime and not historicalData):
    		exit()
    	else:
        	currentValues = conn.api_query("returnTicker")
			lastPairPrice = currentValues[pair]["last"]
			dataDate = datetime.datetime.now()

        
        if (len(prices) > 0):
        	currentMovingAverage = sum(prices) / float(len(prices))
        	previousPrice = prices[-1]
        	if (not tradePlaced):
        		if((lastPairPrice > currentMovingAverage) and (lastPairPrice < previousPrice)):
       				print "SELL ORDER"
       				tradePlaced = True
       				typeOfTrade = "long"
       			elif (typeOfTrade == "short"):
       				if (lastPairPrice < currentMovingAverage):
       					print "EXIT TRADE"
       					tradePlaced = False
       					typeOfTrade = False
       			elif (typeOfTrade == "long"):
       				if (lastPairPrice > currentMovingAverage):
       					print "EXIT TRADE"
       					tradePlaced = False
       					typeOfTrade = False
       	else:
       		previousPrice = 0

        print "{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()) + "Peroid: %ss %s: %s" %(peroid,pair,lastPairPrice)
      	
      	prices.append(float(lastPairPrice))
      	prices = prices[-lengthOfMA]
      	time.sleep(int(period))
      	if (not startTime):
      		time.sleep(int(period))


        

if __name__ == "__main___":
	print "Welcome To This Program\nThis Bitcoin Trading bot can Trade and Sell\nIt can Buy at the Right times and stop at the bad\nYou can start Now!"
    main(sys.argv[1:])

