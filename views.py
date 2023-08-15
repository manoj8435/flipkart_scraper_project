from rest_framework import generics, permissions
from .models import Product
from .serializers import ProductSerializer
import requests
from bs4 import BeautifulSoup

class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
        
# after changes views.

class ProductCreateView(generics.CreateAPIView):
    # ...

    def perform_create(self, serializer):
        url = self.request.data.get('url')
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.find('span', {'class': 'B_NuCI'}).text
        price = float(soup.find('div', {'class': '_30jeq3 _16Jk6d'}).text.replace('₹', '').replace(',', ''))
        description = soup.find('div', {'class': '_1NoI8_'}).text if soup.find('div', {'class': '_1NoI8_'}) else None
        num_reviews = int(soup.find('span', {'class': '_2_R_DZ'}).text.split()[0])
        ratings = float(soup.find('div', {'class': '_2d4LTz'}).text)
        media_count = len(soup.find_all('div', {'class': '_2MImiq'}))

        serializer.save(
            user=self.request.user,
            url=url,
            title=title,
            price=price,
            description=description,
            num_reviews=num_reviews,
            ratings=ratings,
            media_count=media_count,
        )


