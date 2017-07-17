#Script used for data analysis; meant to be run line-by-line rather than executed as a whole.

library(stats)

champs <- data.frame(read.csv("Champs-Table 1.csv"))
items <- na.omit(data.frame(read.csv("Items-Table 1.csv")))
#consider only where we have reddit data


summary(champs)
summary(items)

#champs
wilcox.test(champs$Norm.Sum, champs$Reddit.Norm) #all riot vs reddit
wilcox.test(champs$Sum, champs$Reddit.Norm)
#region by region
wilcox.test(champs$KR, champs$NA.)
wilcox.test(champs$KR, champs$EUW)
wilcox.test(champs$KR, champs$EUNE)
wilcox.test(champs$EUW, champs$NA.)
wilcox.test(champs$NA.,champs$EUNE)
wilcox.test(champs$EUW, champs$EUNE)

cor.test(champs$Norm.Sum, champs$Reddit.Norm, method="kendall")
cor.test(champs$Sum, champs$Reddit.Norm, method = "kendall")

cor.test(champs$KR, champs$NA., method="kendall")
cor.test(champs$KR, champs$EUW, method="kendall")
cor.test(champs$KR, champs$EUNE, method="kendall")
cor.test(champs$EUW, champs$NA., method="kendall")
cor.test(champs$EUNE, champs$NA., method="kendall")
cor.test(champs$EUW, champs$EUNE, method="kendall")

#cf reddit
wilcox.test(champs$KR, champs$Reddit.Norm)
wilcox.test(champs$NA., champs$Reddit.Norm)
wilcox.test(champs$EUW, champs$Reddit.Norm)
wilcox.test(champs$EUNE, champs$Reddit.Norm)

cor.test(champs$KR, champs$Reddit.Norm, method="kendall")
cor.test(champs$NA., champs$Reddit.Norm, method="kendall")
cor.test(champs$EUW, champs$Reddit.Norm, method="kendall")
cor.test(champs$EUNE, champs$Reddit.Norm, method="kendall")

#items
wilcox.test(items$Norm.Sum, items$Reddit.Norm) #all riot vs reddit
wilcox.test(items$Sum, items$Reddit.Norm)

#region by region
wilcox.test(items$KR, items$NA.)
wilcox.test(items$KR, items$EUW)
wilcox.test(items$KR, items$EUNE)
wilcox.test(items$EUW, items$NA.)
wilcox.test(items$NA.,items$EUNE)
wilcox.test(items$EUW, items$EUNE)

cor.test(items$Norm.Sum, items$Reddit.Norm, method="kendall")
cor.test(items$Sum, items$Reddit.Norm, method="kendall")

cor.test(items$KR, items$NA., method="kendall")
cor.test(items$KR, items$EUW, method="kendall")
cor.test(items$KR, items$EUNE, method="kendall")
cor.test(items$EUW, items$NA., method="kendall")
cor.test(items$EUNE, items$NA., method="kendall")
cor.test(items$EUW, items$EUNE, method="kendall")

#cf reddit
wilcox.test(items$KR, items$Reddit.Norm)
wilcox.test(items$NA., items$Reddit.Norm)
wilcox.test(items$EUW, items$Reddit.Norm)
wilcox.test(items$EUNE, items$Reddit.Norm)

cor.test(items$KR, items$Reddit.Norm, method="kendall")
cor.test(items$NA., items$Reddit.Norm, method="kendall")
cor.test(items$EUW, items$Reddit.Norm, method="kendall")
cor.test(items$EUNE, items$Reddit.Norm, method="kendall")

#subreddit comparisons
wilcox.test(champs$r.leagueoflegends, champs$Reddit.Norm)
wilcox.test(champs$r.leagueoflegendsmeta, champs$Reddit.Norm)
wilcox.test(champs$r.summonerschool, champs$Reddit.Norm)

cor.test(champs$r.leagueoflegends, champs$Reddit.Norm, method="kendall")
cor.test(champs$r.leagueoflegendsmeta, champs$Reddit.Norm, method="kendall")
cor.test(champs$r.summonerschool, champs$Reddit.Norm, method="kendall")

wilcox.test(champs$r.leagueoflegends, champs$Reddit.Norm)
wilcox.test(champs$r.leagueoflegendsmeta, champs$Reddit.Norm)
wilcox.test(champs$r.summonerschool, champs$Reddit.Norm)

cor.test(champs$r.leagueoflegends, champs$Sum, method="kendall")
cor.test(champs$r.leagueoflegendsmeta, champs$Sum, method="kendall")
cor.test(champs$r.summonerschool, champs$Sum, method="kendall")

#items
wilcox.test(items$r.leagueoflegends, items$Reddit.Norm)
wilcox.test(items$r.leagueoflegendsmeta, items$Reddit.Norm)
wilcox.test(items$r.summonerschool, items$Reddit.Norm)

cor.test(items$r.leagueoflegends, items$Reddit.Norm, method="kendall")
cor.test(items$r.leagueoflegendsmeta, items$Reddit.Norm, method="kendall")
cor.test(items$r.summonerschool, items$Reddit.Norm, method="kendall")

wilcox.test(items$r.leagueoflegends, items$Reddit.Norm)
wilcox.test(items$r.leagueoflegendsmeta, items$Reddit.Norm)
wilcox.test(items$r.summonerschool, items$Reddit.Norm)

cor.test(items$r.leagueoflegends, items$Sum, method="kendall")
cor.test(items$r.leagueoflegendsmeta, items$Sum, method="kendall")
cor.test(items$r.summonerschool, items$Sum, method="kendall")

