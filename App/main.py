from window import Window
import sys
from PyQt6.QtWidgets import QApplication

from Chord import Chord
from Chord import Tuner

app = QApplication(sys.argv)

window = Window()


akord_c = Chord(variant="C_chords", x_cor=330, y_cor=200, wg=150, hg=50,
                image_7="border-image:url(Chords/C-7.png)", image_dur="border-image:url(Chords/C-dur.png)", image_mol="border-image:url(Chords/C-mol.png)",
                sound_7="Sounds/rocket.wav", sound_dur="Sounds/rocket.wav", sound_mol="Sounds/rocket.wav")

akord_d = Chord(variant="D_chords", x_cor=240, y_cor=300, wg=150, hg=50,
                image_7="border-image:url(Chords/D-7.png)", image_dur="border-image:url(Chords/D-dur.png)", image_mol="border-image:url(Chords/D-mol.png)",
                sound_7="Sounds/rocket.wav", sound_dur="Sounds/rocket.wav", sound_mol="Sounds/rocket.wav")

akord_e = Chord(variant="E_chords", x_cor=600, y_cor=300, wg=150, hg=50,
                image_7="border-image:url(Chords/E-7.png)", image_dur="border-image:url(Chords/E-dur.png)", image_mol="border-image:url(Chords/E-mol.png)",
                sound_7="Sounds/rocket.wav", sound_dur="Sounds/rocket.wav", sound_mol="Sounds/rocket.wav")

akord_f = Chord(variant="F_chords", x_cor=150, y_cor=400, wg=150, hg=50,
                image_7="border-image:url(Chords/F-7.png)", image_dur="border-image:url(Chords/F-dur.png)", image_mol="border-image:url(Chords/F-mol.png)",
                sound_7="Sounds/rocket.wav", sound_dur="Sounds/rocket.wav", sound_mol="Sounds/rocket.wav")

akord_g = Chord(variant="G_chords", x_cor=510, y_cor=400, wg=150, hg=50,
                image_7="border-image:url(Chords/G-7.png)", image_dur="border-image:url(Chords/G-dur.png)", image_mol="border-image:url(Chords/G-mol.png)",
                sound_7="Sounds/rocket.wav", sound_dur="Sounds/rocket.wav", sound_mol="Sounds/rocket.wav")

akord_a = Chord(variant="A_chords", x_cor=240, y_cor=500, wg=150, hg=50,
                image_7="border-image:url(Chords/A-7.png)", image_dur="border-image:url(Chords/A-dur.png)", image_mol="border-image:url(Chords/A-mol.png)",
                sound_7="Sounds/rocket.wav", sound_dur="Sounds/rocket.wav", sound_mol="Sounds/rocket.wav")

akord_b = Chord(variant="B_chords", x_cor=420, y_cor=500, wg=150, hg=50,
                image_7="border-image:url(Chords/B-7.png)", image_dur="border-image:url(Chords/B-dur.png)", image_mol="border-image:url(Chords/B-mol.png)",
                sound_7="Sounds/rocket.wav", sound_dur="Sounds/rocket.wav", sound_mol="Sounds/rocket.wav")

akord_cis = Chord(variant="Cis_chords", x_cor=60, y_cor=300, wg=150, hg=50,
                  image_7="border-image:url(Chords/Cis-7.png)", image_dur="border-image:url(Chords/Cis-dur.png)", image_mol="border-image:url(Chords/Cis-mol.png)",
                sound_7="Sounds/rocket.wav", sound_dur="Sounds/rocket.wav", sound_mol="Sounds/rocket.wav")

akord_dis = Chord(variant="Dis_chords", x_cor=420, y_cor=300, wg=150, hg=50,
                  image_7="border-image:url(Chords/Dis-7.png)", image_dur="border-image:url(Chords/Dis-dur.png)", image_mol="border-image:url(Chords/Dis-mol.png)",
                sound_7="Sounds/rocket.wav", sound_dur="Sounds/rocket.wav", sound_mol="Sounds/rocket.wav")

akord_fis = Chord(variant="Fis_chords", x_cor=330, y_cor=400, wg=150, hg=50,
                  image_7="border-image:url(Chords/Fis-7.png)", image_dur="border-image:url(Chords/Fis-dur.png)", image_mol="border-image:url(Chords/Fis-mol.png)",
                sound_7="Sounds/rocket.wav", sound_dur="Sounds/rocket.wav", sound_mol="Sounds/rocket.wav")

akord_gis = Chord(variant="Gis_chords", x_cor=60, y_cor=500, wg=150, hg=50,
                  image_7="border-image:url(Chords/Gis-7.png)", image_dur="border-image:url(Chords/Gis-dur.png)", image_mol="border-image:url(Chords/Gis-mol.png)",
                sound_7="Sounds/rocket.wav", sound_dur="Sounds/rocket.wav", sound_mol="Sounds/rocket.wav")

akord_h = Chord(variant="H_chords", x_cor=600, y_cor=500, wg=150, hg=50,
                image_7="border-image:url(Chords/H-7.png)", image_dur="border-image:url(Chords/H-dur.png)", image_mol="border-image:url(Chords/H-mol.png)",
                sound_7="Sounds/rocket.wav", sound_dur="Sounds/rocket.wav", sound_mol="Sounds/rocket.wav")





tuner = Tuner(variant="Tuner", x_cor=600, y_cor=100, wg=150, hg=150,
                image_e6="border-image:url(C-7.png)", image_a="border-image:url(C-dur.png)", image_d="border-image:url(C-mol.png)",
                image_g="border-image:url(C-mol.png)", image_b="border-image:url(C-mol.png)", image_e1="border-image:url(C-mol.png)",
                sound_e6="Sounds/E6.wav", sound_a="Sounds/A.wav", sound_d="Sounds/D.wav", sound_g="Sounds/G.wav",
                sound_b="Sounds/B.wav", sound_e1="Sounds/E1.wav")



akord_list = [akord_c, akord_d, akord_e, akord_f, akord_g, akord_a, akord_b, akord_cis, akord_dis, akord_fis, akord_gis, akord_h, tuner]

for akord in akord_list:
    akord.create_button(window)
    akord.create_new_window()



window.create_logo()



#if __name__ = "__main__":
window.show()

sys.exit(app.exec())
