import pandas as pd
import matplotlib.pyplot as plt

# read data
df = pd.read_json('data.json')
date = 'date'
product = 'product'
city = 'city'
genre = 'genre'
like = 'like'
month = 'month'

# clean data
pd.to_datetime(df[date])
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# add month
df.insert(loc=1, column=month, value=df[date].apply(lambda d: d.month))

# products
_, _, bars = plt.hist(df[product], bins=df[product].nunique())
plt.bar_label(bars)
plt.xlabel('product id')
plt.ylabel('count')
plt.show()


# var-products
def var_products(var: str):
    _group = df.groupby(var)[product]
    _, _, _bars = plt.hist(x=_group.groups, weights=_group.count(), bins=_group.ngroups)
    plt.bar_label(_bars)
    plt.xlabel(var)
    plt.ylabel('no of products')
    plt.show()


# genre-products
var_products(genre)

# city-products
var_products(city)

# month-products
group = df.groupby(month)[product]
plt.plot(group.groups.keys(), group.count(), marker='o')
plt.xlabel(month)
plt.ylabel('no of products')
plt.show()

# month-earns
group = df.groupby(month)[product]
plt.plot(group.groups.keys(), group.sum(), marker='o')
plt.xlabel(month)
plt.ylabel('earns')
plt.show()

# month-every-product
group = df.groupby(product)[month]
group.hist(legend=True)
plt.xlabel(month)
plt.show()
