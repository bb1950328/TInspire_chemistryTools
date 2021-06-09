import math
import re

ORGANIC_NAMES = ["meth", "eth", "prop", "but", "pent", "hex", "hept", "oct", "non", "dec"]
GREEK_NUMBERS = ["mono", "di", "tri", "tetra", "penta", "hexa", "hepta", "octa", "nona", "deca", "undeca", "dodeca", "trideca"]
RELATIVE_ATOMMASSE = "Relative Atommasse"
PERIODE = "Periode"
GRUPPE = "Gruppe"
ZUSTAND = "Zustand"
TYP = "Typ"
ATOMRADIUS = "Atomradius"
ELEKTRONEGATIVITAET = "Elektronegativität"
DICHTE = "Dichte"
SCHMELZPUNKT_K = "Schmelzpunkt (K)"
SIEDEPUNKT_K = "Siedepunkt (K)"
ISOTOPE = "Isotope"
ELEKTRONENKONFIGURATION = "Elektronenkonfiguration"
VALENZELEKTRONEN = "Valenzelektronen"
IONENLADUNGEN = "Ionenladungen"
PERIODIC_TABLE_HEADS = ["Protonenzahl", "Name", "Symbol", RELATIVE_ATOMMASSE, PERIODE, GRUPPE, ZUSTAND, TYP, ATOMRADIUS, ELEKTRONEGATIVITAET, DICHTE, SCHMELZPUNKT_K, SIEDEPUNKT_K, ISOTOPE, ELEKTRONENKONFIGURATION, VALENZELEKTRONEN, IONENLADUNGEN]
PERIODIC_TABLE_DATA = [
    [1, 'Wasserstoff', 'H', 1.00794, 1, 1, 'gas', 'Nichtmetall', 0.79, 2.1, 8.988e-05, 14.175, 20.28, 3, '1s1', 1, [+1, -1]],
    [2, 'Helium', 'He', 4.002602, 1, 18, 'gas', 'Edelgas', 0.49, None, 0.0001785, None, 4.22, 5, '1s2', 2, []],
    [3, 'Lithium', 'Li', 6.941, 2, 1, 'solid', 'Alkalimetall', 2.1, 0.98, 0.534, 453.85, 1615, 5, '[He] 2s1', 1, [+1]],
    [4, 'Beryllium', 'Be', 9.012182, 2, 2, 'solid', 'Erdalkalimetall', 1.4, 1.57, 1.85, 1560.15, 2742, 6, '[He] 2s2', 2, [+2]],
    [5, 'Bor', 'B', 10.811, 2, 13, 'solid', 'Metalloid', 1.2, 2.04, 2.34, 2573.15, 4200, 6, '[He] 2s2 2p1', 3, []],
    [6, 'Kohlenstoff', 'C', 12.0107, 2, 14, 'solid', 'Nichtmetall', 0.91, 2.55, 2.267, 3948.15, 4300, 7, '[He] 2s2 2p2', 4, []],
    [7, 'Stickstoff', 'N', 14.0067, 2, 15, 'gas', 'Nichtmetall', 0.75, 3.04, 0.0012506, 63.29, 77.36, 8, '[He] 2s2 2p3', 5, [-3]],
    [8, 'Sauerstoff', 'O', 15.9994, 2, 16, 'gas', 'Nichtmetall', 0.65, 3.44, 0.001429, 50.5, 90.2, 8, '[He] 2s2 2p4', 6, [-2]],
    [9, 'Fluor', 'F', 18.9984032, 2, 17, 'gas', 'Halogen', 0.57, 3.98, 0.001696, 53.63, 85.03, 6, '[He] 2s2 2p5', 7, [-1]],
    [10, 'Neon', 'Ne', 20.1797, 2, 18, 'gas', 'Edelgas', 0.51, None, 0.0008999, 24.703, 27.07, 8, '[He] 2s2 2p6', 8, []],
    [11, 'Natrium', 'Na', 22.98976928, 3, 1, 'solid', 'Alkalimetall', 2.2, 0.93, 0.971, 371.15, 1156, 7, '[Ne] 3s1', 1, [+1]],
    [12, 'Magnesium', 'Mg', 24.305, 3, 2, 'solid', 'Erdalkalimetall', 1.7, 1.31, 1.738, 923.15, 1363, 8, '[Ne] 3s2', 2, [+2]],
    [13, 'Aluminum', 'Al', 26.9815386, 3, 13, 'solid', 'Metal', 1.8, 1.61, 2.698, 933.4, 2792, 8, '[Ne] 3s2 3p1', 3, [+3]],
    [14, 'Silicium', 'Si', 28.0855, 3, 14, 'solid', 'Metalloid', 1.5, 1.9, 2.3296, 1683.15, 3538, 8, '[Ne] 3s2 3p2', 4, []],
    [15, 'Phosphor', 'P', 30.973762, 3, 15, 'solid', 'Nichtmetall', 1.2, 2.19, 1.82, 317.25, 553, 7, '[Ne] 3s2 3p3', 5, [-3]],
    [16, 'Schwefel', 'S', 32.065, 3, 16, 'solid', 'Nichtmetall', 1.1, 2.58, 2.067, 388.51, 717.8, 10, '[Ne] 3s2 3p4', 6, [-2]],
    [17, 'Chlor', 'Cl', 35.453, 3, 17, 'gas', 'Halogen', 0.97, 3.16, 0.003214, 172.31, 239.11, 11, '[Ne] 3s2 3p5', 7, [-1]],
    [18, 'Argon', 'Ar', 39.948, 3, 18, 'gas', 'Edelgas', 0.88, None, 0.0017837, 83.96, 87.3, 8, '[Ne] 3s2 3p6', 8, []],
    [19, 'Kalium', 'K', 39.0983, 4, 1, 'solid', 'Alkalimetall', 2.8, 0.82, 0.862, 336.5, 1032, 10, '[Ar] 4s1', 1, [+1]],
    [20, 'Calcium', 'Ca', 40.078, 4, 2, 'solid', 'Erdalkalimetall', 2.2, 1, 1.54, 1112.15, 1757, 14, '[Ar] 4s2', 2, [+2]],
    [21, 'Scandium', 'Sc', 44.955912, 4, 3, 'solid', 'Übergangsmetall', 2.1, 1.36, 2.989, 1812.15, 3109, 15, '[Ar] 3d1 4s2', 2, [+3]],
    [22, 'Titan', 'Ti', 47.867, 4, 4, 'solid', 'Übergangsmetall', 2, 1.54, 4.54, 1933.15, 3560, 9, '[Ar] 3d2 4s2', 2, [+3, +4]],
    [23, 'Vanadium', 'V', 50.9415, 4, 5, 'solid', 'Übergangsmetall', 1.9, 1.63, 6.11, 2175.15, 3680, 9, '[Ar] 3d3 4s2', 2, [+3]],
    [24, 'Chrom', 'Cr', 51.9961, 4, 6, 'solid', 'Übergangsmetall', 1.9, 1.66, 7.15, 2130.15, 2944, 9, '[Ar] 3d5 4s1', 1, [+3]],
    [25, 'Mangan', 'Mn', 54.938045, 4, 7, 'solid', 'Übergangsmetall', 1.8, 1.55, 7.44, 1519.15, 2334, 11, '[Ar] 3d5 4s2', 2, [+2]],
    [26, 'Eisen', 'Fe', 55.845, 4, 8, 'solid', 'Übergangsmetall', 1.7, 1.83, 7.874, 1808.15, 3134, 10, '[Ar] 3d6 4s2', 2, [+2, +3]],
    [27, 'Cobalt', 'Co', 58.933195, 4, 9, 'solid', 'Übergangsmetall', 1.7, 1.88, 8.86, 1768.15, 3200, 14, '[Ar] 3d7 4s2', 2, [+2]],
    [28, 'Nickel', 'Ni', 58.6934, 4, 10, 'solid', 'Übergangsmetall', 1.6, 1.91, 8.912, 1726.15, 3186, 11, '[Ar] 3d8 4s2', 2, [+2]],
    [29, 'Copper', 'Cu', 63.546, 4, 11, 'solid', 'Übergangsmetall', 1.6, 1.9, 8.96, 1357.75, 2835, 11, '[Ar] 3d10 4s1', 1, [+1, +2]],
    [30, 'Zink', 'Zn', 65.38, 4, 12, 'solid', 'Übergangsmetall', 1.5, 1.65, 7.134, 692.88, 1180, 15, '[Ar] 3d10 4s2', 2, [+2]],
    [31, 'Gallium', 'Ga', 69.723, 4, 13, 'solid', 'Metal', 1.8, 1.81, 5.907, 302.91, 2477, 14, '[Ar] 3d10 4s2 4p1', 3, [+3]],
    [32, 'Germanium', 'Ge', 72.64, 4, 14, 'solid', 'Metalloid', 1.5, 2.01, 5.323, 1211.45, 3106, 17, '[Ar] 3d10 4s2 4p2', 4, []],
    [33, 'Arsen', 'As', 74.9216, 4, 15, 'solid', 'Metalloid', 1.3, 2.18, 5.776, 1090.15, 887, 14, '[Ar] 3d10 4s2 4p3', 5, [+3]],
    [34, 'Selen', 'Se', 78.96, 4, 16, 'solid', 'Nichtmetall', 1.2, 2.55, 4.809, 494.15, 958, 20, '[Ar] 3d10 4s2 4p4', 6, [-2]],
    [35, 'Brom', 'Br', 79.904, 4, 17, 'liq', 'Halogen', 1.1, 2.96, 3.122, 266.05, 332, 19, '[Ar] 3d10 4s2 4p5', 7, [-1]],
    [36, 'Krypton', 'Kr', 83.798, 4, 18, 'gas', 'Edelgas', 1, None, 0.003733, 115.93, 119.93, 23, '[Ar] 3d10 4s2 4p6', 8, []],
    [37, 'Rubidium', 'Rb', 85.4678, 5, 1, 'solid', 'Alkalimetall', 3, 0.82, 1.532, 312.79, 961, 20, '[Kr] 5s1', 1, [+1]],
    [38, 'Strontium', 'Sr', 87.62, 5, 2, 'solid', 'Erdalkalimetall', 2.5, 0.95, 2.64, 1042.15, 1655, 18, '[Kr] 5s2', 2, [+2]],
    [39, 'Yttrium', 'Y', 88.90585, 5, 3, 'solid', 'Übergangsmetall', 2.3, 1.22, 4.469, 1799.15, 3609, 21, '[Kr] 4d1 5s2', 2, [+3]],
    [40, 'Zirconium', 'Zr', 91.224, 5, 4, 'solid', 'Übergangsmetall', 2.2, 1.33, 6.506, 2125.15, 4682, 20, '[Kr] 4d2 5s2', 2, [+4]],
    [41, 'Niob', 'Nb', 92.90638, 5, 5, 'solid', 'Übergangsmetall', 2.1, 1.6, 8.57, 2741.15, 5017, 24, '[Kr] 4d4 5s1', 1, []],
    [42, 'Molybdän', 'Mo', 95.96, 5, 6, 'solid', 'Übergangsmetall', 2, 2.16, 10.22, 2890.15, 4912, 20, '[Kr] 4d5 5s1', 1, []],
    [43, 'Technetium', 'Tc', 98, 5, 7, 'künstlich', 'Übergangsmetall', 2, 1.9, 11.5, 2473.15, 5150, 23, '[Kr] 4d5 5s2', 1, []],
    [44, 'Ruthenium', 'Ru', 101.07, 5, 8, 'solid', 'Übergangsmetall', 1.9, 2.2, 12.37, 2523.15, 4423, 16, '[Kr] 4d7 5s1', 1, []],
    [45, 'Rhodium', 'Rh', 102.9055, 5, 9, 'solid', 'Übergangsmetall', 1.8, 2.28, 12.41, 2239.15, 3968, 20, '[Kr] 4d8 5s1', 1, []],
    [46, 'Palladium', 'Pd', 106.42, 5, 10, 'solid', 'Übergangsmetall', 1.8, 2.2, 12.02, 1825.15, 3236, 21, '[Kr] 4d10', None, [+2]],
    [47, 'Silber', 'Ag', 107.8682, 5, 11, 'solid', 'Übergangsmetall', 1.8, 1.93, 10.501, 1234.15, 2435, 27, '[Kr] 4d10 5s1', 1, [+1]],
    [48, 'Cadmium', 'Cd', 112.411, 5, 12, 'solid', 'Übergangsmetall', 1.7, 1.69, 8.69, 594.33, 1040, 22, '[Kr] 4d10 5s2', 2, [+2]],
    [49, 'Indium', 'In', 114.818, 5, 13, 'solid', 'Metall', 2, 1.78, 7.31, 429.91, 2345, 34, '[Kr] 4d10 5s2 5p1', 3, [+3]],
    [50, 'Zinn', 'Sn', 118.71, 5, 14, 'solid', 'Metall', 1.7, 1.96, 7.287, 505.21, 2875, 28, '[Kr] 4d10 5s2 5p2', 4, [+2, +4]],
    [51, 'Antimon', 'Sb', 121.76, 5, 15, 'solid', 'Metalloid', 1.5, 2.05, 6.685, 904.05, 1860, 29, '[Kr] 4d10 5s2 5p3', 5, [+3]],
    [52, 'Tellur', 'Te', 127.6, 5, 16, 'solid', 'Metalloid', 1.4, 2.1, 6.232, 722.8, 1261, 29, '[Kr] 4d10 5s2 5p4', 6, []],
    [53, 'Iod', 'I', 126.90447, 5, 17, 'solid', 'Halogen', 1.3, 2.66, 4.93, 386.65, 457.4, 24, '[Kr] 4d10 5s2 5p5', 7, [-1]],
    [54, 'Xenon', 'Xe', 131.293, 5, 18, 'gas', 'Edelgas', 1.2, None, 0.005887, 161.45, 165.03, 31, '[Kr] 4d10 5s2 5p6', 8, []],
    [55, 'Cäsium', 'Cs', 132.9054519, 6, 1, 'solid', 'Alkalimetall', 3.3, 0.79, 1.873, 301.7, 944, 22, '[Xe] 6s1', 1, [+1]],
    [56, 'Barium', 'Ba', 137.327, 6, 2, 'solid', 'Erdalkalimetall', 2.8, 0.89, 3.594, 1002.15, 2170, 25, '[Xe] 6s2', 2, [+2]],
    [57, 'Lanthan', 'La', 138.90547, 6, 3, 'solid', 'Lanthanide', 2.7, 1.1, 6.145, 1193.15, 3737, 19, '[Xe] 5d1 6s2', 2, [+3]],
    [58, 'Cer', 'Ce', 140.116, 6, 19, 'solid', 'Lanthanide', 2.7, 1.12, 6.77, 1071.15, 3716, 19, '[Xe] 4f1 5d1 6s2', 2, []],
    [59, 'Praseodym', 'Pr', 140.90765, 6, 20, 'solid', 'Lanthanide', 2.7, 1.13, 6.773, 1204.15, 3793, 15, '[Xe] 4f3 6s2', 2, []],
    [60, 'Neodym', 'Nd', 144.242, 6, 21, 'solid', 'Lanthanide', 2.6, 1.14, 7.007, 1289.15, 3347, 16, '[Xe] 4f4 6s2', 2, []],
    [61, 'Promethium', 'Pm', 145, 6, 22, 'künstlich', 'Lanthanide', 2.6, 1.13, 7.26, 1204.15, 3273, 14, '[Xe] 4f5 6s2', 2, []],
    [62, 'Samarium', 'Sm', 150.36, 6, 23, 'solid', 'Lanthanide', 2.6, 1.17, 7.52, 1345.15, 2067, 17, '[Xe] 4f6 6s2', 2, []],
    [63, 'Europium', 'Eu', 151.964, 6, 24, 'solid', 'Lanthanide', 2.6, 1.2, 5.243, 1095.15, 1802, 21, '[Xe] 4f7 6s2', 2, []],
    [64, 'Gadolinium', 'Gd', 157.25, 6, 25, 'solid', 'Lanthanide', 2.5, 1.2, 7.895, 1585.15, 3546, 17, '[Xe] 4f7 5d1 6s2', 2, []],
    [65, 'Terbium', 'Tb', 158.92535, 6, 26, 'solid', 'Lanthanide', 2.5, 1.2, 8.229, 1630.15, 3503, 24, '[Xe] 4f9 6s2', 2, []],
    [66, 'Dysprosium', 'Dy', 162.5, 6, 27, 'solid', 'Lanthanide', 2.5, 1.22, 8.55, 1680.15, 2840, 21, '[Xe] 4f10 6s2', 2, []],
    [67, 'Holmium', 'Ho', 164.93032, 6, 28, 'solid', 'Lanthanide', 2.5, 1.23, 8.795, 1743.15, 2993, 29, '[Xe] 4f11 6s2', 2, []],
    [68, 'Erbium', 'Er', 167.259, 6, 29, 'solid', 'Lanthanide', 2.5, 1.24, 9.066, 1795.15, 3503, 16, '[Xe] 4f12 6s2', 2, []],
    [69, 'Thulium', 'Tm', 168.93421, 6, 30, 'solid', 'Lanthanide', 2.4, 1.25, 9.321, 1818.15, 2223, 18, '[Xe] 4f13 6s2', 2, []],
    [70, 'Ytterbium', 'Yb', 173.054, 6, 31, 'solid', 'Lanthanide', 2.4, 1.1, 6.965, 1097.15, 1469, 16, '[Xe] 4f14 6s2', 2, []],
    [71, 'Lutetium', 'Lu', 174.9668, 6, 32, 'solid', 'Lanthanide', 2.3, 1.27, 9.84, 1936.15, 3675, 22, '[Xe] 4f14 5d1 6s2', 2, [+3]],
    [72, 'Hafnium', 'Hf', 178.49, 6, 4, 'solid', 'Übergangsmetall', 2.2, 1.3, 13.31, 2500.15, 4876, 17, '[Xe] 4f14 5d2 6s2', 2, [+4]],
    [73, 'Tantal', 'Ta', 180.94788, 6, 5, 'solid', 'Übergangsmetall', 2.1, 1.5, 16.654, 3269.15, 5731, 19, '[Xe] 4f14 5d3 6s2', 2, []],
    [74, 'Wolfram', 'W', 183.84, 6, 6, 'solid', 'Übergangsmetall', 2, 2.36, 19.25, 3680.15, 5828, 22, '[Xe] 4f14 5d4 6s2', 2, []],
    [75, 'Rhenium', 'Re', 186.207, 6, 7, 'solid', 'Übergangsmetall', 2, 1.9, 21.02, 3453.15, 5869, 21, '[Xe] 4f14 5d5 6s2', 2, []],
    [76, 'Osmium', 'Os', 190.23, 6, 8, 'solid', 'Übergangsmetall', 1.9, 2.2, 22.61, 3300.15, 5285, 19, '[Xe] 4f14 5d6 6s2', 2, []],
    [77, 'Iridium', 'Ir', 192.217, 6, 9, 'solid', 'Übergangsmetall', 1.9, 2.2, 22.56, 2716.15, 4701, 25, '[Xe] 4f14 5d7 6s2', 2, []],
    [78, 'Platin', 'Pt', 195.084, 6, 10, 'solid', 'Übergangsmetall', 1.8, 2.28, 21.46, 2045.15, 4098, 32, '[Xe] 4f14 5d9 6s1', 1, [+2]],
    [79, 'Gold', 'Au', 196.966569, 6, 11, 'solid', 'Übergangsmetall', 1.8, 2.54, 19.282, 1337.73, 3129, 21, '[Xe] 4f14 5d10 6s1', 1, [+1, +3]],
    [80, 'Quecksilber', 'Hg', 200.59, 6, 12, 'liq', 'Übergangsmetall', 1.8, 2, 13.5336, 234.43, 630, 26, '[Xe] 4f14 5d10 6s2', 2, [+1, +2]],
    [81, 'Thallium', 'Tl', 204.3833, 6, 13, 'solid', 'Metall', 2.1, 2.04, 11.85, 577.15, 1746, 28, '[Xe] 4f14 5d10 6s2 6p1', 3, [+1]],
    [82, 'Blei', 'Pb', 207.2, 6, 14, 'solid', 'Metall', 1.8, 2.33, 11.342, 600.75, 2022, 29, '[Xe] 4f14 5d10 6s2 6p2', 4, [+2, +4]],
    [83, 'Bismut', 'Bi', 208.9804, 6, 15, 'solid', 'Metall', 1.6, 2.02, 9.807, 544.67, 1837, 19, '[Xe] 4f14 5d10 6s2 6p3', 5, [+3]],
    [84, 'Polonium', 'Po', 210, 6, 16, 'solid', 'Metalloid', 1.5, 2, 9.32, 527.15, 1235, 34, '[Xe] 4f14 5d10 6s2 6p4', 6, []],
    [85, 'Astat', 'At', 210, 6, 17, 'solid', 'Edelgas', 1.4, 2.2, 7, 575.15, 610, 21, '[Xe] 4f14 5d10 6s2 6p5', 7, [-1]],
    [86, 'Radon', 'Rn', 222, 6, 18, 'gas', 'Alkalimetall', 1.3, None, 0.00973, 202.15, 211.3, 20, '[Xe] 4f14 5d10 6s2 6p6', 8, []],
    [87, 'Francium', 'Fr', 223, 7, 1, 'solid', 'Erdalkalimetall', None, 0.7, 1.87, 300.15, 950, 21, '[Rn] 7s1', 1, [+1]],
    [88, 'Radium', 'Ra', 226, 7, 2, 'solid', 'Actinoid', None, 0.9, 5.5, 973.15, 2010, 15, '[Rn] 7s2', 2, [+2]],
    [89, 'Actinium', 'Ac', 227, 7, 3, 'solid', 'Actinoid', None, 1.1, 10.07, 1323.15, 3471, 11, '[Rn] 6d1 7s2', 2, []],
    [90, 'Thorium', 'Th', 232.03806, 7, 19, 'solid', 'Actinoid', None, 1.3, 11.72, 2028.15, 5061, 12, '[Rn] 6d2 7s2', 2, []],
    [91, 'Protactinium', 'Pa', 231.03588, 7, 20, 'solid', 'Actinoid', None, 1.5, 15.37, 1873.15, 4300, 14, '[Rn] 5f2 6d1 7s2', 2, []],
    [92, 'Uran', 'U', 238.02891, 7, 21, 'solid', 'Actinoid', None, 1.38, 18.95, 1405.15, 4404, 15, '[Rn] 5f3 6d1 7s2', 2, []],
    [93, 'Neptunium', 'Np', 237, 7, 22, 'künstlich', 'Actinoid', None, 1.36, 20.45, 913.15, 4273, 153, '[Rn] 5f4 6d1 7s2', 2, []],
    [94, 'Plutonium', 'Pu', 244, 7, 23, 'künstlich', 'Actinoid', None, 1.28, 19.84, 913.15, 3501, 163, '[Rn] 5f6 7s2', 2, []],
    [95, 'Americium', 'Am', 243, 7, 24, 'künstlich', 'Actinoid', None, 1.3, 13.69, 1267.15, 2880, 133, '[Rn] 5f7 7s2', 2, []],
    [96, 'Curium', 'Cm', 247, 7, 25, 'künstlich', 'Actinoid', None, 1.3, 13.51, 1340.15, 3383, 133, None, 2, []],
    [97, 'Berkelium', 'Bk', 247, 7, 26, 'künstlich', 'Actinoid', None, 1.3, 14.79, 1259.15, 983, 83, None, 2, []],
    [98, 'Californium', 'Cf', 251, 7, 27, 'künstlich', 'Actinoid', None, 1.3, 15.1, 1925.15, 1173, 123, None, 2, []],
    [99, 'Einsteinium', 'Es', 252, 7, 28, 'künstlich', 'Actinoid', None, 1.3, 13.5, 1133.15, None, 123, None, 2, []],
    [100, 'Fermium', 'Fm', 257, 7, 29, 'künstlich', 'Actinoid', None, 1.3, None, None, None, 103, None, 2, []],
    [101, 'Mendelevium', 'Md', 258, 7, 30, 'künstlich', 'Actinoid', None, 1.3, None, None, None, 33, None, 2, []],
    [102, 'Nobelium', 'No', 259, 7, 31, 'künstlich', 'Actinoid', None, 1.3, None, None, None, 73, None, 2, []],
    [103, 'Lawrencium', 'Lr', 262, 7, 32, 'künstlich', 'Actinoid', None, None, None, None, None, 203, None, 3, []],
    [104, 'Rutherfordium', 'Rf', 261, 7, 4, 'künstlich', 'Lanthanoid', None, None, 18.1, None, None, None, None, None, []],
    [105, 'Dubnium', 'Db', 262, 7, 5, 'künstlich', 'Lanthanoid', None, None, 39, None, None, None, None, None, []],
    [106, 'Seaborgium', 'Sg', 266, 7, 6, 'künstlich', 'Lanthanoid', None, None, 35, None, None, None, None, None, []],
    [107, 'Bohrium', 'Bh', 264, 7, 7, 'künstlich', 'Lanthanoid', None, None, 37, None, None, None, None, None, []],
    [108, 'Hassium', 'Hs', 267, 7, 8, 'künstlich', 'Lanthanoid', None, None, 41, None, None, None, None, None, []],
    [109, 'Meitnerium', 'Mt', 268, 7, 9, 'künstlich', 'Lanthanoid', None, None, 35, None, None, None, None, None, []],
    [110, 'Darmstadtium', 'Ds', 271, 7, 10, 'künstlich', 'Lanthanoid', None, None, None, None, None, None, None, None, []],
    [111, 'Roentgenium', 'Rg', 272, 7, 11, 'künstlich', 'Lanthanoid', None, None, None, None, None, None, None, None, []],
    [112, 'Copernicium', 'Cn', 285, 7, 12, 'künstlich', 'Lanthanoid', None, None, None, None, None, None, None, None, []],
    [113, 'Ununtrium', 'Uut', 284, 7, 13, 'künstlich', None, None, None, None, None, None, None, None, None, []],
    [114, 'Ununquadium', 'Uuq', 289, 7, 14, 'künstlich', 'Lanthanoid', None, None, None, None, None, None, None, None, []],
    [115, 'Ununpentium', 'Uup', 288, 7, 15, 'künstlich', None, None, None, None, None, None, None, None, None, []],
    [116, 'Ununhexium', 'Uuh', 292, 7, 16, 'künstlich', 'Lanthanoid', None, None, None, None, None, None, None, None, []],
    [117, 'Ununseptium', 'Uus', 295, 7, 17, 'künstlich', None, None, None, None, None, None, None, None, None, []],
    [118, 'Ununoctium', 'Uuo', 294, 7, 18, 'künstlich', 'Edelgas', None, None, None, None, None, None, None, None, []],
]

