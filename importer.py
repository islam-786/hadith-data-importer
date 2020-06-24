import json

from hadith_bukhari import HadithBukhari
import fireo

mypath = './bukhari'

onlyfiles = []

for n in range(1, 98):
    onlyfiles.append(str(n) + ".json")

overAllHadithCount = 1

for single_file in onlyfiles:

    file_location_en = "./bukhari/" + single_file
    f_en = open(file_location_en, "r", encoding="utf8")

    file_location_ur = "./bukhari-urdu/" + single_file
    f_ur = open(file_location_ur, "r", encoding="utf8")

    hadith_batch = fireo.batch()
    count = 0

    data_en = json.load(f_en)
    data_ur = json.load(f_ur)

    for en, ur in zip(data_en, data_ur):
        hadith = HadithBukhari()
        hadith.id = str(overAllHadithCount)
        hadith.bookName = en['book']
        hadith.bookNameArabic = en['arabicBook']
        hadith.bookNumber = en['number']
        hadith.hadithNumber = en['hadithNumber']
        hadith.numberInBook = en['NumberInBook']
        hadith.chapterName = en['chapter']
        hadith.chapterNameArabic = en['arabicChapter']
        hadith.narratedBy = en['narratedBy']
        hadith.narratedByArabic = en['narratedByArabic']
        hadith.narratedByArabicDetail = en['narratedByDetail']
        hadith.narratedByUrdu = ur['narratedBy']
        hadith.text = en['text']
        hadith.textArabic = en['arabicText']
        hadith.textUrdu = ur['text']

        #hadith.save(batch=hadith_batch)

        
        overAllHadithCount += 1
        count += 1
        if(count >= 400):
            #hadith_batch.commit()
            count = 0

    f_en.close()
    f_ur.close()

    print('============Complete '+single_file+'===================')
    #hadith_batch.commit()