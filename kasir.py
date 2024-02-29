rokok, minyak, gula, saldo, diskon = 20000, 25000, 11000, 100000, 10000

total = rokok + minyak + gula
totalsetelahdiskon = total - diskon
kembalian = saldo - totalsetelahdiskon

print('Ucup membeli rokok seharga', rokok, ',', 'minyak seharga', minyak, ',', 'dan gula seharga', gula, 'dengan total seluruhnya', total, '.', 'lalu ucup mendapat diskon sebesar', diskon, 'dan total seluruhnya menjadi', totalsetelahdiskon, '.')
print('ucup membayar dengan uang sebesar', saldo, ',', 'maka kembalian ucup adalah', kembalian)

print('===================================================================')
print('|                         yang simple                             |')
print('')
print('Uang Ucup =', saldo)
print('')
print('rokok =', rokok)
print('minyak =', minyak)
print('gula', gula)
print('diskon', diskon)
print('')
print('total belanja =', totalsetelahdiskon)
print('')
print('kembalian =', kembalian)
