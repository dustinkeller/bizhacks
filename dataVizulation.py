import matplotlib.pyplot as plt
import io
from database import bizzHackBot_db as bhb_db

class bizzHackGraph:

    def stats(ctx, user = None):
        #get data
        df = bhb_db.individual_score(user)
        user = df['Name'][0]

        plt.style.use('dark_background')
        fig, ax = plt.subplots()
        counts = df['Date'].value_counts().sort_index(ascending=True)
        dates = counts.index
        payouts = counts.values

        ax.set_xlabel('Date')
        ax.set_ylabel('Correct Answers')

        ax.scatter(dates, payouts, marker='.', s = 75, color = '#47a0ff')
        ax.plot(counts, color = '#47a0ff')
        ax.yaxis.grid()
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        
        num_dates = len(dates)
        tick_positions = [0, num_dates // 3, 2 * num_dates // 3, num_dates - 1]
        tick_labels = [dates[i] for i in tick_positions]
        plt.xticks(tick_positions, tick_labels, color='white')
        plt.savefig('graph.png', transparent=True)
        plt.close(fig)
        with open('graph.png', 'rb') as f:
            file = io.BytesIO(f.read())
        return file