SUPERSCRIPT_DIGITS = "⁰¹²³⁴⁵⁶⁷⁸⁹"
SUBSCRIPT_DIGITS = "₀₁₂₃₄₅₆₇₈₉"

SUPERSCRIPT_MINUS = "⁻"
SUPERSCRIPT_PLUS = "⁺"

SUBSCRIPT_MINUS = "₋"
SUBSCRIPT_PLUS = "₊"

AVOGADRO_KONSTANTE = 6.02214076e+23


class Element:
    protonen = 0
    name = ""
    symbol = ""

    data = {}

    def get_neutronen_approx(self):
        return self.data[RELATIVE_ATOMMASSE] - self.protonen

    def get_valenzelektronen_from_orbital(self):
        ek = self.data[ELEKTRONENKONFIGURATION]
        if ek is None:
            return None
        per_schale = {i: 0 for i in range(1, 8)}
        for o in ek.split(" "):
            if o[0] == "[":
                continue
            s, n = re.findall(r"[\d]+", o)
            s = int(s)
            n = int(n)
            per_schale[s] += n
        for i in range(7, 0, -1):
            n = per_schale[i]
            if n > 0:
                if n == 2 * i * i:
                    n = 0
                return n


ELEMENTS_BY_SYMBOL = {}  #: Dict[str, Element]
ELEMENTS = []  #: List[Element]

