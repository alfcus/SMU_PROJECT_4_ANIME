import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import NearestNeighbors

class ModelHelper():
    def __init__(self):
        pass

    def makePredictions(df, animeName="", genre="", score=0, n_neighbors=10):
        df = pd.read_csv("static/data/anime_rec.csv")
        df_sub = df.drop(["Name", "English name", "Genres"], axis=1)

        if animeName != "":
            model_knn = NearestNeighbors(metric='cosine', n_neighbors=n_neighbors)
            model_knn.fit(df_sub)
            
            anime = df.loc[df["Name"] == animeName]
            anime = anime.drop(["Name", "English name", "Genres"], axis=1)
            anime = anime.to_numpy()
            
            distances, indices = model_knn.kneighbors(anime, n_neighbors = n_neighbors)
            
            result = df.iloc[indices.flatten()]
            result["Distance"] = distances.flatten()

            plt.plot(result["Name"], result["Distance"])
            plt.title("Distance Between Neighbors", fontsize=16, fontweight="bold")
            plt.xlabel("Anime", fontsize=14)
            plt.xticks(rotation = 90)
            plt.ylabel("Distance", fontsize=14)
            plt.savefig('static/images/graph01.png', bbox_inches = "tight")

            result = result[["Name", "English name", "Score", "Genres"]].to_json(orient='records')
            
            return result
        else:
            model_knn = NearestNeighbors(metric='cosine', n_neighbors=n_neighbors)
            model_knn.fit(df_sub)
            
            anime = df.loc[(df[genre] == 1) & (df.Score > score)].sample(1)
            anime = anime.drop(["Name", "English name", "Genres"], axis=1)
            anime = anime.to_numpy()
            
            distances, indices = model_knn.kneighbors(anime, n_neighbors = n_neighbors)
            
            result = df.iloc[indices.flatten()]
            result["Distance"] = distances.flatten()

            plt.plot(result["Name"], result["Distance"])
            plt.title("Distance Between Neighbors", fontsize=16, fontweight="bold")
            plt.xlabel("Anime", fontsize=14)
            plt.xticks(rotation = 90)
            plt.ylabel("Distance", fontsize=14)
            plt.savefig('static/images/graph02.png', bbox_inches = "tight")

            result = result[["Name", "English name", "Score", "Genres"]].to_json(orient='records')
            
            return result
