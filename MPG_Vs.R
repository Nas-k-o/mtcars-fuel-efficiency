#In this R script we will compare Miles Per Gallon variable against Horsepower, Weight and Number of Cylinders
#Plotting MPG against HP
plot(mtcars$hp, mtcars$mpg,
     main = "Miles per Gallon against Horsepower",
     ylab = "Miles per Gallon",
     xlab = "Horsepower",
     col = "steelblue",
     pch = 19,
     cex = 1.5)

abline(lm(mtcars$mpg ~ mtcars$hp), col = "red", lwd = 2)


#Plotting MPG against Weight
plot(mtcars$wt, mtcars$mpg,
     main = "Miles per Gallon against Weight",
     ylab = "Miles per Gallon",
     xlab = "Weight in TONS",
     col = "steelblue",
     pch = 19,
     cex = 1.5)

abline(lm(mtcars$mpg ~ mtcars$wt), col = "red", lwd = 2)



#Plotting MPG against CYL
plot(mtcars$cyl, mtcars$mpg,
     main = "Miles per Gallon against Number of Cylinders",
     ylab = "Miles per Gallon",
     xlab = "Number of Cylinders",
     col = "steelblue",
     pch = 19,
     cex = 1.5)
