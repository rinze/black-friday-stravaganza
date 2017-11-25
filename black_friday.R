library(ggplot2)
theme_set(theme_bw(16))


elmundo <- data.frame(date = 2008:2017,
                      n = c(1, 1, 6, 7, 8, 12, 22, 74, 80, 71),
                      journal = "elmundo.es")

elpais <- data.frame(date = 2008:2017,
                     n = c(1, 1, 2, 3, 6, 8, 28, 80, 84, 104),
                     journal = "elpais.com")

abc <- data.frame(date = 2008:2017,
                  n = c(1, 0, 4, 17, 17, 19, 28, 54, 109, 135),
                  journal = "abc.es")

all <- rbind(elmundo, elpais, abc)

plt1 <- ggplot(all, aes(x = date, y = n, color = journal)) + 
    geom_line(size = 1.3) +
    geom_point(size = 3) +
    scale_color_brewer(palette = "Set1", name = "Panfleto") +
    scale_x_continuous(breaks = 2008:2017) +
    scale_y_continuous(breaks = seq(0, 150, 20)) +
    ylab("Número de artículos publicados con la cadena \"black friday\"") +
    xlab("Año") +
    ggtitle("Hasta el infinito y más allá, 2008 - 2017",
            subtitle = "La tarjeta de crédito como sustituto del DNI")
plot(plt1)
