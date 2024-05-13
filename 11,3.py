inpt = input("Masukan Nama File = ")
def count_hours(input):
    # Dict kosong
    Dict = {}
    
    # Membuka file
    with open(input, "r") as file:
        # Membaca setiap lines pada file
        lines = file.readlines()
        
        # Looping setiap kata dalam kalimat
        for line in lines:
            # Mencari kalimat waktu
            if line.startswith("From") and len(line.split()) > 3:
                # Ketika kalimat sudah ditemukan maka akan displit
                kata = line.split()
                
                # Mencari jam
                waktu = kata[-2].split(":")
                hour = waktu[0]
                
                # Mengecek apakah jam sudah pernah ditambah ke dict
                if hour not in Dict:
                    # Jika belom ada maka akan dibuat dict baru
                    Dict[hour] = 1
                else:
                    # Jika sudah ada maka akan ditambah satu
                    Dict[hour] += 1

    # Mengubah dict menjadi tuple
    t = list(Dict.items())
    
    # Mensortir tuple
    t.sort()
    
    # Looping dan print setiap tuple
    for x, y in t:
        print(x, y)
        
count_hours(inpt)