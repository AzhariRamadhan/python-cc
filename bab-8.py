#8-1
print("\n#8-1")

def display_message():
    print('hello everyone, today i learn about def python')

display_message()

#8-2 favorite book
print('\n#8-2 favorite book')

def favorite_book(title):
    print('one of my favorite book is ' + title)

favorite_book('Alice in Wonderland')

#8-3 T-Shirt
print('\n#8-3 T-Shirt')

def make_shirt(size, text):
    print('A shirt size is = ' + size + ' ,Text print = ' + text)

make_shirt('L', 'Jancok')
make_shirt(text='Jancok', size='L')

#8-4 Large Shirts
print('\n#8-4 Large Shirts')

def make_shirts(size='L', text='I love Python'):
    print('A shirt of size: ' + size + ' will be printed with the words: ' + text)

make_shirts()
make_shirts(size='M')
make_shirt('S', "Saya Cinta PHP, tapi Bo'ong")

#8-5 Cities
print('\n#8-5 Cities')

def describe_city(nama, provinsi='Jakarta'):
    print(nama + ' sedang berada di ' + provinsi)

describe_city('Jokowi')
describe_city(nama='Ucok')
describe_city('lucinta luna', 'Bandung')

#8-6 City Names
print('\n#8-6 City Names')

def city_country(name, country):
    return name.title() + ', ' + country.title()

print(city_country('Bandung', 'jawa barat'))
print(city_country('jogja', 'jawa tengah'))
print(city_country('palembang', 'sumatra selatan'))

#8-7 Album
print('\n#8-7 Album')

def make_album(artis, title, tracks=0):
    if tracks != 0:
        return {'artist': artis, 'title': title, 'tracks': tracks}
    return {'artist': artis, 'title': title}

print(make_album('Judika', 'Cinta karena Cinta'))
print(make_album('Andmesh', 'Hanya Rindu'))
print(make_album('NF', 'If i grow up'))
print(make_album('NF', 'Time', 10))

#8-8 User Album
while True:
    print('Tekan "q" untuk keluar')
    artis = input('Masukkan Nama Penyanyi: ')
    if artis == 'q':
        break
    album = input('Masukkan nama album: ')
    if album == 'q':
        break
    print(make_album(artis, album))