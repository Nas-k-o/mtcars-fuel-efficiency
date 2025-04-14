#Adding the data set
data(mtcars)

#Loading package
install.packages("psych")
install.packages("dplyr")
p_load("psych")
library(ggplot2)
library(dplyr)
library(gridExtra)

#Sample look at the data set
?mtcars
head(mtcars)


#Factoring the data in a new data frame
engine <- as.factor(mtcars$vs)
transmission <- as.factor(mtcars$am)
gear <- as.factor(mtcars$gear)
carb <- as.factor(mtcars$carb)
cyl <- as.factor(mtcars$cyl)
Automobiles <- data.frame(engine, transmission, gear, carb, cyl)
str(Automobiles)


#Variables for easier use
FuelConsumption <- mtcars$mpg
HorsePower <- mtcars$hp
CarWeight <- mtcars$wt
cyl_counts <- table(mtcars$cyl)
QuarterMile <- mtcars$qsec
Engine <- mtcars$vs
Transmission <- mtcars$am

#Basic graphs
#Graphing a histogram to see what are the frequencies for each main variable in the data set

#Miles per Gallon
hist(FuelConsumption, 
     breaks = 5,
     xlab = "Miles per Gallon",
     ylab = "Amount of Automobiles",
     main = "Miles per Gallon Frequencies, for 32 automobiles (1973–74 models)
     included int the 1974 Motor Trend US magazine.",
     col = "steelblue",
     pch = 19,
     cex = 1.5
)
grid(nx = NULL, ny = NULL, col = "#8e44ad", lty = "dotted", lwd = 2)
rug(FuelConsumption, lwd = 2, col = '#2c3e50')

#Horsepower
hist(HorsePower,
     breaks = 5,
     xlab = "HorsePower Range",
     ylab = "Amount of cars which relate",
     main = "HorsePower Range Frequencies, for 32 automobiles (1973–74 models)
     included int the 1974 Motor Trend US magazine.",
     col = "steelblue",
     pch = 19,
     cex = 1.5)
grid(nx = NULL, ny = NULL, col = "#8e44ad", lty = "dotted", lwd = 2)
rug(HorsePower, lwd = 2, col = "#2c3e50")

#Weight
hist(CarWeight,
     breaks = 5,
     xlab = "Weight Range in TONS",
     main = "Weight Range Frequencies, for 32 automobiles (1973–74 models)
     included int the 1974 Motor Trend US magazine.",
     col = "steelblue",
     pch = 19,
     cex = 1.5)
grid(nx = NULL, ny = NULL, col = "#8e44ad", lty = "dotted", lwd = 2)
rug(CarWeight, lwd = 2, col = "#2c3e50")

#Number of Cylinders
labels <- paste(names(cyl_counts), "cyl -", cyl_counts)
pie(cyl_counts, 
    labels = labels,
    main = "Car Counts by Cylinder for 32 automobiles (1973–74 models)
     included int the 1974 Motor Trend US magazine.", 
    col = c("#3498db", "#2ecc71", "#e74c3c"))


#Defining summaries
summary(mtcars)
write.csv(summary(mtcars), "Summary.csv")
#-------------------------------------------------------#
summary(fastestCars)
summary(SlowerCars)
write.csv(summary(fastestCars), "fastestCarsSummary.csv")
write.csv(summary(SlowerCars), "slowerCarsSummary.csv")
#---------------------------------------------------------#
summary(automaticCars)
summary(manualCars)
write.csv(summary(automaticCars), "automaticCarsSummary.csv")
write.csv(summary(manualCars), "manualCarsSummary.csv")
#--------------------------------------------------------#
summary(engineV)
summary(engineS)
write.csv(summary(engineV), "engineVSummary.csv")
write.csv(summary(manualCars), "engineSSummary.csv")

plot(mtcars$mpg, mtcars$hp)


#Summarizing and Quantifying the median of categorical variables
am_summary <- mtcars %>%
  group_by(am) %>%
  summarize(median_mpg = median(mpg))
am_summary

vs_summary <- mtcars %>%
  group_by(vs) %>%
  summarise(median_mpg = median(mpg))
vs_summary

