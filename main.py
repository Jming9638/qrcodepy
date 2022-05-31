import cv2
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import *
from qrcode.image.styles.colormasks import *

module_drawer = [SquareModuleDrawer(),
                 GappedSquareModuleDrawer(),
                 CircleModuleDrawer(),
                 RoundedModuleDrawer(),
                 VerticalBarsDrawer(),
                 HorizontalBarsDrawer()]

color_mask = [SolidFillColorMask(),
              RadialGradiantColorMask(),
              SquareGradiantColorMask(),
              HorizontalGradiantColorMask(),
              VerticalGradiantColorMask()]

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=2
)

qr.add_data('https://www.facebook.com/')
qr.make(fit=True)

img = qr.make_image(
    fill_color="black",
    back_color="white",
    image_factory=StyledPilImage,
    module_drawer=module_drawer[0],
    color_mask=color_mask[0]
)

img.save("sample.png")
im = cv2.imread("sample.png")
cv2.imshow("QRcode", im)
cv2.waitKey(0)
