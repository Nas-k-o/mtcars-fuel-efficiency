#Here we will compare speed stats
#Histogram to show the performances of cars in 1/4 mile test in range of seconds 
hist(mtcars$qsec,
     breaks = 5,
     main = "performances of automobiles in 1/4 mile test
     from the 1974 Motor Trend US magazine",
     xlab = "Range of time in seconds",
     col = "steelblue",
     pch = 19,
     cex = 1.5)
grid(nx = NULL, ny = NULL, col = "#8e44ad", lty = "dotted", lwd = 2)
rug(mtcars$qsec, lwd = 2, col = "#34495e")

#Comparing the results based on Horsepower
plot(mtcars$hp,mtcars$qsec,
     main = "performances of automobiles in 1/4 mile test
     against their horsepower
     from the 1974 Motor Trend US magazine",
     xlab = "Horsepower",
     ylab = "Result of 1/4 mile test (in seconds)",
     col = "steelblue",
     pch = 19,
     cex = 1.5) 

abline(lm(mtcars$hp ~ mtcars$qsec), col = "red", lwd = 2)


#Comparing the results based on Weight
plot(mtcars$wt,mtcars$qsec,
     main = "performances of automobiles in 1/4 mile test
     against their horsepower
     from the 1974 Motor Trend US magazine",
     xlab = "WEIGHT IN TONS",
     ylab = "Result of 1/4 mile test (in seconds)",
     col = "steelblue",
     pch = 19,
     cex = 1.5)

#Comparing The results based on Cylinders
plot(mtcars$cyl,mtcars$qsec,
     main = "performances of automobiles in 1/4 mile test
     against their horsepower
     from the 1974 Motor Trend US magazine",,
     xlab = "Number of Cylinders",
     ylab = "Result of 1/4 mile test (in seconds)",
     col = "steelblue",
     pch = 19,
     cex = 1.5)

#Comparing the results against gear style
boxplot(mtcars$qsec ~ mtcars$am,
        main = "Performances of Automobiles in 1/4 Mile Test
        Against Their Transmission Type",
        pch = 19,
        col = c("#2980b9", "#e74c3c"), 
        ylab = "Result of 1/4 Mile Test (in seconds)",
        xlab = "Transmission (0 = Automatic, 1 = Manual)",
        border = "#1abc9c", 
        horizontal = FALSE,)

#Comparing against Engine Type
boxplot(mtcars$qsec ~ mtcars$vs,
        main = "Performances of Automobiles in 1/4 Mile Test
        Against Their Engine Type",
        pch = 19,
        col = c("#2980b9", "#e74c3c"), 
        ylab = "Result of 1/4 Mile Test (in seconds)",
        xlab = "Engine (0 = V-shaped, 1 = Straight)",
        border = "#1abc9c", 
        horizontal = FALSE)

#Making Graphs to describe the 1/4 mile performance based on specs for the cars included in the magazine
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
     ylab = "Gross Horsepower",
     xlab = "1/4 Mile time in seconds",
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
        