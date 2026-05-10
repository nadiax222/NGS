#determine sys of encoding quality (Phred+33 or Phred+64)
sequence = 'ACGTGCATAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC'
quality = 'ACDFAAEHHHBBAA?;<<CDEAD98,;;,ADE??,874873012,/.'
min_ascii = min(ord(ch) for ch in quality)
if min_ascii < 64:
    encoding = "Phred+33"
else:
    encoding = "Phred+64"
print(f"The encoding type is: {encoding}")
