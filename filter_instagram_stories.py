import os
import shutil

def filtrar_stories(ruta_origen):
    if not os.path.exists(ruta_origen):
        print("La ruta especificada no existe.")
    ruta_destino = os.path.join(os.path.dirname(ruta_origen), "Instagram_Stories_filtered")
    os.makedirs(ruta_destino, exist_ok=True)
    
    for carpeta_actual, _, archivos in os.walk(ruta_origen):
        for archivo in archivos:
            if archivo.endswith(".jpg") or archivo.endswith(".mp4"):
                ruta_archivo = os.path.join(carpeta_actual, archivo)
                shutil.move(ruta_archivo, os.path.join(ruta_destino, archivo))
                print(f"Movido: {archivo}")
    
    print("Proceso completado. Archivos filtrados y movidos correctamente.")

# Ruta de la carpeta de exportación de Instagram. Dentro de ella se deben encontrar las carpetas de las historias.
ruta_exportacion = "C:" + os.sep + "Users" + os.sep + "User" + os.sep + "Downloads" + os.sep + "Instagram" + os.sep + "stories"
filtrar_stories(ruta_exportacion)
