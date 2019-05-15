input_date = input("Geben Sie ein Datum in der Form DD. Monat JJJJ ein:")

if input_date[:2].isnumeric() and input_date[-3:].isnumeric():
    input_date = input_date.split()
    print("{:s} {:s}, {:s}".format(input_date[1], input_date[0].strip('.'), input_date[2]))
else:
    print("Sie haben kein gültiges Datum eingegeben.")
