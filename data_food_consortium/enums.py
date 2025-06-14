from django.db import models


DFC_PT_URL = "https://raw.githubusercontent.com/datafoodconsortium/taxonomies/refs/heads/main/productTypes.rdf"


class ProductType(models.TextChoices):
    AROMATIC = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#aromatic",
        "Aromatic",
    )
    APERITIF = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#aperitif",
        "Aperitif",
    )
    DRIED_HERB = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#dried_herb",
        "Dried_herb",
    )
    GOAT_YOGURT_WITH_FRUITS = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#goat-yogurt-with-fruits",
        "Goat yogurt with fruits",
    )
    BEEF = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#beef",
        "Beef",
    )
    CORN_SALAD = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#corn-salad",
        "Corn salad",
    )
    DRIED_GOODS = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#dried_goods",
        "Dried goods",
    )
    HIERLOOM_TOMATO = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#hierloom-tomato",
        "Hierloom tomato",
    )
    HERB = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#herb",
        "Herb",
    )
    GRAIN = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#grain",
        "Grain",
    )
    QUAIL = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#quail",
        "Quail",
    )
    FIG = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#fig",
        "Fig",
    )
    CHERVIL = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#chervil",
        "Chervil",
    )
    YOGURT_WITH_FRUITS = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#yogurt-with-fruits",
        "Yogurt with fruits",
    )
    NON_LOCAL_VEGETABLE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#non-local-vegetable",
        "Non local vegetable",
    )
    BEER = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#beer",
        "Beer",
    )
    LAUREL = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#laurel",
        "Laurel",
    )
    RADISH = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#radish",
        "Radish",
    )
    YOGURT_ON_A_BED_OF_FRUIT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#yogurt-on-a-bed-of-fruit",
        "Yogurt on a bed of fruit",
    )
    MEAT_PRODUCT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#meat-product",
        "Meat product",
    )
    DUCK = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#duck",
        "Duck",
    )
    ROMANESCO = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#romanesco",
        "Romanesco",
    )
    ROSEMARY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#rosemary",
        "Rosemary",
    )
    BOTTLED_VEGETABLE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#bottled-vegetable",
        "Bottled vegetable",
    )
    FROZEN_MEAL = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#frozen-meal",
        "Frozen meal",
    )
    ORANGE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#orange",
        "Orange",
    )
    CELERIAC = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#celeriac",
        "Celeriac",
    )
    HONEY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#honey",
        "Honey",
    )
    RUTABAGA = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#rutabaga",
        "Rutabaga",
    )
    COW_DAIRY_PRODUCT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#cow-dairy-product",
        "Cow dairy product",
    )
    APRICOT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#apricot",
        "Apricot",
    )
    LEMON = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#lemon",
        "Lemon",
    )
    CHICKEN = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#chicken",
        "Chicken",
    )
    FOURTH_RANGE_VEGETABLE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#fourth-range-vegetable",
        "Fourth range vegetable",
    )
    OTHER_DAIRY_PRODUCT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#other-dairy-product",
        "Other dairy product",
    )
    BUTTERNUT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#butternut",
        "Butternut",
    )
    BUTTER = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#butter",
        "Butter",
    )
    VIENNOISERIE_ = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#viennoiserie-",
        "Viennoiserie ",
    )
    CHINESE_CABBAGE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#chinese-cabbage",
        "Chinese cabbage",
    )
    PARSNIP = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#parsnip",
        "Parsnip",
    )
    PARIS_MUSHROOM = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#paris-mushroom",
        "Paris mushroom",
    )
    GOAT_DAIRY_DESSERT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#goat-dairy-dessert",
        "Goat dairy dessert",
    )
    SHALLOT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#shallot",
        "Shallot",
    )
    BLUEBERRY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#blueberry",
        "Blueberry",
    )
    OTHER_MILK = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#other-milk",
        "Other milk",
    )
    SOUP = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#soup",
        "Soup",
    )
    DEATHS_TRUMPET = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#deaths-trumpet",
        "Deaths trumpet",
    )
    PLUM = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#plum",
        "Plum",
    )
    KALE_CABBAGE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#kale-cabbage",
        "Kale cabbage",
    )
    CLUSTER_TOMATO = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#cluster-tomato",
        "Cluster tomato",
    )
    BASIL = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#basil",
        "Basil",
    )
    DRINK = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#drink",
        "Drink",
    )
    TOMATO = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#tomato",
        "Tomato",
    )
    INEDIBLE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#inedible",
        "Inedible",
    )
    DRIED_VEGETABLE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#dried-vegetable",
        "Dried vegetable",
    )
    FLAVORED_YOGURT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#flavored-yogurt",
        "Flavored yogurt",
    )
    SPINACH = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#spinach",
        "Spinach",
    )
    FRESH_CREAM = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#fresh-cream",
        "Fresh cream",
    )
    CHESTNUT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#chestnut",
        "Chestnut",
    )
    CAULIFLOWER = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#cauliflower",
        "Cauliflower",
    )
    UCHIKI_KURI_SQUASH = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#uchiki-kuri-squash",
        "Uchiki kuri squash",
    )
    GOAT_MATURE_CHEESE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#goat-mature-cheese",
        "Goat mature cheese",
    )
    MOUSSERON = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#mousseron",
        "Mousseron",
    )
    MINT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#mint",
        "Mint",
    )
    LAMB = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#lamb",
        "Lamb",
    )
    ROCKET = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#rocket",
        "Rocket",
    )
    SEED = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#seed",
        "Seed",
    )
    PRUNE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#prune",
        "Prune",
    )
    RHUBARB = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#rhubarb",
        "Rhubarb",
    )
    RICE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#rice",
        "Rice",
    )
    GOAT_SWEET_YOGURT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#goat-sweet-yogurt",
        "Goat sweet yogurt",
    )
    STRAWBERRY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#strawberry",
        "Strawberry",
    )
    CANNED_FRUIT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#canned-fruit",
        "Canned fruit",
    )
    OIL = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#oil",
        "Oil",
    )
    SALSIFY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#salsify",
        "Salsify",
    )
    TURKEY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#turkey",
        "Turkey",
    )
    GOAT_FRESH_CHEESE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#goat-fresh-cheese",
        "Goat fresh cheese",
    )
    LEEK = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#leek",
        "Leek",
    )
    MESCLUN = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#mesclun",
        "Mesclun",
    )
    SAVORY_GROCERIES = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#savory-groceries",
        "Savory groceries",
    )
    RED_CABBAGE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#red-cabbage",
        "Red cabbage",
    )
    SHEEP_SWEET_YOGURT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#sheep-sweet-yogurt",
        "Sheep sweet yogurt",
    )
    PASTRY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#pastry",
        "Pastry",
    )
    COURGETTE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#courgette",
        "Courgette",
    )
    COULEMELLE_MUSHROOM = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#coulemelle-mushroom",
        "Coulemelle mushroom",
    )
    BLACKBERRY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#blackberry",
        "Blackberry",
    )
    JAM = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#jam",
        "Jam",
    )
    SHEEP_MILK = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#sheep-milk",
        "Sheep milk",
    )
    DRIED_FRUIT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#dried-fruit",
        "Dried fruit",
    )
    KOHLRABI = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#kohlrabi",
        "Kohlrabi",
    )
    DILL = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#dill",
        "Dill",
    )
    SAGE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#sage",
        "Sage",
    )
    SHEEP_DAIRY_DESSERT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#sheep-dairy-dessert",
        "Sheep dairy dessert",
    )
    PROCESSED_FRUIT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#processed-fruit",
        "Processed fruit",
    )
    SALTING = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#salting",
        "Salting",
    )
    GOAT_NATURAL_YOGURT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#goat-natural-yogurt",
        "Goat natural yogurt",
    )
    WINE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#wine",
        "Wine",
    )
    OYSTER_MUSHROOM = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#oyster-mushroom",
        "Oyster mushroom",
    )
    CABBAGE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#cabbage",
        "Cabbage",
    )
    CHEWED_UP = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#chewed-up",
        "Chewed up",
    )
    SHEEP_YOGURT_ON_A_BED_OF_FRUIT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#sheep-yogurt-on-a-bed-of-fruit",
        "Sheep yogurt on a bed of fruit",
    )
    SHEEP_YOGURT_WITH_FRUITS = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#sheep-yogurt-with-fruits",
        "Sheep yogurt with fruits",
    )
    READY_MEAL = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#ready-meal",
        "Ready meal",
    )
    DAIRY_DESSERT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#dairy-dessert",
        "Dairy dessert",
    )
    OTHER_CHEESE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#other-cheese",
        "Other cheese",
    )
    FRUIT_JUICE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#fruit-juice",
        "Fruit juice",
    )
    SIMMERING_MEAT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#simmering-meat",
        "Simmering meat",
    )
    EGG = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#egg",
        "Egg",
    )
    FRUIT_IN_COMPOTE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#fruit-in-compote",
        "Fruit in compote",
    )
    MANDARIN = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#mandarin",
        "Mandarin",
    )
    CORIANDER = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#coriander",
        "Coriander",
    )
    GOAT_YOGURT_ON_A_BED_OF_FRUIT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#goat-yogurt-on-a-bed-of-fruit",
        "Goat yogurt on a bed of fruit",
    )
    CHICORY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#chicory",
        "Chicory",
    )
    SEASHELL = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#seashell",
        "Seashell",
    )
    FIFTH_RANGE_VEGETABLE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#fifth-range-vegetable",
        "Fifth range vegetable",
    )
    CHERRY_TOMATO = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#cherry-tomato",
        "Cherry tomato",
    )
    FRESH_CHEESE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#fresh-cheese",
        "Fresh cheese",
    )
    QUINOA = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#quinoa",
        "Quinoa",
    )
    SALAD_MIX = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#salad-mix",
        "Salad mix",
    )
    QUINCE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#quince",
        "Quince",
    )
    OLD_VARIETY_TOMATO = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#old-variety-tomato",
        "Old variety tomato",
    )
    SAVOY_CABBAGE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#savoy-cabbage",
        "Savoy cabbage",
    )
    FLAKE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#flake",
        "Flake",
    )
    FROZEN = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#frozen",
        "Frozen",
    )
    DANDELION = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#dandelion",
        "Dandelion",
    )
    PATTYPAN_SQUASH = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#pattypan-squash",
        "Pattypan squash",
    )
    SOFT_DRINK = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#soft-drink",
        "Soft drink",
    )
    PROCESSED_VEGETABLE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#processed-vegetable",
        "Processed vegetable",
    )
    FISHERY_PRODUCT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#fishery-product",
        "Fishery product",
    )
    FESTIVE_POULTRY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#festive-poultry",
        "Festive poultry",
    )
    CREPE_AND_GALETTE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#crepe-and-galette",
        "Crepe and galette",
    )
    LETTUCE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#lettuce",
        "Lettuce",
    )
    HIERLOOM_SQUASH = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#hierloom-squash",
        "Hierloom squash",
    )
    DELICATESSEN = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#delicatessen",
        "Delicatessen",
    )
    FROZEN_VEGETABLE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#frozen-vegetable",
        "Frozen vegetable",
    )
    SHELLFISH = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#shellfish",
        "Shellfish",
    )
    GRAPE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#grape",
        "Grape",
    )
    ROUND_TOMATO = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#round-tomato",
        "Round tomato",
    )
    SALT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#salt",
        "Salt",
    )
    NON_LOCAL_FRUIT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#non-local-fruit",
        "Non local fruit",
    )
    CONFECTIONERY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#confectionery",
        "Confectionery",
    )
    CREAM_CHEESE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#cream-cheese",
        "Cream cheese",
    )
    TRUFFLE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#truffle",
        "Truffle",
    )
    PEAS = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#peas",
        "Peas",
    )
    NUT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#nut",
        "Nut",
    )
    CHILLI_PEPPER = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#chilli-pepper",
        "Chilli pepper",
    )
    PUMPKIN = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#pumpkin",
        "Pumpkin",
    )
    CHERRY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#cherry",
        "Cherry",
    )
    PARSLEY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#parsley",
        "Parsley",
    )
    SALAD = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#salad",
        "Salad",
    )
    EGGPLANT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#eggplant",
        "Eggplant",
    )
    RABBIT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#rabbit",
        "Rabbit",
    )
    NECTARINE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#nectarine",
        "Nectarine",
    )
    PLANT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#plant",
        "Plant",
    )
    PORK = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#pork",
        "Pork",
    )
    VEAL = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#veal",
        "Veal",
    )
    ENDIVE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#endive",
        "Endive",
    )
    FISH = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#fish",
        "Fish",
    )
    SHEEPFOOT_MUSHROOM = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#sheepfoot-mushroom",
        "Sheepfoot mushroom",
    )
    LEMONADE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#lemonade",
        "Lemonade",
    )
    FLOWER = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#flower",
        "Flower",
    )
    GOOSEBERRY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#gooseberry",
        "Gooseberry",
    )
    CHIVE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#chive",
        "Chive",
    )
    KIWI = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#kiwi",
        "Kiwi",
    )
    GOOSE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#goose",
        "Goose",
    )
    FRUIT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#fruit",
        "Fruit",
    )
    CHANTERELLE_MUSHROOM = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#chanterelle-mushroom",
        "Chanterelle mushroom",
    )
    SMOOTH_CABBAGE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#smooth-cabbage",
        "Smooth cabbage",
    )
    MILK = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#milk",
        "Milk",
    )
    SWEET_YOGURT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#sweet-yogurt",
        "Sweet yogurt",
    )
    SWEET_GROCERIES = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#sweet-groceries",
        "Sweet groceries",
    )
    FROZEN_MEAT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#frozen-meat",
        "Frozen meat",
    )
    PASTA = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#pasta",
        "Pasta",
    )
    CURRANT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#currant",
        "Currant",
    )
    KALE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#kale",
        "Kale",
    )
    CRESS = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#cress",
        "Cress",
    )
    LENTILS = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#lentils",
        "Lentils",
    )
    ALCOHOLIC_BEVERAGE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#alcoholic-beverage",
        "Alcoholic beverage",
    )
    VEGETABLE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#vegetable",
        "Vegetable",
    )
    PIGEON = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#pigeon",
        "Pigeon",
    )
    THYME = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#thyme",
        "Thyme",
    )
    BLUEFOOT_MUSHROOM = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#bluefoot-mushroom",
        "Bluefoot mushroom",
    )
    CHARD = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#chard",
        "Chard",
    )
    COSMETIC = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#cosmetic",
        "Cosmetic",
    )
    MUSHROOM = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#mushroom",
        "Mushroom",
    )
    DIGESTIVE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#digestive",
        "Digestive",
    )
    MELON = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#melon",
        "Melon",
    )
    BEETROOT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#beetroot",
        "Beetroot",
    )
    SHEEP_DAIRY_PRODUCT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#sheep-dairy-product",
        "Sheep dairy product",
    )
    YAM = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#yam",
        "Yam",
    )
    CARROT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#carrot",
        "Carrot",
    )
    ALMOND = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#almond",
        "Almond",
    )
    NATURAL_YOGURT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#natural-yogurt",
        "Natural yogurt",
    )
    FROZEN_FRUIT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#frozen-fruit",
        "Frozen fruit",
    )
    TARRAGON = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#tarragon",
        "Tarragon",
    )
    SHEEP_MATURE_CHEESE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#sheep-mature-cheese",
        "Sheep mature cheese",
    )
    SNAILS = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#snails",
        "Snails",
    )
    CELERY_BRANCH = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#celery-branch",
        "Celery branch",
    )
    POTATO = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#potato",
        "Potato",
    )
    BREAD = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#bread",
        "Bread",
    )
    CUCUMBER = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#cucumber",
        "Cucumber",
    )
    GUINEA_FOWL = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#guinea-fowl",
        "Guinea fowl",
    )
    FLOUR = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#flour",
        "Flour",
    )
    CLEMENTINE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#clementine",
        "Clementine",
    )
    CANNED_VEGETABLE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#canned-vegetable",
        "Canned vegetable",
    )
    GIROLLE_MUSHROOM = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#girolle-mushroom",
        "Girolle mushroom",
    )
    GOAT_DAIRY_PRODUCT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#goat-dairy-product",
        "Goat dairy product",
    )
    GARLIC = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#garlic",
        "Garlic",
    )
    JERUSALEM_ARTICHOKE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#jerusalem-artichoke",
        "Jerusalem artichoke",
    )
    PIE_PASTRY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#pie-pastry",
        "Pie pastry",
    )
    PEAR = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#pear",
        "Pear",
    )
    SEMOLINA = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#semolina",
        "Semolina",
    )
    GRILLING_MEAT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#grilling-meat",
        "Grilling meat",
    )
    PEPPER = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#pepper",
        "Pepper",
    )
    BRUSSELS_SPROUTS = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#brussels-sprouts",
        "Brussels sprouts",
    )
    SQUASH = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#squash",
        "Squash",
    )
    ARTICHOKE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#artichoke",
        "Artichoke",
    )
    SHEEP_FLAVORED_YOGURT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#sheep-flavored-yogurt",
        "Sheep flavored yogurt",
    )
    HAZELNUT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#hazelnut",
        "Hazelnut",
    )
    PORCINI = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#porcini",
        "Porcini",
    )
    MATURE_CHEESE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#mature-cheese",
        "Mature cheese",
    )
    WALNUT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#walnut",
        "Walnut",
    )
    COOKED_MEAT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#cooked-meat",
        "Cooked meat",
    )
    FRESH_MEAT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#fresh-meat",
        "Fresh meat",
    )
    DAIRY_PRODUCT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#dairy-product",
        "Dairy product",
    )
    SHEEP_FRESH_CHEESE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#sheep-fresh-cheese",
        "Sheep fresh cheese",
    )
    MEDLAR = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#medlar",
        "Medlar",
    )
    BAKERY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#bakery",
        "Bakery",
    )
    BLACKCURRANT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#blackcurrant",
        "Blackcurrant",
    )
    GOAT_FLAVORED_YOGURT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#goat-flavored-yogurt",
        "Goat flavored yogurt",
    )
    LOCAL_GROCERY_STORE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#local-grocery-store",
        "Local grocery store",
    )
    BISCUIT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#biscuit",
        "Biscuit",
    )
    BERRY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#berry",
        "Berry",
    )
    BROCCOLI_CABBAGE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#broccoli-cabbage",
        "Broccoli cabbage",
    )
    APPLES = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#apples",
        "Apples",
    )
    BEANS = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#beans",
        "Beans",
    )
    GOAT_MILK = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#goat-milk",
        "Goat milk",
    )
    MOREL = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#morel",
        "Morel",
    )
    GREEN_GARLIC = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#green-garlic",
        "Green garlic",
    )
    POULTRY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#poultry",
        "Poultry",
    )
    FENNEL = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#fennel",
        "Fennel",
    )
    SHEEP_NATURAL_YOGURT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#sheep-natural-yogurt",
        "Sheep natural yogurt",
    )
    PEACH = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#peach",
        "Peach",
    )
    ASPARAGUS = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#asparagus",
        "Asparagus",
    )
    BOTTLED_FRUIT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#bottled-fruit",
        "Bottled fruit",
    )
    ONION = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#onion",
        "Onion",
    )
    BEAN = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#bean",
        "Bean",
    )
    MILKY_MUSHROOM = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#milky-mushroom",
        "Milky mushroom",
    )
    SMOOTHIE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#smoothie",
        "Smoothie",
    )
    TURNIP = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#turnip",
        "Turnip",
    )
    CIDER = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#cider",
        "Cider",
    )
    RASPBERRY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#raspberry",
        "Raspberry",
    )
