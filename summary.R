#Adding the data set
data(mtcars)

#Sample look at the data set
?mtcars
head(mtcars)

#Variables for easier use
FuelConsumption <- mtcars$mpg
HorsePower <- mtcars$hp
CarWeight <- mtcars$wt
cyl_counts <- table(mtcars$cyl)

#Basic graphs
#Graphing a histogram to see what are the frequencies for each main variable in the data set

#Miles per Gallon
hist(FuelConsumption, 
     breaks = 5,
     xlab = "Miles per Gallon",
     ylab = "Count of cars which relate",
     main = "Miles per Gallon Frequencies, for 32 automobiles (1973–74 models)
     included int the 1974 Motor Trend US magazine.",
     col = "#2980b9"
     )

rug(FuelConsumption, lwd = 2, col = '#2c3e50')

#Horsepower
hist(HorsePower,
     breaks = 5,
     xlab = "HorsePower Range",
     ylab = "Amount of cars which relate",
     main = "HorsePower Range Frequencies, for 32 automobiles (1973–74 models)
     included int the 1974 Motor Trend US magazine.",
     col = "#2980b9")

rug(HorsePower, lwd = 2, col = "#2c3e50")

#Weight
hist(CarWeight,
     breaks = 5,
     xlab = "Weight Range in TONS",
     main = "Weight Range Frequencies, for 32 automobiles (1973–74 models)
     included int the 1974 Motor Trend US magazine.",
     col = "#2980b9")

rug(CarWeight, lwd = 2, col = "#2c3e50")

#Number of Cylinders
labels <- paste(names(cyl_counts), "cyl -", round(100 * cyl_counts / sum(cyl_counts), 1), "%")
pie(cyl_counts, 
    labels = labels,
    main = "Car Counts by Cylinder for 32 automobiles (1973–74 models)
     included int the 1974 Motor Trend US magazine.", 
    col = c("#3498db", "#2ecc71", "#e74c3c"))

#Base information
#Making Graphs to describe the range of specs for the cars included in the magazine




