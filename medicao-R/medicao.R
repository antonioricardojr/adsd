library(dplyr, quietly=TRUE)
library(ggplot2, quietly = TRUE)

gvt35MB_jardim_tavares <- read.csv("~/Documents/adsd/medicao-R/GVT35MB-joao.txt")
gvt35MB_catole <- read.csv("~/Documents/adsd/medicao-R/GVT35MB-antonio.txt")
gvt15MB_bodocongo <- read.csv("~/Documents/adsd/gvt15MB-carol/GVT35MB-carol.txt")


summary(gvt35MB_jardim_tavares)
summary(gvt35MB_catole)
summary(gvt15MB_bodocongo)

jardim_test <- t.test(gvt35MB_jardim_tavares$time, alternative = "two.sided", conf.int=TRUE)
catole_test <- t.test(gvt35MB_catole$time, alternative = "two.sided", conf.int=TRUE)
bodocongo_test <- t.test(gvt15MB_bodocongo$time, alternative = "two.sided", conf.int=TRUE)

ic_jardim <- c(jardim_test$conf.int[1], jardim_test$conf.int[2])
ic_catole <- c(catole_test$conf.int[1], catole_test$conf.int[2])
ic_bodocongo <- c(bodocongo_test$conf.int[1], bodocongo_test$conf.int[2])

bairros <- rbind(mutate(gvt35MB_jardim_tavares, bairro="jardim tavares"), 
                       mutate(gvt35MB_catole, bairro="catole"),
                       mutate(gvt15MB_bodocongo, bairro="bodocongo"))

summary(bairros)


toPlot <- bairros %>% group_by(bairro) %>% summarise(media = mean(time, na.rm=TRUE))

toPlot = mutate(toPlot, lower = ifelse(toPlot$bairro == "catole",ic_catole[1],
                                       ifelse(toPlot$bairro == "bodocongo", ic_bodocongo[1] ,ic_jardim[1])))
toPlot = mutate(toPlot, upper = ifelse(toPlot$bairro == "catole",ic_catole[2],
                                       ifelse(toPlot$bairro == "bodocongo", ic_bodocongo[2],ic_jardim[2])))

ggplot(toPlot, aes(x = bairro, y=media, colour = bairro)) + 
  geom_point() +
  geom_errorbar(aes(ymin=lower, ymax=upper), width=.1) + theme_bw()


##JITTERS

jitters <- read.csv("~/Documents/adsd/medicao-R/Jitters.csv")


ggplot(data=jitters, aes(x=jitter, fill=bairro)) + geom_bar() + facet_wrap(~ dia) + theme_bw()


ggplot(data=jitters, aes(x=jitter, fill=bairro)) + 
  geom_freqpoly(aes(group = factor(bairro), colour = factor(bairro))) + facet_wrap(~ dia)  + theme_bw()



ggplot(data=jitters, aes(factor(bairro), jitter)) + geom_boxplot() + theme_bw() + labs(x="Bairro")

jitters_quinta <- jitters %>% filter(dia == "1-Quinta")
ggplot(data=jitters_quinta, aes(x=jitter, fill=bairro)) + geom_bar() + facet_wrap(~ bairro) + 
  labs(title="Quinta-Feira") + theme_bw()

jitters_sexta <- jitters %>% filter(dia == "2-Sexta")
ggplot(data=jitters_sexta, aes(x=jitter, fill=bairro)) + geom_bar() + facet_wrap(~ bairro) + 
  labs(title="Sexta-Feira") + theme_bw()

jitters_domingo <- jitters %>% filter(dia == "3-Domingo")
ggplot(data=jitters_domingo, aes(x=jitter, fill=bairro)) + geom_bar() + facet_wrap(~ bairro) + 
  labs(title="Domingo") + theme_bw()
