import matplotlib.pyplot as plt

import io
from database import bizzHackBot_db as bh_db
import pandas as pd

class bizzHackGraph:

    def stats(user):
        #get data
        df = bh_db.individual_score(user)

        #set up the data
        df['date'] = pd.to_datetime(df['date'])
        sum_by_date = df[df['points'] == 1.0].groupby('date')['points'].sum()


        plt.style.use('dark_background')
        fig, ax = plt.subplots()
        ax.set_xlabel('Date')
        ax.set_ylabel('Correct Answers')

        ax.plot(sum_by_date, color = '#47a0ff')
        ax.yaxis.grid()
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)

        num_ticks = 3  # Set the desired number of ticks
        x_values = sum_by_date.index
        x_ticks = pd.date_range(start=x_values.min(), end=x_values.max(), periods=num_ticks).tolist()
        x_tick_labels = [tick.strftime('%Y-%m-%d') for tick in x_ticks]
        plt.xticks(x_ticks, x_tick_labels)

        plt.savefig('graph.png', transparent=True)
        plt.close(fig)
        with open('graph.png', 'rb') as f:
            file = io.BytesIO(f.read())
        return file