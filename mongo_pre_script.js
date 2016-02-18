
// create an index on with type 'text' to make it searchable
use amthal
db.sayings.createIndex(
    { text : "text"}, 
    { default_langauge: "arabic"}
)

// --------------------------------

// add list of all arabic countries
use amthal
db.countries.insert(
    [
     { 
       '_id': 'EG', 
       'country': [
           {'language': 'english', 'name': 'Egypt'},
           {'language': 'arabic',  'name': 'مصر'}
       ]

     },
     { 
       '_id': 'DZ', 
       'country': [
           {'language': 'english', 'name': 'Algeria'},
           {'language': 'arabic',  'name': 'الجزائر'}
       ]
     },
     { 
       '_id': 'SD', 
       'country': [
           {'language': 'english', 'name': 'Sudan'},
           {'language': 'arabic',  'name': 'السودان'}
       ]
     },
     { 
       '_id': 'IQ', 
       'country': [
           {'language': 'english', 'name': 'Iraq'},
           {'language': 'arabic',  'name': 'العراق'}
       ]
     },
     { 
       '_id': 'MA', 
       'country': [
           {'language': 'english', 'name': 'Morocco'},
           {'language': 'arabic',  'name': 'المغرب'}
       ]
     },
     { 
       '_id': 'SA', 
       'country': [
           {'language': 'english', 'name': 'Saudi Arabia'},
           {'language': 'arabic',  'name': 'المملكة العربية السعودية'}
       ]
     },
     { 
       '_id': 'YE', 
       'country': [
           {'language': 'english', 'name': 'Yemen'},
           {'language': 'arabic',  'name': 'اليمن'}
       ]
     },
     { 
       '_id': 'SY', 
       'country': [
           {'language': 'english', 'name': 'Syria'},
           {'language': 'arabic',  'name': 'سوريا'}
       ]
     },
     { 
       '_id': 'TN', 
       'country': [
           {'language': 'english', 'name': 'Tunisia'},
           {'language': 'arabic',  'name': 'تونس‎'}
       ]
     },
     { 
       '_id': 'SO', 
       'country': [
           {'language': 'english', 'name': 'Somalia'},
           {'language': 'arabic',  'name': 'الصومال'}
       ]
     },
     { 
       '_id': 'JO', 
       'country': [
           {'language': 'english', 'name': 'Jordan'},
           {'language': 'arabic',  'name': 'الأردن'}
       ]
     },
     { 
       '_id': 'AE', 
       'country': [
           {'language': 'english', 'name': 'United Arab Emirates'},
           {'language': 'arabic',  'name': 'الإمارات العربية المتحدة'}
       ]
     },
     { 
       '_id': 'LY', 
       'country': [
           {'language': 'english', 'name': 'Libya'},
           {'language': 'arabic',  'name': 'ليبيا'}
       ]
     },
     { 
       '_id': 'PS', 
       'country': [
           {'language': 'english', 'name': 'Palestine'},
           {'language': 'arabic',  'name': 'فلسطين'}
       ]
     },
     { 
       '_id': 'LB', 
       'country': [
           {'language': 'english', 'name': 'Lebanon'},
           {'language': 'arabic',  'name': 'لبنان'}
       ]
     },
     { 
       '_id': 'OM', 
       'country': [
           {'language': 'english', 'name': 'Oman'},
           {'language': 'arabic',  'name': 'عمان'}
       ]
     },
     { 
       '_id': 'KW', 
       'country': [
           {'language': 'english', 'name': 'Kuwait'},
           {'language': 'arabic',  'name': 'الكويت'}
       ]
     },
     { 
       '_id': 'MR', 
       'country': [
           {'language': 'english', 'name': 'Mauritania'},
           {'language': 'arabic',  'name': 'موريتانيا'}
       ]
     },
     { 
       '_id': 'QA', 
       'country': [
           {'language': 'english', 'name': 'Qatar'},
           {'language': 'arabic',  'name': 'قطر'}
       ]
     },
     { 
       '_id': 'BH', 
       'country': [
           {'language': 'english', 'name': 'Bahrain'},
           {'language': 'arabic',  'name': 'البحرين'}
       ]
     },
     { 
       '_id': 'DJ', 
       'country': [
           {'language': 'english', 'name': 'Djibouti'},
           {'language': 'arabic',  'name': 'جيبوتي'}
       ]
     },
     { 
       '_id': 'KM', 
       'country': [
           {'language': 'english', 'name': 'Comoros'},
           {'language': 'arabic',  'name': 'جزر القمر'}
       ]
     }
    ])