for _row in PERIODIC_TABLE_DATA:
    el = Element()
    el.protonen = _row[0]
    el.name = _row[1]
    el.symbol = _row[2]
    el.data = {PERIODIC_TABLE_HEADS[i]: _row[i] for i in range(len(_row))}
    ELEMENTS_BY_SYMBOL[el.symbol] = el
    ELEMENTS.append(el)

LONGEST_ELEMENT_DATA_HEADER = max(map(len, PERIODIC_TABLE_HEADS))

HNOFClBrI = [
    ELEMENTS_BY_SYMBOL["H"],
    ELEMENTS_BY_SYMBOL["N"],
    ELEMENTS_BY_SYMBOL["O"],
    ELEMENTS_BY_SYMBOL["F"],
    ELEMENTS_BY_SYMBOL["Cl"],
    ELEMENTS_BY_SYMBOL["Br"],
    ELEMENTS_BY_SYMBOL["I"],
]


def levenshtein_distance(s, t):
    # Initialize matrix of zeros
    rows = len(s) + 1
    cols = len(t) + 1
    distance = [[0] * cols for _ in range(rows)]

    # Populate matrix of zeros with the indeces of each character of both strings
    for i in range(1, rows):
        for k in range(1, cols):
            distance[i][0] = i
            distance[0][k] = k

    # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions
    for col in range(1, cols):
        for row in range(1, rows):
            cost = 0 if s[row - 1] == t[col - 1] else 1
            distance[row][col] = min(distance[row - 1][col] + 1,  # Cost of deletions
                                     distance[row][col - 1] + 1,  # Cost of insertions
                                     distance[row - 1][col - 1] + cost)  # Cost of substitutions
    return distance[row][col]


