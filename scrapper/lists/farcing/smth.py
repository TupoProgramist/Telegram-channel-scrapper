list1 = [
    "ГУРТ", "Грантові фішки - Grantovy Phishky - Гранти", "Гранти UA", "Grant UP!", "Гранти та можливості",
    "Громадський Простір", "Гуманітарний вісник", "lawyer for NGOs", "Ukrainian Startup Fund",
    "House of Europe", "Korobova | Бізнес | Гранти | Навчання", "Центр Лідерства УКУ", "Твій космос можливостей 🚀",
    "Стипендії, гранти, можливості для молоді", "USAID AГРО || Відкриті можливості та новини",
    "Бізнес та розвиток: канал агенції PPV", "ГРАНТОВІ МОЖЛИВОСТІ", "Неформальне «О»", "БЛІЦ",
    "Українська Волонтерська Служба", "Forbes Ukraine", "УКФ_ЩОДНЯ", "Навзаєм", "IN OMNIA PARATUS",
    "Простір твого зростання / Your development space", "Разом!", "ГО 'Сила підприємців'🇺🇦", "UGEN 🇺🇦", 
    "PRAGMATIKA", "UAS | Українська асоціація студентів 💛", "Об'єднання роботодавців", "КУЛЬТУРА. МОЖЛИВОСТІ.",
    "Гранти для бізнесу - грантрайтер Олена Черкаська", "Співпраця освіти та бізнесу: Uni-Biz Bridge від UGEN",
    "GEN Ukraine | Global Ecovillage Network", "Можливості для 🇺🇦 молоді від 🇪🇺", 
    "Молодіжна рада Харкова | Kharkiv Youth City Council", "МІЖ ІНШИМ", "UniCompass 👩‍🎓✈️ Можливості, обміни, стипендії, стажування, гранти",
    "soul✨mate", "Вотум довіри: гранти, тренінги, розвиток ОГС", "ГРАНТИ для бізнесу України", "Seeds of Bravery",
    "ГРА В ДОВГУ", "СМІЛИВІ - спільнота молодіжних рад України"
]

# Second list
list2 = [
    "IN OMNIA PARATUS", "Deeds4kids", "EducationUSA.Ukraine", "МІНІСТЕРСТВО ПЕРСПЕКТИВ", 
    "Твій космос можливостей 🚀", "Grant UP!", "UNI WORK", "on the record | media&culture",
    "UniCompass 👩‍🎓✈️ Можливості, обміни,", "Lead List Youth: обміни, програми,", 
    "Грантові фішки - Grantovy Phishky", "soul✨mate", "Гранти та можливості", "kpimobility — Мобільність КПІ", 
    "#КорисностіКанал", "International Youth Opportunities", "10:11 Включайся", 
    "ChannelOfYoungScientistsOfNASU", "academic journey🎯", "МІНІСТЕРСТВО ПЕРСПЕКТИВ", 
    "Можливості для 🇺🇦 молоді від 🇪🇺", "Неформальне «О»", "Центр розвитку кар'єри КПІ ім. Ігоря", 
    "Можливості для учнів", "Стипендії, гранти, можливості для", "ГРАНТОВІ МОЖЛИВОСТІ", 
    "Kyiv Academic University", "Разом!", "Deeds4kids", "ГУРТ", "Гранти UA", "STUDWAY - СТУДВЕЙ", 
    "ДНВР 🇺🇦", "Простір твого зростання / Your development"
]

# Combine the two lists and remove duplicates using set()
combined_list = list(set(list2 + list1))

# Sort the list if needed (optional)
combined_list.sort()

# Print the combined list
for item in combined_list:
    print(item)