import csv
#__________________________________________________________INPUT DELIMIT______OUTPUT_DELIMIT__________
def separate_first_column(input_csv_path, output_csv_path, delimiter="\t", output_delimiter=","):
    with open(input_csv_path, 'r') as infile, open(output_csv_path, 'w', newline='') as outfile:
        csv_reader = csv.reader(infile, delimiter=delimiter)
        csv_writer = csv.writer(outfile, delimiter=output_delimiter)    
        for row in csv_reader:           
            first_column = row[0]
            other_columns = row[1:]   
            csv_writer.writerow([first_column] + other_columns)
    print(f"Processed file saved as: {output_csv_path}")

# Define file paths (Local directories only)
input_csv_path_1 = r"C:\Users\NikolaosSapounas\Downloads\EXTR1.csv"
output_csv_path_1 = r"C:\Users\NikolaosSapounas\Downloads\EEXTR1.csv"

input_csv_path_2 = r"C:\Users\NikolaosSapounas\Downloads\EXTR2.csv"
output_csv_path_2 = r"C:\Users\NikolaosSapounas\Downloads\EEXTR2.csv"

separate_first_column(input_csv_path_1, output_csv_path_1)
separate_first_column(input_csv_path_2, output_csv_path_2)
