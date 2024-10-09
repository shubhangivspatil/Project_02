import streamlit as st
import pandas as pd
import plotly.express as px
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
import pydeck as pdk
import requests
import json

# Set the Streamlit page configuration
st.set_page_config(page_title="PhonePe Pulse Data Visualization", layout="wide")

# Database Connection
DATABASE_URL = "postgresql://postgres:admin@localhost:5432/phone_pe1"
engine = sqlalchemy.create_engine(DATABASE_URL)

# Caching the data fetching functions
@st.cache_data
def fetch_data(table, year):
    query = f'SELECT * FROM "{table}" WHERE "Year" = \'{year}\';'
    try:
        with engine.connect() as conn:
            return pd.read_sql(query, conn)
    except SQLAlchemyError as e:
        st.error(f"Error fetching data: {str(e)}")
        return pd.DataFrame()  # Return empty DataFrame on error

def fetch_agg_trans(year, quarter):
    query = f"""
    SELECT "State", "Transaction_type", "Transaction_count", "Transaction_amount"
    FROM public."Agg_Trans"
    WHERE "Year" = '{year}' AND "Quater" = {quarter}
    """
    return pd.read_sql(query, engine)

def fetch_agg_insurance(year, quarter):
    query = f"""
    SELECT "State", "Year", "Quater", "Insurance_type", "Insurance_count", "Insurance_amount"
    FROM public."Agg_Insurance"
    WHERE "Year" = '{year}' AND "Quater" = {quarter}
    """
    return pd.read_sql(query, engine)

def fetch_map_data(year):
    query = f"""
    SELECT "lat", "lng", "metric", "label", "Year"
    FROM public."map_Insurance"
    WHERE "Year" = '{year}'
    """
    return pd.read_sql(query, engine)

def get_geojson():
    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response = requests.get(url)
    
    if response.status_code == 200:
        try:
            return response.json()
        except json.JSONDecodeError as e:
            st.error(f"Error parsing GeoJSON data: {e}")
            return None
    else:
        st.error(f"Error fetching GeoJSON data: {response.status_code}")
        return None

# Static function for 3D map visualization
def visualize_3d_map(map_data, title, color):
    try:
        layer = pdk.Layer(
            'ColumnLayer',
            data=map_data,
            get_position='[lng, lat]',
            get_elevation='metric',
            elevation_scale=500,
            radius=10000,
            get_fill_color=color,
            pickable=True,
            extruded=True
        )

        view_state = pdk.ViewState(
            latitude=22.0,
            longitude=77.0,
            zoom=4,
            pitch=50
        )

        r = pdk.Deck(
            layers=[layer],
            initial_view_state=view_state,
            tooltip={"text": "{label}\n{metric}"}
        )

        st.pydeck_chart(r)
    except Exception as e:
        st.error(f"Error creating {title} map: {e}")

def display_chart(df, x, y, title, kind='bar'):
    if df.empty:
        st.write("No data available for the selected year.")
        return

    try:
        if kind == 'bar':
            fig = px.bar(df, x=x, y=y, title=title)
        elif kind == 'pie':
            fig = px.pie(df, names=x, values=y, title=title)
        elif kind == 'line':
            fig = px.line(df, x=x, y=y, title=title)
        elif kind == 'heatmap':
            fig = px.density_heatmap(df, x=x, y=y, title=title)

        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"Error creating chart: {str(e)}")

# Load GeoJSON data
india_geojson = get_geojson()

# Title for the whole app
st.title("PhonePe Pulse Data Visualization and Exploration")

# Sidebar for page navigation
page = st.sidebar.selectbox("Select a Page", ["Home", "Geo Map - Insurance", 
                                                "Geo Map - Transactions", 
                                                "Transaction Summary", 
                                                "Data Analysis"])

# Sidebar for Year and Quarter Selection
selected_year = st.sidebar.selectbox("Select Year", [2018, 2019, 2020, 2021, 2022])
selected_quarter = st.sidebar.selectbox("Select Quarter", ["Q1", "Q2", "Q3", "Q4"])

# Convert quarter string to integer
quarter_map = {"Q1": 1, "Q2": 2, "Q3": 3, "Q4": 4}
quarter = quarter_map[selected_quarter]

