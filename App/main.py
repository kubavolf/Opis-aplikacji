from window import Window
import sys
from PyQt6.QtWidgets import QApplication
from Chord import Akord

app = QApplication(sys.argv)

window = Window()


akord_c = Akord(variant="C_chords")
akord_d = Akord(variant="D_chords")
akord_e = Akord(variant="E_chords")
akord_f = Akord(variant="F_chords")
akord_g = Akord(variant="G_chords")
akord_a = Akord(variant="A_chords")
akord_b = Akord(variant="B_chords")


window.create_main_button(name=akord_c.variant, x_cor=60, y_cor=300, wg=150, hg=50)
window.create_main_button(name=akord_d.variant, x_cor=240, y_cor=300, wg=150, hg=50)
window.create_main_button(name=akord_e.variant, x_cor=420, y_cor=300, wg=150, hg=50)
window.create_main_button(name=akord_f.variant, x_cor=600, y_cor=300, wg=150, hg=50)
window.create_main_button(name=akord_g.variant, x_cor=150, y_cor=400, wg=150, hg=50)
window.create_main_button(name=akord_a.variant, x_cor=330, y_cor=400, wg=150, hg=50)
window.create_main_button(name=akord_b.variant, x_cor=510, y_cor=400, wg=150, hg=50)
window.create_logo()

window.new_window_c.create_sound_button(image="border-image:url(C-7.png)", x_cor=60, y_cor=100, wg=285, hg=197)
window.new_window_c.create_sound_button(image="border-image:url(C-dur.png)", x_cor=440, y_cor=100, wg=285, hg=197)
window.new_window_c.create_sound_button(image="border-image:url(C-mol.png)", x_cor=250, y_cor=350, wg=285, hg=197)

window.new_window_d.create_sound_button(image="border-image:url(D-7.png)", x_cor=60, y_cor=100, wg=285, hg=197)
window.new_window_d.create_sound_button(image="border-image:url(D-dur.png)", x_cor=440, y_cor=100, wg=285, hg=197)
window.new_window_d.create_sound_button(image="border-image:url(D-mol)", x_cor=250, y_cor=350, wg=285, hg=197)

window.new_window_e.create_sound_button(image="border-image:url(E-7.png)", x_cor=60, y_cor=100, wg=285, hg=197)
window.new_window_e.create_sound_button(image="border-image:url(E-dur.png)", x_cor=440, y_cor=100, wg=285, hg=197)
window.new_window_e.create_sound_button(image="border-image:url(E-mol.png)", x_cor=250, y_cor=350, wg=285, hg=197)

window.new_window_f.create_sound_button(image="border-image:url(F-7.png)", x_cor=60, y_cor=100, wg=285, hg=197)
window.new_window_f.create_sound_button(image="border-image:url(F-dur.png)", x_cor=440, y_cor=100, wg=285, hg=197)
window.new_window_f.create_sound_button(image="border-image:url(F-mol.png)", x_cor=250, y_cor=350, wg=285, hg=197)

window.new_window_g.create_sound_button(image="border-image:url(G-7.png)", x_cor=60, y_cor=100, wg=285, hg=197)
window.new_window_g.create_sound_button(image="border-image:url(G-dur-G5.png)", x_cor=440, y_cor=100, wg=285, hg=197)
window.new_window_g.create_sound_button(image="border-image:url(G-mol.png)", x_cor=250, y_cor=350, wg=285, hg=197)

window.new_window_a.create_sound_button(image="border-image:url(A-7.png)", x_cor=60, y_cor=100, wg=285, hg=197)
window.new_window_a.create_sound_button(image="border-image:url(A-dur.png)", x_cor=440, y_cor=100, wg=285, hg=197)
window.new_window_a.create_sound_button(image="border-image:url(A-mol.png)", x_cor=250, y_cor=350, wg=285, hg=197)

window.new_window_b.create_sound_button(image="border-image:url(B-7.png)", x_cor=60, y_cor=100, wg=285, hg=197)
window.new_window_b.create_sound_button(image="border-image:url(B-dur.png)", x_cor=440, y_cor=100, wg=285, hg=197)
window.new_window_b.create_sound_button(image="border-image:url(B-mol.png)", x_cor=250, y_cor=350, wg=285, hg=197)





window.show()

sys.exit(app.exec())