def get_best(score_func, data):
    scores = list(map(score_func, data))
    return data[scores.index(max(scores))]


def format_superscript(num, show_plus_sign=False, show_sign_at_the_end=False):
    if num < 0:
        sign = SUPERSCRIPT_MINUS
        num *= -1
    elif show_plus_sign:
        sign = SUPERSCRIPT_PLUS
    else:
        sign = ""
    sign_begin = sign if not show_sign_at_the_end else ""
    sign_end = sign if show_sign_at_the_end else ""
    return sign_begin + "".join([SUPERSCRIPT_DIGITS[int(digit)] for digit in str(num)]) + sign_end


def format_subscript(num, show_plus_sign=False, show_sign_at_the_end=False):
    if num < 0:
        sign = SUBSCRIPT_MINUS
        num *= -1
    elif show_plus_sign:
        sign = SUBSCRIPT_PLUS
    else:
        sign = ""
    sign_begin = sign if not show_sign_at_the_end else ""
    sign_end = sign if show_sign_at_the_end else ""
    return sign_begin + "".join([SUBSCRIPT_DIGITS[int(digit)] for digit in str(num)]) + sign_end


def to_title_case(s):
    if not s.strip():
        return s
    return " ".join([word[0].upper() + word[1:] for word in s.split(" ")])


