def chatbot():
    print("🤖 ¡Hola! Soy el chatbot de Harrison Capia.")
    print("Puedes preguntarme sobre sus proyectos, habilidades o contacto.")
    print("Escribe 'salir' para terminar.\n")

    while True:
        entrada = input("Usuario: ").lower()

        if "hola" in entrada or "hi" in entrada:
            print("Hola, ¿en qué puedo ayudarte?\n")

        elif "habilidades" in entrada or "tecnologías" in entrada:
            print("Habilidades y tecnologías:")
            print("- R: ggplot2, dplyr, caret, shiny")
            print("- Python: pandas, matplotlib, scikit-learn, seaborn")
            print("- Modelos estadísticos: regresión, pruebas de hipótesis, bootstrap")
            print("- SQL y bases de datos relacionales (MySQL, SQLite)")
            print("- Visualización de datos y dashboards")
            print("- Automatización de tareas y reportes")
            print("- Introducción a IA y aprendizaje automático\n")

        elif "proyecto" in entrada:
            print("Proyectos académicos:")
            print("- Prueba t-student + ANOVA: Análisis estadístico comparativo entre grupos usando R")
            print("- Pruebas_Estadisticas_shiny: Aplicación web en R Shiny")
            print("- agente_gatos: Simulación de un agente inteligente")
            print("- ia_aplicacion: Aplicación con IA en Python")
            print("- prueba T-student: Evaluación de diferencias de medias")
            print("- random_pack: Generación y análisis de datos aleatorios\n")

        elif "contacto" in entrada:
            print("Correo: hacapoxd@gmail.com")
            print("LinkedIn: harricapiat")
            print("Web: hacapoxd.github.io/Finesi-lp3\n")

        elif "salir" in entrada or "exit" in entrada:
            print("👋 ¡Gracias por tu visita! Hasta pronto.")
            break

        else:
            print("Lo siento, no entiendo tu pregunta. Puedes preguntar sobre habilidades, proyectos o contacto.\n")

# Iniciar el chatbot
if __name__ == "__main__":
    chatbot()
