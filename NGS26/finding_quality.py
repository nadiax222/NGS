#find position of highest and lowest quality
offset = 33
qual = [ord(ch) - offset for ch in quality]
min_quality = min(qual)
max_quality = max(qual)
min_pos = qual.index(min_quality)+1
max_pos = qual.index(max_quality)+1
print("Min:" min_quality, "max:" max_quality, "max pos: " max_pos, "min_posl: "min_pos )

