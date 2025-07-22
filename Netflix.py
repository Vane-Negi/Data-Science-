import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

try:
    df = pd.read_csv("netflix_titles.csv")
except FileNotFoundError:
    print("Error: 'netflix_titles.csv' not found. Make sure it's in the correct directory.")
    exit()

# Clean data
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df.dropna(subset=['title', 'date_added'], inplace=True) #inple=True ka matbla hai ki orignal DF main changes honge 
df = df.drop_duplicates()

# Empty data ko full kar rahe hai 
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Not Rated').str.upper()
df['listed_in'] = df['listed_in'].fillna('Unknown')
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['duration'] = df['duration'].fillna('Unknown')
df['type'] = df['type'].str.strip().str.title().replace({'Tv Show': 'TV Show'})

#Columns
df['year_added'] = df['date_added'].dt.year #year shoe karega
df['month_added'] = df['date_added'].dt.month_name() #month show karega
df['main_country'] = df['country'].str.split(',').str[0].str.strip() #India,USA ha to phale split karega uske baad (main country show karega) i.e India 
df['genre'] = df['listed_in'].str.split(',').str[0].str.strip() #ismain bhi same hai phale split uske baad genre show karega

#Style
sns.set_style("whitegrid") #ye to style ke liye hai backgrund style :)
plt.rcParams.update({'font.size': 12, 'figure.autolayout': True}) #ye kuch to hai rcParams default setting hai matplotlib ki ismian font size, line style, fig size aur bhi hoga esa sa hi hai kuch hai ye 

title_font = {'family': 'serif', 'color': '#2c3e50', 'size': 18, 'weight': 'bold'} #ye to batane ki jarurat nahi ye to samajh main a gaya hoga :)
label_font = {'family': 'serif', 'color': '#34495e', 'size': 13}

#Ab khud samajh lena

# 1. Movies vs TV Shows
plt.figure(figsize=(6, 4)) 
type_counts = df['type'].value_counts()
sns.barplot(x=type_counts.index, y=type_counts.values, palette='Set2', edgecolor='black')  # ye to samajh main a gaya hoga main ye man kar chal raha hu :)
plt.title("Netflix: Movies vs TV Shows", fontdict=title_font)
plt.ylabel("Number of Titles", fontdict=label_font)
plt.xlabel("Content Type", fontdict=label_font)
for i, val in enumerate(type_counts.values): #ye jo hai, ye no. show karva raha hai bar chat main 
    plt.text(i, val + 50, val, ha='center', fontweight='bold')
plt.show()

# 2. Monthly Additions
monthly_trend = df['date_added'].dt.to_period('M').value_counts().sort_index() # ye month show karega ex 2025-02-27 to ye 02 sirf month show karega
monthly_trend.index = monthly_trend.index.to_timestamp() #ye converts karta ha specific date main shayad :)
plt.figure(figsize=(12, 4))
sns.lineplot(x=monthly_trend.index, y=monthly_trend.values, marker='o', color='#e67e22')    
plt.title("Monthly Additions on Netflix", fontdict=title_font)
plt.xlabel("Date", fontdict=label_font)
plt.ylabel("Titles Added", fontdict=label_font)
plt.xticks(rotation=45) # ye rotation add karne ke liye hai
plt.grid(alpha=0.3) # ye line add karne ke liye hai 
plt.show()

# 3. Top 10 Countries
top_countries = df['main_country'].value_counts().head(10).sort_values() # ye head ka use karke top 10 countries show karega count ke help se :)
plt.figure(figsize=(9, 5))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='coolwarm', edgecolor='black')
plt.title("Top 10 Countries by Title Count", fontdict=title_font)
plt.xlabel("Number of Titles", fontdict=label_font)
plt.ylabel("Country", fontdict=label_font)
for i, v in enumerate(top_countries.values): #ye same no. show karva raha hai 
    plt.text(v + 10, i, str(v), va='center', fontweight='bold')
plt.show()

# 4. Rating Distribution (Top 8)
rating_counts = df['rating'].value_counts().head(8) # same count aur heas ke help se top 8 show karega.....
colors = sns.color_palette("pastel", len(rating_counts))
plt.figure(figsize=(8, 8))
wedges, texts, autotexts = plt.pie(
    rating_counts, #Values size allot karega shayad
    labels=rating_counts.index, #Names for each slice, shown outside or near each slice (e.g., 'TV-MA', 'PG').
    autopct='%1.1f%%', #Shows percentage labels 
    startangle=140, #Rotates the pie chart 140 degrees
    colors=colors, #custom color palette to each slice
    textprops={'fontsize': 11},
    wedgeprops={'edgecolor': 'black'} # black border
)
for autotext in autotexts: 
    autotext.set_fontsize(12) #size hai 25.1 in sab ka
    autotext.set_weight('bold') #bold kata ha 
plt.title("Top 8 Content Ratings on Netflix", fontdict=title_font)
plt.show()

# 5. Top 10 Genres
top_genres = df['listed_in'].str.split(', ').explode().value_counts().head(10).sort_values() 
plt.figure(figsize=(9, 6))
sns.barplot(x=top_genres.values, y=top_genres.index, palette='mako', edgecolor='black')
plt.title("Top 10 Genres on Netflix", fontdict=title_font)
plt.xlabel("Number of Titles", fontdict=label_font)
plt.ylabel("Genre", fontdict=label_font)
for i, v in enumerate(top_genres.values):
    plt.text(v + 10, i, str(v), va='center', fontweight='bold')
plt.show()

# 6. Genre Trend Over Time
genre_trend = df[df['genre'].isin(top_genres.index)].groupby(['year_added', 'genre']).size().unstack().fillna(0)
plt.figure(figsize=(12, 6))
sns.lineplot(data=genre_trend, palette='tab10', linewidth=2)
plt.title("Genre Trends Over Years", fontdict=title_font)
plt.xlabel("Year", fontdict=label_font)
plt.ylabel("Titles Released", fontdict=label_font)
plt.legend(title="Genre", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(alpha=0.4)
plt.show()

#Bhai dekh lo kuch to kiya hai agar samajh mein a jaaye to mujhe bhi samjha dena aur jo miane comments dale hai..
#Vo maine bs dal diye hai, pata nahi vo kitne sahi hai... :)