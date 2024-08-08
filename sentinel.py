import pandas as pd

def dms_to_decimal(dms_str):
 parts = dms_str.split()
 grados = float(parts[0].replace('°', ''))
 minutos = float(parts[1].replace('\'', ''))
 segundos = float(parts[2].replace('\"', '').replace(',', '.'))
 direccion = parts[3]
 decimal = grados + minutos / 60 + segundos / 3600
 if direccion in ['W', 'S']:
  decimal *= -1
 return decimal
df = pd.DataFrame({'coordenada': ["71° 41' 13,477\" W", "34° 3' 2,000\" N"]
})
df['coordenada_decimal'] = df['coordenada'].apply(dms_to_decimal)
print(df)   