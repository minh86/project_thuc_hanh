import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Configuration
st.set_page_config(
    page_title="Vietnam Population Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Module 1: CSV Data Loading
@st.cache_data
def load_population_data():
    """
    Load and preprocess Vietnam population data from CSV
    Returns cleaned DataFrame with population data by age groups
    """
    try:
        # Read CSV data
        df = pd.read_csv('vietnam_population_data.csv')
        
        # Combine estimates and medium variants for complete data
        df['age_0_14'] = df['Population - Sex: all - Age: 0-14 - Variant: estimates'].fillna(
            df['Population - Sex: all - Age: 0-14 - Variant: medium'])
        df['age_15_64'] = df['Population - Sex: all - Age: 15-64 - Variant: estimates'].fillna(
            df['Population - Sex: all - Age: 15-64 - Variant: medium'])
        df['age_65_plus'] = df['Population - Sex: all - Age: 65+ - Variant: estimates'].fillna(
            df['Population - Sex: all - Age: 65+ - Variant: medium'])
        
        # Remove rows with missing data
        df_clean = df.dropna(subset=['age_0_14', 'age_15_64', 'age_65_plus'])
        
        # Convert population to millions for better readability
        df_clean['pop_0_14_millions'] = df_clean['age_0_14'] / 1_000_000
        df_clean['pop_15_64_millions'] = df_clean['age_15_64'] / 1_000_000
        df_clean['pop_65_plus_millions'] = df_clean['age_65_plus'] / 1_000_000
        
        # Add total population
        df_clean['total_population_millions'] = (
            df_clean['pop_0_14_millions'] + 
            df_clean['pop_15_64_millions'] + 
            df_clean['pop_65_plus_millions']
        )
        
        # Add data type classification
        df_clean['data_type'] = df_clean['Year'].apply(
            lambda x: 'Historical' if x <= 2023 else 'Projection'
        )
        
        return df_clean
    
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Module 2: Data Filtering by Year Range
def filter_data_by_year_range(df, start_year, end_year):
    """
    Filter DataFrame based on selected year range
    Returns filtered DataFrame
    """
    if df is None:
        return None
    
    filtered_df = df[
        (df['Year'] >= start_year) & 
        (df['Year'] <= end_year)
    ].copy()
    
    return filtered_df

# Module 3: Reactive Chart Visualization
def create_population_chart(filtered_df):
    """
    Create interactive population chart using Plotly
    Range Slider controls data display timeframe
    """
    if filtered_df is None or filtered_df.empty:
        return None
    
    # Create figure with separate legends for each subplot
    fig = make_subplots(
        rows=2, cols=1,
        subplot_titles=('Population by Age Groups', 'Total Population Trend'),
        vertical_spacing=0.15,
        specs=[[{"secondary_y": False}], [{"secondary_y": False}]]
    )
    
    # Update subplot titles to align left
    fig.update_annotations(
        xanchor='left',
        x=0.05,
        font=dict(size=14)
    )
    
    # Split data by type for styling
    historical_data = filtered_df[filtered_df['data_type'] == 'Historical']
    projection_data = filtered_df[filtered_df['data_type'] == 'Projection']
    
    # Age group populations (top chart)
    # Working age (15-64) - Green
    if not historical_data.empty:
        fig.add_trace(
            go.Scatter(
                x=historical_data['Year'],
                y=historical_data['pop_15_64_millions'],
                mode='lines',
                name='Working (15-64)',
                line=dict(color='green', width=3),
                hovertemplate='Year: %{x}<br>Population: %{y:.1f}M<extra></extra>',
                legendgroup='working',
                showlegend=True
            ),
            row=1, col=1
        )
    
    if not projection_data.empty:
        fig.add_trace(
            go.Scatter(
                x=projection_data['Year'],
                y=projection_data['pop_15_64_millions'],
                mode='lines',
                name='Working (15-64)',
                line=dict(color='green', width=3, dash='dash'),
                hovertemplate='Year: %{x}<br>Population: %{y:.1f}M<extra></extra>',
                legendgroup='working',
                showlegend=False
            ),
            row=1, col=1
        )
    
    # Elderly (65+) - Red
    if not historical_data.empty:
        fig.add_trace(
            go.Scatter(
                x=historical_data['Year'],
                y=historical_data['pop_65_plus_millions'],
                mode='lines',
                name='Elderly (65+)',
                line=dict(color='red', width=3),
                hovertemplate='Year: %{x}<br>Population: %{y:.1f}M<extra></extra>',
                legendgroup='elderly',
                showlegend=True
            ),
            row=1, col=1
        )
    
    if not projection_data.empty:
        fig.add_trace(
            go.Scatter(
                x=projection_data['Year'],
                y=projection_data['pop_65_plus_millions'],
                mode='lines',
                name='Elderly (65+)',
                line=dict(color='red', width=3, dash='dash'),
                hovertemplate='Year: %{x}<br>Population: %{y:.1f}M<extra></extra>',
                legendgroup='elderly',
                showlegend=False
            ),
            row=1, col=1
        )
    
    # Young (0-14) - Orange
    if not historical_data.empty:
        fig.add_trace(
            go.Scatter(
                x=historical_data['Year'],
                y=historical_data['pop_0_14_millions'],
                mode='lines',
                name='Young (0-14)',
                line=dict(color='orange', width=3),
                hovertemplate='Year: %{x}<br>Population: %{y:.1f}M<extra></extra>',
                legendgroup='young',
                showlegend=True
            ),
            row=1, col=1
        )
    
    if not projection_data.empty:
        fig.add_trace(
            go.Scatter(
                x=projection_data['Year'],
                y=projection_data['pop_0_14_millions'],
                mode='lines',
                name='Young (0-14)',
                line=dict(color='orange', width=3, dash='dash'),
                hovertemplate='Year: %{x}<br>Population: %{y:.1f}M<extra></extra>',
                legendgroup='young',
                showlegend=False
            ),
            row=1, col=1
        )
    
    # Total population (bottom chart)
    if not historical_data.empty:
        fig.add_trace(
            go.Scatter(
                x=historical_data['Year'],
                y=historical_data['total_population_millions'],
                mode='lines',
                name='Total Population',
                line=dict(color='blue', width=3),
                hovertemplate='Year: %{x}<br>Total: %{y:.1f}M<extra></extra>',
                legendgroup='total',
                showlegend=True
            ),
            row=2, col=1
        )
    
    if not projection_data.empty:
        fig.add_trace(
            go.Scatter(
                x=projection_data['Year'],
                y=projection_data['total_population_millions'],
                mode='lines',
                name='Total Population',
                line=dict(color='blue', width=3, dash='dash'),
                hovertemplate='Year: %{x}<br>Total: %{y:.1f}M<extra></extra>',
                legendgroup='total',
                showlegend=False
            ),
            row=2, col=1
        )
    
    # Update layout with improved legend positioning
    fig.update_layout(
        title={
            'text': f'Vietnam Population Structure ({filtered_df["Year"].min()} - {filtered_df["Year"].max()})',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20}
        },
        height=750,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01,
            bgcolor="rgba(255,255,255,0.8)",
            bordercolor="gray",
            borderwidth=1,
            font=dict(size=10)
        ),
        hovermode='x unified',
        margin=dict(t=80, b=40, l=40, r=40)
    )
    
    # Update x-axes
    fig.update_xaxes(title_text="Year", row=1, col=1)
    fig.update_xaxes(title_text="Year", row=2, col=1)
    
    # Update y-axes
    fig.update_yaxes(title_text="Population (Millions)", row=1, col=1)
    fig.update_yaxes(title_text="Total Population (Millions)", row=2, col=1)
    
    # Add vertical line for historical/projection split if both exist
    if not historical_data.empty and not projection_data.empty:
        fig.add_vline(
            x=2023, 
            line_dash="dot", 
            line_color="gray", 
            opacity=0.5,
            annotation_text="Historical → Projection",
            annotation_position="top"
        )
    
    return fig

