import pandas as pd
import json
import numpy as np
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / 'crop_recommendation.csv'

def analyze_seasons():
    df = pd.read_csv(DATA_PATH, sep='\t')
    
    seasons = ['Kharif', 'Rabi', 'Zaid', 'Post-Monsoon']
    season_recs = {}
    
    for season in seasons:
        season_df = df[df['Season'] == season]
        if season_df.empty:
            continue
            
        crop_counts = season_df['Crop'].value_counts()
        top_crops = crop_counts.head(5).to_dict()
        
        # Average features for this season
        avg_features = season_df[['N', 'P', 'K', 'Temperature', 'humidity', 'pH', 'Rainfall']].mean().to_dict()
        
        season_recs[season] = {
            'top_crops': top_crops,
            'count': len(season_df),
            'avg_features': {k: round(v, 2) for k, v in avg_features.items()}
        }
    
    # Save JSON
    output_path = BASE_DIR / 'season_recs.json'
    with open(output_path, 'w') as f:
        json.dump(season_recs, f, indent=2)
    
    print(f'Saved season_recs.json with {len(season_recs)} seasons')
    print(json.dumps(season_recs, indent=2))
    
    return season_recs

if __name__ == '__main__':
    analyze_seasons()

