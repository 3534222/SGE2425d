import csv
import uuid

def generar_id():
    """Genera un ID único para cada registro."""
    return str(uuid.uuid4())[:8]  # Generamos un ID único truncado

def procesar_actores(actores_str):
    """Convierte la cadena de actores separados por '-' en el formato requerido."""
    actores = actores_str.split('-')
    refs = [f"ref('{actor.strip()}')" for actor in actores]
    return f"[(6,0,[{', '.join(refs)}])]"

def transformar_csv_a_xml(csv_path, xml_path):
    try:
        with open(csv_path, 'r') as csv_file, open(xml_path, 'w') as xml_file:
            lector_csv = csv.DictReader(csv_file)
            xml_file.write('<odoo>\n')
            for i, fila in enumerate(lector_csv, start=1):
                id_registro = f"film_{i}"
                xml_file.write(f'  <record id="{id_registro}" model="videoclub.peliculas">\n')
                
                for campo in ['name', 'director', 'release', 'country', 'duration', 'rating', 'file']:
                    valor = fila.get(campo, '').strip()
                    if campo == 'director':
                        xml_file.write(f'    <field name="{campo}" ref="{valor}" />\n')
                    elif campo == 'file':
                        xml_file.write(f'    <field file="{valor}" name="cover" type="base64" />\n')
                    else:
                        xml_file.write(f'    <field name="{campo}">{valor}</field>\n')

                # Procesa los actores
                actores_xml = procesar_actores(fila.get('actors', ''))
                xml_file.write(f'    <field name="actors" eval="{actores_xml}" />\n')

                xml_file.write('  </record>\n')
            xml_file.write('</odoo>\n')
        
        print(f"Transformación completada: XML guardado en {xml_path}")

    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

# Ejecuta la función con los nombres de archivo
csv_path = "peliculas.csv"  # Nombre del archivo CSV de entrada
xml_path = "peliculas.xml"  # Nombre del archivo XML de salida
transformar_csv_a_xml(csv_path, xml_path)
