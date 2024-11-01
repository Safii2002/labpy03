print('LATIHAN 2')
print('Memasukkan Bilangan, Jika masukan 0 akan berhenti dan memasukkan bilangan terbesar')

blngn_max = None

while True:
    bilangan = float(input('Masukan Bilangan,(0 untuk berhenti):'))

    if bilangan == 0:
        break
    

    if blngn_max is None or bilangan > blngn_max:
        blngn_max = bilangan


if blngn_max is not None:
     print('Bilangan Terbesar adalah:', blngn_max)
else:
    print('Tidak ada bilangan yang dimasukkan')
