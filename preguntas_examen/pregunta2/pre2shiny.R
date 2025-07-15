library(shiny)

ui <- fluidPage(
  titlePanel("Distribución normal estándar - Simulación y comparación"),
  sidebarLayout(
    sidebarPanel(
      numericInput("n", "Tamaño de la muestra:", value = 10000, min = 100, step = 100),
      actionButton("generar", "Generar muestra"),
      verbatimTextOutput("estadisticas")
    ),
    mainPanel(
      plotOutput("histograma")
    )
  )
)

server <- function(input, output) {
  datos <- eventReactive(input$generar, {
    rnorm(input$n, mean = 0, sd = 1)
  })
  
  output$estadisticas <- renderPrint({
    muestra <- datos()
    cat("Media muestral:", mean(muestra), "\n")
    cat("Desviación estándar muestral:", sd(muestra), "\n")
  })
  
  output$histograma <- renderPlot({
    muestra <- datos()
    hist(muestra, breaks = 50, probability = TRUE,
         main = "Histograma con curva teórica N(0,1)",
         xlab = "Valor", col = "lightblue", border = "white")
    curve(dnorm(x, mean = 0, sd = 1), col = "red", lwd = 2, add = TRUE)
    legend("topright", legend = "Curva normal teórica", col = "red", lwd = 2)
  })
}

shinyApp(ui = ui, server = server)

