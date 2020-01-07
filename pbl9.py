# Special Pythagorean triplet
msg = ''
for a in range(1, int(1000 / 3)):
    for b in range(a + 1, 1000 - 2 * a - 1):
        if a ** 2 + b ** 2  == (1000 - a - b) ** 2:
            c = 1000 - a - b
            msg = f'The 3 natural numbers are {a}, {b}, {c}. a*b*c={a * b * c}'
            break
if msg == '':
    msg = 'No triplet has been found'

print(msg)
# Answer: The 3 natural numbers are 200, 375, 425. a*b*c=31875000