# League of Legends Build Choices Reflected in Reddit Comments and Game Data
Final paper written for Cluster Computing class in spring 2016

## Abstract
In the game League of Legends, players’ in-game choices of champions and items are widely considered a route to mastery.  Discussion of which choices are best often takes place on forums such as Reddit, while Riot Games’ development API allows for analysis of what players actually choose.  However, most analyses focus separately on play patterns of the highest ranked players only, with no connection to discussion.  In this paper I compare mentions of champions and items in Reddit comments to their in-game use across four regions of play data.  To do so, I use analysis scripts written in Spark and run on a Hadoop cluster to efficiently process large amounts of game and comment data.

My results show small but significant correlations between Reddit data and real game choices, particularly for champions.  

## Background
### League of Legends
League of Legends is a free-to-play session-based multiplayer online battle arena game developed and operated by Riot Games (Riot Games, 2016a). The developers claim it is both the largest online gaming community and most active competitive eSport.  The most popular mode, Summoner’s Rift, is a matchup between two five-person teams each attempting to break the nexus in the enemy team’s base.  Games in this mode can be either ranked (competitive, with statistics tracking; players are assigned ranks which change based on their wins and losses) or normal (casual, players have a hidden matchmaking for matchmaking purposes but no formal ranking)  (Riot Games, 2016b).

For each game, players choose a single champion to play.  Champions represent characters in the game world who serve as the player’s avatar for the duration of the game.  Different champions have different strengths and weaknesses, as well as different abilities which make them more and less suited for different roles in the team.  Over the course of the game, the player earns gold by killing enemies and breaking enemy structures.  This gold can then be spent on a variety of items which will increase the champion’s strengths and/or perform some action when activated.  Since the game is session-based, the choice of items happens anew every game (Riot Games, 2016b).  The choice of items, and which items best suit which champions (referred to as a champion’s “build”), is one of the game’s main avenues for mastery and therefore a significant subject for discussion among the playerbase  (League of Legends, 2015).

Riot Games offers free, rate-limited access to a variety of game data, including detailed statistics for games in the ranked mode.  These data are used by a variety of web apps to convey various statistics to players, such as the player and their teammates’ and opponents’ performance history such as OP.GG (n.d.), or the choices most common among highly skilled players of the game such as LoLMasters (Gicos, n.d.) or  Pro Builds (SoloMid, 2009).  

### Reddit
Reddit is a massive online community composed of many discussion forums known as subreddits.  The primary subreddit for League of Legends, /r/leagueoflegends, has over 800,000 subscribers and is a center for the game’s community (League of Legends, n.d.)  There exist other subreddits for the game, including several focusing on mastery of in-game choices, such as /r/LeagueOfLegendsMeta/ (LoL Meta, n.d.) and /r/SummonerSchool (Summoner School, n.d.).  Riot developers have said that the Reddit community is “a hardcore demographic” (Lin, 2015b), but “isn’t really a representative sample of the overall playerbase” (Lin, 2015a).

I use a dataset representing Reddit comments from 2015, themselves a part of a larger corpus ranging from 2006-2015.  Data were pulled from the Reddit API and stored as compressed JSON files.  (Stuck\_In\_The\_Matrix, 2015).  

### Spark
Spark is a “fast, large-scale data processing engine” (Hortonworks) for cluster computing.  It combines the MapReduce paradigm with resilient distributed datasets which allow for greater scalability, reliability, and fault-tolerance (Zaharia et al, 2010).  While the primary implementation is in Scala, bindings to other languages exist; I used the Python binding PySpark for this project.  

## Methods
Reddit data were taken from a subset of the larger Reddit corpus, representing only 2015 and missing the month of July.  Processing of the Reddit comments was done on a cluster via Spark.  Comments from the subreddits LeagueOfLegends, LeagueOfLegendsMeta, and summonerschool were extracted and checked for names of champions and items.  Lists of common champion and item nicknames were compiled from my domain knowledge and used to extract more references.   Certain items were omitted: those that are specifically locked to a champion, such as Viktor’s Hex Core and Kalista’s Black Spear, boot enchantments, wards, warding totems, and items for modes other than Summoner’s Rift.  These items were excluded because they were too specific (champion only items), hard to correlate with their base item (boots plus their enchantments, which are listed as separate items in the Riot data), too general (wards and warding totems), or not relevant to the Riot data (non-SR items).  

