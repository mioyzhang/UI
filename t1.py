import os
import faker
import random


faker = faker.Faker()


print(random.randint(0, 10000))
print(random.randint(0, 3))
print(f'text: {faker.text()}')

img_path = '/home/dell/workspace/UI/resource/icon'
imgs = os.listdir(img_path)

random_img = random.sample(imgs, random.randint(1, len(imgs)))
print(random_img)
