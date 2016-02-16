
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
     }
    ])