Riot data were collected via the Riot Games Developer API (Riot Games, 2015), using the open-source Python library Cassiopeia (Meraki Analytics, 2016) to pull data and a SQLite database for data storage.  Data collection was performed on a single local machine as the cluster’s SQLite install was incompatible with Cassiopeia.  A total of 2.1 GB of match data was collected from the North American, Korean, European (West), and European (Northeast) servers, most of it from North America and Europe (West), representing a total of 28,450 matches.  The number of matches per region is displayed in the following table: 

|Region|NA|KR|EUW|EUNE|
|---|---|---|---|---|
|Matches|9716|5135|10337|3262|

Table 1: Matches per region.

For NA, this represents only ranked 5v5 matches; while the other regions ostensibly follow the same pattern and received the same requests, the presence of 3v3-only items in the match data suggests that some ranked 3v3 matches were pulled from those regions.  

After data collection, the champion and item usage statistics were pulled from the database and compiled via Spark on the cluster.  Information provided by Riot was used to convert the champion and item listings back to their canonical names.  

## Results
Rank correlation tests showed strong correlations between the Reddit and the Riot data, as well as across regions within the Riot data.  Results were significant for champions on both a Mann-Whitney and Kendall tau rank correlation test. (Mann-Whitney: W = 17161, p-value <2.2 x 10-16 ; Kendall tau: p-value 6.728 x 10-16, τ = 0.4423)  Results for items were also significant as long as rows with no available Reddit data were excluded, but at a much lower tau. (Mann-Whitney: W = 5929, p-value <2.2 x 10-16 ; Kendall tau: p-value = 0.0094, τ = 0.2570 )  These results remained significant when results for each region were normed before adding, weighting all the regions equally despite the different number of games for each.  

Correlations between the regions were also significant, with the exception that for both champions and items the Mann-Whitney test showed a non-significant p-value of 0.6615 (champions) and 0.9065 (items) between Europe West and North America, though the Kendall tau was still significant between the two at p < 2.2 x 10-16 for both.  It is unclear why this result arose, as each region in question is significantly correlated with the other regions and there is no known reason for the metagame in Western Europe and North America to be more different than between other regions.  Between regions, the tau for items was often stronger than the tau for champions, while the opposite was typically true when comparing to the Reddit data.


||NA|KR|EUW|EUNE|
|---|---|---|---|---|
|NA|	1||||			
|KR|	0.7239|1|||		
|EUW|	0.8039|0.7516|1||	
|EUNE|	0.6959|0.5968|0.6607|1|

Table 2: Kendall Tau between regions for Riot data on champions.

||NA|KR|EUW|EUNE|
|---|---|---|---|---|
|NA|	1||||		
|KR|	0.8356|1|||		
|EUW|	0.9139|0.8259|1||	
|EUNE|	0.8961|0.8096|0.8756|1|

Table 3: Kendall Tau between regions for Riot data on items.

Correlations were also computed between each individual region’s game data and the Reddit data.  These were significant for all regions on both tests, though with higher tau for champions than for items.  

|Region|cf Reddit (Champions)|cf Reddit (Items)|
|---|---|---|
|NA|	0.4662|	0.2686|
|KR|	0.3683|	0.2598|
|EUW|	0.4179|	0.2454|
|EUNE|	0.4804|	0.2727|

Table 4: Kendall Tau between each region’s Riot data and the Reddit data.

Correlations were also computed between each of the contributing subreddits and the total Reddit data, as well as between each subreddit and the aggregate champion and item data.  As would be expected given the much greater size of /r/leagueoflegends, it had a much higher correlation with the total, indicating it likely contributed most of the content.  For champions, the highest tau between a subreddit and items was for the larger /r/leagueoflegends subreddit, while for items it was for /r/summonerschool.  All correlations had significant p-values.  

