import pandas as pd


def csv_to_list(file_path):

    df = pd.read_csv(file_path)
    data_list = df.values.tolist()
    data_list.insert(0, df.columns.tolist())
    return data_list

"""
This is an example of the final variables that would be produced with the test_attributes and test_list inputted into the encoding functions.

test_attributes = ["name", "favorite color", "age"]
test_list = [["Fred", "orange", 5],["Mary", "orange", 22],["Terry", "blue", 22],["Susan", "blue", 7]]

possible values:
{'name': ['Fred', 'Mary', 'Terry', 'Susan'], 'favorite color': ['orange', 'blue'], 'age': [5, 22, 7]}

new attributes:
['name_is_Fred', 'name_is_Mary', 'name_is_Terry', 'name_is_Susan', 'favorite color_is_orange', 'favorite color_is_blue', 'age']

index map:
{'name': {'name_is_Fred': 0, 'name_is_Mary': 1, 'name_is_Terry': 2, 'name_is_Susan': 3}, 'favorite color': {'favorite color_is_orange': 4, 'favorite color_is_blue': 5}, 'age': {'!ANY!': 6}}

encoded data:
[['name_is_Fred', 'name_is_Mary', 'name_is_Terry', 'name_is_Susan', 'favorite color_is_orange', 'favorite color_is_blue', 'age'], [1, 0, 0, 0, 1, 0, 5], [0, 1, 0, 0, 1, 0, 22], [0, 0, 1, 0, 0, 1, 22], [0, 0, 0, 1, 0, 1, 7]]
"""

#take a list of lists and return a dictionary where attributes are the keys and the values are the possible values of those attributes as found in the lists.
def get_possible_values(attributes, list_of_lists):
    possible_values = {}

    #add attributes as keys with empty lists as values.
    for attribute in attributes:
        possible_values[attribute] = []

    #iterate through all lists.
    for current_list in list_of_lists:
        #iterate through each index in the current list.
        for i in range(len(current_list)):
            #check if the value in the current index is currently in the list of possible values for the attribute found at the same index.
            #possible_values[attributes[i]] returns the list of possible values for the attribute at index i.
            if current_list[i] not in possible_values[attributes[i]]:
                #if the value is not in the list of possible values, add it.
                possible_values[attributes[i]].append(current_list[i])

    return possible_values

#take a dictionary of possible values
def encode_data(possible_values_dict, list_of_lists):
    #start by generating a new set of attributes. Any attributes that contain data not pare-sable as float will be split into multiple attributes which may contain either 0 or 1 as values.
    new_attributes = []
    #index map is used to keep track of which index certain attributes are at. It is a dictionary with the original attributes as keys and the values are
    #a dictionary with possible values (if non-numerical) as key and index where the new attribute can be found as values. "!ANY!" is used as the possible
    #value for numerical attributes in the map, as the index is the same for all values.
    index_map = {}
    #encoded data is a list of lists where the attributes are values have been encoded for linear regression.
    encoded_data = []

    current_index = 0

    is_numerical = True #define variable outside of loop so we don't have to create a new variable with each iteration.
    for attribute in possible_values_dict.keys():
        is_numerical = True

        #check if the attribute is numerical in all possible values. If so, the attribute can be added normally. If not, it must be split into multiple attributes.
        for value in possible_values_dict[attribute]:
            try:
                float(value)
            except:
                is_numerical = False
                break

        if is_numerical is True:
            new_attributes.append(attribute)
            index_map[attribute] = {"!ANY!" : current_index}
            current_index = current_index + 1
        else:
            index_map[attribute] = {}
            for value in possible_values_dict[attribute]:
                new_attributes.append(attribute + "_is_" + value)
                index_map[attribute][attribute + "_is_" + value] = current_index
                current_index = current_index + 1

    #now that we have an index map and our new attributes, we convert the data from list_of_lists into its encoded form.

    #the first list in encoded_data is the new attributes.
    encoded_data.append(new_attributes)

    encoded_index = 0 #index used to reference the encoded_data list corresponding to the current entry.
    current_attribute = ""
    for entry in list_of_lists:
        encoded_index = encoded_index + 1
        encoded_data.append([])

        #each value starts at 0
        for i in range(len(new_attributes)):
            encoded_data[encoded_index].append(0)

        for i in range(len(entry)):
            #possible_values_dict.keys()[i] will return the name of the attribute currently being encoded.
            current_attribute = list(possible_values_dict.keys())[i]
            if "!ANY!" in index_map[current_attribute].keys():
                encoded_data[encoded_index][index_map[current_attribute]["!ANY!"]] = entry[i]
            else:
                encoded_data[encoded_index][index_map[current_attribute][current_attribute + "_is_" + entry[i]]] = 1

    return encoded_data

def export_file(encoded_data_list):
    #create the new file and open for writing.
    new_file = open("Encoded.csv",'w')

    string_to_write = ""
    for entry in encoded_data_list:
        string_to_write = ""

        string_to_write += str(entry[0])
        for i in range(1,len(entry)):
           string_to_write += "," + str(entry[i])

        new_file.write(string_to_write + "\n")

    new_file.close()

file_path = "Maths.csv"
data_list = csv_to_list(file_path)

attributes_data = data_list[0]
values_data = data_list[1:len(data_list)]
possible_values_data = get_possible_values(attributes_data,values_data)
encoded_data = encode_data(possible_values_data,values_data)
export_file(encoded_data)
