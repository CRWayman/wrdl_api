import pandas as pd

from datetime import datetime, timedelta, date

def fetch_word(input_date):
        
    # Scrape daily Wordle answers
    url = "https://wordfinder.yourdictionary.com/wordle/answers/"
    
    # Create data frame 
    df = pd.read_html(url, index_col=0)
    df = pd.concat(df).reset_index()
    
    # Find length of data frame
    n_words = len(df)
    
    # Find today's date
    today = date.today()
    
    # Fix date column using date of first word (Jun. 19, 2021)
    start_date = today - timedelta(days=n_words)
    
    new_dates = pd.date_range(start_date, today)

    # Exclude current (today's) word
    new_dates = new_dates[0:-1]
    
    # Insert new dates in reverse order
    df["Date"] = new_dates.values[::-1]
    
    # Return output
    output = df[df["Date"]==input_date].Answer.values[0]
    
    return output
