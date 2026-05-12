# Napisz skrypt, który z załączonych wyników mapowania RNA-seq (introns.sam):
# a) Zwróci minimalną, średnią i maksymalną długość intronu
# b) Wygeneruje histogram długości intronów
# c) Policzy średni procentowy udział softclipowanych i hardclipowanych pozycji w odczytach

import re #importujemy moduł re do pracy z wyrażeniami regularnymi
import matplotlib.pyplot as plt #importujemy moduł matplotlib.pyplot do tworzenia wykresów
filename = 'introns.sam' #nazwa pliku SAM z wynikami mapowania RNA-seq
softclip_percentages = [] #softclip_percentages to lista, w której będziemy przechowywać procentowy udział softclipowanych pozycji w odczytach
hardclip_percentages = [] #hardclip_percentages to lista, w której będziemy przechowywać procentowy udział hardclipowanych pozycji w odczytach
with open(filename) as f:
    for line in f:
        if line.startswith('@'):
            continue
        fields = line.strip().split('\t')

        cigar = fields[5] #CIGAR string jest w 6 polu (indeks 5)
        #cigar jest potrzebny do obliczenia długości intronu oraz procentowego udziału softclipowanych i hardclipowanych pozycji
        if cigar == "*":
            continue #jeśli CIGAR string jest "*", to oznacza, że odczyt jest niezmapowany, więc pomijamy te linie
        cigar_parts = re.findall(r'(\d+)([MIDNSHP=X])', cigar) #używamy wyrażenia regularnego do podzielenia CIGAR string na części, gdzie \d+ oznacza liczbę, a [MIDNSHP=X] oznacza literę reprezentującą operację)

        softclip = 0
        hardclip = 0
        read_length = 0

        for length, op in cigar_parts:
            length = int(length)
            #konwertujemy długość na int
        if operation == 'N':
            introns.append(length)
        #jeśli operacja to 'N', to oznacza, że mamy do czynienia z intronem, więc dodajemy jego długość do listy introns
        if operation == 'S':
            softclip += length
        #jeśli operacja to 'S', to oznacza, że mamy do czynienia z softclipem, więc dodajemy jego długość do zmiennej softclip
        if operation == 'H':
            hardclip += length
        #jeśli operacja to 'H', to oznacza, że mamy do czynienia z hardclipem, więc dodajemy jego długość do zmiennej hardclip
        if operation in ['M', 'I', 'S', '=', 'X']:
        #jeśli operacja to 'M', 'I', 'S', '=', lub 'X', to oznacza, że te operacje wpływają na długość odczytu, więc dodajemy ich długość do zmiennej read_length
            read_length += length
        if read_length > 0:
            softclip_percentage = (softclip / read_length) * 100
            hardclip_percentage = (hardclip / read_length) * 100
            softclip_percentages.append(softclip_percentage)
            hardclip_percentages.append(hardclip_percentage)
        #obliczamy procentowy udział softclipowanych i hardclipowanych pozycji w odczytach i dodajemy te wartości do odpowiednich list
if len(introns) > 0:
    min_intron = min(introns)
    mean_intron = sum(introns) / len(introns)
    max_intron = max(introns)

    print(f"Minimalna długość intronu: {min_intron}")
    print(f"Średnia długość intronu: {mean_intron}")
    print(f"Maksymalna długość intronu: {max_intron}")
    plt.hist(introns, bins=20, edgecolor='black')
    plt.title('Histogram długości intronów')
    plt.xlabel('Długość intronu')
    plt.ylabel('Liczba intronów')
    plt.show()

    else:
        print("Nie znaleziono intronów w pliku SAM.")
if len(softclip_percentages) > 0:
    average_softclip_percentage = sum(softclip_percentages) / len(softclip_percentages)
    print(f"Średni procentowy udział softclipowanych pozycji: {average_softclip_percentage:.2f}%"))
    else:
        print("Nie znaleziono softclipowanych pozycji w pliku SAM.")
    mean_hardclip = sum(hardclip_percentages) / len(hardclip_percentages)
    print(f"Średni procentowy udział hardclipowanych pozycji: {average_hardclip_percentage:.2f}%"))
    else:
        print("Nie znaleziono hardclipowanych pozycji w pliku SAM.")

    