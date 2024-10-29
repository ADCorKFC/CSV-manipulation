import csv
# Define Delimiter (\t for Tabulator) & size
def split_txt_to_csv(input_txt_path, output_csv_path_1, output_csv_path_2, split_size_mb=450, delimiter=";"):
    # Convert MB to bytes
    split_size_bytes = split_size_mb * 1024 * 1024
    
    # Initialize counters and variables
    file_size = 0
    current_file_number = 1
    output_csv_path = output_csv_path_1

    with open(input_txt_path, 'r') as infile:
        with open(output_csv_path, 'w', newline='') as outfile:
            csv_writer = csv.writer(outfile, delimiter=";")
            
            # Optional: Write header if the text file has a header row
            header = infile.readline().strip().split(delimiter)
            csv_writer.writerow(header, delimiter=";")
            file_size += len(",".join(header).encode('utf-8')) + 1  # Update for header

            # Loop through each line in the text file
            for line in infile:
                # Split the line by the delimiter
                row = line.strip().split(delimiter)
                csv_writer.writerow(row)

                # Update the file size
                file_size += len(line.encode('utf-8'))

                # If we've reached the split size, start writing to the next CSV file
                if file_size >= split_size_bytes:
                    # Close the current file and reset counters
                    outfile.close()
                    
                    # Switch to the next output file
                    current_file_number += 1
                    output_csv_path = output_csv_path_2 if current_file_number == 2 else output_csv_path_1
                    
                    # Reset file size for the new part
                    file_size = 0

                    # Open the new output file and write the header again
                    outfile = open(output_csv_path, 'w', newline='')
                    csv_writer = csv.writer(outfile, delimiter=";")
                    csv_writer.writerow(header, delimiter=";")  # Write header in the new file as well

    print("Splitting complete. Files saved as:")
    print(output_csv_path_1)
    print(output_csv_path_2)

# Define the file paths
input_txt_path = r"C:\Users\NikolaosSapounas\Downloads\Cube V0003 Total Sales Value Inc Vat (D, Site, SKU, TSeason, STT).txt"
output_csv_path_1 = r"C:\Users\NikolaosSapounas\Downloads\EXTR1.csv"
output_csv_path_2 = r"C:\Users\NikolaosSapounas\Downloads\EXTR2.csv"

# Call the function
split_txt_to_csv(input_txt_path, output_csv_path_1, output_csv_path_2, delimiter=";")


