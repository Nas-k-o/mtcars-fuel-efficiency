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
        xlab = "Engine (0 = V-shaped, 1 = Manual)",
        border = "#1abc9c", 
        horizontal = FALSE)

        