# Main Application
def main():
    st.title("📊 Vietnam Population Dashboard")
    st.markdown("### Interactive Time Series Analysis with Range Filter")
    
    # Load data
    df = load_population_data()
    
    if df is None:
        st.error("Unable to load data. Please check the CSV file.")
        return
    
    # Get year range from data
    min_year = int(df['Year'].min())
    max_year = int(df['Year'].max())
    
    # Sidebar with Range Slider
    st.sidebar.markdown("## ⏰ Time Filter")
    st.sidebar.markdown("*Range Slider controls data display timeframe*")
    
    # Range Slider for year selection
    selected_year_range = st.sidebar.slider(
        "Select Year Range:",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year),  # Default to full range
        step=1,
        help="Drag to select the time period to display"
    )
    
    start_year, end_year = selected_year_range
    
    # Display current selection
    st.sidebar.markdown(f"**Selected Period:** {start_year} - {end_year}")
    st.sidebar.markdown(f"**Years Displayed:** {end_year - start_year + 1}")
    
    # Filter data based on selection
    filtered_df = filter_data_by_year_range(df, start_year, end_year)
    
    # Main content area
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("### Population Trends")
        
        # Create and display chart
        fig = create_population_chart(filtered_df)
        if fig:
            st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        st.markdown("### 📈 Statistics")
        
        if not filtered_df.empty:
            # Calculate statistics for selected period
            first_year_data = filtered_df.iloc[0]
            last_year_data = filtered_df.iloc[-1]
            
            st.metric(
                "Total Population (Start)",
                f"{first_year_data['total_population_millions']:.1f}M",
                f"Year {first_year_data['Year']}"
            )
            
            st.metric(
                "Total Population (End)",
                f"{last_year_data['total_population_millions']:.1f}M",
                f"Year {last_year_data['Year']}"
            )
            
            population_change = last_year_data['total_population_millions'] - first_year_data['total_population_millions']
            st.metric(
                "Population Change",
                f"{population_change:+.1f}M",
                f"{((population_change/first_year_data['total_population_millions'])*100):+.1f}%"
            )
            
            # Age group distribution at end of period
            st.markdown("#### Age Distribution (End Period)")
            
            age_0_14_pct = (last_year_data['pop_0_14_millions'] / last_year_data['total_population_millions']) * 100
            age_15_64_pct = (last_year_data['pop_15_64_millions'] / last_year_data['total_population_millions']) * 100
            age_65_plus_pct = (last_year_data['pop_65_plus_millions'] / last_year_data['total_population_millions']) * 100
            
            st.write(f"🟠 Young (0-14): {age_0_14_pct:.1f}%")
            st.write(f"🟢 Working (15-64): {age_15_64_pct:.1f}%")
            st.write(f"🔴 Elderly (65+): {age_65_plus_pct:.1f}%")
    
    # Data table (expandable)
    with st.expander("📋 View Raw Data"):
        st.dataframe(
            filtered_df[['Year', 'total_population_millions', 'pop_0_14_millions', 
                        'pop_15_64_millions', 'pop_65_plus_millions', 'data_type']],
            use_container_width=True,
            hide_index=True
        )
    
    # Footer
    st.markdown("---")
    st.markdown("*💡 Tip: Use the range slider in the sidebar to explore different time periods*")

if __name__ == "__main__":
    main()
