#Adding the data set
data(mtcars)

#Loading package
install.packages("psych")
p_load("psych")

#Sample look at the data set
?mtcars
head(mtcars)

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
     ylab = "Count of cars which relate",
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
labels <- paste(names(cyl_counts), "cyl -", round(100 * cyl_counts / sum(cyl_counts), 1), "%")
pie(cyl_counts, 
    labels = labels,
    main = "Car Counts by Cylinder for 32 automobiles (1973–74 models)
     included int the 1974 Motor Trend US magazine.", 
    col = c("#3498db", "#2ecc71", "#e74c3c"))


#Making Graphs to describe the 1/4 mile performance based on specs for the cars included in the magazine
table <- describe(mtcars)
print(table)

fastestCars <- mtcars[mtcars$qsec <= 17.85, ]
SlowerCars <- mtcars[mtcars$qsec > 17.85, ]

hist(fastestCars$qsec,
     main = "Best results of the 1/4 mile test (below average), for 32 automobiles (1973–74 models)
     included int the 1974 Motor Trend US magazine.",
     xlab = "BEST TIME (range in seconds)",
     ylab = "Count of Automobiles",
     col = "steelblue",
     pch = 19,
     cex = 1.5)
grid(nx = NULL, ny = NULL, col = "#8e44ad", lty = "dotted", lwd = 2)
rug(QuarterMile, lwd = 2, col = "#2c3e50")

plot(Engine[mtcars$qsec <= 17.85], fastestCars$qsec, xaxt = "n",
     main = "Engine type of the best performing automobiles
     included in the 1974 Motor Trend US magazine",
     xlab = "Engine Type",
     ylab = "1/4 Mile time in seconds",
     col = "steelblue",
     pch = 19,
     cex = 1.5)
axis(side = 1, at = c(0, 1), labels = c("V-shaped", "Straight"))

plot(Transmission[mtcars$qsec <= 17.85], fastestCars$qsec, xaxt = "n",
     main = "Engine type of the best performing automobiles
     included in the 1974 Motor Trend US magazine",
     xlab = "Transmission Type",
     ylab = "1/4 Mile time in seconds",
     col = "steelblue",
     pch = 19,
     cex = 1.5)
axis(side = 1, at = c(0, 1), labels = c("Automatic", "Manual"))

plot(fastestCars$qsec, HorsePower[mtcars$qsec <= 17.85],
     main = "GROSS Horsepower of the best performing automobiles
     included in the 1974 Motor Trend US magazine",
     xlab = "Gross Horsepower",
     ylab = "1/4 Mile time in seconds",
     col = "steelblue",
     pch = 19,
     cex = 1.5)

plot(fastestCars$qsec, CarWeight[mtcars$qsec <= 17.85],
     main = "Weight in TONS of the best performing automobiles
     included in the 1974 Motor Trend US magazine",
     ylab = "Weight in TONS",
     xlab = "1/4 Mile time in seconds",
     col = "steelblue",
     pch = 19,
     cex = 1.5)


hist(SlowerCars$qsec,
     main = "Above average results of the 1/4 mile test, for 32 automobiles (1973–74 models)
     included int the 1974 Motor Trend US magazine.",
     xlab = "TIME (range in seconds)",
     ylab = "Count of Automobiles",
     col = "steelblue",
     pch = 19,
     cex = 1.5)
grid(nx = NULL, ny = NULL, col = "#8e44ad", lty = "dotted", lwd = 2)
rug(QuarterMile, lwd = 2, col = "#2c3e50")

plot(Engine[mtcars$qsec > 17.85], SlowerCars$qsec, xaxt = "n",
     main = "Engine type of the comparable slower performing automobiles
     included in the 1974 Motor Trend US magazine",
     xlab = "Engine Type",
     ylab = "1/4 Mile time in seconds")
axis(side = 1, at = c(0, 1), labels = c("V-shaped", "Straight"))

plot(Transmission[mtcars$qsec > 17.85], SlowerCars$qsec, xaxt = "n",
     main = "Engine type of the comparable slower performing automobiles
     included in the 1974 Motor Trend US magazine",
     xlab = "Transmission Type",
     ylab = "1/4 Mile time in seconds")
axis(side = 1, at = c(0, 1), labels = c("Automatic", "Manual"))

plot(SlowerCars$qsec, HorsePower[mtcars$qsec > 17.85],
     main = "GROSS Horsepower of the comparable slower performing automobiles
     included in the 1974 Motor Trend US magazine",
     ylab = "Gross Horsepower",
     xlab = "1/4 Mile time in seconds",
     col = "steelblue",
     pch = 19,
     cex = 1.5)

plot(SlowerCars$qsec, CarWeight[mtcars$qsec > 17.85],
     main = "Weight in TONS of the comparable slower performing automobiles
     included in the 1974 Motor Trend US magazine",
     ylab = "Weight in TONS",
     xlab = "1/4 Mile time in seconds",
     col = "steelblue",
     pch = 19,
     cex = 1.5)
