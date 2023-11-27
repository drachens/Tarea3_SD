import wikipediaapi
import os
import requests

def get_links(page):
    counter = 30
    pages = []
    links = page.links
    o = True
    while o:
        for title in sorted(links.keys()):
            if counter > 0:
                titulo = title.replace(" ","_")
                pages.append(titulo)
                counter = counter - 1
            else:
                o = False
                break
    return pages

wiki_wiki = wikipediaapi.Wikipedia(
    user_agent='Tarea3SD (merlin@example.com)', 
    language='en',
    extract_format=wikipediaapi.ExtractFormat.WIKI
    )
page_py = wiki_wiki.page('Roman_Empire')
links = get_links(page_py)

p_wiki = wiki_wiki.page(links[0])
print(p_wiki.text)
#Crear carpetas
for i in range(2):
    nombre_carpeta=f"carpeta_{i+1}"
    ruta_carpeta = os.path.join(os.getcwd(), nombre_carpeta)

    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)
        print(f"Se ha creado la carpeta '{nombre_carpeta}'.")
    else:
        print(f"La carpeta '{nombre_carpeta}' ya existe.")


count = 0
for i in range(2):
    nombre_carpeta = f"carpeta_{i+1}"
    ruta_carpeta = os.path.join(os.getcwd(), nombre_carpeta)
    for i in range(15):
        nombre_archivo = f"Documento_{count+1}.txt"
        archivo_ruta = os.path.join(ruta_carpeta,nombre_archivo)
        pagina = wiki_wiki.page(links[count])
        if not os.path.exists(archivo_ruta):
            with open(archivo_ruta,"w", encoding="utf-8") as archivo:
                archivo.write(pagina.text)
                print(f"Se ha creado el archivo '{nombre_archivo}' dentro de '{nombre_carpeta}'")
        else:
            print(f"El archivo '{nombre_archivo}' ya existe dentro de '{nombre_carpeta}'")
        count = count + 1
        

#print(links)
