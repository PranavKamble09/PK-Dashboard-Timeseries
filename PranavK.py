# To run app (put this in Terminal):
#   streamlit run app.py

import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration and styling
st.set_page_config(page_title="Business Dashboard", page_icon="📊", layout="wide")
st.markdown(
    """
    <style>
        /* General CSS for better styling */
        body {
            background-color: #F5F5F5;
        }
        .main .block-container {
            padding: 2rem;
            border-radius: 15px;
            background-color: #FFFFFF;
        }
        h1 {
            color: #ff6347;
            text-align: center;
            font-size: 3rem;
        }
        .header {
            color: #4682B4;
        }
        .footer {
            font-size: 0.9rem;
            color: #A9A9A9;
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True
)

# 1.0 Title and Introduction
st.title("📊 Business Dashboard")
st.markdown("""
This dashboard provides insights into sales, customer demographics, and product performance.
**Upload your data to get started!**""")

# 2.0 Data Input
st.markdown("## Upload Business Data")
uploaded_file = st.file_uploader("📁 Choose a CSV File", type="csv")

# 3.0 App Body
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("### Preview of the Uploaded Data")
    st.write(data.head())

    # Sales Insights
    st.markdown("## 📈 Sales Insights")
    if 'sales_date' in data.columns and 'sales_amount' in data.columns:
        st.markdown("### Sales Over Time")
        fig = px.line(
            data, 
            x='sales_date', 
            y='sales_amount', 
            title='Sales Over Time', 
            color_discrete_sequence=["#ff7f0e"]
        )
        fig.update_layout(
            xaxis_title="Date",
            yaxis_title="Sales Amount",
            title_font=dict(size=20),
            plot_bgcolor="#FAFAFA"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Please ensure your data has 'sales_date' and 'sales_amount' columns for sales visualization.")

    # Customer Segmentation by Region
    st.markdown("## 🌎 Customer Segmentation")
    if 'region' in data.columns and 'sales_amount' in data.columns:
        st.markdown("### Sales by Region")
        fig = px.pie(
            data, 
            names="region", 
            values="sales_amount", 
            title="Sales Distribution by Region", 
            color_discrete_sequence=px.colors.sequential.RdBu
        )
        fig.update_traces(textinfo="percent+label")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Please ensure your data has 'region' and 'sales_amount' columns for customer segmentation.")

    # Product Analysis
    st.markdown("## 📊 Product Analysis")
    if 'product' in data.columns and 'sales_amount' in data.columns:
        st.markdown("### Top Products by Sales")
        top_products_df = data.groupby('product').sum(numeric_only=True)['sales_amount'].nlargest(10)
        fig = px.bar(
            top_products_df, 
            x=top_products_df.index, 
            y="sales_amount", 
            title="Top Products by Sales",
            color_discrete_sequence=["#1f77b4"]
        )
        fig.update_layout(
            xaxis_title="Product",
            yaxis_title="Sales Amount",
            title_font=dict(size=20),
            plot_bgcolor="#FAFAFA"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Please ensure your data has 'product' and 'sales_amount' columns for product analysis.")

    # Feedback Form
    st.markdown("## 📝 Feedback")
    feedback = st.text_area("Your feedback or suggestions are welcome:")
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")

# Footer
st.markdown("---")
st.markdown("<p class='footer'>This business dashboard is flexible. Feel free to customize it further!</p>", unsafe_allow_html=True)

# Run the Streamlit app with improved style
if __name__ == "__main__":
    pass