def left_pad(s, length):
    return s + " " * (length - len(s))


def mp_round(value, digits):
    ten_mult = 10 ** digits
    return str(int(value * ten_mult) / ten_mult)


def kgv(nums):
    if len(nums) == 2:
        return abs(nums[0] * nums[1]) // ggt(nums)
    val = kgv(nums[:2])
    for i in range(2, len(nums)):
        val = kgv([val, nums[i]])
    return val


def ggt(nums):
    if len(nums) == 2:
        x, y = nums
        while y != 0:
            (x, y) = (y, x % y)
        return x
    val = ggt(nums[:2])
    for i in range(2, len(nums)):
        val = ggt([val, nums[i]])
    return val


def simplify_numbers(nums):
    options = []
    for i in range(len(nums)):
        factor = 1000 / nums[i]
        o = [int(n / factor) for n in nums]
        gg = ggt(o)
        options.append([int(n / gg) for n in o])
    return get_best(lambda opt: -sum(opt), options)


def zeros_matrix(rows, cols):
    A = []
    for _ in range(rows):
        A.append([])
        for _ in range(cols):
            A[-1].append(0.0)

    return A


def copy_matrix(original):
    rows = len(original)
    cols = len(original[0])

    copied = zeros_matrix(rows, cols)

    for i in range(rows):
        for j in range(cols):
            copied[i][j] = original[i][j]

    return copied


def matrix_multiply(mat_a, mat_b):
    rows_a = len(mat_a)
    cols_a = len(mat_a[0])

    rows_b = len(mat_b)
    cols_b = len(mat_b[0])

    if cols_a != rows_b:
        print('WARNING: Number of A columns must equal number of B rows.')

    result = zeros_matrix(rows_a, cols_b)

    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for ii in range(cols_a):
                total += mat_a[i][ii] * mat_b[ii][j]
            result[i][j] = total

    return result


def solve_linear_equation_system(mat_a, mat_b):
    a_modified = copy_matrix(mat_a)
    b_modified = copy_matrix(mat_b)
    n = len(a_modified)

    fd = 1  # fd stands for focus diagonal OR the current diagonal
    fd_scaler = 1. / a_modified[fd][fd]

    for j in range(n):  # using j to indicate cycling thru columns
        a_modified[fd][j] = fd_scaler * a_modified[fd][j]
    b_modified[fd][0] = fd_scaler * b_modified[fd][0]

    n = len(mat_a)
    indices = list(range(n))

    for i in indices[0:fd] + indices[fd + 1:]:  # *** skip row with fd in it.
        cr_scaler = a_modified[i][fd]  # cr stands for "current row".
        for j in range(n):  # cr - cr_scaler * fdRow, but one element at a time.
            a_modified[i][j] = a_modified[i][j] - cr_scaler * a_modified[fd][j]
        b_modified[i][0] = b_modified[i][0] - cr_scaler * b_modified[fd][0]

    a_modified = copy_matrix(mat_a)
    b_modified = copy_matrix(mat_b)
    n = len(a_modified)

    indices = list(range(n))  # to allow flexible row referencing ***
    for fd in range(0, n):  # fd stands for focus diagonal
        fd_scaler = 1.0 / a_modified[fd][fd]
        # FIRST: scale fd row with fd inverse.
        for j in range(n):  # Use j to indicate column looping.
            a_modified[fd][j] *= fd_scaler
        b_modified[fd][0] *= fd_scaler

        # SECOND: operate on all rows except fd row.
        for i in indices[:fd] + indices[fd + 1:]:  # *** skip row with fd in it.
            cr_scaler = a_modified[i][fd]  # cr stands for "current row".
            for j in range(n):  # cr - cr_scaler * fdRow, but one element at a time.
                a_modified[i][j] = a_modified[i][j] - cr_scaler * a_modified[fd][j]
            b_modified[i][0] = b_modified[i][0] - cr_scaler * b_modified[fd][0]

    return b_modified


def gauss_elimination(mat):
    n = len(mat)
    a = mat
    x = [0] * n
    # Applying Gauss Elimination
    for i in range(n):
        if a[i][i] == 0.0:
            raise ValueError('Divide by zero detected!')

        for j in range(i + 1, n):
            ratio = a[j][i] / a[i][i]

            for k in range(n + 1):
                a[j][k] = a[j][k] - ratio * a[i][k]

    # Back Substitution
    x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = a[i][n]

        for j in range(i + 1, n):
            x[i] = x[i] - a[i][j] * x[j]

        x[i] = x[i] / a[i][i]

    return x


def format_roman_number(num):
    # https://www.w3resource.com/python-exercises/class-exercises/python-class-exercise-1.php
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    res = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            res += syb[i]
            num -= val[i]
        i += 1
    return res


