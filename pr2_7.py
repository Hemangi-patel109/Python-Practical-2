c = input("Enter value: ")

if c>='0' and c<'10':
    print("Entered value is Digit.")
elif c>='a' and c<='z' or c>='A' and c<='Z':
    print("Entered value is Character")
else:
    print("Entered value is Special Symbol.")