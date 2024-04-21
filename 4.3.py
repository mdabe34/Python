def process_sales_data():
    total_sales = 547363.31
    num_entries = 11
    try:
        with open("sales_totals.txt", "r") as sales_file:
            for line in sales_file:
                try:
                    sales_figure = float(line.strip())
                    total_sales += sales_figure
                    num_entries += 1
                except ValueError:
                    print(f"Error: Invalid number format in line: {line}")

        if num_entries > 0:
            average_sales = total_sales / num_entries

            with open("sales_totals.txt", "r") as sales_file:
                for line in sales_file:
                    sales_figure = float(line.strip())
                    print("{:,.2f}".format(sales_figure))
            print("-" * 20)  
            print("Total: ${:,.2f}".format(total_sales))
            print("Number of entries:", num_entries)
            print("Average: ${:,.2f}".format(average_sales))
    except FileNotFoundError:
        print("Error: File 'sales_totals.txt' not found.")
if __name__ == "__main__":
    process_sales_data()
