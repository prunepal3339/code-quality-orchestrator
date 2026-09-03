def lastNameLensort(names):
    return sorted(names, key=lambda x: (-len(x.split()[1]), x))

names = [
  "Jennifer Figueoara",
  "Hather Mcgee',
  "Amand Schwartz",
  'Nicole Yder',
  "Meliss Hoffman"
]

print(lastNameLensort(names))
