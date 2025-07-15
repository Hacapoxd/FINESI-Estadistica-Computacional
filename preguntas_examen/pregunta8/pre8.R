set.seed(123)

# Simular 500 valores uniformes entre 0 y 1
valores <- runif(500, min = 0, max = 1)

# Preparar datos para gráfico de dispersión x[i] vs x[i+1]
x <- valores[-length(valores)]     # Todos menos el último
y <- valores[-1]                   # Todos menos el primero

# Graficar
plot(x, y,
     main = "Gráfico de dispersión: valores consecutivos (x[i] vs x[i+1])",
     xlab = expression(x[i]),
     ylab = expression(x[i+1]),
     pch = 19, col = "blue")
abline(lm(y ~ x), col = "red", lwd = 2) # Línea de regresión para referencia

