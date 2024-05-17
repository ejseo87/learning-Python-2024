
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

print("버전:", mpl.__version__)
print("설치위치:", mpl.__file__)
print("설정위치:", mpl.get_configdir())
print("캐시위치:", mpl.get_cachedir())
print("설정파일위치:", mpl.matplotlib_fname())
f1 = fm.findSystemFonts(fontpaths=None, fontext='ttf')
#print(f1)
f2 = [f2.name for f2 in fm.fontManager.ttflist]
#print(f2)


a = open("./data/p01_RedHair_utf8.txt","r")
rr = a.read()
word = input("원하는 단어 검색 : ").split()
count = []
for i in word:
    n = rr.count(i)
    print("%s : %d"%(i,n))
    count.append(n)

plt.rc("font",family="NanumGothic")

#plt.plot(word,count)
plt.bar(word, count)
plt.xlabel("검색 단어")
plt.ylabel("개수")
plt.show()
a.close()
