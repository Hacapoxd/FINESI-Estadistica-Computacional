library(shiny)

ui <- fluidPage(
  titlePanel("Simulación y coeficiente de variación"),
  sidebarLayout(
    sidebarPanel(
      numericInput("n", "Tamaño de la muestra:", value = 500, min = 100),
      numericInput("media", "Media:", value = 20),
      numericInput("sd", "Desviación estándar:", value = 4),
      actionButton("simular", "Simular muestra"),
      br(), br(),
      verbatimTextOutput("resultados")
    ),
    mainPanel(
      plotOutput("histograma")
    )
  )
)

server <- function(input, output) {
  datos <- eventReactive(input$simular, {
    rnorm(input$n, mean = input$media, sd = input$sd)
  })
  
  output$resultados <- renderPrint({
    muestra <- datos()
    media <- mean(muestra)
    sd <- sd(muestra)
    cv <- (sd / media) * 100
    
    cat(sprintf("Media muestral: %.3f\n", media))
    cat(sprintf("Desviación estándar muestral: %.3f\n", sd))
    cat(sprintf("Coeficiente de variación (CV): %.2f%%\n", cv))
    
    if (cv < 15) {
      cat("Interpretación: Hay poca dispersión relativa.\n")
    } else if (cv < 30) {
      cat("Interpretación: Hay dispersión moderada.\n")
    } else {
      cat("Interpretación: Hay mucha dispersión relativa.\n")
    }
  })
  
  output$histograma <- renderPlot({
    muestra <- datos()
    hist(muestra, breaks = 40, col = "lightblue", border = "white",
         main = "Histograma de la muestra simulada",
         xlab = "Valores")
  })
}

shinyApp(ui = ui, server = server)

