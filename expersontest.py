import os
print('Personality Test\n')

print('Pertanyaan pertama')
print('Dari warna di bawah ini, apa pilihan mu?')
print('''1.Merah
2.Hijau
3.Biru''')
q1 = input('pilihan (1-3) : ')
os.system('clear')
print('Pertanyaan kedua')
print('Dari hewan di bawah ini, apa pilihan mu?')
print('''1.Harimau
2.Gajah
3.Serigala''')
q2 = input('pilihan (1-3) : ')
os.system('clear')
print('Pertanyaan ketiga')
print('Dari unsur di bawah ini, apa pilihan mu?')
print('''1.Api
2.Air
3.Angin''')
q3 = input('pilihan (1-3) : ')
os.system('clear')
if q1 == '1' and q2 == '1' and q3 == '1':
  print('kamu seorang yang tegas dan mandiri')
elif q1 == '2' and q2 == '2' and q3 == '2':
  print('kamu seorang yang lembut dan suka menghindari pertikaian')
elif q1 == '3' and q2 == '3' and q3 == '3':
  print('kamu seorang yang mudah beradaptasi dan kreatif')
elif q1 == '1' and q2 == '2' and q3 == '3':
  print('kamu seorang yang fleksibel dan cuek')
elif q1 == '2' and q2 == '1' and q3 == '3':
  print('kamu seorang yang terlihat tenang dan santai di luar, tetapi sebenarnya bersungguh-sungguh')
elif q1 == '3' and q2 == '2' and q3 == '1':
  print('kamu seorang yang sabar dan berkemauan kuat')