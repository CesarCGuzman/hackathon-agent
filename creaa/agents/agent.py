from google.cloud import storage
from google.adk.tools import FunctionTool
from google.cloud import bigquery
from typing import List

def property_search(region: str = None, max_price: int = None, asset_type: str = None) -> str:
    """
    Queries BigQuery for commercial properties based on region, price, and type. Then returns the results.
    If empty please state that no results were found.
    """
    client = bigquery.Client()

    query = "SELECT title, price, address, type, area FROM `ccibt-hack25ww7-734`.`cre`.`properties` WHERE 1=1"
    
    if region:
        query += f" AND (address LIKE '%{region}%' OR text LIKE '%{region}%')"
    if max_price:
        query += f" AND price <= {max_price}"
    if asset_type:
        query += f" AND type = '{asset_type}'"
        
    query += " LIMIT 10" # Safety limit for the agent's context
    
    query_job = client.query(query)
    results = query_job.to_dataframe()
    
    if results.empty:
        return "No properties found matching those specific criteria."
    
    return results.to_markdown(index=False)

property_search_tool = FunctionTool(func=property_search)
    