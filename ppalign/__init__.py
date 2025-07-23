"""
PPAlign initialization
"""

__author__ = "Vuong Quoc Phong(contact.quocphongvuong@gmail.com), Vic Luu(lvphuc186@gmail.com)"
__version__ = "1.0.0"


from ppalign.encoder import Encoder


model_name = "LaBSE"
model = Encoder(model_name)

from ppalign.aligner import Bertalign