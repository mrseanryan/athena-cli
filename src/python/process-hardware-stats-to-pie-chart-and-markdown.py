import os
import matplotlib.pyplot as plt
import pandas as pd

CHARTS_DIR="../../charts/"

jsonFs1 = "../../data/dashboard-1/hardware-stats.json"
print("Loading JSON in \"{0:s}\"".format(jsonFs1))
data1 = pd.read_json(jsonFs1)

normalized_data = pd.json_normalize(data1['data'])

# convert to numbers
normalized_data['number_of_screens_int'] = normalized_data['number_of_screens'].astype(int)
normalized_data['processor_count_int'] = normalized_data['processor_count'].astype(int)
normalized_data['screen_width_rounded_to_nearest_100_int'] = normalized_data['screen_width_rounded_to_nearest_100'].astype(int)

print(normalized_data)

df = normalized_data.reset_index()

def nullRowFilter(_):
	return True

def create_pie_for(title, short_title, column, chart_filename, row_filter = nullRowFilter):
	# === Prepare the data, counting and then aggregating by 'count'
	df_grouped = df.groupby([column])[column].count().reset_index(name='count').sort_values('count', ascending = False)
	df_grouped = df_grouped.set_index(column)

	filtering = df_grouped.apply(row_filter, axis = 1)
	df_grouped_filtered = df_grouped[filtering]

	# Take the top 5 categories. All other categories are aggregated together into one 'other' group
	TOP_N = 5
	df_top_n = df_grouped_filtered[:TOP_N].copy()
	df_others = pd.DataFrame(data = {
		column : ['Other'],
		'count' : [df_grouped_filtered['count'][TOP_N:].sum()]
	})
	df_others = df_others.set_index(column)

	df_top_n_and_others = pd.concat([df_top_n, df_others])

	# === Plot the pie chart, with an 'other' slice
	fig, ax = plt.subplots(figsize=(15,7))
	ax.set_title(title)
	
	# If a slice is greater than MIN_PC %, then show a label with its % value
	MIN_PC = 3
	autopct_min_5pc = lambda v: f'{v:1.0f}%' if v > MIN_PC else None
	df_top_n_and_others.plot(kind="pie", autopct=autopct_min_5pc, colormap='tab20b', legend=True, title=short_title, y='count',  ax=ax, ylabel='')

	pngFs1 = CHARTS_DIR + chart_filename + ".png"
	print("{0:s} (chart as image)".format(pngFs1))
	fig.savefig(pngFs1, bbox_inches="tight")

def create_md_for(title, column, md_filename, row_filter = nullRowFilter):
	# === Prepare the data, aggregating by 'count'
	df_grouped = df.groupby([column])[column].count().reset_index(name='count').sort_values('count', ascending = False)
	df_grouped = df_grouped.set_index(column)

	filtering = df_grouped.apply(row_filter, axis = 1)
	df_grouped_filtered = df_grouped[filtering]

	df2 = df_grouped_filtered.reset_index()
	column_int = column + '_int'
	df2[column_int]  = df2[column].astype(int)
	
	# Add a percent column with calculated values:
	df2['percent'] = (df2[column_int] / df2[column_int].sum()) * 100
	df2_sorted = df2.sort_values(by=column_int, ascending=False)

	columns_out = [column_int, 'percent']
	df_to_output = df2_sorted[columns_out]
	
	# generate the markdown text:
	markdown_text = df_to_output.set_index(column_int).to_markdown()

	# save the markdown to a new file:
	md_filepath = CHARTS_DIR + md_filename + ".md"
	with open(md_filepath, 'w') as f:
		f.write('# ' + title)
		f.write(os.linesep)
		f.write(os.linesep)
		f.write(markdown_text)

	print(f'Markdown written to {md_filepath}')

# === Screen Count ================================
# "number_of_screens": "1",
create_pie_for("Screen Count", 'Screen Count', 'number_of_screens', 'screen-count')

# === CPU Cores ================================
# "processor_count": "8",
create_pie_for("CPU Cores", 'CPU Cores', 'processor_count', 'cpu-cores')

# === Primary Screen Width (pixels) ================================
create_pie_for("Screen Width (pixels)", 'Screen Width (pixels)', 'screen_width_rounded_to_nearest_100', 'primary-screen-width')

create_md_for("Screen Width (pixels)", 'screen_width_rounded_to_nearest_100', 'primary-screen-width')
