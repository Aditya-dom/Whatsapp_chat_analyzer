library('tidyverse')
# how to pass parameters to R scripts I wonder :/
text_stats = read.csv("data/<input csv>.csv");

text_stats$time = as.POSIXct(text_stats$time, format="%I:%M:%S %p");
text_stats$date <- as.Date(text_stats$date, format="%d/%m/%y");

daily_text_count = text_stats %>% count(date)
sender_text_count = text_stats %>% count(sender, sort=TRUE)
top_ten_sender_data = text_stats %>% filter(sender %in% sender_text_count[1:10,]$sender)