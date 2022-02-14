# Generator Pipeline
file_name = 'techcrunch.csv'
lines = (line for line in open(file_name))
row = (s.rstrip().split(',') for s in lines)
columns = next(row)  # First row

print(columns)

data_dicts = (dict(zip(columns, data)) for data in row)
funding = (
    int(data_dict['raisedAmt'])
    for data_dict in data_dicts
    if data_dict['round'] == 'a'
)
# In this code snippet, your generator expression 
# iterates through the results of company_dicts 
# and takes the raisedAmt for any company_dict 
# where the round key is "a".

total_series_a = sum(funding)
print(f"Total series A fundraising: ${total_series_a}")
