a = 'A'
b = 'B'
c = 1.1

formato = 'a= {} b= {} c= {:.2f}'.format(a,b,c)

formato2 = 'a= {0} a= {0} c= {2:.2f}'.format(a,b,c) # usando os indices

formato3 = 'a= {nome1} c= {nome3:.2f} b= {nome2}'.format(nome1= a, nome2 =  b, nome3=  c) # parametro nomeado



print(formato)
print(formato2)
print(formato3)