def tool_element_info():
    while True:
        inp = input("Symbol oder Name eingeben: ")
        if not inp.strip():
            print("Tool beendet.")
            return
        if inp[0].isdigit():
            num = 0
            rest = ""
            for i, c in enumerate(inp):
                if c.isdigit():
                    num = 10 * num + int(c)
                else:
                    rest = to_title_case(inp[i:])
                    break
            if rest in ELEMENTS_BY_SYMBOL:
                el = ELEMENTS_BY_SYMBOL[rest]
                if num == el.protonen:
                    print(format_subscript(el.protonen) + el.symbol, "hat", num, "Protonen und durchschnittlich", el.get_neutronen_approx(), "Neutronen")
                else:
                    print(format_superscript(num) + el.symbol, "könnte ein", el.name + "-Isotop mit", el.protonen, "Protonen und", num - el.protonen, "Neutronen sein.")
                continue

        el = get_best(lambda elem: max(-levenshtein_distance(elem.name, inp), -levenshtein_distance(elem.symbol, inp)), ELEMENTS)
        for h in PERIODIC_TABLE_HEADS:
            print("{}: {}".format(h, el.data[h]))


class ElektronenVerteilung:
    def __init__(self):
        self.fill = [0] * 7
        self.capacity = [2 * n * n for n in range(1, 8)]
        self.chars = [chr(ord('K') + i) for i in range(7)]

    def fill_for(self, e):
        if e <= 2:
            self.fill[0] += 1
        elif e <= 10:
            self.fill[1] += 1
        elif e <= 18:
            self.fill[2] += 1
        elif 19 <= e <= 20 or 31 <= e <= 36:
            self.fill[3] += 1
        elif 37 <= e <= 37 or 49 <= e <= 54:
            self.fill[4] += 1
        elif 55 <= e <= 56 or 81 <= e <= 86:
            self.fill[4] += 1
        elif 87 <= e <= 88:
            self.fill[4] += 1
        else:
            self.fill_innerst()

    def fill_for_all(self, electrons):
        for e in range(1, electrons + 1):
            self.fill_for(e)

    def fill_innerst(self):
        for i in range(7):
            if self.fill[i] < self.capacity[i]:
                self.fill[i] += 1
                return

    def print(self):
        for i in range(7):
            if self.fill[i] == 0:
                break
            print("Schale", self.chars[i], self.fill[i], "von", self.capacity[i], "Elektronen")


def tool_bohrsches_atommodell():
    while True:
        inp = to_title_case(input("Elementsymbol eingeben: "))
        if not inp.strip():
            print("Tool beendet.")
            return
        elif inp in ELEMENTS_BY_SYMBOL:
            el = ELEMENTS_BY_SYMBOL[inp]
            print("Elektronenvereilung von", el.name)
            verteilung = ElektronenVerteilung()
            verteilung.fill_for_all(el.protonen)
            verteilung.print()
            print("Kern:", el.protonen, "Protonen und ca.", el.get_neutronen_approx(), "Neutronen")
        else:
            print("Kein Element mit Symbol", inp)


def tool_delta_en():
    while True:
        inp = input("Mehrere Elementsymbole getrennt mit Komma: ")
        if len(inp) == 0:
            print("Tool beendet.")
            return
        else:
            symbols = [to_title_case(e) for e in inp.split(",")]
            if len(symbols) < 2:
                print("Bitte mehrere Elemente angeben")
            elif len(symbols) == 2:
                el1 = ELEMENTS_BY_SYMBOL[symbols[0]]
                el2 = ELEMENTS_BY_SYMBOL[symbols[1]]
                en1 = el1.data[ELEKTRONEGATIVITAET]
                en2 = el2.data[ELEKTRONEGATIVITAET]
                print("ΔEN =", abs(en1 - en2), "(EN von", el1.name, "=", en1, "und EN von", el2.name, "=", en2)
            else:
                print("    ", *[left_pad(s, 4) for s in symbols])
                for s1 in symbols:
                    en1 = ELEMENTS_BY_SYMBOL[s1].data[ELEKTRONEGATIVITAET]
                    values = []
                    for s2 in symbols:
                        en2 = ELEMENTS_BY_SYMBOL[s2].data[ELEKTRONEGATIVITAET]
                        values.append(mp_round(abs(en1 - en2), 2))
                    print(left_pad(s1, 4), *[left_pad(v, 4) for v in values])


def print_simple_organic_structure(stammlaenge, seitenketten):
    for i in range(1, stammlaenge + 1):
        padded_i = left_pad(str(i), 2)
        padded_spaces = len(padded_i) * " "
        if i != 1:
            print(padded_spaces, "|")
        relevant = [sk for sk in seitenketten if sk[0] == i]
        if len(relevant) == 0:
            print(padded_i, "C")
        elif len(relevant) == 1:
            print(padded_i, "C" + "-C" * relevant[0][1])
        else:
            print(padded_spaces, "| ╱" + "-C" * relevant[0][1])
            print(padded_i, "C")
            print(padded_spaces, "| ╲" + "-C" * relevant[1][1])


def tool_organic_name_decoder():
    while True:
        full_name = input("Name einer organischen Verbindung: ").lower()
        if not full_name.strip():
            print("Tool beendet.")
            return
        else:
            seitenketten = []
            yl_splits = full_name.split("yl")
            stamm = yl_splits[-1]
            stammlaenge = 0
            for i, n in enumerate(ORGANIC_NAMES):
                if n in stamm:
                    stammlaenge = i + 1
                    break
            for sk_string in yl_splits[:-1]:
                if sk_string[0] == "-":
                    sk_string = sk_string[1:]
                indices_str, name_str = sk_string.split("-")
                indices = list(map(int, indices_str.split(",")))
                length = 0
                for i, n in enumerate(ORGANIC_NAMES):
                    if n in name_str:
                        length = i + 1
                        break
                for i in indices:
                    seitenketten.append([i, length])
            c_count = stammlaenge
            print_simple_organic_structure(stammlaenge, seitenketten)
            print("Summenformel: C" + format_subscript(c_count) + "H" + format_subscript(2 * c_count + 2))
            # TODO print info about endigs -en -an and so on


def tool_organic_name_encoder():
    stammlaenge = int(input("Stammlänge: "))
    c_count = stammlaenge
    seitenketten = []
    while True:
        index = input("Index Seitenkette (leer lassen zum Beenden): ")
        if not index.strip():
            break
        else:
            index = int(index)
            length = int(input("Länge der Seitenkette: "))
            seitenketten.append([index, length])
            c_count += length

    print("Summenformel: C" + format_subscript(c_count) + "H" + format_subscript(2 * c_count + 2))
    indices_by_length = {}
    idx_min = None
    idx_max = None
    for idx, length in seitenketten:
        if idx_min is None:
            idx_min = idx_max = idx
        else:
            idx_min = min(idx_min, idx)
            idx_max = max(idx_max, idx)
        if length not in indices_by_length:
            indices_by_length[length] = [idx]
        else:
            indices_by_length[length].append(idx)

    inverse = stammlaenge - idx_max + 1 < idx_min

    preassembled = []
    for length, indices in indices_by_length.items():
        idx_string = ",".join(map(str, sorted([stammlaenge - i + 1 for i in indices] if inverse else indices)))
        index_count_name = GREEK_NUMBERS[len(indices) - 1] if len(indices) > 1 else ""
        length_name = ORGANIC_NAMES[length - 1]
        preassembled.append([idx_string, index_count_name, length_name])
    preassembled.sort(key=lambda row: row[1])
    print("-".join(["{}-{}{}yl".format(*row) for row in preassembled]) + ORGANIC_NAMES[stammlaenge - 1] + "an")


