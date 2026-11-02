def harf_notu_hesapla():
    vize = float(input('Vize notunuzu giriniz: '))
    final = float(input('Final notunuzu giriniz: '))

    ortalama = (vize * 0.40) + (final * 0.60)
    print(f'Ders ortalamanız: {ortalama:.2f}')

    if ortalama >= 85:
        harf = 'AA'
    elif ortalama >= 70:
        harf = 'BB'
    elif ortalama >= 60:
        harf = 'CC'
    elif ortalama >= 50:
        harf = 'DD'
    else:
        harf = 'FF (Kaldınız)'
    
    print(f'Harf notunuz: {harf}')

harf_notu_hesapla()


    

    

