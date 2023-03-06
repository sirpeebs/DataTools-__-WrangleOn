import streamlit as st
import pandas as pd

st.title('Inner Left Join')

# Upload the two files
file_1 = st.file_uploader('Upload the first file', type=['csv', 'xls', 'xlsx'])
file_2 = st.file_uploader('Upload the second file', type=['csv', 'xls', 'xlsx'])

# Read the files
if file_1 is not None and file_2 is not None:
    df_1 = pd.read_excel(file_1)
    df_2 = pd.read_excel(file_2)

#pandas read xls
    # Get the column names
    cols_1 = df_1.columns.tolist()
    cols_2 = df_2.columns.tolist()

    # Select the columns to join on
    col_1 = st.selectbox('Select the column from the first file', cols_1)
    col_2 = st.selectbox('Select the column from the second file', cols_2)

    # Perform the join
    if col_1 and col_2:
        joined_df = df_1.merge(df_2, left_on=col_1, right_on=col_2, how='inner')
        st.dataframe(joined_df)
        st.success('Inner left join complete!')

        if st.button('Download'):
            # To write to an excel file
            joined_df.to_excel('output.xlsx', index=False)

            # To download the file
            tmp_download_link = download_link(joined_df, 'output.xlsx', 'Click here to download your data!')
            st.markdown(tmp_download_link, unsafe_allow_html=True)
        #add a button to download the file
        #download_link' is not defined