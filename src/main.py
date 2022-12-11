import streamlit as st
import yaml
from kedro.framework.context import  KedroContext

st.title('SDG Goals')
from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project
from pathlib import Path

company_name = st.text_input('Enter the Company Name...')
start_year = st.text_input('Enter the start year')
end_year = st.text_input('Enter the end year')
if st.button('Search..'):
    with open('./conf/base/parameters.yml','w') as f:
        yaml.dump({'company_name':company_name,'start_year':start_year,'end_year':end_year},f)
    bootstrap_project(Path.cwd())
    with KedroSession.create() as session:
        context = session.load_context()
        session.run()
        company_data = context.catalog.load('labelled_data')
        st.dataframe(company_data.head(20))
        # company_params = context.params
        # st.text(company_params['company_name'])
# bootstrap_project(Path.cwd())
# with KedroSession.create() as session:
#     context = session.load_context()
#     company_name = st.text_input('Company Name')
#     company_params = context.params
    # company_params=context._extra_params('company_name': company_name )
    # st.text(company_params['company_name'])
    
    
    
    # company_data = context.catalog.load('cleaned_data')
    # st.text(company_data)
# from kedro.framework.session import get_current_session
# from kedro.framework.session import KedroSession

# with KedroSession.create("name_of_proyect") as session:
#     key = "item_of_catalog"
#     session = get_current_session()
#     context = session.load_context()
#     company_data = context.
# company = st.text_input('Company Name')
# context = KedroContext('./')
# company_data = context..load('cleaned_data')
# st.text(company_data)