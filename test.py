# include standard modules
import getopt, sys



unixOptions = "hd:l:t"
gnuOptions = ["help", "data=", "learningRate=", "threshold="]

try:
    arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))
    sys.exit(2)


for currentArgument, currentValue in arguments:
    if currentArgument in ("-h", "--help"):
        print ("displaying help")
    elif currentArgument in ("-d", "--data"):
        print ("data = ", currentValue)
    elif currentArgument in ("-l", "--learningRate"):
        print ("learningRate = ", currentValue)
    elif currentArgument in ("-t", "--threshold"):
        print ("threshold = ", currentValue)