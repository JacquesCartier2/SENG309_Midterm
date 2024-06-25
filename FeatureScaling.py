import pandas as pd

def csv_to_list(file_path):

    df = pd.read_csv(file_path)
    data_list = df.values.tolist()
    data_list.insert(0, df.columns.tolist())
    return data_list

#iterates through a list of lists and returns a list with the highest value for each index. Ignores non-numbers.
def find_maxs(list_of_lists):
    max_list = []
    currentItem = ""
    for entry in list_of_lists:
        for i in range(len(entry)):
            currentItem = entry[i]

            #skip this item if it is not a number.
            try:
                float(currentItem)
            except:
                continue

            #make sure there are enough items in the max_list.
            while(len(max_list) - 1 < i):
                max_list.append("none")

            #if no other number is at the index, put this number there.
            if max_list[i] == "none":
                max_list[i] = currentItem
            #else if the current item is larger than the current max for that index, make the current item the new max.
            elif max_list[i] < currentItem:
                max_list[i] = currentItem

    return max_list

#iterates through a list of lists and returns a list with the lowest value for each index. Ignores non-numbers.
def find_mins(list_of_lists):
    min_list = []
    currentItem = ""
    for entry in list_of_lists:
        for i in range(len(entry)):
            currentItem = entry[i]

            #skip this item if it is not a number.
            try:
                float(currentItem)
            except:
                continue

            #make sure there are enough items in the min_list.
            while(len(min_list) - 1 < i):
                min_list.append("none")

            #if no other number is at the index, put this number there.
            if min_list[i] == "none":
                min_list[i] = currentItem
            #else if the current item is larger than the current max for that index, make the current item the new max.
            elif min_list[i] > currentItem:
                min_list[i] = currentItem

    return min_list

def normalize(list_of_lists, min_list, max_list):
    for entry in list_of_lists:
        for i in range(len(entry)):
            try:
                float(entry[i])
            except:
                continue

            entry[i] = (entry[i] - min_list[i])/(max_list[i] - min_list[i])

def export_file(encoded_data_list, filename):
    #create the new file and open for writing.
    new_file = open(filename + ".csv",'w')

    string_to_write = ""
    for entry in encoded_data_list:
        string_to_write = ""

        string_to_write += str(entry[0])
        for i in range(1,len(entry)):
           string_to_write += "," + str(entry[i])

        new_file.write(string_to_write + "\n")

    new_file.close()

data_list = csv_to_list("Encoded.csv")
minimums = find_mins(data_list)
maximums = find_maxs(data_list)
normalize(data_list, minimums, maximums)

export_file(data_list, "Normalized")
