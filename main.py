filepath = 'programa.txt'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       linha = line.strip().split(' ')
       linha
       
       line = fp.readline()
       cnt += 1