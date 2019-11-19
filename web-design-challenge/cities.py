import pandas as pd
data = pd.read_csv("data.csv") 
html = data.to_html()
print(html)