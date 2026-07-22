from django.db import models


DFC_B_URL = "https://raw.githubusercontent.com/datafoodconsortium/ontology/refs/heads/master/src/DFC_BusinessOntology.owl"
DFC_PT_URL = "http://w3id.org/dfc/taxonomies/productTypes.rdf"


class ShippingOptionType(models.TextChoices):
    PICKUP = (f"{DFC_B_URL}#PickupOption", "Pick-up")
    DELIVERY = (f"{DFC_B_URL}#DeliveryOption", "Delivery")


class ResourceImportSource(models.TextChoices):
    ADMIN_SITE = ("admin_site", "Admin site")
    COMMAND_LINE = ("command_line", "Command line")
    UPDATE_WEBHOOK = ("update_webhook", "Update webhook event")
    REFRESH_WEBHOOK = ("refresh_webhook", "Refresh webhook event")


class WebhookEventSource(models.TextChoices):
    ADMIN_SITE = ("admin_site", "Admin site")
    DATASERVER = ("dataserver", "Received from dataserver")


class ProductType(models.TextChoices):
    ALCOHOLIC_BEVERAGE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#alcoholic-beverage",
        "Alcoholic beverage",
    )
    ALCOHOLICBEVERAGE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#alcoholicbeverage",
        "Alcoholicbeverage",
    )
    ALMOND = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#almond", "Almond")
    APERITIF = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#aperitif", "Aperitif")
    APPLES = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#apples", "Apples")
    APRICOT = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#apricot", "Apricot")
    ARTICHOKE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#artichoke",
        "Artichoke",
    )
    ASPARAGUS = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#asparagus",
        "Asparagus",
    )
    BAKERY = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#bakery", "Bakery")
    BASIL = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#basil", "Basil")
    BEAN = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#bean", "Bean")
    BEANS = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#beans", "Beans")
    BEEF = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#beef", "Beef")
    BEER = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#beer", "Beer")
    BEETROOT = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#beetroot", "Beetroot")
    BERRY = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#berry", "Berry")
    BISCUIT = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#biscuit", "Biscuit")
    BLACKBERRY = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#blackberry",
        "Blackberry",
    )
    BLACKCURRANT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#blackcurrant",
        "Blackcurrant",
    )
    BLUEBERRY = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#blueberry",
        "Blueberry",
    )
    BLUEFOOT_MUSHROOM = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#bluefoot-mushroom",
        "Bluefoot mushroom",
    )
    BLUEFOOTMUSHROOM = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#bluefootmushroom",
        "Bluefootmushroom",
    )
    BOTTLED_FRUIT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#bottled-fruit",
        "Bottled fruit",
    )
    BOTTLED_VEGETABLE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#bottled-vegetable",
        "Bottled vegetable",
    )
    BOTTLEDFRUIT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#bottledfruit",
        "Bottledfruit",
    )
    BOTTLEDVEGETABLE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#bottledvegetable",
        "Bottledvegetable",
    )
    BREAD = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#bread", "Bread")
    BROCCOLI_CABBAGE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#broccoli-cabbage",
        "Broccoli cabbage",
    )
    BROCCOLICABBAGE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#broccolicabbage",
        "Broccolicabbage",
    )
    BRUSSELS_SPROUTS = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#brussels-sprouts",
        "Brussels sprouts",
    )
    BRUSSELSSPROUTS = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#brusselssprouts",
        "Brusselssprouts",
    )
    BUTTER = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#butter", "Butter")
    BUTTERNUT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#butternut",
        "Butternut",
    )
    CABBAGE = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#cabbage", "Cabbage")
    CANNED_FRUIT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#canned-fruit",
        "Canned fruit",
    )
    CANNED_VEGETABLE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#canned-vegetable",
        "Canned vegetable",
    )
    CANNEDFRUIT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#cannedfruit",
        "Cannedfruit",
    )
    CANNEDGOODS = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#cannedgoods",
        "Cannedgoods",
    )
    CANNEDVEGETABLE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#cannedvegetable",
        "Cannedvegetable",
    )
    CARROT = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#carrot", "Carrot")
    CAULIFLOWER = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#cauliflower",
        "Cauliflower",
    )
    CELERIAC = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#celeriac", "Celeriac")
    CELERY_BRANCH = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#celery-branch",
        "Celery branch",
    )
    CELERYBRANCH = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#celerybranch",
        "Celerybranch",
    )
    CHANTERELLE_MUSHROOM = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#chanterelle-mushroom",
        "Chanterelle mushroom",
    )
    CHANTERELLEMUSHROOM = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#chanterellemushroom",
        "Chanterellemushroom",
    )
    CHARD = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#chard", "Chard")
    CHERRY = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#cherry", "Cherry")
    CHERRY_TOMATO = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#cherry-tomato",
        "Cherry tomato",
    )
    CHERRYTOMATO = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#cherrytomato",
        "Cherrytomato",
    )
    CHERVIL = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#chervil", "Chervil")
    CHESTNUT = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#chestnut", "Chestnut")
    CHICKEN = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#chicken", "Chicken")
    CHICORY = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#chicory", "Chicory")
    CHILLI_PEPPER = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#chilli-pepper",
        "Chilli pepper",
    )
    CHILLIPEPPER = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#chillipepper",
        "Chillipepper",
    )
    CHINESE_CABBAGE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#chinese-cabbage",
        "Chinese cabbage",
    )
    CHINESECABBAGE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#chinesecabbage",
        "Chinesecabbage",
    )
    CHIVE = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#chive", "Chive")
    CIDER = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#cider", "Cider")
    CLEMENTINE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#clementine",
        "Clementine",
    )
    CLUSTER_TOMATO = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#cluster-tomato",
        "Cluster tomato",
    )
    CLUSTERTOMATO = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#clustertomato",
        "Clustertomato",
    )
    CONFECTIONERY = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#confectionery",
        "Confectionery",
    )
    COOKED_MEAT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#cooked-meat",
        "Cooked meat",
    )
    COOKEDMEAT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#cookedmeat",
        "Cookedmeat",
    )
    CORIANDER = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#coriander",
        "Coriander",
    )
    CORN_SALAD = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#corn-salad",
        "Corn salad",
    )
    CORNSALAD = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#cornsalad",
        "Cornsalad",
    )
    COSMETIC = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#cosmetic", "Cosmetic")
    COULEMELLE_MUSHROOM = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#coulemelle-mushroom",
        "Coulemelle mushroom",
    )
    COULEMELLEMUSHROOM = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#coulemellemushroom",
        "Coulemellemushroom",
    )
    COURGETTE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#courgette",
        "Courgette",
    )
    COW_DAIRY_PRODUCT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#cow-dairy-product",
        "Cow dairy product",
    )
    COWDAIRYPRODUCT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#cowdairyproduct",
        "Cowdairyproduct",
    )
    CREAM_CHEESE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#cream-cheese",
        "Cream cheese",
    )
    CREAMCHEESE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#creamcheese",
        "Creamcheese",
    )
    CREPE_AND_GALETTE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#crepe-and-galette",
        "Crepe and galette",
    )
    CREPEANDGALETTE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#crepeandgalette",
        "Crepeandgalette",
    )
    CRESS = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#cress", "Cress")
    CUCUMBER = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#cucumber", "Cucumber")
    CURRANT = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#currant", "Currant")
    DAIRY_DESSERT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#dairy-dessert",
        "Dairy dessert",
    )
    DAIRY_PRODUCT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#dairy-product",
        "Dairy product",
    )
    DAIRYDESSERT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#dairydessert",
        "Dairydessert",
    )
    DAIRYPRODUCT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#dairyproduct",
        "Dairyproduct",
    )
    DANDELION = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#dandelion",
        "Dandelion",
    )
    DEATHS_TRUMPET = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#deaths-trumpet",
        "Deaths trumpet",
    )
    DEATHSTRUMPET = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#deathstrumpet",
        "Deathstrumpet",
    )
    DELICATESSEN = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#delicatessen",
        "Delicatessen",
    )
    DIGESTIVE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#digestive",
        "Digestive",
    )
    DILL = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#dill", "Dill")
    DRIED_FRUIT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#dried-fruit",
        "Dried fruit",
    )
    DRIED_VEGETABLE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#dried-vegetable",
        "Dried vegetable",
    )
    DRIED_GOODS = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#dried_goods",
        "Dried_goods",
    )
    DRIED_HERB = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#dried_herb",
        "Dried_herb",
    )
    DRIEDFRUIT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#driedfruit",
        "Driedfruit",
    )
    DRIEDGOODS = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#driedgoods",
        "Driedgoods",
    )
    DRIEDHERB = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#driedherb",
        "Driedherb",
    )
    DRIEDVEGETABLE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#driedvegetable",
        "Driedvegetable",
    )
    DRINK = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#drink", "Drink")
    DUCK = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#duck", "Duck")
    EGG = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#egg", "Egg")
    EGGPLANT = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#eggplant", "Eggplant")
    ENDIVE = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#endive", "Endive")
    FENNEL = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#fennel", "Fennel")
    FERMENT = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#ferment", "Ferment")
    FESTIVE_POULTRY = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#festive-poultry",
        "Festive poultry",
    )
    FESTIVEPOULTRY = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#festivepoultry",
        "Festivepoultry",
    )
    FIFTH_RANGE_VEGETABLE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#fifth-range-vegetable",
        "Fifth range vegetable",
    )
    FIFTHRANGEVEGETABLE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#fifthrangevegetable",
        "Fifthrangevegetable",
    )
    FIG = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#fig", "Fig")
    FISH = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#fish", "Fish")
    FISHERY_PRODUCT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#fishery-product",
        "Fishery product",
    )
    FISHERYPRODUCT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#fisheryproduct",
        "Fisheryproduct",
    )
    FLAKE = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#flake", "Flake")
    FLAVORED_YOGURT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#flavored-yogurt",
        "Flavored yogurt",
    )
    FLAVOREDYOGURT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#flavoredyogurt",
        "Flavoredyogurt",
    )
    FLOUR = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#flour", "Flour")
    FLOWER = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#flower", "Flower")
    FOURTH_RANGE_VEGETABLE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#fourth-range-vegetable",
        "Fourth range vegetable",
    )
    FOURTHRANGEVEGETABLE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#fourthrangevegetable",
        "Fourthrangevegetable",
    )
    FRESH_CHEESE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#fresh-cheese",
        "Fresh cheese",
    )
    FRESH_CREAM = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#fresh-cream",
        "Fresh cream",
    )
    FRESH_MEAT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#fresh-meat",
        "Fresh meat",
    )
    FRESHCHEESE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#freshcheese",
        "Freshcheese",
    )
    FRESHCREAM = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#freshcream",
        "Freshcream",
    )
    FRESHMEAT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#freshmeat",
        "Freshmeat",
    )
    FROZEN = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#frozen", "Frozen")
    FROZEN_FRUIT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#frozen-fruit",
        "Frozen fruit",
    )
    FROZEN_MEAL = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#frozen-meal",
        "Frozen meal",
    )
    FROZEN_MEAT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#frozen-meat",
        "Frozen meat",
    )
    FROZEN_VEGETABLE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#frozen-vegetable",
        "Frozen vegetable",
    )
    FROZENFRUIT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#frozenfruit",
        "Frozenfruit",
    )
    FROZENMEAL = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#frozenmeal",
        "Frozenmeal",
    )
    FROZENMEAT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#frozenmeat",
        "Frozenmeat",
    )
    FROZENVEGETABLE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#frozenvegetable",
        "Frozenvegetable",
    )
    FRUIT = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#fruit", "Fruit")
    FRUIT_IN_COMPOTE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#fruit-in-compote",
        "Fruit in compote",
    )
    FRUIT_JUICE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#fruit-juice",
        "Fruit juice",
    )
    FRUITINCOMPOTE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#fruitincompote",
        "Fruitincompote",
    )
    FRUITJUICE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#fruitjuice",
        "Fruitjuice",
    )
    GARLIC = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#garlic", "Garlic")
    GIROLLE_MUSHROOM = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#girolle-mushroom",
        "Girolle mushroom",
    )
    GIROLLEMUSHROOM = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#girollemushroom",
        "Girollemushroom",
    )
    GOAT_DAIRY_DESSERT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#goat-dairy-dessert",
        "Goat dairy dessert",
    )
    GOAT_DAIRY_PRODUCT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#goat-dairy-product",
        "Goat dairy product",
    )
    GOAT_FLAVORED_YOGURT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#goat-flavored-yogurt",
        "Goat flavored yogurt",
    )
    GOAT_FRESH_CHEESE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#goat-fresh-cheese",
        "Goat fresh cheese",
    )
    GOAT_MATURE_CHEESE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#goat-mature-cheese",
        "Goat mature cheese",
    )
    GOAT_MILK = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#goat-milk",
        "Goat milk",
    )
    GOAT_NATURAL_YOGURT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#goat-natural-yogurt",
        "Goat natural yogurt",
    )
    GOAT_SWEET_YOGURT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#goat-sweet-yogurt",
        "Goat sweet yogurt",
    )
    GOAT_YOGURT_ON_A_BED_OF_FRUIT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#goat-yogurt-on-a-bed-of-fruit",
        "Goat yogurt on a bed of fruit",
    )
    GOAT_YOGURT_WITH_FRUITS = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#goat-yogurt-with-fruits",
        "Goat yogurt with fruits",
    )
    GOATDAIRYDESSERT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#goatdairydessert",
        "Goatdairydessert",
    )
    GOATDAIRYPRODUCT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#goatdairyproduct",
        "Goatdairyproduct",
    )
    GOATFLAVOREDYOGURT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#goatflavoredyogurt",
        "Goatflavoredyogurt",
    )
    GOATFRESHCHEESE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#goatfreshcheese",
        "Goatfreshcheese",
    )
    GOATMATURECHEESE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#goatmaturecheese",
        "Goatmaturecheese",
    )
    GOATMILK = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#goatmilk", "Goatmilk")
    GOATNATURALYOGURT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#goatnaturalyogurt",
        "Goatnaturalyogurt",
    )
    GOATSWEETYOGURT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#goatsweetyogurt",
        "Goatsweetyogurt",
    )
    GOATYOGURTONABEDOFFRUIT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#goatyogurtonabedoffruit",
        "Goatyogurtonabedoffruit",
    )
    GOATYOGURTWITHFRUITS = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#goatyogurtwithfruits",
        "Goatyogurtwithfruits",
    )
    GOOSE = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#goose", "Goose")
    GOOSEBERRY = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#gooseberry",
        "Gooseberry",
    )
    GRAIN = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#grain", "Grain")
    GRAPE = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#grape", "Grape")
    GREEN_GARLIC = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#green-garlic",
        "Green garlic",
    )
    GREENGARLIC = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#greengarlic",
        "Greengarlic",
    )
    GRILLING_MEAT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#grilling-meat",
        "Grilling meat",
    )
    GRILLINGMEAT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#grillingmeat",
        "Grillingmeat",
    )
    GUINEA_FOWL = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#guinea-fowl",
        "Guinea fowl",
    )
    GUINEAFOWL = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#guineafowl",
        "Guineafowl",
    )
    HAZELNUT = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#hazelnut", "Hazelnut")
    HERB = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#herb", "Herb")
    HIERLOOM_SQUASH = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#hierloom-squash",
        "Hierloom squash",
    )
    HIERLOOM_TOMATO = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#hierloom-tomato",
        "Hierloom tomato",
    )
    HIERLOOMSQUASH = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#hierloomsquash",
        "Hierloomsquash",
    )
    HIERLOOMTOMATO = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#hierloomtomato",
        "Hierloomtomato",
    )
    HONEY = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#honey", "Honey")
    INEDIBLE = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#inedible", "Inedible")
    JAM = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#jam", "Jam")
    JERUSALEM_ARTICHOKE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#jerusalem-artichoke",
        "Jerusalem artichoke",
    )
    JERUSALEMARTICHOKE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#jerusalemartichoke",
        "Jerusalemartichoke",
    )
    KALE = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#kale", "Kale")
    KALE_CABBAGE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#kale-cabbage",
        "Kale cabbage",
    )
    KALECABBAGE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#kalecabbage",
        "Kalecabbage",
    )
    KIWI = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#kiwi", "Kiwi")
    KOHLRABI = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#kohlrabi", "Kohlrabi")
    LAMB = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#lamb", "Lamb")
    LAUREL = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#laurel", "Laurel")
    LEEK = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#leek", "Leek")
    LEMON = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#lemon", "Lemon")
    LEMONADE = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#lemonade", "Lemonade")
    LENTILS = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#lentils", "Lentils")
    LETTUCE = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#lettuce", "Lettuce")
    LOCAL_GROCERY_STORE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#local-grocery-store",
        "Local grocery store",
    )
    LOCALGROCERYSTORE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#localgrocerystore",
        "Localgrocerystore",
    )
    MANDARIN = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#mandarin", "Mandarin")
    MATURE_CHEESE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#mature-cheese",
        "Mature cheese",
    )
    MATURECHEESE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#maturecheese",
        "Maturecheese",
    )
    MEAT_PRODUCT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#meat-product",
        "Meat product",
    )
    MEATPRODUCT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#meatproduct",
        "Meatproduct",
    )
    MEDLAR = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#medlar", "Medlar")
    MELON = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#melon", "Melon")
    MESCLUN = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#mesclun", "Mesclun")
    MILK = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#milk", "Milk")
    MILKY_MUSHROOM = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#milky-mushroom",
        "Milky mushroom",
    )
    MILKYMUSHROOM = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#milkymushroom",
        "Milkymushroom",
    )
    MINT = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#mint", "Mint")
    MOREL = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#morel", "Morel")
    MOUSSERON = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#mousseron",
        "Mousseron",
    )
    MUSHROOM = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#mushroom", "Mushroom")
    NATURAL_YOGURT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#natural-yogurt",
        "Natural yogurt",
    )
    NATURALYOGURT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#naturalyogurt",
        "Naturalyogurt",
    )
    NECTARINE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#nectarine",
        "Nectarine",
    )
    NON_LOCAL_FRUIT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#non-local-fruit",
        "Non local fruit",
    )
    NON_LOCAL_VEGETABLE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#non-local-vegetable",
        "Non local vegetable",
    )
    NONLOCALFRUIT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#nonlocalfruit",
        "Nonlocalfruit",
    )
    NONLOCALVEGETABLE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#nonlocalvegetable",
        "Nonlocalvegetable",
    )
    NUT = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#nut", "Nut")
    OIL = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#oil", "Oil")
    ONION = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#onion", "Onion")
    ORANGE = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#orange", "Orange")
    OTHER_CHEESE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#other-cheese",
        "Other cheese",
    )
    OTHER_DAIRY_PRODUCT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#other-dairy-product",
        "Other dairy product",
    )
    OTHER_MILK = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#other-milk",
        "Other milk",
    )
    OTHERCHEESE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#othercheese",
        "Othercheese",
    )
    OTHERDAIRYPRODUCT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#otherdairyproduct",
        "Otherdairyproduct",
    )
    OTHERMILK = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#othermilk",
        "Othermilk",
    )
    OYSTER_MUSHROOM = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#oyster-mushroom",
        "Oyster mushroom",
    )
    OYSTERMUSHROOM = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#oystermushroom",
        "Oystermushroom",
    )
    PARIS_MUSHROOM = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#paris-mushroom",
        "Paris mushroom",
    )
    PARISMUSHROOM = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#parismushroom",
        "Parismushroom",
    )
    PARSLEY = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#parsley", "Parsley")
    PARSNIP = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#parsnip", "Parsnip")
    PASTA = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#pasta", "Pasta")
    PASTRY = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#pastry", "Pastry")
    PATTYPAN_SQUASH = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#pattypan-squash",
        "Pattypan squash",
    )
    PATTYPANSQUASH = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#pattypansquash",
        "Pattypansquash",
    )
    PEACH = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#peach", "Peach")
    PEAR = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#pear", "Pear")
    PEAS = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#peas", "Peas")
    PEPPER = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#pepper", "Pepper")
    PIE_PASTRY = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#pie-pastry",
        "Pie pastry",
    )
    PIEPASTRY = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#piepastry",
        "Piepastry",
    )
    PIGEON = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#pigeon", "Pigeon")
    PLANT = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#plant", "Plant")
    PLUM = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#plum", "Plum")
    PORCINI = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#porcini", "Porcini")
    PORK = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#pork", "Pork")
    POTATO = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#potato", "Potato")
    POULTRY = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#poultry", "Poultry")
    PROCESSED_FRUIT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#processed-fruit",
        "Processed fruit",
    )
    PROCESSED_VEGETABLE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#processed-vegetable",
        "Processed vegetable",
    )
    PROCESSEDFRUIT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#processedfruit",
        "Processedfruit",
    )
    PROCESSEDVEGETABLE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#processedvegetable",
        "Processedvegetable",
    )
    PRUNE = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#prune", "Prune")
    PULSE = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#pulse", "Pulse")
    PUMPKIN = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#pumpkin", "Pumpkin")
    PURSLANE = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#purslane", "Purslane")
    QUAIL = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#quail", "Quail")
    QUINCE = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#quince", "Quince")
    QUINOA = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#quinoa", "Quinoa")
    RABBIT = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#rabbit", "Rabbit")
    RADISH = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#radish", "Radish")
    RASPBERRY = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#raspberry",
        "Raspberry",
    )
    READY_MEAL = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#ready-meal",
        "Ready meal",
    )
    READYMEAL = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#readymeal",
        "Readymeal",
    )
    RED_CABBAGE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#red-cabbage",
        "Red cabbage",
    )
    REDCABBAGE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#redcabbage",
        "Redcabbage",
    )
    RHUBARB = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#rhubarb", "Rhubarb")
    RICE = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#rice", "Rice")
    ROCKET = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#rocket", "Rocket")
    ROMANESCO = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#romanesco",
        "Romanesco",
    )
    ROSEMARY = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#rosemary", "Rosemary")
    ROUND_TOMATO = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#round-tomato",
        "Round tomato",
    )
    ROUNDTOMATO = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#roundtomato",
        "Roundtomato",
    )
    RUTABAGA = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#rutabaga", "Rutabaga")
    SAGE = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#sage", "Sage")
    SALAD = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#salad", "Salad")
    SALAD_MIX = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#salad-mix",
        "Salad mix",
    )
    SALADMIX = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#saladmix", "Saladmix")
    SALSIFY = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#salsify", "Salsify")
    SALT = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#salt", "Salt")
    SALTING = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#salting", "Salting")
    SAVORY_GROCERIES = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#savory-groceries",
        "Savory groceries",
    )
    SAVORYGROCERIES = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#savorygroceries",
        "Savorygroceries",
    )
    SAVOY_CABBAGE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#savoy-cabbage",
        "Savoy cabbage",
    )
    SAVOYCABBAGE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#savoycabbage",
        "Savoycabbage",
    )
    SEASHELL = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#seashell", "Seashell")
    SEED = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#seed", "Seed")
    SEMOLINA = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#semolina", "Semolina")
    SHALLOT = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#shallot", "Shallot")
    SHEEP_DAIRY_DESSERT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#sheep-dairy-dessert",
        "Sheep dairy dessert",
    )
    SHEEP_DAIRY_PRODUCT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#sheep-dairy-product",
        "Sheep dairy product",
    )
    SHEEP_FLAVORED_YOGURT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#sheep-flavored-yogurt",
        "Sheep flavored yogurt",
    )
    SHEEP_FRESH_CHEESE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#sheep-fresh-cheese",
        "Sheep fresh cheese",
    )
    SHEEP_MATURE_CHEESE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#sheep-mature-cheese",
        "Sheep mature cheese",
    )
    SHEEP_MILK = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#sheep-milk",
        "Sheep milk",
    )
    SHEEP_NATURAL_YOGURT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#sheep-natural-yogurt",
        "Sheep natural yogurt",
    )
    SHEEP_SWEET_YOGURT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#sheep-sweet-yogurt",
        "Sheep sweet yogurt",
    )
    SHEEP_YOGURT_ON_A_BED_OF_FRUIT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#sheep-yogurt-on-a-bed-of-fruit",
        "Sheep yogurt on a bed of fruit",
    )
    SHEEP_YOGURT_WITH_FRUITS = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#sheep-yogurt-with-fruits",
        "Sheep yogurt with fruits",
    )
    SHEEPDAIRYDESSERT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#sheepdairydessert",
        "Sheepdairydessert",
    )
    SHEEPDAIRYPRODUCT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#sheepdairyproduct",
        "Sheepdairyproduct",
    )
    SHEEPFLAVOREDYOGURT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#sheepflavoredyogurt",
        "Sheepflavoredyogurt",
    )
    SHEEPFOOT_MUSHROOM = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#sheepfoot-mushroom",
        "Sheepfoot mushroom",
    )
    SHEEPFOOTMUSHROOM = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#sheepfootmushroom",
        "Sheepfootmushroom",
    )
    SHEEPFRESHCHEESE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#sheepfreshcheese",
        "Sheepfreshcheese",
    )
    SHEEPMATURECHEESE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#sheepmaturecheese",
        "Sheepmaturecheese",
    )
    SHEEPMILK = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#sheepmilk",
        "Sheepmilk",
    )
    SHEEPNATURALYOGURT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#sheepnaturalyogurt",
        "Sheepnaturalyogurt",
    )
    SHEEPSWEETYOGURT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#sheepsweetyogurt",
        "Sheepsweetyogurt",
    )
    SHEEPYOGURTONABEDOFFRUIT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#sheepyogurtonabedoffruit",
        "Sheepyogurtonabedoffruit",
    )
    SHEEPYOGURTWITHFRUITS = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#sheepyogurtwithfruits",
        "Sheepyogurtwithfruits",
    )
    SHELLFISH = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#shellfish",
        "Shellfish",
    )
    SIMMERING_MEAT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#simmering-meat",
        "Simmering meat",
    )
    SIMMERINGMEAT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#simmeringmeat",
        "Simmeringmeat",
    )
    SMOOTH_CABBAGE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#smooth-cabbage",
        "Smooth cabbage",
    )
    SMOOTHCABBAGE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#smoothcabbage",
        "Smoothcabbage",
    )
    SMOOTHIE = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#smoothie", "Smoothie")
    SNACK = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#snack", "Snack")
    SNAILS = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#snails", "Snails")
    SOFT_DRINK = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#soft-drink",
        "Soft drink",
    )
    SOFTDRINK = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#softdrink",
        "Softdrink",
    )
    SOUP = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#soup", "Soup")
    SPINACH = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#spinach", "Spinach")
    SQUASH = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#squash", "Squash")
    STRAWBERRY = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#strawberry",
        "Strawberry",
    )
    SWEET_GROCERIES = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#sweet-groceries",
        "Sweet groceries",
    )
    SWEET_YOGURT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#sweet-yogurt",
        "Sweet yogurt",
    )
    SWEETGROCERIES = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#sweetgroceries",
        "Sweetgroceries",
    )
    SWEETYOGURT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#sweetyogurt",
        "Sweetyogurt",
    )
    TARRAGON = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#tarragon", "Tarragon")
    THYME = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#thyme", "Thyme")
    TOMATO = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#tomato", "Tomato")
    TRUFFLE = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#truffle", "Truffle")
    TURKEY = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#turkey", "Turkey")
    TURNIP = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#turnip", "Turnip")
    UCHIKI_KURI_SQUASH = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#uchiki-kuri-squash",
        "Uchiki kuri squash",
    )
    UCHIKIKURISQUASH = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#uchikikurisquash",
        "Uchikikurisquash",
    )
    VEAL = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#veal", "Veal")
    VEGETABLE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#vegetable",
        "Vegetable",
    )
    VENISON = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#venison", "Venison")
    VIENNOISERIE = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#viennoiserie",
        "Viennoiserie",
    )
    VIENNOISERIE_ = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#viennoiserie-",
        "Viennoiserie ",
    )
    WALNUT = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#walnut", "Walnut")
    WINE = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#wine", "Wine")
    YAM = ("https://w3id.org/dfc/taxonomies/productTypes.rdf#yam", "Yam")
    YOGURT_ON_A_BED_OF_FRUIT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#yogurt-on-a-bed-of-fruit",
        "Yogurt on a bed of fruit",
    )
    YOGURT_WITH_FRUITS = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#yogurt-with-fruits",
        "Yogurt with fruits",
    )
    YOGURTONABEDOFFRUIT = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#yogurtonabedoffruit",
        "Yogurtonabedoffruit",
    )
    YOGURTWITHFRUITS = (
        "https://w3id.org/dfc/taxonomies/productTypes.rdf#yogurtwithfruits",
        "Yogurtwithfruits",
    )
