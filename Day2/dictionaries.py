contact_info = {
    "Gerti" : "48 000 000",
    "Dreni" : "49 123 456"
}

dren_phone = contact_info["Dreni"]
print("+383" , dren_phone)

contact_info["Dreni"] = "49 681 802"
dren_phone = contact_info["Dreni"]
print("+383", dren_phone)

contact_info["Amant"] = "45 627 345"
print("+383" , contact_info["Amant"])

del contact_info["Gerti"]
print(contact_info)

contact_information = {
    "Dren":{
        "Phone":"49 681 802",
        "Email":"dren@gmail.com",
        "Birthday":"26/03/2009"
    },
    "Gerti":{
        "Phone":"49 134 456",
        "Email":"gerti@gmail.com",
        "Birthday":"28/06/2013"
    },
    "Amant":{
        "Phone":"49 876 543",
        "Email":"amant@gmail.com",
        "Birthday":"15/10/2011"
    }
}
print(contact_information)

dren_info = contact_information["Dren"]
print(dren_info)

contact = {
    "Dren":("49681802", "dren@gmail.com", "26/03/2009"),
    "Gerti":("89234751", "gerti@gmail.com", "28/06/2013"),
    "Amant":("1094851", "amant@gmail.com", "15/10/2011"),
}

gerti_info = contact["Gerti"]
gerti_birthday = gerti_info[2]
print(gerti_birthday)
