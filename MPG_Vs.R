#In this R script we will compare Miles Per Gallon variable against Horsepower, Weight and Number of Cylinders
#Plotting MPG against HP
p <- ggplot(mtcars, aes(x = hp, y = mpg)) +
  geom_point(color = "steelblue", lwd = 3) +  
  geom_smooth(method = "lm", color = "red", size = 1.5, se = FALSE) +  
  labs(
    title = "Miles per Gallon against Horsepower",
    x = "Horsepower",
    y = "Miles per Gallon"
  ) +
  theme_minimal(base_size = 14)

print(p)

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