class ElementarMolekul:
    def __init__(self, num=1, el=None):
        self.num = num
        self.element = el
        self.ionenladung = None

    def __str__(self):
        return self.element.symbol + (format_subscript(self.num) if self.num > 1 else "") + (format_superscript(self.ionenladung, True, True) if self.ionenladung is not None else "")

    @staticmethod
    def parse(inp):
        i = 0
        while i < len(inp) and not inp[i].isdigit():
            i += 1
        res = ElementarMolekul()
        symbol = to_title_case(inp[:i])
        res.element = ELEMENTS_BY_SYMBOL[symbol]
        num_str = inp[i:]
        if num_str:
            res.num = int(num_str)
        else:
            res.num = 1
        return res

    def copy(self):
        c = ElementarMolekul()
        c.num = self.num
        c.element = self.element
        return c


class Molekul:
    def __init__(self, elementar_molekuls=None):
        if elementar_molekuls is None:
            elementar_molekuls = []
        self.elementar_molekuls = elementar_molekuls

    def __str__(self):
        return "".join([str(em) for em in self.elementar_molekuls])

    @staticmethod
    def parse(inp):
        buf = ""
        res = Molekul()
        for c in inp:
            if len(buf) == 0 or (not buf[-1].isdigit() and c.lower() == c):
                buf += c
            elif c.isdigit():
                buf += c
            else:
                res.elementar_molekuls.append(ElementarMolekul.parse(buf))
                buf = c
        if buf:
            res.elementar_molekuls.append(ElementarMolekul.parse(buf))
        return res

    def get_molar_mass(self):
        return sum(em.element.data[RELATIVE_ATOMMASSE] * em.num for em in self.elementar_molekuls)

    def reorder_binary_if_needed(self):
        if (len(self.elementar_molekuls) == 2
                and (
                        self.elementar_molekuls[1].element.data[GRUPPE] in [14, 15]
                        or self.elementar_molekuls[0].element.data[ELEKTRONEGATIVITAET] > self.elementar_molekuls[1].element.data[ELEKTRONEGATIVITAET]
                )):
            self.elementar_molekuls.reverse()


class Reaction:
    def __init__(self):
        self.molekule_before = []
        self.molekule_after = []

    def __str__(self):
        return " + ".join(map(str, self.molekule_before)) + " -> " + " + ".join(map(str, self.molekule_after))

    @staticmethod
    def parse(reaktion):
        raw_before, raw_after = reaktion.split("->")
        res = Reaction()
        res.molekule_before = [Molekul.parse(m.strip()) for m in raw_before.split("+")]
        res.molekule_after = [Molekul.parse(m.strip()) for m in raw_after.split("+")]
        return res


class BalancedReaction:
    def __init__(self):
        self.molekule_before = []
        self.molekule_after = []

    @staticmethod
    def _format_molecule_and_coeff(coeff, molecule):
        return ("" if coeff == 1 else str(coeff)) + str(molecule)

    def __str__(self):
        fmt_before = [self._format_molecule_and_coeff(c, m) for c, m in self.molekule_before]
        fmt_after = [self._format_molecule_and_coeff(c, m) for c, m in self.molekule_after]
        return " + ".join(fmt_before) + " -> " + " + ".join(fmt_after)

    @staticmethod
    def balance(unbalanced):
        num_verbindungen = len(unbalanced.molekule_before) + len(unbalanced.molekule_after)
        a = zeros_matrix(num_verbindungen, num_verbindungen + 1)
        elements = []
        for i, mo in enumerate(unbalanced.molekule_before + unbalanced.molekule_after):
            sign = -1 if i >= len(unbalanced.molekule_before) else 1
            for el in mo.elementar_molekuls:
                if el.element.symbol in elements:
                    idx = elements.index(el.element.symbol)
                else:
                    idx = len(elements)
                    elements.append(el.element.symbol)
                a[idx][i] += el.num * sign
        for i in range(len(elements), num_verbindungen):
            a[i][0] = 1
            a[i][num_verbindungen] = 1000

        a_rearranged = BalancedReaction._sort_equations(a, num_verbindungen)

        res = gauss_elimination(a_rearranged)
        res = simplify_numbers(res)
        res = [int(r) for r in res]
        div = ggt(res)
        res = [int(r / div) for r in res]

        balanced = BalancedReaction()
        balanced.molekule_before = [[res[i], ub] for i, ub in enumerate(unbalanced.molekule_before)]
        balanced.molekule_after = [[res[i + len(unbalanced.molekule_before)], ub] for i, ub in enumerate(unbalanced.molekule_after)]
        return balanced

    @staticmethod
    def _sort_equations(a, num_verbindungen):
        a_rearranged = [None] * num_verbindungen
        rows_with_nonzero_cols = [[] for _ in range(num_verbindungen)]  # rows_with_nonzero_cols[2] = [3, 4] means that col 2 is nonzero in row 3 and 4
        for i, row in enumerate(a):
            for col in range(num_verbindungen):
                if row[col] != 0:
                    rows_with_nonzero_cols[col].append(i)
        s_nums = sorted([(c, n) for c, n in enumerate(rows_with_nonzero_cols)], key=lambda x: len(x[1]))
        while len(s_nums):
            col, rows = s_nums.pop(0)
            r = rows[0]
            a_rearranged[col] = a[r]
            a[r] = None
            for j in range(len(s_nums)):
                if r in s_nums[j][1]:
                    s_nums[j][1].remove(r)
            s_nums.sort(key=lambda x: len(x[1]))
        return a_rearranged


# _x CH4 + _y O2 -> _z C + _a H2O
# _x*1 - _z*1 = 0 | C-Atome
# _x*4 - _a*2 = 0 | H-Atome
# _y*2 - _a*1 = 0 | O-Atome


def tool_ausgleichen():
    raw_str = input("Bitte Reaktionsgleichung eingeben: ")
    if not raw_str.strip():
        return
    reaktion = Reaction.parse(raw_str)
    print(reaktion)
    balanced = BalancedReaction.balance(reaktion)
    print(balanced)


def tool_vollstaendig_verbrennung():
    while True:
        inp = input("Molekül zum Verbrennen: ")
        if not inp.strip():
            print("Tool beendet.")
            return
        mo = Molekul.parse(inp)
        ub = Reaction()
        ub.molekule_before = [mo, Molekul.parse("O2")]
        ub.molekule_after = [Molekul.parse("CO2"), Molekul.parse("H2O")]
        br = BalancedReaction.balance(ub)
        print(ub)
        print(br)


