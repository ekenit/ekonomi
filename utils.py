# Utility Module
# Common utility functions and shared code snippets...

def shared_function():
    # Code for a shared utility function...
    pass

# Other related utility functions...
expenses_mapping = {
    #BILTEMA
    'BILTEMA SWED': 'BILTEMA',
    'BILTEMA SWEDEN KATRI': 'BILTEMA',
    'BILTEMA SWEDEN KATRINE': 'BILTEMA',
    #COOP
    'COOP KATRINE': 'COOP',
    'COOP STENBÄR': 'COOP',
    'STORA COOP N': 'COOP',
    'COOP KONSUM': 'COOP',
    'COOP STENBAR': 'COOP',
    'COOP OXELÖSU': 'COOP',
    'COOP GARNISO': 'COOP',
    'COOP KATRINEHOLM': 'COOP',
    'COOP KONSUM T-CENTRALE': 'COOP',
    #MATPIRATEN
    'MATPIRATEN F': 'MATPIRATEN',
    'MATPIRATEN FLEN': 'MATPIRATEN',
    'MATPIRATEN K': 'MATPIRATEN',
    'MATPIRATEN KATRINEHO': 'MATPIRATEN',
    #FOODORA
    'FOODORA SWED': 'FOODORA AB',
    'Foodora AB': 'FOODORA AB',
    #TEMPO
    'TEMPO VALLA STORGATAN': 'TEMPO',
    'TEMPO VALLA STORGATA': 'TEMPO',
    'TEMPO OXELÖS': 'TEMPO',
    'TEMPO VALLA': 'TEMPO',
    #SYSTEMBOLAGET
    'Systembolaget': 'SYSTEMBOLAGET',
    'SYSTEMBOLAGE': 'SYSTEMBOLAGET',
    #MAX
    'MAX  NYKOPIN': 'MAX HAMBURGER',
    'WWW MAX SE': 'MAX HAMBURGER',
    'MAX BURGERS': 'MAX HAMBURGER',
    'K*MAX BURGER': 'MAX HAMBURGER',
    'MAX I NYKOPI': 'MAX HAMBURGER',
    #MCDONALDS
    'MCDONALDS  A': 'MCDONALDS',
    'MCDONALDS 21': 'MCDONALDS',
    'MCD 041 - NY': 'MCDONALDS',
    'MCD 41 NYKOP': 'MCDONALDS',
    'MCDONALDS KATRI': 'MCDONALDS',
    'MCD 218 - KA': 'MCDONALDS',
    'MCD INGELSTA': 'MCDONALDS',
    'McD 0218 Katrineholm': 'MCDONALDS',
    'MCD 218 - KATRI': 'MCDONALDS',
    'MCD 0179 STH': 'MCDONALDS',


    #BURGER KING
    'Burger King Katrineh': 'BURGER KING',
    'BURGER KING5': 'BURGER KING',
    'BURGER KING KAT': 'BURGER KING',
    #KLARNA
    'KLARNA  RATS': 'KLARNA',
    'KLARNA BANK': 'KLARNA',
    'Klarna*ratsit.se': 'KLARNA',
    'KLARNA BANK AB': 'KLARNA',
    'KLARNA AB': 'KLARNA',
    'Klarna*hatstore.se': 'KLARNA',
    'KLARNA  XXL': 'KLARNA',
    'Klarna*Gymgrossisten.c': 'KLARNA',
    'Klarna*casall.com': 'KLARNA',
    'Klarna*beckmann-norw': 'KLARNA',
    'KLARNA DUSTI': 'KLARNA',
    'Klarna*outnorth.se': 'KLARNA',
    #RUSTA
    'RUSTA - 69 K': 'RUSTA',
    'RUSTA - 38 N': 'RUSTA',
    'RUSTA NYKOPI': 'RUSTA',
    'RUSTA - 69 KATRINEHOLM': 'RUSTA',

    #KATRINEHOLM KOMMUN
    'KATRINEHOLMS K': 'KATRINEHOLMS KOMMUN',
    # GOOGLE
    'GOOGLE  GOOG': 'GOOGLE',
    'GOOGLE  YOUT': 'GOOGLE',
    'GOOGLE GOOGL': 'GOOGLE',
    'GOOGLE *YouTubePremi': 'GOOGLE',
    'GOOGLE YOUTU': 'GOOGLE',
    'CCÖGOOGLE CO': 'GOOGLE',
    'GOOGLE *YouTubePremium': 'GOOGLE',
    'G CO/HELPPAY': 'GOOGLE',
    # SJ
    'SJ.SE': 'SJ',
    'SJ AB': 'SJ',
    # AMAZON

    # PROTON
    'GENEVA': 'PROTONMAIL',
    'PROTON': 'PROTONMAIL',
    # IF
    'IF SKADEFÖRSÄKRING AB': 'IF SKADEFÖRSÄKRING',
    'IF SKADEFÖRS': 'IF SKADEFÖRSÄKRING',
    'IF SKADEFÖRSÄK': 'IF SKADEFÖRSÄKRING',
    'IF SKADEFÖRSÄKRING AB (P': 'IF SKADEFÖRSÄKRING',

    # WILLYS
    'WILLYS FLEN TISTELN': 'WILLYS',
    'WILLYS KATRI': 'WILLYS',
    'WILLYS NYKÖP': 'WILLYS',
    'WILLYS FLEN': 'WILLYS',
    'K*WILLY:S AB': 'WILLYS',
    'WILLYS KATRINEHOLM ': 'WILLYS',
    'WILLYS KATRINEHOLM': 'WILLYS',


    # ICA
    'ICA KVANTUM': 'ICA',
    'MAXI ICA STO': 'ICA',
    'MAXI ICA STORMARKNAD': 'ICA',
    'ICA NARA VIB': 'ICA',
    'ICA SUPERMAR': 'ICA',
    'MAXI ICA STORMARKNAD K': 'ICA',
    'ICA KVANTUM FLEN': 'ICA',
    'ICA MAXI KATRINEHOLM': 'ICA',
    
    # AMAZON
    'AMAZONMKTPLC': 'AMAZON',
    'AMAZON VIDEO': 'AMAZON',
    'Amazon Prime': 'AMAZON',
    'AMAZON COM': 'AMAZON',
    'AMAZON PRIME': 'AMAZON',
    'AMAZONRETAIL': 'AMAZON',

    'AMAZONRETAIL*H80O43Y': 'AMAZON',
    'AMAZONMKTPLC*164L87Y': 'AMAZON',
    'AMAZONMKTPLC*GU2YE3I': 'AMAZON',
    'AMAZONMKTPLC*437TY9L': 'AMAZON',
    'AAMAZONMKTPLC*1K7840H': 'AMAZON',
    'AMAZONMKTPLC*MV2L23B': 'AMAZON',
    'AMAZONMKTPLC*VQ7179X': 'AMAZON',
    'AMAZONMKTPLC*1L6XE6Q': 'AMAZON',
    'AMAZONMKTPLC*VG6LG0E': 'AMAZON',
    'AMAZONRETAIL*DA0TR0KK5': 'AMAZON',
    'AMAZONRETAIL*DA0TR0KK5': 'AMAZON',


    # APPLE
    'APPLE COM/BI': 'APPLE',
    'APPLE.COM/BILL': 'APPLE',

    # LIDL
    'LIDL 192 / K': 'LIDL',
    'LIDL 117 / N': 'LIDL',

    # SL
    'AB STORSTOCKHO': 'SL',
    'AB STORSTOCK': 'SL',
    'LAB STORSTOCK': 'SL',
    'SL APP': 'SL',

    # CIRKLE K 
    'CIRCLE K NYK': 'CIRKLE K',
    'CIRCLE K FLEN': 'CIRKLE K',
    'CIRCLE K GEV': 'CIRKLE K',
    'CIRCLE K ENGELHOLM': 'CIRKLE K',
    'CIRCLE K KAL': 'CIRKLE K',
    
    #TEKNISKA VERKEN
    'TEKNISKA VERKEN I LINKÖP': 'TEKNISKA VERKEN',
    'TEKNISKA VERKEL': 'TEKNISKA VERKEN',
    'TEKNISKA VERKE': 'TEKNISKA VERKEN',
    'TEKNISKA VERKEN': 'TEKNISKA VERKEN',
    # REMEMBER
    'ENTERCARD GROUP AB': 'REMEMBERCARD',

    # IKEA
    'IKEA-LINKOPI': 'IKEA',
    'IKEA LINKOPI': 'IKEA',
    'IKEA SVENSKA': 'IKEA',
    'WWW IKEA SE': 'IKEA',
    'IKEA LINKOPING HFB E': 'IKEA',

    # JYSK
    'JYSK NYKOPIN': 'JYSK',
    'JYSK KATRINE': 'JYSK',
    'JYSK KATRINE': 'JYSK',
    # GODADDY
    'DNH GODADDY': 'GODADDY',
    'DNH*GODADDY.COM SEK': 'GODADDY',

    # KJELL
    'KJELL & CO 7': 'KJELL',
    'KJELL & CO 104': 'KJELL',
    'KJELL & CO 1': 'KJELL',
    # O O B
    'OOB KATRINEH': 'OOB',
    'OOB NYKOPING': 'OOB',

    # RATSIT
    'RATSIT SE': 'RATSIT',
    'RATSIT.SE': 'RATSIT',

    # HEMKOP
    'HEMKÖP NYKÖP': 'HEMKOP',
    'HEMKÖP DELSB': 'HEMKOP',

    # LINDEX
    'LINDEX/27': 'LINDEX',
    'LINDEX KATRI': 'LINDEX',

    # SECOND HAND
    'PMU SECOND HAND KATR': 'SECOND HAND',
    'PMU SECOND H': 'SECOND HAND',

    # STOCKHOLM MAT
    'Sushi Rebellion G{rd': 'LUNCHMAT STOCKHOLM',
    'Lulu Sushi och Poke': 'LUNCHMAT STOCKHOLM',
    'FUTURE DININ': 'LUNCHMAT STOCKHOLM',
    'Lulu Sushi och Poke': 'LUNCHMAT STOCKHOLM',
    'PIZZERIA GYL': 'LUNCHMAT STOCKHOLM',
    'WKB GA.RDET': 'LUNCHMAT STOCKHOLM',
    'PHILS BURGER SANDHAMNS': 'LUNCHMAT STOCKHOLM',
    'RESTAURANG A': 'LUNCHMAT STOCKHOLM',


    #UTEMAT KATRINEHOLM
    'CAMILLA OCH': 'UTEMAT',
    'YAM-YAM': 'UTEMAT',
    'CHOPCHOP NYK': 'UTEMAT',
    'KAEN ARITO': 'UTEMAT',
    'PIZZERIA ESP': 'UTEMAT',
    'CALOMIDA KAT': 'UTEMAT',
    'KFC NYKOPING': 'UTEMAT',
    'DELIVERY HER': 'UTEMAT',
    'THAI FOOD &amp; SUSHI': 'UTEMAT',
    'SAILORKICKIS': 'UTEMAT',
    'BRODERNAS ST': 'UTEMAT',
    'KOHIRO SUSHI': 'UTEMAT',
    'THAI FOOD &': 'UTEMAT',
    'NK BAR OCH KOK': 'UTEMAT',
    'PINCHOS NYKO': 'UTEMAT',
    'ORDER.YAMYAMRESTAURANG': 'UTEMAT',
    # LADDNING
    'OPIGO SE': 'LADDNING',
    'FORTUM COM': 'LADDNING',
    'FORTUM MARKE': 'LADDNING',
    'FORTUM CHA': 'LADDNING',
    'E ON 50KW OK': 'LADDNING',
    # FIK 
    'ESPRESSO H 3': 'FIK',
    'SKAFFERIET': 'FIK',
    'ESPRESSO HOU': 'FIK',
    'BR@D & SALT BAG': 'FIK',
    # STREAMING
    'HBO NORDIC A': 'STREAMING',
    'HBO MAX': 'STREAMING',
    'ESPRESSO HOU': 'STREAMING',
    'VIAPLAY AB': 'STREAMING',
    'ESPRESSO HOU': 'STREAMING',

    # Lägg till fler poster efter behov

    # SVENSKA SPEL
    'AB SVENSKA S': 'SVENSKA SPEL',
    'HBO MAX': 'SVENSKA SPEL',
    'ESPRESSO HOU': 'SVENSKA SPEL',

}