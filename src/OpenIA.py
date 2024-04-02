from OpenIA import openai, Error
import readline
import sys

api_key = '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'
ultima_consulta = ""
buffer_consultas = []

def consultar_chatGPT(consulta):
    try:
        # Formatear la consulta con "You:" antes de enviarla
        consulta_formateada = "You: " + consulta
        
        # Llamar al API de chatGPT
        respuesta = openai.Completion.create(
            engine="davinci",
            prompt=consulta_formateada,
            max_tokens=100
        )
        
        # Obtener la respuesta del modelo
        respuesta_formateada = respuesta.choices[0].text.strip()
        
        # Imprimir la respuesta formateada con "chatGPT:"
        print("chatGPT:", respuesta_formateada)
        
        # Agregar la respuesta al buffer de consultas
        buffer_consultas.append(respuesta_formateada)
    except Error as e:
        print("Se produjo un error al llamar al API de OpenAI:", e)

def obtener_ultima_consulta():
    global ultima_consulta
    return ultima_consulta

def main():
    global buffer_consultas
    conversacion = False
    
    # Verificar si se ha proporcionado el argumento --convers
    if len(sys.argv) > 1 and sys.argv[1] == "--convers":
        conversacion = True
    
    while True:
        try:
            # Leer la consulta del usuario
            entrada = input("Ingrese su consulta (o 'salir' para terminar): ")
            
            # Si el usuario presiona la tecla "Cursor Up", recuperar la última consulta realizada
            if entrada == "":
                entrada = obtener_ultima_consulta()
            
            # Verificar si el usuario quiere salir
            if entrada.lower() == 'salir':
                print("Saliendo del programa...")
                break
            
            # Verificar si la consulta tiene texto
            if entrada:
                # Actualizar la última consulta realizada
                global ultima_consulta
                ultima_consulta = entrada
                
                # Imprimir el contenido de la consulta
                print("Consulta:", entrada)
                
                # Invocar el API de chatGPT con la consulta
                consultar_chatGPT(entrada)
                
                # Si se está en modo conversación, utilizar el buffer de consultas
                if conversacion:
                    for consulta in buffer_consultas:
                        consultar_chatGPT(consulta)
            else:
                print("La consulta está vacía.")
        except KeyboardInterrupt:
            print("\nOperación interrumpida por el usuario.")
            break
        except Exception as e:
            print("Se produjo un error durante la ejecución:", e)

if __name__ == "__main__":
    openai.api_key = api_key
    main()
