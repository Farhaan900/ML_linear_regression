"""
@author : Mohammed Farhaan Shaikh
@email : mfarhaan.shaikh95@gmail.com

Machine leaning linear regression model using gradient descent
"""
import sys, getopt
import numpy as np
import csv
from decimal import Decimal


''' reads the csv file and returns the data '''
def read_csv(csv_name):

    data = np.genfromtxt(csv_name, delimiter=",")
    return data


''' returns the prediction for curent weights '''
def calculate_outputs(data, weights):

    x = data[:, :len(data[0])-1]
    pred_y = x * weights
    pred_y = list(map(sum, pred_y))
    # print(pred_y)
    return pred_y


''' returns the su, of squared errors '''
def sum_of_squared_errors(data, prediction):

    y = (data[:, len(data[0])-1:]).ravel()
    # print("NEW")
    y = y - prediction
    y = y * y
    total = round(np.sum(y), 4)
    # print ("sum of squared errors = ", total)
    return total


''' calculates gradient '''
def calculate_gradient(data, prediction):

    gradients = []
    y = data[:, len(data[0]) - 1:].ravel()
    z = y - prediction

    for x in range (len(data[0])-1):
        z1 = z * (data [:, x:x+1]).ravel()
        total = np.sum(z1)
        # print("W", x, " = ", (0 + (0.0001 * total)))
        # print (total)
        gradients.append(total)

    return gradients


''' calculates and returns new weights '''
def recalculate_weights(weights, gradients, learning_rate):

    new_weights = weights + [x*learning_rate for x in gradients]
    return new_weights


''' writes data to the csv file '''
def write_to_csv(data, csv_name):

    with open(csv_name, mode='a') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,
                                     lineterminator='\n')
        employee_writer.writerow(data)


''' generates a name for the csv file '''
def generate_csv_name(data, learning_rate, threshold):

    name = data[:-4]+"_eta"+str(learning_rate)+"_thres"+str(threshold)+".csv"
    return name


def main(argv):

    file_name = "random.csv"
    learning_rate = 0.000
    threshold = 0.000

    unix_options = "hd:l:t"
    gnu_options = ["help", "data=", "learningRate=", "threshold="]

    try:
        arguments, values = getopt.getopt(argv, unix_options, gnu_options)
    except getopt.error as err:
        # output error, and return with an error code
        print(str(err))
        print("linearregr.py --data <PathToData> --learningRate <LearningRate> --threshold <Threshold>")
        sys.exit(2)

    if len(arguments) < 1:
        print("Use this format")
        print("linearregr.py --data <PathToData> --learningRate <LearningRate> --threshold <Threshold>")
        sys.exit(2)

    for currentArgument, currentValue in arguments:
        if currentArgument in ("-h", "--help"):
            print("linearregr.py --data <PathToData> --learningRate <LearningRate> --threshold <Threshold>")
            sys.exit()
        elif currentArgument in ("-d", "--data"):
            file_name = currentValue
        elif currentArgument in ("-l", "--learningRate"):
            learning_rate = float(currentValue)
        elif currentArgument in ("-t", "--threshold"):
            threshold = float(currentValue)

    output_file_name = generate_csv_name(file_name,learning_rate,threshold)
    #print(output_file_name)

    # print(threshold)
    data = read_csv(file_name)
    # adding 1 to all the records to represent x0 to help make the code simple
    data = np.concatenate((np.ones((len(data),1), dtype=float), data), axis=1)
    # print(data)

    ''' initializing the weight matrix with 0s '''
    weights = np.zeros((len(data), len(data[0])-1), dtype=float)
    # print(weights)

    previous_squared_error = 0

    print("Running...")

    for x in range(sys.maxsize):

        prediction = calculate_outputs(data, weights)
        # print(prediction)

        sose = sum_of_squared_errors(data, prediction)
        # print(x, " Sum of squared errors = ", sose)

        ''' Creating list which is sent to be stored in a csv file '''
        out_list = [x]
        for w in weights[0]:
            out_list.append(round(w,4))
        out_list.append(sose)

        # print(out_list)

        write_to_csv(out_list, output_file_name)

        ''' End of execution as squared errors reached the threshold '''
        if(abs(round(sose - previous_squared_error, 4))) < threshold:
            # print(sose - previous_squared_error)
            # print(round(0.0005 - 0.0004 , 4))
            break
        previous_squared_error = sose
        # print(sose)

        gradients = calculate_gradient(data, prediction)
        # print ("gradients = ", gradients)

        weights = recalculate_weights(weights, gradients, learning_rate)
        # print(weights)

    # prediction = calculate_outputs(data, weights)
    # sose = sum_of_squared_errors(data, prediction)

    print ("\nExecution complete.\nOutput stored in >> ",output_file_name)

if __name__ == '__main__':
    main(sys.argv[1:])
