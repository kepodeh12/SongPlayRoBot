import os
API_ID = int(os.getenv("7762794"))
API_HASH = os.getenv("4dd2b770cc78fa05f32060541d8324d9")
BOT_TOKEN = os.getenv("1913539839:AAGInE_3K8rWaenkm1sWWz97Tc1iN9uDowc")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("1845397962", "").split()})
