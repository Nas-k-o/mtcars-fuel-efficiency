#In this R script we will compare Miles Per Gallon variable against Horsepower, Weight and Number of Cylinders
#Plotting MPG against HP
MPG_HP <- ggplot(mtcars, aes(x = hp, y = mpg)) +
  geom_point(color = "steelblue", lwd = 3) +  
  geom_smooth(method = "lm", color = "red", size = 1.5, se = TRUE) +  
  labs(
    title = "Miles per Gallon against Horsepower",
    x = "Horsepower",
    y = "Miles per Gallon"
  ) +
  theme_minimal(base_size = 14)

print(MPG_HP)

#Plotting MPG against Weight
MPG_WT <- ggplot(mtcars, aes(x = wt, y = mpg))+
  geom_point(color = "steelblue", lwd = 3) +
  geom_smooth(method = "lm", color = "red", size = 1,5, se = FALSE) +
  labs(
    title = "Miles per Gallon against WEIGHT in TONS",
    x = "Weight in TONS",
    y = "Miles per Gallon"
  ) +
  theme_minimal(base_size = 14)

print(MPG_WT)

#Plotting MPG against CYL
plot(mtcars$cyl, mtcars$mpg,
     main = "Miles per Gallon against Number of Cylinders",
     ylab = "Miles per Gallon",
     xlab = "Number of Cylinders",
     col = "steelblue",
     pch = 19,
     cex = 1.5)
