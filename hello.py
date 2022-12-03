print("Hello World")
name = input("Qual é seu nome? ").strip().title() # Tira os espaços de name e coloca todas maiúsculas tipo título
idade = input("Qual sua idade? ").strip()

#name = name.capitalize() #coloca a primeira em maiúsculo 

#divdir primeiro e segundo nome
first, last = name.split(" ") #troca o nome e sobrenome
print(f"Seu nome é! {last} , Sua idade é! {idade}") #last sobrenome


