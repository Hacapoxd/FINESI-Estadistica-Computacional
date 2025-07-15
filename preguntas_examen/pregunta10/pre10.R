set.seed(123)

# Parámetros
n_agentes <- 100
grid_size <- 10
pasos <- 10

# Inicializar posiciones aleatorias (coordenadas x,y entre 1 y 10)
pos_inicial <- data.frame(
  id = 1:n_agentes,
  x = sample(1:grid_size, n_agentes, replace = TRUE),
  y = sample(1:grid_size, n_agentes, replace = TRUE)
)

pos_actual <- pos_inicial

# Función para mover un agente una unidad en dirección aleatoria
mover_agente <- function(x, y, grid_size) {
  direccion <- sample(c("arriba", "abajo", "izquierda", "derecha"), 1)
  if (direccion == "arriba" && y < grid_size) y <- y + 1
  else if (direccion == "abajo" && y > 1) y <- y - 1
  else if (direccion == "izquierda" && x > 1) x <- x - 1
  else if (direccion == "derecha" && x < grid_size) x <- x + 1
  return(c(x, y))
}

# Simular movimientos en cada paso
for (t in 1:pasos) {
  for (i in 1:n_agentes) {
    nueva_pos <- mover_agente(pos_actual$x[i], pos_actual$y[i], grid_size)
    pos_actual$x[i] <- nueva_pos[1]
    pos_actual$y[i] <- nueva_pos[2]
  }
}

# Visualizar posiciones iniciales y finales
library(ggplot2)
pos_inicial$estado <- "Inicial"
pos_actual$estado <- "Final"
pos_final <- rbind(pos_inicial, pos_actual)

ggplot(pos_final, aes(x = x, y = y, color = estado)) +
  geom_point(alpha = 0.7, size = 3) +
  facet_wrap(~estado) +
  scale_x_continuous(breaks = 1:grid_size, limits = c(0.5, grid_size + 0.5)) +
  scale_y_continuous(breaks = 1:grid_size, limits = c(0.5, grid_size + 0.5)) +
  labs(title = "Posiciones iniciales y finales de 100 agentes en cuadrícula 10x10",
       x = "Coordenada X",
       y = "Coordenada Y") +
  theme_minimal()
