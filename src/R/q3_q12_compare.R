setwd('/Users/lumizhang/Desktop/数学建模/CUMCM2023Problems/B题')

res1_math <- read.csv('result1.csv')
res1_lt <- read.csv('result1_lt.csv', header = F)

res1_math[nrow(res1_math) + 1,] <- c('海水深度',res1_lt$V1)
res1_math[nrow(res1_math) + 1,] <- c('覆盖面积',res1_lt$V2)

library(pheatmap)
res1 <- res1_math[c(1,4,2,5), 2:10]

colnames(res1) <- c('-800', '-600', '-400', '-200', '0', '200', '400', '600', '800')
rownames(res1) <- c('Sea depth/m','Sea depth(new)/m','Width/m','Width(new)/m')

for(col in names(res1)){
  res1[[col]] <- as.numeric(res1[[col]])
}


depth <- pheatmap(res1[1:2,],
             cluster_cols = F,
             cluster_rows = F)
width <- pheatmap(res1[3:4,],
                  cluster_cols = F,
                  cluster_rows = F)

library(ComplexHeatmap)
depth <- Heatmap(t(res1[1:2,]),
                cluster_rows = F,
                cluster_columns = F)
width <- Heatmap(t(res1[3:4,]),
                 cluster_rows = F,
                 cluster_columns = F)
depth + width
depth

old <- Heatmap(t(res1[c(1,3),]),
               cluster_rows = F,
               cluster_columns = F,
               column_names_rot = 90,
               column_title_rot = 90,
               row_names_rot = 90,
               row_names_centered = T,
               column_title = 'Mathematics')
new <- Heatmap(t(res1[c(2,4),]),
               cluster_rows = F,
               cluster_columns = F,
               column_names_rot = 90,
               column_title_rot = 90,
               row_names_rot = 90,
               row_names_centered = T,
               column_title = 'Binary Search')
old + new


res2_math <- read.csv('result2.csv', header = TRUE, row.names = 1)
colnames(res2_math) <- c('0', '0.3', '0.6', '0.9', '1.2', '1.5', '1.8', '2.1')
res2_lt <- read.csv('result2_lt.csv', header = F)
colnames(res2_lt) <- colnames(res2_math)
rownames(res2_lt) <- rownames(res2_math)
blue_to_white_palette <- colorRampPalette(c("white", "blue"))
old <- Heatmap(t(res2_math),
               cluster_rows = F,
               cluster_columns = F,
               column_title = 'Mathematics',
               col = blue_to_white_palette(100))
new <- Heatmap(t(res2_lt),
                   cluster_rows = F,
                   cluster_columns = F,
                   column_title = 'Binary Search',
                   col = blue_to_white_palette(100))
old + new
