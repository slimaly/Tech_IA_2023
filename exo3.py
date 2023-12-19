# °F = (°C x 1,8) + 32
#T°C = (T°F - 32) x 5/9

def converted_degree(temperature):
    
    return (temperature * 1.8) + 32

temperature = 18
print(converted_degree(temperature))

def converted_degree1(degres):
    return (degres - 32) * 5/9

degres = 72
print(converted_degree1(degres))





def average_grade(grades):
   return sum(grades)/ len(grades)

eleves = ["Lucas", "Emma", "Gabriel", "Mia", "Noah", "Charlotte", "Ethan", "Sophia", "Liam", "Olivia" ]
note_maths1 = [17, 18, 16, 18, 17, 18, 16, 19, 18, 16]
note_maths2 = [18, 17, 17, 17, 18, 18, 17, 18, 17, 18]
note_francais1 = [15, 19, 16, 16, 18, 19, 15, 17, 18, 17]
note_francais2 = [16, 18, 15, 18, 18, 17, 16, 19, 19, 16]
note_francais3 = [19, 18, 17, 18, 16, 19, 15, 18, 17, 18]
note_histoire = [17, 16, 18, 15, 17, 17, 19, 15, 18, 16]

print(average_grade(grades = note_maths1  + note_maths2))

print(average_grade(grades= note_francais1 + note_francais2 + note_francais3))

print(average_grade(grades= note_histoire))
print(average_grade(grades= note_maths1 + note_maths2 + note_francais1 + note_francais2 + note_francais3 + note_histoire))

#for eleve in eleves: 


    



