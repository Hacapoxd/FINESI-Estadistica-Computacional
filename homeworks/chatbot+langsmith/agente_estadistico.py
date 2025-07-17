import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType

# Cargar variables de entorno
load_dotenv()

# === Herramientas personalizadas para análisis estadístico ===

def prueba_t_estadistica(input_str):
    import numpy as np
    from scipy import stats
    print("[INFO] Realizando Prueba T de dos muestras...")
    grupo_a = np.random.normal(loc=50, scale=10, size=30)
    grupo_b = np.random.normal(loc=55, scale=10, size=30)
    t_stat, p_valor = stats.ttest_ind(grupo_a, grupo_b)
    return f"Estadístico t: {t_stat:.4f}, Valor p: {p_valor:.4f}"

def anova_estadistica(input_str):
    import numpy as np
    from scipy import stats
    print("[INFO] Realizando ANOVA de una vía...")
    grupo1 = np.random.normal(loc=50, scale=10, size=30)
    grupo2 = np.random.normal(loc=52, scale=10, size=30)
    grupo3 = np.random.normal(loc=58, scale=10, size=30)
    f_stat, p_valor = stats.f_oneway(grupo1, grupo2, grupo3)
    return f"Estadístico F: {f_stat:.4f}, Valor p: {p_valor:.4f}"

# === Definir herramientas ===

tools = [
    Tool(
        name="Prueba T",
        func=prueba_t_estadistica,
        description="Realiza una prueba t de dos muestras para comparar medias."
    ),
    Tool(
        name="ANOVA",
        func=anova_estadistica,
        description="Realiza un análisis de varianza (ANOVA) de una vía."
    )
]

# === Conectar con ChatGPT ===

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# === Inicializar agente ===

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
)

# === Función para interactuar con el agente ===

def chat_con_agente():
    print("💬 Bienvenido al agente estadístico conversacional. Escribe 'salir' para terminar.")
    while True:
        pregunta = input("Usuario: ")
        if pregunta.lower() in ["salir", "exit"]:
            print("👋 ¡Hasta pronto!")
            break
        respuesta = agent.invoke({"input": pregunta})
        print("Agente:", respuesta['output'])

# === Iniciar conversación ===

if __name__ == "__main__":
    chat_con_agente()