# Fetch data based on the selected option
trans_data = fetch_agg_trans(selected_year, quarter)
insurance_data = fetch_agg_insurance(selected_year, quarter)
map_data = fetch_map_data(selected_year)

# Clean trans_data to ensure numeric columns are of correct type
if not trans_data.empty:
    trans_data['Transaction_amount'] = pd.to_numeric(trans_data['Transaction_amount'], errors='coerce')
    trans_data['Transaction_count'] = pd.to_numeric(trans_data['Transaction_count'], errors='coerce')

# --- Page 1: Home ---
if page == "Home":
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/3/39/PhonePe_Logo.svg/1200px-PhonePe_Logo.svg.png", width=200)
    
    st.write("""    
    **Project Title**: PhonePe Pulse Data Visualization and Exploration
    
    **Technologies**: Python, Pandas, PostgreSQL, Streamlit, Plotly.
    
    **Domain**: Fintech
    
    **Creator**: Shubhangi Patil
    
    **GitHub Link**: [GitHub Repository](https://github.com/shubhangivspatil)
    
    ### Key Features:
    
    - Analyze transaction types and their distribution across Indian states.
    
    - Explore insurance policies and their coverage across the country.
    
    - Visualize data with interactive 3D maps.
    
    - Gain valuable insights from trends over the years.
    """)

# --- Page 2: Geo Map - Insurance ---
elif page == "Geo Map - Insurance":
    st.header("Insurance Geo Map")
    
    st.write(f"Visualizing insurance data for the year {selected_year}, Quarter: {selected_quarter}.")
    
    if not map_data.empty:
        visualize_3d_map(map_data, "Insurance Data Across India", [0, 255, 255])  
    else:
        st.write("No geospatial data available.")

# --- Page 3: Geo Map - Transactions ---
elif page == "Geo Map - Transactions":
    st.header("Transactions Geo Map")
    
    st.write(f"Visualizing transaction data for the year {selected_year}, Quarter: {selected_quarter}.")
    
    if not map_data.empty:
        visualize_3d_map(map_data, "Transactions Data Across India", [255, 165, 0])  
    else:
        st.write("No geospatial data available.")

# --- Page 4: Transaction Summary ---
elif page == "Transaction Summary":
    st.header("Transaction Summary and Insights")
    
    if not trans_data.empty:
        total_transactions = trans_data['Transaction_amount'].sum()
        
        st.sidebar.metric(label="Total Transaction Amount", value=f"₹ {total_transactions:,.2f}")
        
        # Display summary of transaction types and amounts
        st.write("### Transaction Summary by Type")
        
        for t_type in trans_data['Transaction_type'].unique():
            t_data = trans_data[trans_data['Transaction_type'] == t_type]
            total_amount = t_data['Transaction_amount'].sum()
            
            st.metric(label=t_type, value=f"₹ {total_amount:,.2f}")

