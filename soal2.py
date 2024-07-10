import pandas as pd
data = {
    'Mahasiswa1':[90,80],
    'Mahasiswa2':[50,60],
    'Mahasiswa3':[65,70]
}
df = pd.DataFrame(data,index=['Algoritma Struktur Data 2','Matematika Numerik']).T
print(df,'\n')


df['Rata-rata Mata Kuliah'] = df.mean(axis=1)

df.loc['Rata-rata Mahasiswa'] = df.mean()

print(df)