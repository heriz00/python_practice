def printTable(tableData):
    # Find the longest word in each column
    colWidths = []
    for col in tableData:
        maxWidth = max(len(word) for word in col)  # Get max length in the column
        colWidths.append(maxWidth)  # Store it for alignment

    # Transpose the table (convert columns to rows)
    tableRows = zip(*tableData)  # Rearranges tableData to print row-wise

    # Print each row with proper alignment
    for row in tableRows:
        for i in range(len(row)):
            print(row[i].rjust(colWidths[i]), end=' ')  # Right-align each word
        print()  # Move to the next line after printing a row

# Example usage
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