class StochiometrieData:
    def __init__(self):
        self.n = None
        self.m = None
        self.M = None
        self.N = None

    def __str__(self):
        vals = {
            "n": "?" if self.n is None else (str(self.n) + "mol"),
            "m": "?" if self.m is None else (str(self.m) + "g"),
            "M": "?" if self.M is None else (str(self.M) + "g/mol"),
            "N": "?" if self.N is None else str(self.N)
        }
        return ", ".join(k + "=" + v for k, v in vals.items())

    def copy(self):
        c = StochiometrieData()
        c.n = self.n
        c.m = self.m
        c.M = self.M
        c.N = self.N
        return c

    def solve_rest(self):
        while self._solve_rest_internal():
            pass

    def _solve_rest_internal(self):
        if self.n is not None and self.N is None:
            self.N = AVOGADRO_KONSTANTE * self.n
            return True
        if self.n is None and self.N is not None:
            self.n = self.N / AVOGADRO_KONSTANTE
            return True
        if self.n is None and self.m is not None and self.M is not None:
            self.n = self.m / self.M
            return True
        if self.m is None and self.n is not None and self.M is not None:
            self.m = self.n * self.M
            return True
        if self.M is None and self.n is not None and self.m is not None:
            self.M = self.m / self.n
            return True
        return False


def tool_stochiometrie():
    print("Bekannte Informationen eingeben. z.B. 'n=6' für Stoffmenge 6 Mol")
    entered = StochiometrieData()
    while True:
        calced = entered.copy()
        calced.solve_rest()
        print("Gegeben:", entered)
        print("Berechnet:", calced)
        command = input("> ")
        if not command.strip():
            return
        if command == "=":
            entered = StochiometrieData()
        if command.count("=") != 1:
            print("Ungültiger Befehl. Keine Aktion.")
            continue
        var, val = command.split("=")
        var = var.strip()
        if var == "M":
            entered.M = Molekul.parse(val.strip()).get_molar_mass()
        else:
            try:
                val = float(val)
            except ValueError:
                val = None
            if var == "n":
                entered.n = val
            elif var == "m":
                entered.m = val
            elif var == "N":
                entered.N = val


def tool_ionenverbindung():
    while True:
        kation = ElementarMolekul.parse(input("Symbol Metall/Kation: "))
        available_ladungen = [k for k in (kation.element.data[IONENLADUNGEN]) if k > 0]
        if len(available_ladungen) == 0:
            print(kation.element.name, "eignet sich nicht als Kation.")
        elif len(available_ladungen) == 1:
            kation.ionenladung = available_ladungen[0]
            break
        else:
            print(kation.element.name, "mehrere Optionen: ", end="")
            for k in available_ladungen:
                print(k, "+" if k > 0 else "-", sep="", end=" ")
            print()
            choice = input("Auswahl: ")
            if choice.isdigit():
                for k in available_ladungen:
                    if abs(int(choice)) == abs(k):
                        kation.ionenladung = k
                        break
            else:
                kation.ionenladung = available_ladungen[0]
            break
    while True:
        anion = ElementarMolekul.parse(input("Symbol Nichtmetall/Anion: "))
        available_ladungen = [k for k in (anion.element.data[IONENLADUNGEN]) if k < 0]
        if len(available_ladungen) == 0:
            print(anion.element.name, "eignet sich nicht als Anion.")
        elif len(available_ladungen) == 1:
            anion.ionenladung = available_ladungen[0]
            break
        else:
            print(anion.element.name, "mehrere Optionen: ", end="")
            for k in available_ladungen:
                print(k, "+" if k > 0 else "-", sep="", end=" ")
            print()
            choice = input("Auswahl: ")
            if choice.isdigit():
                for k in available_ladungen:
                    if abs(int(choice)) == abs(k):
                        anion.ionenladung = k
                        break
            else:
                anion.ionenladung = available_ladungen[0]
            break

    kation_frei_elektron_count = kation.ionenladung * kation.num
    anion_frei_elektron_count = anion.ionenladung * anion.num
    ion_count = kgv([kation_frei_elektron_count, -anion_frei_elektron_count])
    print(kation.element.symbol, format_superscript(kation_frei_elektron_count, show_plus_sign=True, show_sign_at_the_end=True), sep="", end=" + ")
    print(anion.element.symbol, format_superscript(anion_frei_elektron_count, show_plus_sign=True, show_sign_at_the_end=True), sep="", end="")
    print(" (Kation + Anion)")
    kation.num *= int(ion_count / kation_frei_elektron_count)
    anion.num *= int(ion_count / -anion_frei_elektron_count)
    verbindung = Molekul([kation, anion])
    verbindung.reorder_binary_if_needed()
    print("Verbindung:", verbindung)

    ausgang_kation = kation.copy()
    ausgang_anion = anion.copy()
    ausgang_kation.num = 1
    ausgang_anion.num = 2 if anion.element in HNOFClBrI else 1
    unbalanced = Reaction()
    unbalanced.molekule_before = [Molekul([ausgang_kation]), Molekul([ausgang_anion])]
    unbalanced.molekule_after = [verbindung]
    balanced = BalancedReaction.balance(unbalanced)
    print("Herstellung: ", balanced)

    print("Name: ", end="")
    print_binaer_molekul_name(verbindung)


def print_binaer_molekul_name(verbindung):
    em0 = verbindung.elementar_molekuls[0]
    em1 = verbindung.elementar_molekuls[1]

    if em0.num > 1:
        print(GREEK_NUMBERS[em0.num - 1], end="")
    print(em0.element.name.lower(), end="")
    if len(em0.element.data[IONENLADUNGEN]) > 1:
        il = em0.ionenladung if em0.ionenladung is not None else em0.element.data[IONENLADUNGEN][0]
        print("(", format_roman_number(il), ")-", end="", sep="")
    if em1.num > 1:
        print(GREEK_NUMBERS[em1.num - 1], end="")
    if em1.element.symbol == "O":
        print("oxid")
    elif em1.element.symbol == "S":
        print("sulfid")
    elif em1.element.symbol == "H":
        print("hydrid")
    elif em1.element.symbol == "P":
        print("phosphid")
    elif em1.element.symbol == "N":
        print("nitrid")
    else:
        print(em1.element.name.lower() + "id")
        if len(em1.element.data[IONENLADUNGEN]) > 1:
            il = em1.ionenladung if em1.ionenladung is not None else em1.element.data[IONENLADUNGEN][0]
            print("(", format_roman_number(il), ")-", end="", sep="")


def tool_binar_molekul_name():
    while True:
        inp = input("Binäres Molekül: ")
        if not inp.strip():
            print("Tool beendet.")
            return
        mo = Molekul.parse(inp)
        mo.reorder_binary_if_needed()
        print(mo, " ist ", end="")
        print_binaer_molekul_name(mo)


tools = [
    [1, "Element-Info", tool_element_info],
    [2, "Bohrsches Atommodell", tool_bohrsches_atommodell],
    [3, "Delta-EN", tool_delta_en],
    [4, "Organischer Namens-Decoder", tool_organic_name_decoder],
    [5, "Organischer Namens-Encoder", tool_organic_name_encoder],
    [6, "Reaktionsgleichung ausgleichen", tool_ausgleichen],
    [7, "Vollständige Verbrennung", tool_vollstaendig_verbrennung],
    [8, "Stöchiometrie", tool_stochiometrie],
    [9, "Ionenverbindung", tool_ionenverbindung],
    [10, "Name von binärem Molekül", tool_binar_molekul_name],
]

while True:
    for num, name, func in tools:
        print("{:<4} {}".format(num, name))
    choice = input("Toolnummer: ")
    if not choice.strip():
        print("Programm beendet.")
        break
    if choice.isdigit():
        filtered = [t for t in tools if t[0] == int(choice)]
        if filtered:
            filtered[0][2]()
        else:
            print("Ungültige Toolnummer.")
    else:
        print("Ungültige Toolnummer.")
