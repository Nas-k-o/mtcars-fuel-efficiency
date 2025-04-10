#Here we will see the numbers of cars with significant differences from each other
hist(mtcars$am,
     breaks = 2,
     xlab = "Transmission type (0 - Automatic, 1 - Manuel)",
     main = "Transmission type for the 32 automobiles (1973–74 models)
     included int the 1974 Motor Trend US magazine.",
     col = "#2980b9")


hist(mtcars$vs,
     breaks = 2,
     xlab = "Engine type (0 - V-shaped, 1 - straight)",
     main = "Engine type for the 32 automobiles (1973–74 models)
     included int the 1974 Motor Trend US magazine.",
     col = "#2980b9")

automaticCars <- mtcars[mtcars$am == 0, ]
manualCars <- mtcars[mtcars$am == 1, ]

engineV <- mtcars[mtcars$vs == 0, ]
engineS <- mtcars[mtcars$vs == 1, ]
