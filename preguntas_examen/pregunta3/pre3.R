# Establecer semilla para reproducibilidad
set.seed(123)

# Simular muestra de 500 datos con media 20 y desviación estándar 4
muestra <- rnorm(500, mean = 20, sd = 4)

# Calcular media y desviación estándar muestral
media_muestral <- mean(muestra)
desviacion_muestral <- sd(muestra)

# Calcular coeficiente de variación (CV)
coef_variacion <- (desviacion_muestral / media_muestral) * 100

# Mostrar resultados
cat("Media muestral:", media_muestral, "\n")
cat("Desviación estándar muestral:", desviacion_muestral, "\n")
cat("Coeficiente de variación (CV):", coef_variacion, "%\n")

# Interpretación
if (coef_variacion < 15) {
  cat("Interpretación: Hay poca dispersión relativa.\n")
} else if (coef_variacion < 30) {
  cat("Interpretación: Hay una dispersión moderada.\n")
} else {
  cat("Interpretación: Hay mucha dispersión relativa.\n")
}

