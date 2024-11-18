import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (ensure this path is correct)
df = pd.read_csv('sentimentscore.csv')

# Check the first few rows to make sure sentiment is calculated
print(df[['product_name', 'Sentiment']].head())

# Group by product and sentiment, and count the occurrences of each sentiment
sentiment_counts = df.groupby(['product_name', 'Sentiment']).size().reset_index(name='count')

# Pivot the table to make it easier to plot
sentiment_pivot = sentiment_counts.pivot(index='product_name', columns='Sentiment', values='count').fillna(0)

# Plot the sentiment distribution for each product
plt.figure(figsize=(12, 8))

# Plot the stacked bar plot as before
sns.barplot(data=sentiment_pivot.reset_index(), x='product_name', y='Positive', color='green', label='Positive', errorbar=None)
sns.barplot(data=sentiment_pivot.reset_index(), x='product_name', y='Negative', color='red', label='Negative', errorbar=None, bottom=sentiment_pivot['Positive'])
sns.barplot(data=sentiment_pivot.reset_index(), x='product_name', y='Neutral', color='gray', label='Neutral', errorbar=None, bottom=sentiment_pivot['Positive']+sentiment_pivot['Negative'])

# Get the product with the highest number of positive reviews
reset_df = sentiment_pivot.reset_index()  # Convert index to column
top_product_index = reset_df['Positive'].idxmax()  # Find the index of the top product

# Get the top product name and sentiment counts
top_product_name = reset_df.loc[top_product_index, 'product_name']
top_product_positive_count = reset_df.loc[top_product_index, 'Positive']
top_product_negative_count = reset_df.loc[top_product_index, 'Negative']
top_product_neutral_count = reset_df.loc[top_product_index, 'Neutral']

# Add labels and title
plt.title('Sentiment Distribution per Product')
plt.xlabel('Product Name')
plt.ylabel('Number of Reviews')
plt.xticks(rotation=90)  # Rotate product names to make them readable
plt.legend(title='Sentiment')

# Annotate the top product with detailed information
# Position the annotation slightly above the positive bar for the top product
top_product_x_position = reset_df.loc[top_product_index, 'product_name']

# Annotating the top product (highlighting the bar)
plt.text(x=top_product_x_position, 
         y=reset_df.loc[top_product_index, 'Positive'] + 5,  # Adjust Y position to be above the bar
         s=f"Top Product: {top_product_name}\nPositive: {top_product_positive_count}\nNegative: {top_product_negative_count}\nNeutral: {top_product_neutral_count}",
         color='black', ha='center', fontsize=10, bbox=dict(facecolor='white', alpha=0.7))

plt.tight_layout()

# Show the plot
plt.show()

# Display the top product with the most positive reviews
print(f"Top product with most positive reviews: {top_product_name} ({top_product_positive_count} Positive reviews)")