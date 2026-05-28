import pandas as pd

df = pd.read_csv('data/grants.csv', low_memory=False)
ncmr = df[df['ProjectTitle'].str.contains('New Construction and Major Renovation', case=False, na=False)].copy()

ncmr['amount_num'] = ncmr['TotalAwardAmount'].str.replace(r'[$,]', '', regex=True).astype(float)

print(f"Total NCMR grants: {len(ncmr)}")
print(f"Total dollar value: {ncmr['amount_num'].sum():,.0f}")
print()
print("By recipient type:")
print(ncmr.groupby('RecipientType')['amount_num'].agg(['count', 'sum']).sort_values('sum', ascending=False))
print()

at_max = ncmr[ncmr['amount_num'] == 1500000]
print(f"\nGrants at exactly $1,500,000: {len(at_max)}")
print("Breakdown by type:")
print(at_max['RecipientType'].value_counts())
print()
print("Business recipients at $1.5M:")
biz_max = at_max[at_max['RecipientType'] == 'Business']
print(biz_max[['RecipientName', 'TotalAwardAmount', 'CountiesServed']].to_string())
