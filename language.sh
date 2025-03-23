#!/bin/bash
echo "Arabic"
pyside6-lupdate ./Classes/*.py ./Interface/*.ui -ts ./Interface/translations/ar.ts
echo "Hebrow"
pyside6-lupdate ./Classes/*.py ./Interface/*.ui -ts ./Interface/translations/he.ts
echo "Russian"
pyside6-lupdate ./Classes/*.py ./Interface/*.ui -ts ./Interface/translations/ru.ts
echo "Others"
pyside6-lupdate ./Classes/*.py ./Interface/*.ui -ts ./Interface/translations/fr.ts
pyside6-lupdate ./Classes/*.py ./Interface/*.ui -ts ./Interface/translations/es.ts
pyside6-lupdate ./Classes/*.py ./Interface/*.ui -ts ./Interface/translations/de.ts
pyside6-lupdate ./Classes/*.py ./Interface/*.ui -ts ./Interface/translations/it.ts
pyside6-lupdate ./Classes/*.py ./Interface/*.ui -ts ./Interface/translations/pt.ts
pyside6-lupdate ./Classes/*.py ./Interface/*.ui -ts ./Interface/translations/tr.ts
pyside6-lupdate ./Classes/*.py ./Interface/*.ui -ts ./Interface/translations/fa.ts
pyside6-lupdate ./Classes/*.py ./Interface/*.ui -ts ./Interface/translations/ge.ts
