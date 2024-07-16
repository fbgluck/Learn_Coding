# Example program that shows retrieving data and sorting and displaying top n results
get-process | select-object ProcessName, StartTime,CPU,TotalProcessorTime -first 5 |sort-object -property TotalProcessorTime -descending

