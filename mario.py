def main():
    height = get_height()
    for i in range(height):
        print("#")
        
def get_height():
    while True:
        try:
            n =  int(input("height: "))
            if n > 0:
                break
        except ValueError:
            print("Não é um número")
            
        
        
    return n

main()
