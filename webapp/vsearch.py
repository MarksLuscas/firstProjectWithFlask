

def buscarVogais(phrase: str) -> set: # mostra o tipo da variável que espera receber e se algo dê errado, ele mostra qual tipo de dado era para ter passado
 vowels = set('aeiou') 
 return vowels.intersection(set(phrase)) #set(letters) -> cria um obj conjunto a partir dos caracteres nas variavel letters

# print(buscarVogais("Lapis")) #tem que passar uma palavra e as letras que espera encontrar na palavra ja estão setas pela funcao

def buscarLetras(phrase: str, letters: str='aeiou') -> set: # mostra o tipo da variável que espera receber e se algo dê errado, ele mostra qual tipo de dado era para ter passado
 return set(letters).intersection(set(phrase)) #set(letters) -> cria um obj conjunto a partir dos caracteres nas variavel letters

print(buscarLetras("Lapis", 'as'))  #agora é possivel passar as letras específicas que espera achar, 
                       # pois já estamos definindo como padrao as letras aeiou, na linha phrase: str, letters: str='aeiou'