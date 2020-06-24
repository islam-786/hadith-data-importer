from fireo.models import Model
from fireo.fields import IDField, TextField, NumberField

class HadithBukhari(Model):
    id = IDField()
    bookName = TextField()
    bookNameArabic = TextField()
    bookNumber = NumberField()
    hadithNumber = TextField()
    numberInBook = NumberField()
    chapterName = TextField()
    chapterNameArabic = TextField()
    narratedBy = TextField()
    narratedByArabic = TextField()
    narratedByArabicDetail = TextField()
    narratedByUrdu = TextField()
    text = TextField()
    textArabic = TextField()
    textUrdu = TextField()

    class Meta:
        collection_name = 'hadith_bukhari'