|Subreddit|Champions	|Items|
|---|---|---|
|leagueoflegends|	0.4365	|0.2085|
|leagueoflegendsmeta|0.3706	|0.2496|
|summonerschool|	0.4067	|0.2943|

Table 5: Kendall Tau between each subreddit’s data and the total Riot data.	

## Discussion

The significant correlations between the Riot and Reddit data support the hypothesis that Reddit mentions have some predictive value for actual in-game choices.  However, the low Kendall tau, particularly for items, also supports the developers’ assertion that what’s discussed on Reddit is not fully representative of the wider League of Legends playerbase. 
	
The much better correlation between different regions than between the regions and Reddit also speaks to the difficulty of extracting reliable data from Reddit.  Many of the champion and item mentions on Reddit likely were never intended to stand as endorsements of playing that character or item.  Some may have been discussions of lore, or even complaints that a champion or item isn’t in a playable state.  Surprisingly, the main subreddit had better predictive power for champion choices than the subreddits focused on discussion of in-game choices, though the opposite was true for items.  The difficulty of telling what a /r/leagueoflegends mention should signify is compounded by the general difficulty of extracting accurate data from casual online speech.  


In particular, item counts were more difficult to extract because of the wide range of possible nicknames for items and the tendency for Redditors not to type the often unwieldy full names of each item.  In an initial pass over the Reddit data where only official names for items were used, the resultant list of items was tiny compared to the wealth of items in the game; adding nicknames and shortenings improved this substantially.  It’s possible that the better item data in the more focused subreddits was because people are more likely to type out the full name of an item when they perceive they are teaching a new player who may not be familiar with the item’s nicknames.  Predicting items from Reddit mentions is probably also inherently harder because some items are more or less salient, while a player’s choice of champion is almost always relevant to discussion.  Some items are starter items commonly bought by many champions and later replaced, others are components that could become many different items, and some are so common that a majority of champions will expect to buy them.  


Another possible explanation for the differences between the Reddit and Riot data is the different times when each was collected.  The Reddit corpus covers most of 2015 excepting the month of July, while the games were gathered in a spiderweb method with the earliest date accepted set to Jan 1 2015. Many of the games came from 2016 instead due to the uncontrollable nature of the crawl.  As the developers intentionally change which champions and items are strong in the games at different times in an attempt to keep the game balanced and interesting, the playerbase almost certainly made different choices in 2015 than in 2016, and indeed from game patch to game patch during each of those years.  Because it isn’t possible to easily pull down games from only a certain time period via the Riot API, to solve this problem would require either more Reddit data or a large enough amount of Riot data to still have usable amounts when pruned down to the time period from the Reddit data.


Looking only at the Riot data, the between-region correlations form an interesting window on the difference in play patterns between regions.  The two European regions, despite their geographical proximity, are each less similar to the other than to North America.  Champion choices are more different than item choices, with Korean champion choices being particularly far from those of the other regions.  Overall the tau remains quite high between regions, suggesting that there are strong overall trends in which champions and items people want to play with worldwide.  

The technical challenges of this project were acquiring the Riot data and analyzing the Reddit data.  Because the match collection script could only be run locally, the amount of data that could be collected was much smaller than could be collected on a cluster.  The rate limits were the main limiting factor, but since the rate limits were applied region by region, the main way to get data faster was to draw from multiple regions at once, and there were limits to how many instances of the script could be run simultaneously on a local machine without performance issues.  Because there is no way to easily query “all matches from January 2015” or similar, the only way to get interesting subsets of sufficient size for further research is to pull down a much greater amount of data and hope it covers the desired games.

