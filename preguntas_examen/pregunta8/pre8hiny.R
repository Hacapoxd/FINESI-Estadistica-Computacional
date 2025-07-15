library(shiny)

ui <- fluidPage(
  titlePanel("Gráfico de dispersión de valores uniformes consecutivos"),
  sidebarLayout(
    sidebarPanel(
      numericInput("n", "Número de valores:", value = 500, min = 100, step = 100),
      actionButton("generar", "Generar valores")
    ),
    mainPanel(
      plotOutput("scatterPlot")
    )
  )
)

server <- function(input, output) {
  valores <- eventReactive(input$generar, {
    set.seed(123)
    runif(input$n, min = 0, max = 1)
  })
  
  output$scatterPlot <- renderPlot({
    x <- valores()[-length(valores())]
    y <- valores()[-1]
    
    plot(x, y,
         main = "Gráfico de dispersión: valores consecutivos (x[i] vs x[i+1])",
         xlab = expression(x[i]),
         ylab = expression(x[i+1]),
         pch = 19, col = "blue")
    abline(lm(y ~ x), col = "red", lwd = 2)
  })
}

shinyApp(ui = ui, server = server)

