sequence = 'ACGTGCATAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC'
quality = 'ACDFAAEHHHBBAA?;<<CDEAD98,;;,ADE??,874873012,/.'
min_ascii = min(ord(ch) for ch in quality)
if min_ascii < 64:
    encoding = "Phred+33"
else:
    encoding = "Phred+64"
print(f"The encoding type is: {encoding}")
offset = 33
qual = [ord(ch) - offset for ch in quality]
min_quality = min(qual)
max_quality = max(qual)
min_pos = qual.index(min_quality)+1
max_pos = qual.index(max_quality)+1
print("Min:" min_quality, "max:" max_quality, "max pos: " max_pos, "min_posl: "min_pos )


#AVERAGE READ QUALITY
avg = sum(qual)/len(qual)
print(f"Average quality: {avg:.2f}")

