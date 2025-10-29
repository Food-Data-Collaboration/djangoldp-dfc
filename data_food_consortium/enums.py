from django.db import models


DFC_B_URL = "https://raw.githubusercontent.com/datafoodconsortium/ontology/refs/heads/master/src/DFC_BusinessOntology.owl"
DFC_PT_URL = "https://raw.githubusercontent.com/datafoodconsortium/taxonomies/refs/heads/main/productTypes.rdf"


class ShippingOptionType(models.TextChoices):
    PICKUP = (f"{DFC_B_URL}#PickupOption", "Pick-up")
    DELIVERY = (f"{DFC_B_URL}#DeliveryOption", "Delivery")


class ResourceImportSource(models.TextChoices):
    ADMIN_SITE = ("admin_site", "Admin site")
    COMMAND_LINE = ("command_line", "Command line")
    UPDATE_WEBHOOK = ("update_webhook", "Update webhook event")
    REFRESH_WEBHOOK = ("refresh_webhook", "Refresh webhook event")


class ProductType(models.TextChoices):
    ALCOHOLIC_BEVERAGE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#alcoholic-beverage",
        "Alcoholic beverage",
    )
    ALMOND = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#almond",
        "Almond",
    )
    APERITIF = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#aperitif",
        "Aperitif",
    )
    APPLES = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#apples",
        "Apples",
    )
    APRICOT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#apricot",
        "Apricot",
    )
    AROMATIC = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#aromatic",
        "Aromatic",
    )
    ARTICHOKE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#artichoke",
        "Artichoke",
    )
    ASPARAGUS = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#asparagus",
        "Asparagus",
    )
    BAKERY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#bakery",
        "Bakery",
    )
    BASIL = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#basil",
        "Basil",
    )
    BEAN = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#bean",
        "Bean",
    )
    BEANS = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#beans",
        "Beans",
    )
    BEEF = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#beef",
        "Beef",
    )
    BEER = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#beer",
        "Beer",
    )
    BEETROOT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#beetroot",
        "Beetroot",
    )
    BERRY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#berry",
        "Berry",
    )
    BISCUIT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#biscuit",
        "Biscuit",
    )
    BLACKBERRY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#blackberry",
        "Blackberry",
    )
    BLACKCURRANT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#blackcurrant",
        "Blackcurrant",
    )
    BLUEBERRY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#blueberry",
        "Blueberry",
    )
    BLUEFOOT_MUSHROOM = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#bluefoot-mushroom",
        "Bluefoot mushroom",
    )
    BOTTLED_FRUIT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#bottled-fruit",
        "Bottled fruit",
    )
    BOTTLED_VEGETABLE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#bottled-vegetable",
        "Bottled vegetable",
    )
    BREAD = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#bread",
        "Bread",
    )
    BROCCOLI_CABBAGE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#broccoli-cabbage",
        "Broccoli cabbage",
    )
    BRUSSELS_SPROUTS = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#brussels-sprouts",
        "Brussels sprouts",
    )
    BUTTER = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#butter",
        "Butter",
    )
    BUTTERNUT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#butternut",
        "Butternut",
    )
    CABBAGE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#cabbage",
        "Cabbage",
    )
    CANNED_FRUIT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#canned-fruit",
        "Canned fruit",
    )
    CANNED_VEGETABLE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#canned-vegetable",
        "Canned vegetable",
    )
    CARROT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#carrot",
        "Carrot",
    )
    CAULIFLOWER = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#cauliflower",
        "Cauliflower",
    )
    CELERIAC = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#celeriac",
        "Celeriac",
    )
    CELERY_BRANCH = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#celery-branch",
        "Celery branch",
    )
    CHANTERELLE_MUSHROOM = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#chanterelle-mushroom",
        "Chanterelle mushroom",
    )
    CHARD = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#chard",
        "Chard",
    )
    CHERRY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#cherry",
        "Cherry",
    )
    CHERRY_TOMATO = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#cherry-tomato",
        "Cherry tomato",
    )
    CHERVIL = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#chervil",
        "Chervil",
    )
    CHESTNUT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#chestnut",
        "Chestnut",
    )
    CHEWED_UP = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#chewed-up",
        "Chewed up",
    )
    CHICKEN = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#chicken",
        "Chicken",
    )
    CHICORY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#chicory",
        "Chicory",
    )
    CHILLI_PEPPER = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#chilli-pepper",
        "Chilli pepper",
    )
    CHINESE_CABBAGE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#chinese-cabbage",
        "Chinese cabbage",
    )
    CHIVE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#chive",
        "Chive",
    )
    CIDER = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#cider",
        "Cider",
    )
    CLEMENTINE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#clementine",
        "Clementine",
    )
    CLUSTER_TOMATO = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#cluster-tomato",
        "Cluster tomato",
    )
    CONFECTIONERY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#confectionery",
        "Confectionery",
    )
    COOKED_MEAT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#cooked-meat",
        "Cooked meat",
    )
    CORIANDER = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#coriander",
        "Coriander",
    )
    CORN_SALAD = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#corn-salad",
        "Corn salad",
    )
    COSMETIC = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#cosmetic",
        "Cosmetic",
    )
    COULEMELLE_MUSHROOM = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#coulemelle-mushroom",
        "Coulemelle mushroom",
    )
    COURGETTE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#courgette",
        "Courgette",
    )
    COW_DAIRY_PRODUCT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#cow-dairy-product",
        "Cow dairy product",
    )
    CREAM_CHEESE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#cream-cheese",
        "Cream cheese",
    )
    CREPE_AND_GALETTE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#crepe-and-galette",
        "Crepe and galette",
    )
    CRESS = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#cress",
        "Cress",
    )
    CUCUMBER = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#cucumber",
        "Cucumber",
    )
    CURRANT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#currant",
        "Currant",
    )
    DAIRY_DESSERT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#dairy-dessert",
        "Dairy dessert",
    )
    DAIRY_PRODUCT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#dairy-product",
        "Dairy product",
    )
    DANDELION = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#dandelion",
        "Dandelion",
    )
    DEATHS_TRUMPET = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#deaths-trumpet",
        "Deaths trumpet",
    )
    DELICATESSEN = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#delicatessen",
        "Delicatessen",
    )
    DIGESTIVE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#digestive",
        "Digestive",
    )
    DILL = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#dill",
        "Dill",
    )
    DRIED_FRUIT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#dried-fruit",
        "Dried fruit",
    )
    DRIED_VEGETABLE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#dried-vegetable",
        "Dried vegetable",
    )
    DRIED_HERB = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#dried_herb",
        "Dried_herb",
    )
    DRIED_GOODS = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#dried_goods",
        "Dried goods",
    )
    DRINK = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#drink",
        "Drink",
    )
    DUCK = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#duck",
        "Duck",
    )
    EGG = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#egg",
        "Egg",
    )
    EGGPLANT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#eggplant",
        "Eggplant",
    )
    ENDIVE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#endive",
        "Endive",
    )
    FENNEL = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#fennel",
        "Fennel",
    )
    FESTIVE_POULTRY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#festive-poultry",
        "Festive poultry",
    )
    FIFTH_RANGE_VEGETABLE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#fifth-range-vegetable",
        "Fifth range vegetable",
    )
    FIG = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#fig",
        "Fig",
    )
    FISH = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#fish",
        "Fish",
    )
    FISHERY_PRODUCT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#fishery-product",
        "Fishery product",
    )
    FLAKE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#flake",
        "Flake",
    )
    FLAVORED_YOGURT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#flavored-yogurt",
        "Flavored yogurt",
    )
    FLOUR = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#flour",
        "Flour",
    )
    FLOWER = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#flower",
        "Flower",
    )
    FOURTH_RANGE_VEGETABLE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#fourth-range-vegetable",
        "Fourth range vegetable",
    )
    FRESH_CHEESE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#fresh-cheese",
        "Fresh cheese",
    )
    FRESH_CREAM = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#fresh-cream",
        "Fresh cream",
    )
    FRESH_MEAT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#fresh-meat",
        "Fresh meat",
    )
    FROZEN = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#frozen",
        "Frozen",
    )
    FROZEN_FRUIT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#frozen-fruit",
        "Frozen fruit",
    )
    FROZEN_MEAL = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#frozen-meal",
        "Frozen meal",
    )
    FROZEN_MEAT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#frozen-meat",
        "Frozen meat",
    )
    FROZEN_VEGETABLE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#frozen-vegetable",
        "Frozen vegetable",
    )
    FRUIT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#fruit",
        "Fruit",
    )
    FRUIT_IN_COMPOTE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#fruit-in-compote",
        "Fruit in compote",
    )
    FRUIT_JUICE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#fruit-juice",
        "Fruit juice",
    )
    GARLIC = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#garlic",
        "Garlic",
    )
    GIROLLE_MUSHROOM = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#girolle-mushroom",
        "Girolle mushroom",
    )
    GOAT_DAIRY_DESSERT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#goat-dairy-dessert",
        "Goat dairy dessert",
    )
    GOAT_DAIRY_PRODUCT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#goat-dairy-product",
        "Goat dairy product",
    )
    GOAT_FLAVORED_YOGURT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#goat-flavored-yogurt",
        "Goat flavored yogurt",
    )
    GOAT_FRESH_CHEESE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#goat-fresh-cheese",
        "Goat fresh cheese",
    )
    GOAT_MATURE_CHEESE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#goat-mature-cheese",
        "Goat mature cheese",
    )
    GOAT_MILK = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#goat-milk",
        "Goat milk",
    )
    GOAT_NATURAL_YOGURT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#goat-natural-yogurt",
        "Goat natural yogurt",
    )
    GOAT_SWEET_YOGURT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#goat-sweet-yogurt",
        "Goat sweet yogurt",
    )
    GOAT_YOGURT_ON_A_BED_OF_FRUIT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#goat-yogurt-on-a-bed-of-fruit",
        "Goat yogurt on a bed of fruit",
    )
    GOAT_YOGURT_WITH_FRUITS = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#goat-yogurt-with-fruits",
        "Goat yogurt with fruits",
    )
    GOOSE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#goose",
        "Goose",
    )
    GOOSEBERRY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#gooseberry",
        "Gooseberry",
    )
    GRAIN = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#grain",
        "Grain",
    )
    GRAPE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#grape",
        "Grape",
    )
    GREEN_GARLIC = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#green-garlic",
        "Green garlic",
    )
    GRILLING_MEAT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#grilling-meat",
        "Grilling meat",
    )
    GUINEA_FOWL = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#guinea-fowl",
        "Guinea fowl",
    )
    HAZELNUT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#hazelnut",
        "Hazelnut",
    )
    HERB = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#herb",
        "Herb",
    )
    HIERLOOM_SQUASH = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#hierloom-squash",
        "Hierloom squash",
    )
    HIERLOOM_TOMATO = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#hierloom-tomato",
        "Hierloom tomato",
    )
    HONEY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#honey",
        "Honey",
    )
    INEDIBLE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#inedible",
        "Inedible",
    )
    JAM = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#jam",
        "Jam",
    )
    JERUSALEM_ARTICHOKE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#jerusalem-artichoke",
        "Jerusalem artichoke",
    )
    KALE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#kale",
        "Kale",
    )
    KALE_CABBAGE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#kale-cabbage",
        "Kale cabbage",
    )
    KIWI = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#kiwi",
        "Kiwi",
    )
    KOHLRABI = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#kohlrabi",
        "Kohlrabi",
    )
    LAMB = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#lamb",
        "Lamb",
    )
    LAUREL = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#laurel",
        "Laurel",
    )
    LEEK = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#leek",
        "Leek",
    )
    LEMON = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#lemon",
        "Lemon",
    )
    LEMONADE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#lemonade",
        "Lemonade",
    )
    LENTILS = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#lentils",
        "Lentils",
    )
    LETTUCE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#lettuce",
        "Lettuce",
    )
    LOCAL_GROCERY_STORE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#local-grocery-store",
        "Local grocery store",
    )
    MANDARIN = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#mandarin",
        "Mandarin",
    )
    MATURE_CHEESE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#mature-cheese",
        "Mature cheese",
    )
    MEAT_PRODUCT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#meat-product",
        "Meat product",
    )
    MEDLAR = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#medlar",
        "Medlar",
    )
    MELON = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#melon",
        "Melon",
    )
    MESCLUN = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#mesclun",
        "Mesclun",
    )
    MILK = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#milk",
        "Milk",
    )
    MILKY_MUSHROOM = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#milky-mushroom",
        "Milky mushroom",
    )
    MINT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#mint",
        "Mint",
    )
    MOREL = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#morel",
        "Morel",
    )
    MOUSSERON = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#mousseron",
        "Mousseron",
    )
    MUSHROOM = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#mushroom",
        "Mushroom",
    )
    NATURAL_YOGURT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#natural-yogurt",
        "Natural yogurt",
    )
    NECTARINE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#nectarine",
        "Nectarine",
    )
    NON_LOCAL_FRUIT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#non-local-fruit",
        "Non local fruit",
    )
    NON_LOCAL_VEGETABLE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#non-local-vegetable",
        "Non local vegetable",
    )
    NUT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#nut",
        "Nut",
    )
    OIL = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#oil",
        "Oil",
    )
    OLD_VARIETY_TOMATO = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#old-variety-tomato",
        "Old variety tomato",
    )
    ONION = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#onion",
        "Onion",
    )
    ORANGE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#orange",
        "Orange",
    )
    OTHER_CHEESE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#other-cheese",
        "Other cheese",
    )
    OTHER_DAIRY_PRODUCT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#other-dairy-product",
        "Other dairy product",
    )
    OTHER_MILK = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#other-milk",
        "Other milk",
    )
    OYSTER_MUSHROOM = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#oyster-mushroom",
        "Oyster mushroom",
    )
    PARIS_MUSHROOM = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#paris-mushroom",
        "Paris mushroom",
    )
    PARSLEY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#parsley",
        "Parsley",
    )
    PARSNIP = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#parsnip",
        "Parsnip",
    )
    PASTA = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#pasta",
        "Pasta",
    )
    PASTRY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#pastry",
        "Pastry",
    )
    PATTYPAN_SQUASH = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#pattypan-squash",
        "Pattypan squash",
    )
    PEACH = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#peach",
        "Peach",
    )
    PEAR = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#pear",
        "Pear",
    )
    PEAS = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#peas",
        "Peas",
    )
    PEPPER = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#pepper",
        "Pepper",
    )
    PIE_PASTRY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#pie-pastry",
        "Pie pastry",
    )
    PIGEON = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#pigeon",
        "Pigeon",
    )
    PLANT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#plant",
        "Plant",
    )
    PLUM = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#plum",
        "Plum",
    )
    PORCINI = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#porcini",
        "Porcini",
    )
    PORK = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#pork",
        "Pork",
    )
    POTATO = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#potato",
        "Potato",
    )
    POULTRY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#poultry",
        "Poultry",
    )
    PROCESSED_FRUIT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#processed-fruit",
        "Processed fruit",
    )
    PROCESSED_VEGETABLE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#processed-vegetable",
        "Processed vegetable",
    )
    PRUNE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#prune",
        "Prune",
    )
    PUMPKIN = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#pumpkin",
        "Pumpkin",
    )
    QUAIL = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#quail",
        "Quail",
    )
    QUINCE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#quince",
        "Quince",
    )
    QUINOA = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#quinoa",
        "Quinoa",
    )
    RABBIT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#rabbit",
        "Rabbit",
    )
    RADISH = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#radish",
        "Radish",
    )
    RASPBERRY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#raspberry",
        "Raspberry",
    )
    READY_MEAL = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#ready-meal",
        "Ready meal",
    )
    RED_CABBAGE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#red-cabbage",
        "Red cabbage",
    )
    RHUBARB = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#rhubarb",
        "Rhubarb",
    )
    RICE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#rice",
        "Rice",
    )
    ROCKET = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#rocket",
        "Rocket",
    )
    ROMANESCO = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#romanesco",
        "Romanesco",
    )
    ROSEMARY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#rosemary",
        "Rosemary",
    )
    ROUND_TOMATO = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#round-tomato",
        "Round tomato",
    )
    RUTABAGA = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#rutabaga",
        "Rutabaga",
    )
    SAGE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#sage",
        "Sage",
    )
    SALAD = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#salad",
        "Salad",
    )
    SALAD_MIX = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#salad-mix",
        "Salad mix",
    )
    SALSIFY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#salsify",
        "Salsify",
    )
    SALT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#salt",
        "Salt",
    )
    SALTING = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#salting",
        "Salting",
    )
    SAVORY_GROCERIES = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#savory-groceries",
        "Savory groceries",
    )
    SAVOY_CABBAGE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#savoy-cabbage",
        "Savoy cabbage",
    )
    SEASHELL = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#seashell",
        "Seashell",
    )
    SEED = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#seed",
        "Seed",
    )
    SEMOLINA = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#semolina",
        "Semolina",
    )
    SHALLOT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#shallot",
        "Shallot",
    )
    SHEEP_DAIRY_DESSERT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#sheep-dairy-dessert",
        "Sheep dairy dessert",
    )
    SHEEP_DAIRY_PRODUCT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#sheep-dairy-product",
        "Sheep dairy product",
    )
    SHEEP_FLAVORED_YOGURT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#sheep-flavored-yogurt",
        "Sheep flavored yogurt",
    )
    SHEEP_FRESH_CHEESE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#sheep-fresh-cheese",
        "Sheep fresh cheese",
    )
    SHEEP_MATURE_CHEESE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#sheep-mature-cheese",
        "Sheep mature cheese",
    )
    SHEEP_MILK = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#sheep-milk",
        "Sheep milk",
    )
    SHEEP_NATURAL_YOGURT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#sheep-natural-yogurt",
        "Sheep natural yogurt",
    )
    SHEEP_SWEET_YOGURT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#sheep-sweet-yogurt",
        "Sheep sweet yogurt",
    )
    SHEEP_YOGURT_ON_A_BED_OF_FRUIT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#sheep-yogurt-on-a-bed-of-fruit",
        "Sheep yogurt on a bed of fruit",
    )
    SHEEP_YOGURT_WITH_FRUITS = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#sheep-yogurt-with-fruits",
        "Sheep yogurt with fruits",
    )
    SHEEPFOOT_MUSHROOM = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#sheepfoot-mushroom",
        "Sheepfoot mushroom",
    )
    SHELLFISH = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#shellfish",
        "Shellfish",
    )
    SIMMERING_MEAT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#simmering-meat",
        "Simmering meat",
    )
    SMOOTH_CABBAGE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#smooth-cabbage",
        "Smooth cabbage",
    )
    SMOOTHIE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#smoothie",
        "Smoothie",
    )
    SNAILS = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#snails",
        "Snails",
    )
    SOFT_DRINK = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#soft-drink",
        "Soft drink",
    )
    SOUP = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#soup",
        "Soup",
    )
    SPINACH = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#spinach",
        "Spinach",
    )
    SQUASH = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#squash",
        "Squash",
    )
    STRAWBERRY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#strawberry",
        "Strawberry",
    )
    SWEET_GROCERIES = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#sweet-groceries",
        "Sweet groceries",
    )
    SWEET_YOGURT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#sweet-yogurt",
        "Sweet yogurt",
    )
    TARRAGON = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#tarragon",
        "Tarragon",
    )
    THYME = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#thyme",
        "Thyme",
    )
    TOMATO = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#tomato",
        "Tomato",
    )
    TRUFFLE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#truffle",
        "Truffle",
    )
    TURKEY = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#turkey",
        "Turkey",
    )
    TURNIP = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#turnip",
        "Turnip",
    )
    UCHIKI_KURI_SQUASH = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#uchiki-kuri-squash",
        "Uchiki kuri squash",
    )
    VEAL = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#veal",
        "Veal",
    )
    VEGETABLE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#vegetable",
        "Vegetable",
    )
    VIENNOISERIE_ = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#viennoiserie-",
        "Viennoiserie ",
    )
    WALNUT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#walnut",
        "Walnut",
    )
    WINE = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#wine",
        "Wine",
    )
    YAM = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#yam",
        "Yam",
    )
    YOGURT_ON_A_BED_OF_FRUIT = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#yogurt-on-a-bed-of-fruit",
        "Yogurt on a bed of fruit",
    )
    YOGURT_WITH_FRUITS = (
        "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/productTypes.rdf#yogurt-with-fruits",
        "Yogurt with fruits",
    )