# --- Page 5: Data Analysis --- (Newly added)
elif page == "Data Analysis":
    st.title("Transaction and Insurance Data Analysis")

    # Define questions for EDA
    questions = [
        "What is the total transaction amount?",
        "Which state has the highest number of transactions?",
        "What are the transaction types and their counts?",
        "What is the trend of insurance policies issued over the years?",
        "How do transactions vary by quarter?",
        "What is the impact of insurance on transaction data over the years?",
        "Which state has the highest insurance coverage?",
        "What is the average transaction amount per state?",
        "What is the ratio of insurance amount to transaction amount?",
        "What are the most common transaction types in a particular state?",
        "How do transaction trends vary from year to year?"
    ]

    selected_question = st.selectbox("Select a question for analysis:", questions)

    def display_eda_results(question):
        query_mapping = {
            "What is the total transaction amount?": """
                SELECT SUM("Transaction_amount") AS total_amount
                FROM public."Agg_Trans"
            """,
            "Which state has the highest number of transactions?": """
                SELECT "State", SUM("Transaction_count") AS total_count
                FROM public."Agg_Trans"
                GROUP BY "State"
                ORDER BY total_count DESC
                LIMIT 1
            """,
            "What are the transaction types and their counts?": """
                SELECT "Transaction_type", COUNT(*) AS count
                FROM public."Agg_Trans"
                GROUP BY "Transaction_type"
            """,
            "What is the trend of insurance policies issued over the years?": """
                SELECT "Year", SUM("Insurance_count") AS total_count
                FROM public."Agg_Insurance"
                GROUP BY "Year"
            """,
            "How do transactions vary by quarter?": """
                SELECT "Quater", SUM("Transaction_amount") AS total_amount
                FROM public."Agg_Trans"
                GROUP BY "Quater"
            """,
            "What is the impact of insurance on transaction data over the years?": """
                SELECT a."Year", SUM(a."Transaction_amount") AS transaction_total, SUM(b."Insurance_count") AS insurance_total
                FROM public."Agg_Trans" a
                JOIN public."Agg_Insurance" b ON a."Year" = b."Year"
                GROUP BY a."Year"
            """,
            "Which state has the highest insurance coverage?": """
                SELECT "State", SUM("Insurance_count") AS total_insured
                FROM public."Agg_Insurance"
                GROUP BY "State"
                ORDER BY total_insured DESC
                LIMIT 1
            """,
            "What is the average transaction amount per state?": """
                SELECT "State", AVG("Transaction_amount") AS average_amount
                FROM public."Agg_Trans"
                GROUP BY "State"
            """,
            "What is the ratio of insurance amount to transaction amount?": """
                SELECT a."Year", a."State", SUM(b."Insurance_amount") / NULLIF(SUM(a."Transaction_amount"), 0) AS ratio
                FROM public."Agg_Insurance" b
                JOIN public."Agg_Trans" a ON a."Year" = b."Year" AND a."State" = b."State"
                GROUP BY a."Year", a."State"
            """,
            "What are the most common transaction types in a particular state?": """
                SELECT "State", "Transaction_type", COUNT(*) AS count
                FROM public."Agg_Trans"
                GROUP BY "State", "Transaction_type"
                ORDER BY count DESC
            """,
            "How do transaction trends vary from year to year?": """
                SELECT "Year", SUM("Transaction_amount") AS total_amount
                FROM public."Agg_Trans"
                GROUP BY "Year"
            """
        }
        
        query = query_mapping[question]
        result_df = pd.read_sql(query, engine)
        
        if result_df.empty:
            st.write("No data available.")
        else:
            st.write(result_df)
            # Generate appropriate graph based on the question
            if question == "What is the total transaction amount?":
                display_chart(result_df, x="total_amount", y=["total_amount"], title="Total Transaction Amount", kind='bar')
            elif question == "Which state has the highest number of transactions?":
                display_chart(result_df, x="State", y="total_count", title="State with Highest Transactions", kind='bar')
            elif question == "What are the transaction types and their counts?":
                display_chart(result_df, x="Transaction_type", y="count", title="Transaction Types and Counts", kind='bar')
            elif question == "What is the trend of insurance policies issued over the years?":
                display_chart(result_df, x="Year", y="total_count", title="Insurance Policies Issued Over the Years", kind='line')
            elif question == "How do transactions vary by quarter?":
                display_chart(result_df, x="Quater", y="total_amount", title="Transactions by Quarter", kind='bar')
            elif question == "What is the impact of insurance on transaction data over the years?":
                display_chart(result_df, x="Year", y=["transaction_total", "insurance_total"], title="Impact of Insurance on Transactions", kind='line')
            elif question == "Which state has the highest insurance coverage?":
                display_chart(result_df, x="State", y="total_insured", title="State with Highest Insurance Coverage", kind='bar')
            elif question == "What is the average transaction amount per state?":
                display_chart(result_df, x="State", y="average_amount", title="Average Transaction Amount per State", kind='bar')
            elif question == "What is the ratio of insurance amount to transaction amount?":
                display_chart(result_df, x=["Year", "State"], y="ratio", title="Ratio of Insurance to Transaction Amount", kind='line')
            elif question == "What are the most common transaction types in a particular state?":
                display_chart(result_df, x=["State", "Transaction_type"], y="count", title="Common Transaction Types by State", kind='bar')
            elif question == "How do transaction trends vary from year to year?":
                display_chart(result_df, x="Year", y="total_amount", title="Transaction Trends Over the Years", kind='line')

    display_eda_results(selected_question)



# Closing the database connection
if engine:
    engine.dispose()
# Footer
st.markdown("---")
st.write("Developed by Shubhangi V. Patil")
