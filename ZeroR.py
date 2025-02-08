import sys
import random

def read_last_column(file_name):
    options = []
    with open(file_name, 'r') as file:
        next(file)  # Skip the header
        for line in file:
            last_element = line.strip().split(',')[-1]
            options.append(last_element)
    return options

def zeroR(options):
    yes_count = options.count('yes')
    no_count = options.count('no')
    return "yes" if yes_count > no_count else "no"

def randR(options):
    return random.choice(options)

if __name__ == '__main__':
    classify_type = "-z"
    if len(sys.argv) < 2:
        print("Usage:  classify {-z|-r} file")
        sys.exit(-1)
    if len(sys.argv) == 3:
        classify_type = sys.argv[1]
        if classify_type != "-z" and classify_type != "-r":
            print("Usage:  classify {-z|-r} file")
            sys.exit(-1)
    fname = sys.argv[-1]

    options = read_last_column(fname)
    majority_vote = zeroR(options) if classify_type == "-z" else randR(options)

    # Calculate and print accuracy
    correct_predictions = sum(1 for option in options if option == majority_vote)
    accuracy = correct_predictions / len(options)
    print(f"Prediction: {majority_vote}, Accuracy: {accuracy:.2f}")