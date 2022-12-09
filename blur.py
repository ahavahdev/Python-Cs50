from PIL import Image, ImageFilter

before = Image.open("bridge.bmp") #abre a imagem
#after = before.filter(ImageFilter.BoxBlur(1)) # filtro para borrar imagem
after = before.filter(ImageFilter.Find_Edges))
after.save("out.bmp")

