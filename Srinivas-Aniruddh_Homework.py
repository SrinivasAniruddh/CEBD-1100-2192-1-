File_Name_wo_extension=input("Enter the abs path of the file without extension within inverted quotes: ")
print("The file name you entered is {}".format(File_Name_wo_extension))
No_Of_Files=int(input("Enter the number of files: "))
print ("The Number of files with this filename is ".format(No_Of_Files))
data_file = File_Name_wo_extension + ".data"
name_file = File_Name_wo_extension + ".names"

""" STEP 1 - LOAD THE DATA FILE """
#data = open(input_file, "r")
headers=[]
refined_list=[]
file_dictionary={}
sorted_list=[]

def get_headers(file_content):
    """ This function splits the file content into lines and gets the first row as header"""
    for index, content in enumerate(file_content):
        unique_content = content.splitlines()
        print("Hello")
        ## CREATE A LIST WITH THE COLUMN NAMES
        if index == 0:
            for name in unique_content:
                headers = list(name.split())
    return headers

def validate_files(number_of_files):
    """ This function verifies the existence of data and names files for the given file name """
    if number_of_files == 1:
        try:
            print ("File is ",data_file)
            data_file_contents = open(data_file, "r")
            headers = get_headers(data_file_contents)
            print (headers)
            data_file_contents.close()
            return headers, data_file_contents
        except IOError:
            print ("Please check the abs path of the file and name")
        except Exception as e:
            raise e
    else:
        try:
            data_file_contents = open(data_file, "r")
            name_file_contents = open(name_file, "r")
            headers=get_headers(name_file_contents)
            print(headers)
            data_file_contents.close()
            name_file_contents.close()
            return headers, data_file_contents
        except IOError:
            print ("No files found! Please check the file name and the number of files ")
            print ("Data file is {} and \nname file is {}".format(data_file, name_file))
        except Exception as e:
            raise e
file_contents= validate_files(No_Of_Files)
print (type(file_contents))

""" STEP 4: INVOKED A FUNCTION THAT IDENTIFIES AND SETS DATA TYPE """
def set_data_type(value):
    if value == "":
        return None
    try:
        intended_value=int(value)
    except:
        try:
            intended_value=float(value)
        except:
            intended_value=str(value)
    finally:
        return intended_value

""" STEP-2: READ EACH LINE OF THE FILE """
# for index, content in enumerate(data):
#     ## STEP 3: SPLIT LINE INTO VALUES
#     unique_content = content.splitlines()
#     ## STEP 4: INVOKED A FUNCTION THAT IDENTIFIES AND SETS DATA TYPE
#     else:
#         for i in unique_content:
#             print("Item is ", i.split())
#             i=list(i.split())
#             print("list is ", i)
#             values_list=[]
#             for it in i:
#                 print("{} is the variable and the type is {} ".format(it, type(it)))
#                 new=set_data_type(it)
#                 values_list.append(new)
#                 print("The value is {} and type is {}".format(new, type(new)))
#             ## STEP 5: STORE ALL PROCESSED VALUES IN LIST OF LISTS
#             refined_list.append(values_list)
# print("The refined list is",refined_list)
# length=len(refined_list[0])
# print("length is ",length)
# for l in range(0,length):
#     sorted_list.append([item[l] for item in refined_list])
# print("The sorted list is {}".format(sorted_list))
#
# ## STEP 6: CREATE DICTIONARY WITH COLUMN NAMES AS KEYS AND THE RESPECTIVE VALUES OF THE COLUMN AS VALUES
# for index, item in enumerate(headers):
#     file_dictionary[item]=sorted_list[index]
# print("The dictionary of lists is ",file_dictionary)
# data.close()