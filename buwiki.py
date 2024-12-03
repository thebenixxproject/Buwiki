import wikipedia

# Función para realizar la búsqueda en Wikipedia
def buscar_wikipedia(termino, idioma="es"):
    try:
        # Cambiar el idioma de Wikipedia
        wikipedia.set_lang(idioma)
        
        # Realiza una búsqueda en Wikipedia usando el término dado
        resultado = wikipedia.summary(termino, sentences=2)  # Obtiene las primeras 2 oraciones
        print(f"\nResults for '{termino}' in {idioma.upper()}:\n")
        print(resultado)
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Disambiguation founded: {e.options}")
    except wikipedia.exceptions.HTTPTimeoutError:
        print("Timeout. Please try again.")
    except wikipedia.exceptions.RedirectError:
        print("Redirection founded. No information could be obtained.")
    except wikipedia.exceptions.PageError:
        print(f"No information found about'{termino}'.")
    except wikipedia.exceptions.RequestError as e:
        print(f"Error in the request: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Función principal para interactuar con el usuario
def main():
    print("Hi, this is the Wikipedia library. Type a word and you'll find it on Wikipedia in seconds!")
    print("READ THIS: es: Español, en: English, fr: Français, de: Deutsch, it: Italiano, pt: Português.")
    while True:
        # Pide el idioma al usuario
        idioma = input("\nSelect your language: ")
        if idioma == "":
            idioma = "es"  # Por defecto, español si no se ingresa nada
            
        termino = input("\nWhat term are you searching for? (or type 'exit' to end): ")
        if termino.lower() == "exit":
            print("¡Bye!")
            break
        else:
            buscar_wikipedia(termino, idioma)

# Ejecutar el bot
if __name__ == "__main__":
    main()
