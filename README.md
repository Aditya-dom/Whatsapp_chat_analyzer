# Whatsapp_chat_analyzer

**Small set of scripts to see whatsapp chat details**

This was mainly made as I'm suspicious of other chat statistics apps (they may
upload their data somewhere and what not). The workflow is as follows:
1. Export whatsapp chat without media
2. Use the `export_to_csv.py` script to parse the whatsapp chat from text to a csv
3. Run the `load_data.r` script, after changing the input csv file
4. Run the `plot_data.r` script once the data has been loaded.

You can do your own custom analysis as well once the data has been loaded. There
are just some basic graphs that are plotted in plot\_data.

Requirements:
```
- Python
- R + Tidyverse
```
