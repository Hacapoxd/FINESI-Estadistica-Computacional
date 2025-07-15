# Establecer semilla para reproducibilidad
set.seed(123)

# Generar muestra de 10,000 números con distribución normal estándar
muestra <- rnorm(10000, mean = 0, sd = 1)

# Calcular estadísticos muestrales
media_muestral <- mean(muestra)
desviacion_muestral <- sd(muestra)

# Mostrar resultados
cat("Media muestral:", media_muestral, "\n")
cat("Desviación estándar muestral:", desviacion_muestral, "\n")

# Graficar histograma con curva teórica
hist(muestra, breaks = 50, probability = TRUE,
     main = "Distribución empírica vs teórica",
     xlab = "Valores", col = "lightblue", border = "white")

# Agregar curva teórica de la normal estándar
curve(dnorm(x, mean = 0, sd = 1), col = "red", lwd = 2, add = TRUE)
legend("topright", legend = c("Curva normal teórica"), col = "red", lwd = 2)

