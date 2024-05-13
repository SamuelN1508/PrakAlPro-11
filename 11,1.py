# Tuple yang dicek
tA = (90, 90, 9, 90)

# Mengubah Tuple menjadi List
ta = list(tA)

# Item pertama dalam list
first = ta[0]
con = True

# Looping setiap item dalam list
for x in ta:
    # Jika ada satupun item yang tidak sama dengan item pertama maka akan False
    if x != first:
        con = False
print(con)