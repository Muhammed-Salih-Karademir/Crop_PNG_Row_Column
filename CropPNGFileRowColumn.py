from PIL import Image

im = Image.open('/home/autonom/Desktop/crop/etiket1.png')

i=0;j=0;a=0
while j<15:
	while i<8:
		im_crop = im.crop((j*256, i*256, (j+1)*256, (i+1)*256))
		i=i+1
		a=a+1
		im_crop.save('/home/autonom/Desktop/crop/'+ str(a) + '.png', quality=95)
	i=0
	j=j+1