The Reddit data processing was a much bigger obstacle and the area where the most improvement would be possible in the future.  The main issue with the Reddit data was searching at the right level within comments while making use of the MapReduce paradigm.  To best take advantage of the power of Spark, comments were mapped to the body of the comment, then flatMapped to produce keys associated with each word from the comment.  However, it proved difficult to get Spark to associate these keys with the original comments, preventing the original analysis of champion-item co-occurrence pairs as well as making it difficult to get data on items which had multiple word names of which no single name could be used as a proxy for the item.  (For example, “statikk shiv” could be found by looking for all occurrences of “statikk”, since no other item shares that name, but “void staff” could not be uniquely found by either “void” or “staff”, since the Void is a location in the game’s lore and there exists an item Archangel’s Staff.)  This was the result of Spark’s inability to handle nesting in its RDDs, which appears to extend to using the RDD at two different levels (each word in the body, compared with the ID associated with the entire comment).  It was by far the main limitation of this project and a workaround would enable a much deeper analysis of the data.

Further work might include the original plan to look at co-occurrence between champion names and item names in Reddit comment data; this might speak to both the ability of Reddit comments to predict behavior and the comparative salience of different items in game discussions.  With more data, subsets by comment and game date could also provide insight into how well game comment data tracks the development of player choices over time.  There is also room for improvement in the natural language processing aspect of the project, going beyond raw counts to try to predict sentiment from the original comment and tell “this is what you should do” from “this is a terrible idea”.



## Conclusion

Basic analysis of Reddit comment data showed a small but significant relation between Reddit mentions and in-game League of Legends choices.  Spark is a powerful tool for processing large-scale data, but makes implementation of natural language processing tools more difficult where they do not fit easily into the MapReduce paradigm.  Reddit data is difficult to analyze in general and more aggressive processing could probably achieve a more accurate prediction of in-game choices.  
	
## Works Cited

Gicos. (n.d.) LoLMasters. Retrieved from http://lolmasters.net/

Hortonworks. (n.d.) Chapter 1. Introduction - Spark Guide.  Retrieved from http://docs.hortonworks.com/HDPDocuments/HDP2/HDP-2.4.0/bk_spark-guide/content/ch_introduction-spark.html

League of Legends. (2015, October 9).  What is League of Legends? Retrieved from https://www.youtube.com/watch?v=-157HBpPZ24

League of Legends (n.d.) Subreddit located at https://www.reddit.com/r/leagueoflegends

Lin, J. (2015, April 4). Would voice chat stop toxicity in League? Message archived at http://www.surrenderat20.net/2015/04/red-post-collection-urf-q-on-april-6th.html

Lin, J. (2015, November 5). Q&A about dynamic queues and new champ select.  Message posted to http://boards.na.leagueoflegends.com/en/c/GD/JNwgrzih-qa-about-dynamic-queues-and-new-champ-select?comment=002b0000

LoL Meta (n.d.) Subreddit located at https://www.reddit.com/r/LeagueofLegendsMeta/

Meraki Analytics (2016, February 17). Cassiopeia [Python library] Retrieved from https://github.com/meraki-analytics/cassiopeia

OP.GG (n.d.) LoL Stats, Record Replay, Database, Guide, MMR. Retrieved from http://na.op.gg/

Riot Games. (2015) Riot Games API. Retrieved from https://developer.riotgames.com/

Riot Games. (2016). League of Legends [video game].  Available from https://signup.na.leagueoflegends.com/en/signup/index?realm_key=na

Riot Games. (2016) What is League of Legends? Retrieved from http://gameinfo.na.leagueoflegends.com/en/game-info/get-started/what-is-lol/

SoloMid. (2009) League of Legends Champion Builds and Guides. Retrieved from http://www.probuilds.net/

Stuck\_In\_the\_Matrix (2015, September 26). Reddit Submission Corpus [Data file]. Retrieved from http://reddit-data.s3.amazonaws.com/RS_full_corpus.bz2

Summoner School (n.d.) Subreddit located at https://www.reddit.com/r/summonerschool/

Zaharia, M., Chowdhury, M., Franklin, M. J., Shenker, S., & Stoica, I. (2010). Spark : Cluster Computing with Working Sets. HotCloud’10 Proceedings of the 2nd USENIX Conference on Hot Topics in Cloud Computing, 10. http://doi.org/10.1007/s00256-009-0861-0
