#Adding the data set
data(mtcars)

#Sample look at the data set
?mtcars
head(mtcars)

#Basic graphs
#Graphing a histogram to see what are the frequencies for each main variable in the data set

#Miles per Gallon
hist(mtcars$mpg, 
     breaks = 5,
     xlab = "Miles per Gallon",
     main = "Miles per Gallon Frequencies, for 32 automobiles (1973–74 models)
     included int the 1974 Motor Trend US magazine.",
     col = "#2980b9"
     )

rug(mtcars$mpg, lwd = 2, col = 'gray')

#Horsepower
hist(mtcars$hp,
     breaks = 5,
     xlab = "HorsePower Range",
     main = "HorsePower Range Frequencies, for 32 automobiles (1973–74 models)
     included int the 1974 Motor Trend US magazine.",
     col = "#2980b9")

rug(mtcars$hp, lwd = 2, col = "#2c3e50")

#Weight
hist(mtcars$wt,
     breaks = 5,
     xlab = "Weight Range in TONS",
     main = "Weight Range Frequencies, for 32 automobiles (1973–74 models)
     included int the 1974 Motor Trend US magazine.",
     col = "#2980b9")

rug(mtcars$wt, lwd = 2, col = "#2c3e50")

#Number of Cylinders
cyl_counts <- table(mtcars$cyl)
labels <- paste(names(cyl_counts), "cyl -", round(100 * cyl_counts / sum(cyl_counts), 1), "%")
pie(cyl_counts, 
    labels = labels,
    main = "Car Counts by Cylinder for 32 automobiles (1973–74 models)
     included int the 1974 Motor Trend US magazine.", 
    col = c("#3498db", "#2ecc71", "#e74c3c"))


