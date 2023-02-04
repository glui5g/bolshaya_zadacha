import os
import sys

import pygame
import requests

api_server = "http://static-maps.yandex.ru/1.x/"
lon, lat = "39.568664", "52.628096"
z = 15
params = {
    "ll": ",".join([lon, lat]),
    "z": z,
    "l": "map"
}
response = requests.get(api_server, params=params)

if not response:
    print("Ошибка выполнения запроса:")
    print(response.url)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # screen.fill((0, 0, 0))
    # pygame.display.flip()
pygame.quit()

os.remove(map_file)