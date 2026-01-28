"""
Simple Vietnam Population Forecasting Pipeline
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def main():
    print("Starting Vietnam Population Forecasting Analysis...")
    
    # Load data
    data = pd.read_csv('vietnam_population_data.csv')
    data = data[data['Entity'] == 'Vietnam'].copy()
    
    print(f"Data loaded: {len(data)} years from {data['Year'].min()} to {data['Year'].max()}")
    
    # Define columns
    cols = {
        'elderly_est': 'Population - Sex: all - Age: 65+ - Variant: estimates',
        'elderly_med': 'Population - Sex: all - Age: 65+ - Variant: medium',
        'working_est': 'Population - Sex: all - Age: 15-64 - Variant: estimates',
        'working_med': 'Population - Sex: all - Age: 15-64 - Variant: medium',
        'children_est': 'Population - Sex: all - Age: 0-14 - Variant: estimates',
        'children_med': 'Population - Sex: all - Age: 0-14 - Variant: medium'
    }
    
    # Fill missing estimates with medium values
    data[cols['elderly_est']] = data[cols['elderly_est']].fillna(data[cols['elderly_med']])
    data[cols['working_est']] = data[cols['working_est']].fillna(data[cols['working_med']])
    data[cols['children_est']] = data[cols['children_est']].fillna(data[cols['children_med']])
    
    # Split data
    train = data[data['Year'] <= 2023].copy()
    test = data[data['Year'] >= 2024].copy()
    
    print(f"Training data: {len(train)} years (1950-2023)")
    print(f"Test data: {len(test)} years (2024-2100)")
    
    # Prepare features
    X_train = train[['Year']].values
    X_test = test[['Year']].values
    
    # Target variables
    y_train = {
        'elderly': train[cols['elderly_est']].values,
        'working': train[cols['working_est']].values,
        'children': train[cols['children_est']].values
    }
    
    y_test = {
        'elderly': test[cols['elderly_med']].values,
        'working': test[cols['working_med']].values,
        'children': test[cols['children_med']].values
    }
    
    # Train models
    models = {}
    predictions = {}
    
    for age_group in ['elderly', 'working', 'children']:
        print(f"\nTraining models for {age_group} population...")
        
        # Remove NaN values
        mask_train = ~np.isnan(y_train[age_group])
        X_train_clean = X_train[mask_train]
        y_train_clean = y_train[age_group][mask_train]
        
        mask_test = ~np.isnan(y_test[age_group])
        X_test_clean = X_test[mask_test]
        y_test_clean = y_test[age_group][mask_test]
        
        # Random Forest
        rf = RandomForestRegressor(n_estimators=100, random_state=42)
        rf.fit(X_train_clean, y_train_clean)
        
        # KNN with scaling
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train_clean)
        knn = KNeighborsRegressor(n_neighbors=5)
        knn.fit(X_train_scaled, y_train_clean)
        
        # Polynomial Regression
        poly_features = PolynomialFeatures(degree=3)
        X_train_poly = poly_features.fit_transform(X_train_clean)
        lin_reg = LinearRegression()
        lin_reg.fit(X_train_poly, y_train_clean)
        
        # Make predictions
        rf_pred = rf.predict(X_test_clean)
        knn_pred = knn.predict(scaler.transform(X_test_clean))
        poly_pred = lin_reg.predict(poly_features.transform(X_test_clean))
        
        # Store results
        models[age_group] = {
            'rf': rf,
            'knn': knn,
            'poly': lin_reg,
            'scaler': scaler,
            'poly_features': poly_features
        }
        
        predictions[age_group] = {
            'rf': rf_pred,
            'knn': knn_pred,
            'poly': poly_pred,
            'actual': y_test_clean
        }
        
        # Calculate metrics
        print(f"Random Forest - RMSE: {np.sqrt(mean_squared_error(y_test_clean, rf_pred)):.0f}")
        print(f"KNN - RMSE: {np.sqrt(mean_squared_error(y_test_clean, knn_pred)):.0f}")
        print(f"Polynomial - RMSE: {np.sqrt(mean_squared_error(y_test_clean, poly_pred)):.0f}")
    
    # Create visualization
    print("\nCreating visualization...")
    fig, axes = plt.subplots(3, 1, figsize=(12, 10))
    
    age_names = {'elderly': 'Elderly (65+)', 'working': 'Working Age (15-64)', 'children': 'Children (0-14)'}
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
    
    for idx, (age_group, name) in enumerate(age_names.items()):
        ax = axes[idx]
        
        # Plot historical data
        years_hist = train['Year'].values
        mask_hist = ~np.isnan(y_train[age_group])
        ax.plot(years_hist[mask_hist], y_train[age_group][mask_hist], 
               'o-', color=colors[idx], label='Historical', linewidth=2)
        
        # Plot actual projections
        years_test = test['Year'].values[:len(predictions[age_group]['actual'])]
        ax.plot(years_test, predictions[age_group]['actual'], 
               's--', color='black', label='Actual Projection', linewidth=2)
        
        # Plot predictions
        ax.plot(years_test, predictions[age_group]['rf'], 
               ':', color='red', label='Random Forest', linewidth=2)
        ax.plot(years_test, predictions[age_group]['knn'], 
               '-.', color='green', label='KNN', linewidth=2)
        ax.plot(years_test, predictions[age_group]['poly'], 
               '--', color='blue', label='Polynomial', linewidth=2)
        
        ax.set_title(f'{name} Population')
        ax.set_xlabel('Year')
        ax.set_ylabel('Population')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('vietnam_population_forecasting.png', dpi=300, bbox_inches='tight')
    print("Visualization saved as 'vietnam_population_forecasting.png'")
    
    # Print summary
    print("\n" + "="*60)
    print("VIETNAM POPULATION FORECASTING SUMMARY")
    print("="*60)
    
    for age_group, name in age_names.items():
        print(f"\n{name}:")
        actual = predictions[age_group]['actual']
        
        for model_name in ['rf', 'knn', 'poly']:
            pred = predictions[age_group][model_name]
            rmse = np.sqrt(mean_squared_error(actual, pred))
            mae = mean_absolute_error(actual, pred)
            r2 = r2_score(actual, pred)
            
            model_display = {'rf': 'Random Forest', 'knn': 'KNN', 'poly': 'Polynomial'}[model_name]
            print(f"  {model_display}: RMSE={rmse:.0f}, MAE={mae:.0f}, R²={r2:.4f}")
    
    print("\nAnalysis complete!")

if __name__ == "__main__":
    main()
