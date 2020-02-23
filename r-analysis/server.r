#
# Web Server just for visualization
#
#

library(shiny)
library(httr)
library(jsonlite)
library(DT)

# This function takes a web API query url, carries out
# the steps of parsing and transforming the data into a dataframe.
get.data <- function() {

  geysers.df <- read.csv('../datasets/a.csv')
  return(geysers.df)
}

# Define UI for application that renders a table of geyser data.
ui <- fluidPage(
  
  # Application title
  titlePanel("Stock Dataset List"),
  
  column(12, dataTableOutput('geyser.table'))
  
)

# Define server logic required to draw a histogram
server <- function(input, output) {
  
  #TODO 2 (5pts): Create output table dataframe. Do this by calling the get.data function and pass in the url that 
  #     returns the list of all geysers (see the "Geysers" part under "GET Requests" on the api doc site).
  
  api_output <- get.data()

  output$geyser.table <- renderDataTable(api_output)
}

# Run the application 
shinyApp(ui = ui, server = server)

