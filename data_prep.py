from dataprep.datasets import get_dataset_names, load_dataset
from dataprep.eda import plot_correlation, plot_missing, plot_diff, create_report

# datasets disponíveis
print(get_dataset_names())

# Load datasert de exemplo
df = load_dataset("titanic")
print(df)

# EDA
plot_correlation(df)
plot_missing(df)

# Comparando 2 dataframes com plot diff
# Dimensão de dado
df.shape

# Criando df1 com as primeiras 500 linhas
df1 = df.loc[:500]
print(df1)

# Criando df2 para as linhas restantes
df2 = df.loc[501:]
print(df2)

# Comparando as dataframes
plot_diff([df1, df2])

# Criando um EDA report
report = create_report(df)
report.show()
report.save()
report.show_browser()
