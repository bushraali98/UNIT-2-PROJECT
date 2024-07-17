from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home_view(request: HttpRequest):
  images = [
    {
      "url": "images/abha.png",
      "title": "Abha",
      "alt": "Image of Abha city",
      "link": "city/abha"
    },
    {
      "url": "images/riyadh.png",
      "title": "Riyadh",
      "alt": "Image of Riyadh city",
      "link": "city/riyadh"
    },
    {
      "url": "images/mekkah.png",
      "title": "Mekkah",
      "alt": "Image of Mekkah city",
      "link": "city/mekkah"
    },
    {
      "url": "images/alula.png",
      "title": "AlUla",
      "alt": "Image of AlUla city",
      "link": "city/alula"
    },
  ]
  context = {
    "images": images
  }
  return render(request, "main/index.html", context)

def destination_view(request: HttpRequest):
   return render(request, "main/destination.html")

def about_view(request: HttpRequest):
   return render(request, "main/about.html")

def guide_view(request: HttpRequest):
   return render(request, "main/guide.html")

def city_view(request: HttpRequest, city_name: str):
    city_data = {
        "abha": {
          "title": "Abha - The City of Fog",
          "top_attractions": [
            {"name": "Asir National Park", "image": "images/abha1.png"},
            {"name": "Jabal Sawda", "image": "images/abha2.png"},
            {"name": "Traditional Markets", "image": "images/abha3.png"},
          ],
          "brief": "Aseer, the cultural heart of Saudi, offers diverse attractions in Abha. Explore Shada Palace, Abha Dam Lake, and Abha Palace Theme Park. Hike Aseer National Park near Souda Mountain and visit Waterfall Park and Abu Kheyal Park. Enjoy Abha’s cable cars, the Aseer Regional Museum, Al Muftaha art village, and local tribal customs in Al Habala and Rijal Almaa.",
          "images": ["images/abha1.png", "images/abha2.png", "images/abha3.png"], 
        },
        "riyadh": {
          "title": "Riyadh - The Capital City",
          "top_attractions": [
            {"name": "Via Riyadh", "image": "images/riyadh1.png"},
            {"name": "Boulevard Riyadh City", "image": "images/riyadh2.png"},
            {"name": "Riyadh Park", "image": "images/riyadh3.png"},
          ],
          "brief": "Riyadh combines ancient history with modern dynamism, offering a glimpse into Arabia’s past and future. Explore the city's rich heritage through souqs, museums, and historical architecture, and experience its modern side with high-rises and a thriving art scene, highlighted by the Riyadh Art initiative that turns the city into an open-air gallery. Don't miss Riyadh Season, featuring themed zones like Boulevard City and the Riyadh Zoo, open year-round. For dining, try local delicacies at Najd Village restaurant. ",
          "images": ["images/riyadh1.png", "images/riyadh2.png", "images/riyadh3.png"], 
        },
        "mekkah": {
          "title": "Mekkah - The Holy City",
          "top_attractions": [
            {"name": "Makkah Museum", "image": "images/mekkah2.png"},
            {"name": "Al Masjed Al Haram", "image": "images/mekkah3.png"},
            {"name": "Hira Cultural District", "image": "images/mekkah4.png"},
          ],
          "brief": "Makkah, the birthplace of Prophet Muhammad and where the Quran was revealed, is a pivotal city in Islam. It hosts the annual Hajj pilgrimage, one of the five pillars of Islam, and welcomes millions for the Umrah pilgrimage year-round. Key sites include Al Masjid Al Haram, the largest mosque in the world, and the historic Masjid-e-Aisha. Beyond its spiritual significance, visitors can explore the Makkah Museum's pre-Islamic artifacts or shop and play at Makkah Mall.",
          "images": ["images/mekkah1.png", "images/mekkah2.png", "images/mekkah3.png"], 
        },
        "alula": {
          "title": "AlUla - The Ancient Oasis",
          "top_attractions": [
            {"name": "AlUla Old Town Village", "image": "images/alula1.png"},
            {"name": "Elephant Rock", "image": "images/alula2.png"},
            {"name": "Tama at Our Habitas", "image": "images/alula3.png"},
          ],
          "brief": "Explore AlUla, Saudi Arabia's first UNESCO World Heritage Site, nestled in the northwest desert. Marvel at ancient tombs from 7,000 years of civilization and stunning rock formations like the 52-meter Elephant Rock. Enjoy the lush AlUla Oasis, adventure sports, and innovative art installations. Each September, experience the Azimuth AlUla festival of art and music set in breathtaking landscapes. Stay in luxury at Banyan Tree AlUla's tented villas or the desert resort, Habitas AlUla.",
          "images": ["images/alula1.png", "images/alula2.png", "images/alula3.png"], 
        },     
    }
    context = city_data[city_name]
    return render(request, 'main/city_detail.html', context)
