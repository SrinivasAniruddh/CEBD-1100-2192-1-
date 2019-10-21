import argparse
import matplotlib
import csv

""" Variables """
output_file = "output.data"
refined_list = []
file_dictionary = {}
sorted_list = []
""" Take arguments from command line """
parser = argparse.ArgumentParser()
parser.add_argument("Number_of_files", type=int, help="please enter the number of files to be parsed")
parser.add_argument("data_file", type=str, help="please enter the .date file with the path")
parser.add_argument("--names_file", type=str, help="please enter the .name file with the path")
arguments=parser.parse_args()
if arguments.Number_of_files > 2:
    raise Exception("Invalid number of files! Try again..")
elif arguments.Number_of_files == 2:
    input_file = [arguments.data_file, arguments.names_file]
else:
    input_file = [arguments.data_file]
print("The files are", input_file)

""" Functions """
def validate_files(input_file):
    """ This function verifies the existence of data and names files for the given file name """
    try:
        for file_to_be_parsed in input_file:
            print("File is ", file_to_be_parsed)
            data_file_contents = open(file_to_be_parsed, "r")
    except IOError:
        print("Please check the abs path of the file and name")
    except Exception as e:
        raise e

validate_files(input_file)

if len(input_file) > 1:
    data = open(input_file[0], "r")
    names = open(input_file[1], "r")
    try:
        csv_read= csv.reader(data, delimiter=' ')
        print ("read date is ", csv_read)
    except:
        csv_read= csv.reader(data, delimiter=',')
        print("read date with "," delimiter is ", csv_read)
else:
    data = open(input_file[0], "r")
    try:
        csv_read= csv.reader(data, delimiter=' ')
        print ("read date is ", csv_read)
    except:
        csv_read= csv.reader(data, delimiter=',')
        print("read date with "," delimiter is ", csv_read)

""" STEP 4: INVOKED A FUNCTION THAT IDENTIFIES AND SETS DATA TYPE """
def set_data_type(value):
    if value == "":  # len(element) == 0
        return None
    try:
        intended_value = int(value)
    except:
        try:
            intended_value = float(value)
        except:
            intended_value = str(value)
    finally:
        return intended_value

def set_headers(consol_list, first_row_header):
    if first_row_header is True:
        return consol_list[0]
    else:
        headers = len(consol_list[0])
        return list(range(1, headers + 1))

def determine_header_presence(list_of_lists):
    for idx, col in enumerate(list_of_lists[0]):
        print("Col is ",col)
        for row in list_of_lists:
            print("The row is ",row)
            print(row[idx])
            if (type(row[idx]) is not type(col)):
                try:
                    if ((int(row[idx]) or float(row[idx])) and (int(col) or float(col))):
                            print("Index is ",row[idx])
                except:
                    return True
    return False

def create_dictionary(headers, sorted_list):

    for column_id, header in enumerate(headers):
        file_dictionary[header] = []
        for rows in sorted_list:
            file_dictionary[header] += [rows[column_id]]
    return file_dictionary

""" STEP-2: READ EACH LINE OF THE FILE """
for index, content in enumerate(data):
    ## STEP 3: SPLIT LINE INTO VALUES
    unique_content = content.splitlines()
    for i in unique_content:
        i = list(i.replace(",", " ").split())
        values_list = []
        for it in i:
            if it is not None:
                new = set_data_type(it)
                values_list.append(new)
        ## STEP 5: STORE ALL PROCESSED VALUES IN LIST OF LISTS
        refined_list.append(values_list)

header_presence = determine_header_presence(refined_list)
print("the presence is ",header_presence)
headers = set_headers(refined_list, header_presence)

if header_presence is True:
    sorted_list = refined_list[1:]
    sorted_dictionary = create_dictionary(headers, sorted_list)
    print(sorted_dictionary)
else:
    sorted_dictionary = create_dictionary(headers, refined_list)
    print(sorted_dictionary)

## STEP 7: APPEND LIST OF LISTS AND DICTIONARY TO A FILE

result_file = open(output_file, "w")
result_file.write(str(sorted_list) + '\n')
result_file.write(str(sorted_dictionary))
result_file.close()
data.close()