from PIL import Image

im_d = Image.open('INPUT_FILES/DESIGN_REFERENCES/desktop_1440.png')
crop_d = im_d.crop((420, 90, 850, 180))
crop_d.save('deliverables/evidence/desktop_header_crop.png')

im_m = Image.open('INPUT_FILES/DESIGN_REFERENCES/mobile_375.png')
crop_m = im_m.crop((20, 20, 350, 90))
crop_m.save('deliverables/evidence/mobile_header_crop.png')

bm = Image.open('INPUT_FILES/IMAGE_ASSETS/brand_mark.png')
print('brand_mark size:', bm.size)
print('Desktop header crop size:', crop_d.size)
print('Mobile header crop size:', crop_m.size)
