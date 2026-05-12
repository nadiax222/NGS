#dla pliku reads.sam napisz skrypt, w którym policzysz A) liczbę sparowanych odczytów, b) liczbę poprawnie sparowanych odczytów primary na nici -, c) liczbę niepoprawnie sparowanych odczytów supplementary
filename = 'reads.sam'
unmapped = 0
Propery_paired_primary_minus = 0
Improperly_paired_supplementary = 0

with open(filename) as f:
    for line in f:
        if line.startswith('@'): #w pliku sam nagłówek zaczyna się od @, więc pomijamy te linie
            continue
        fields = line.strip().split('\t') #line.strip() uwsuwa białe zniaki, split('\t') dzieli linię na pola, które są oddzielone tabulatorem, powstaje lista
        flag = int(fields[1]) #flaga jest w drugim polu (indeks 1), konwertujemy ją na int
        if flag & 4: 
            unmapped += 1

        is_proper_paired = bool(flag & 2) #sprawdzamy czy flaga 2 jest ustawiona, czyli czy odczyt jest poprawnie sparowany
        is_unmapped = bool(flag & 4) #sprawdzamy czy flaga 4 jest ustawiona, czyli czy odczyt jest niezmapowany
        is_minus_strand = bool(flag & 16) #sprawdzamy czy flaga 16 jest ustawiona, czyli czy odczyt jest na nici minus
        is_secondary = bool(flag & 256) #sprawdzamy czy flaga 256 jest ustawiona, czyli czy odczyt jest secondary
        is_supplementary = bool(flag & 2048) #sprawdzamy czy flaga 2048 jest ustawiona, czyli czy odczyt jest supplementary

        is_primary = not is_secondary and not is_supplementary #odczyt jest primary jeśli nie jest ani secondary, ani supplementary
        if is_proper_paired and is primary and is_minus_strand and not is_unmapped:
                        Propery_paired_primary_minus += 1

         if is_supplementary and not is_proper_paired:
                        Improperly_paired_supplementary += 1
print ("a) Liczba niezmapowanych odczytów: ")
print("b) Liczba poprawnie sparowanych odczytów primary na nici -: ")
print("c) Liczba niepoprawnie sparowanych odczytów supplementary: ")



