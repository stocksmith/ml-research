# Analysis
a <- read.csv("../datasets/A.csv")
dim(a)
head(a, 5)

plot(a$date, a$open, xlab="dates", ylab="stock price-opening")
plot(a$date, a$close, xlab="dates", ylab="stock price-closing")

fit.1 <- lm(close ~ open, data=a) 
summary(fit.1)
coef(fit.1)

a.gg <- a[, c("volume", "high", "low", "open", "close", "adjclose")]
ggpairs(data=a.gg)

