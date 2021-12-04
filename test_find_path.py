import os


dirPath = os.getcwd()
target_path = os.path.join(dirPath,"tcxo_temp")
def show_csv_file_nam(target_path):
    csv_list = []
    dirPath = target_path
    for file in os.listdir(dirPath):
        if file[-3:] == "csv":
            csv_list.append(file)
    return csv_list

