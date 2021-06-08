PERIODIC_TABLE_HEADS = ["Protonenzahl", "Name", "Symbol", "Relative Atommasse", "Periode", "Gruppe", "Zustand", "Typ", "Atomradius", "Elektronegativität", "Dichte", "Schmelzpunkt (K)", "Siedepunkt (K)", "Isotope", "Elektronenkonfiguration"]
PERIODIC_TABLE_DATA = [
    [1, 'Wasserstoff', 'H', 1.00794, 1, 1, 'gas', 'Nichtmetall', 0.79, 2.2, 8.988e-05, 14.175, 20.28, 3, '1s1'],
    [2, 'Helium', 'He', 4.002602, 1, 18, 'gas', 'Edelgas', 0.49, None, 0.0001785, None, 4.22, 5, '1s2'],
    [3, 'Lithium', 'Li', 6.941, 2, 1, 'solid', 'Alkalimetall', 2.1, 0.98, 0.534, 453.85, 1615, 5, '[He] 2s1'],
    [4, 'Beryllium', 'Be', 9.012182, 2, 2, 'solid', 'Erdalkalimetall', 1.4, 1.57, 1.85, 1560.15, 2742, 6, '[He] 2s2'],
    [5, 'Bor', 'B', 10.811, 2, 13, 'solid', 'Metalloid', 1.2, 2.04, 2.34, 2573.15, 4200, 6, '[He] 2s2 2p1'],
    [6, 'Kohlenstoff', 'C', 12.0107, 2, 14, 'solid', 'Nichtmetall', 0.91, 2.55, 2.267, 3948.15, 4300, 7, '[He] 2s2 2p2'],
    [7, 'Stickstoff', 'N', 14.0067, 2, 15, 'gas', 'Nichtmetall', 0.75, 3.04, 0.0012506, 63.29, 77.36, 8, '[He] 2s2 2p3'],
    [8, 'Sauerstoff', 'O', 15.9994, 2, 16, 'gas', 'Nichtmetall', 0.65, 3.44, 0.001429, 50.5, 90.2, 8, '[He] 2s2 2p4'],
    [9, 'Fluor', 'F', 18.9984032, 2, 17, 'gas', 'Halogen', 0.57, 3.98, 0.001696, 53.63, 85.03, 6, '[He] 2s2 2p5'],
    [10, 'Neon', 'Ne', 20.1797, 2, 18, 'gas', 'Edelgas', 0.51, None, 0.0008999, 24.703, 27.07, 8, '[He] 2s2 2p6'],
    [11, 'Natrium', 'Na', 22.98976928, 3, 1, 'solid', 'Alkalimetall', 2.2, 0.93, 0.971, 371.15, 1156, 7, '[Ne] 3s1'],
    [12, 'Magnesium', 'Mg', 24.305, 3, 2, 'solid', 'Erdalkalimetall', 1.7, 1.31, 1.738, 923.15, 1363, 8, '[Ne] 3s2'],
    [13, 'Aluminum', 'Al', 26.9815386, 3, 13, 'solid', 'Metal', 1.8, 1.61, 2.698, 933.4, 2792, 8, '[Ne] 3s2 3p1'],
    [14, 'Silicium', 'Si', 28.0855, 3, 14, 'solid', 'Metalloid', 1.5, 1.9, 2.3296, 1683.15, 3538, 8, '[Ne] 3s2 3p2'],
    [15, 'Phosphor', 'P', 30.973762, 3, 15, 'solid', 'Nichtmetall', 1.2, 2.19, 1.82, 317.25, 553, 7, '[Ne] 3s2 3p3'],
    [16, 'Schwefel', 'S', 32.065, 3, 16, 'solid', 'Nichtmetall', 1.1, 2.58, 2.067, 388.51, 717.8, 10, '[Ne] 3s2 3p4'],
    [17, 'Chlor', 'Cl', 35.453, 3, 17, 'gas', 'Halogen', 0.97, 3.16, 0.003214, 172.31, 239.11, 11, '[Ne] 3s2 3p5'],
    [18, 'Argon', 'Ar', 39.948, 3, 18, 'gas', 'Edelgas', 0.88, None, 0.0017837, 83.96, 87.3, 8, '[Ne] 3s2 3p6'],
    [19, 'Kalium', 'K', 39.0983, 4, 1, 'solid', 'Alkalimetall', 2.8, 0.82, 0.862, 336.5, 1032, 10, '[Ar] 4s1'],
    [20, 'Calcium', 'Ca', 40.078, 4, 2, 'solid', 'Erdalkalimetall', 2.2, 1, 1.54, 1112.15, 1757, 14, '[Ar] 4s2'],
    [21, 'Scandium', 'Sc', 44.955912, 4, 3, 'solid', 'Übergangsmetall', 2.1, 1.36, 2.989, 1812.15, 3109, 15, '[Ar] 3d1 4s2'],
    [22, 'Titan', 'Ti', 47.867, 4, 4, 'solid', 'Übergangsmetall', 2, 1.54, 4.54, 1933.15, 3560, 9, '[Ar] 3d2 4s2'],
    [23, 'Vanadium', 'V', 50.9415, 4, 5, 'solid', 'Übergangsmetall', 1.9, 1.63, 6.11, 2175.15, 3680, 9, '[Ar] 3d3 4s2'],
    [24, 'Chrom', 'Cr', 51.9961, 4, 6, 'solid', 'Übergangsmetall', 1.9, 1.66, 7.15, 2130.15, 2944, 9, '[Ar] 3d5 4s1'],
    [25, 'Mangan', 'Mn', 54.938045, 4, 7, 'solid', 'Übergangsmetall', 1.8, 1.55, 7.44, 1519.15, 2334, 11, '[Ar] 3d5 4s2'],
    [26, 'Eisen', 'Fe', 55.845, 4, 8, 'solid', 'Übergangsmetall', 1.7, 1.83, 7.874, 1808.15, 3134, 10, '[Ar] 3d6 4s2'],
    [27, 'Cobalt', 'Co', 58.933195, 4, 9, 'solid', 'Übergangsmetall', 1.7, 1.88, 8.86, 1768.15, 3200, 14, '[Ar] 3d7 4s2'],
    [28, 'Nickel', 'Ni', 58.6934, 4, 10, 'solid', 'Übergangsmetall', 1.6, 1.91, 8.912, 1726.15, 3186, 11, '[Ar] 3d8 4s2'],
    [29, 'Copper', 'Cu', 63.546, 4, 11, 'solid', 'Übergangsmetall', 1.6, 1.9, 8.96, 1357.75, 2835, 11, '[Ar] 3d10 4s1'],
    [30, 'Zink', 'Zn', 65.38, 4, 12, 'solid', 'Übergangsmetall', 1.5, 1.65, 7.134, 692.88, 1180, 15, '[Ar] 3d10 4s2'],
    [31, 'Gallium', 'Ga', 69.723, 4, 13, 'solid', 'Metal', 1.8, 1.81, 5.907, 302.91, 2477, 14, '[Ar] 3d10 4s2 4p1'],
    [32, 'Germanium', 'Ge', 72.64, 4, 14, 'solid', 'Metalloid', 1.5, 2.01, 5.323, 1211.45, 3106, 17, '[Ar] 3d10 4s2 4p2'],
    [33, 'Arsen', 'As', 74.9216, 4, 15, 'solid', 'Metalloid', 1.3, 2.18, 5.776, 1090.15, 887, 14, '[Ar] 3d10 4s2 4p3'],
    [34, 'Selen', 'Se', 78.96, 4, 16, 'solid', 'Nichtmetall', 1.2, 2.55, 4.809, 494.15, 958, 20, '[Ar] 3d10 4s2 4p4'],
    [35, 'Brom', 'Br', 79.904, 4, 17, 'liq', 'Halogen', 1.1, 2.96, 3.122, 266.05, 332, 19, '[Ar] 3d10 4s2 4p5'],
    [36, 'Krypton', 'Kr', 83.798, 4, 18, 'gas', 'Edelgas', 1, None, 0.003733, 115.93, 119.93, 23, '[Ar] 3d10 4s2 4p6'],
    [37, 'Rubidium', 'Rb', 85.4678, 5, 1, 'solid', 'Alkalimetall', 3, 0.82, 1.532, 312.79, 961, 20, '[Kr] 5s1'],
    [38, 'Strontium', 'Sr', 87.62, 5, 2, 'solid', 'Erdalkalimetall', 2.5, 0.95, 2.64, 1042.15, 1655, 18, '[Kr] 5s2'],
    [39, 'Yttrium', 'Y', 88.90585, 5, 3, 'solid', 'Übergangsmetall', 2.3, 1.22, 4.469, 1799.15, 3609, 21, '[Kr] 4d1 5s2'],
    [40, 'Zirconium', 'Zr', 91.224, 5, 4, 'solid', 'Übergangsmetall', 2.2, 1.33, 6.506, 2125.15, 4682, 20, '[Kr] 4d2 5s2'],
    [41, 'Niob', 'Nb', 92.90638, 5, 5, 'solid', 'Übergangsmetall', 2.1, 1.6, 8.57, 2741.15, 5017, 24, '[Kr] 4d4 5s1'],
    [42, 'Molybdän', 'Mo', 95.96, 5, 6, 'solid', 'Übergangsmetall', 2, 2.16, 10.22, 2890.15, 4912, 20, '[Kr] 4d5 5s1'],
    [43, 'Technetium', 'Tc', 98, 5, 7, 'künstlich', 'Übergangsmetall', 2, 1.9, 11.5, 2473.15, 5150, 23, '[Kr] 4d5 5s2'],
    [44, 'Ruthenium', 'Ru', 101.07, 5, 8, 'solid', 'Übergangsmetall', 1.9, 2.2, 12.37, 2523.15, 4423, 16, '[Kr] 4d7 5s1'],
    [45, 'Rhodium', 'Rh', 102.9055, 5, 9, 'solid', 'Übergangsmetall', 1.8, 2.28, 12.41, 2239.15, 3968, 20, '[Kr] 4d8 5s1'],
    [46, 'Palladium', 'Pd', 106.42, 5, 10, 'solid', 'Übergangsmetall', 1.8, 2.2, 12.02, 1825.15, 3236, 21, '[Kr] 4d10'],
    [47, 'Silber', 'Ag', 107.8682, 5, 11, 'solid', 'Übergangsmetall', 1.8, 1.93, 10.501, 1234.15, 2435, 27, '[Kr] 4d10 5s1'],
    [48, 'Cadmium', 'Cd', 112.411, 5, 12, 'solid', 'Übergangsmetall', 1.7, 1.69, 8.69, 594.33, 1040, 22, '[Kr] 4d10 5s2'],
    [49, 'Indium', 'In', 114.818, 5, 13, 'solid', 'Metall', 2, 1.78, 7.31, 429.91, 2345, 34, '[Kr] 4d10 5s2 5p1'],
    [50, 'Zinn', 'Sn', 118.71, 5, 14, 'solid', 'Metall', 1.7, 1.96, 7.287, 505.21, 2875, 28, '[Kr] 4d10 5s2 5p2'],
    [51, 'Antimon', 'Sb', 121.76, 5, 15, 'solid', 'Metalloid', 1.5, 2.05, 6.685, 904.05, 1860, 29, '[Kr] 4d10 5s2 5p3'],
    [52, 'Tellur', 'Te', 127.6, 5, 16, 'solid', 'Metalloid', 1.4, 2.1, 6.232, 722.8, 1261, 29, '[Kr] 4d10 5s2 5p4'],
    [53, 'Iod', 'I', 126.90447, 5, 17, 'solid', 'Halogen', 1.3, 2.66, 4.93, 386.65, 457.4, 24, '[Kr] 4d10 5s2 5p5'],
    [54, 'Xenon', 'Xe', 131.293, 5, 18, 'gas', 'Edelgas', 1.2, None, 0.005887, 161.45, 165.03, 31, '[Kr] 4d10 5s2 5p6'],
    [55, 'Cäsium', 'Cs', 132.9054519, 6, 1, 'solid', 'Alkalimetall', 3.3, 0.79, 1.873, 301.7, 944, 22, '[Xe] 6s1'],
    [56, 'Barium', 'Ba', 137.327, 6, 2, 'solid', 'Erdalkalimetall', 2.8, 0.89, 3.594, 1002.15, 2170, 25, '[Xe] 6s2'],
    [57, 'Lanthan', 'La', 138.90547, 6, 3, 'solid', 'Lanthanide', 2.7, 1.1, 6.145, 1193.15, 3737, 19, '[Xe] 5d1 6s2'],
    [58, 'Cer', 'Ce', 140.116, 6, 19, 'solid', 'Lanthanide', 2.7, 1.12, 6.77, 1071.15, 3716, 19, '[Xe] 4f1 5d1 6s2'],
    [59, 'Praseodym', 'Pr', 140.90765, 6, 20, 'solid', 'Lanthanide', 2.7, 1.13, 6.773, 1204.15, 3793, 15, '[Xe] 4f3 6s2'],
    [60, 'Neodym', 'Nd', 144.242, 6, 21, 'solid', 'Lanthanide', 2.6, 1.14, 7.007, 1289.15, 3347, 16, '[Xe] 4f4 6s2'],
    [61, 'Promethium', 'Pm', 145, 6, 22, 'künstlich', 'Lanthanide', 2.6, 1.13, 7.26, 1204.15, 3273, 14, '[Xe] 4f5 6s2'],
    [62, 'Samarium', 'Sm', 150.36, 6, 23, 'solid', 'Lanthanide', 2.6, 1.17, 7.52, 1345.15, 2067, 17, '[Xe] 4f6 6s2'],
    [63, 'Europium', 'Eu', 151.964, 6, 24, 'solid', 'Lanthanide', 2.6, 1.2, 5.243, 1095.15, 1802, 21, '[Xe] 4f7 6s2'],
    [64, 'Gadolinium', 'Gd', 157.25, 6, 25, 'solid', 'Lanthanide', 2.5, 1.2, 7.895, 1585.15, 3546, 17, '[Xe] 4f7 5d1 6s2'],
    [65, 'Terbium', 'Tb', 158.92535, 6, 26, 'solid', 'Lanthanide', 2.5, 1.2, 8.229, 1630.15, 3503, 24, '[Xe] 4f9 6s2'],
    [66, 'Dysprosium', 'Dy', 162.5, 6, 27, 'solid', 'Lanthanide', 2.5, 1.22, 8.55, 1680.15, 2840, 21, '[Xe] 4f10 6s2'],
    [67, 'Holmium', 'Ho', 164.93032, 6, 28, 'solid', 'Lanthanide', 2.5, 1.23, 8.795, 1743.15, 2993, 29, '[Xe] 4f11 6s2'],
    [68, 'Erbium', 'Er', 167.259, 6, 29, 'solid', 'Lanthanide', 2.5, 1.24, 9.066, 1795.15, 3503, 16, '[Xe] 4f12 6s2'],
    [69, 'Thulium', 'Tm', 168.93421, 6, 30, 'solid', 'Lanthanide', 2.4, 1.25, 9.321, 1818.15, 2223, 18, '[Xe] 4f13 6s2'],
    [70, 'Ytterbium', 'Yb', 173.054, 6, 31, 'solid', 'Lanthanide', 2.4, 1.1, 6.965, 1097.15, 1469, 16, '[Xe] 4f14 6s2'],
    [71, 'Lutetium', 'Lu', 174.9668, 6, 32, 'solid', 'Lanthanide', 2.3, 1.27, 9.84, 1936.15, 3675, 22, '[Xe] 4f14 5d1 6s2'],
    [72, 'Hafnium', 'Hf', 178.49, 6, 4, 'solid', 'Übergangsmetall', 2.2, 1.3, 13.31, 2500.15, 4876, 17, '[Xe] 4f14 5d2 6s2'],
    [73, 'Tantal', 'Ta', 180.94788, 6, 5, 'solid', 'Übergangsmetall', 2.1, 1.5, 16.654, 3269.15, 5731, 19, '[Xe] 4f14 5d3 6s2'],
    [74, 'Wolfram', 'W', 183.84, 6, 6, 'solid', 'Übergangsmetall', 2, 2.36, 19.25, 3680.15, 5828, 22, '[Xe] 4f14 5d4 6s2'],
    [75, 'Rhenium', 'Re', 186.207, 6, 7, 'solid', 'Übergangsmetall', 2, 1.9, 21.02, 3453.15, 5869, 21, '[Xe] 4f14 5d5 6s2'],
    [76, 'Osmium', 'Os', 190.23, 6, 8, 'solid', 'Übergangsmetall', 1.9, 2.2, 22.61, 3300.15, 5285, 19, '[Xe] 4f14 5d6 6s2'],
    [77, 'Iridium', 'Ir', 192.217, 6, 9, 'solid', 'Übergangsmetall', 1.9, 2.2, 22.56, 2716.15, 4701, 25, '[Xe] 4f14 5d7 6s2'],
    [78, 'Platin', 'Pt', 195.084, 6, 10, 'solid', 'Übergangsmetall', 1.8, 2.28, 21.46, 2045.15, 4098, 32, '[Xe] 4f14 5d9 6s1'],
    [79, 'Gold', 'Au', 196.966569, 6, 11, 'solid', 'Übergangsmetall', 1.8, 2.54, 19.282, 1337.73, 3129, 21, '[Xe] 4f14 5d10 6s1'],
    [80, 'Quecksilber', 'Hg', 200.59, 6, 12, 'liq', 'Übergangsmetall', 1.8, 2, 13.5336, 234.43, 630, 26, '[Xe] 4f14 5d10 6s2'],
    [81, 'Thallium', 'Tl', 204.3833, 6, 13, 'solid', 'Metall', 2.1, 2.04, 11.85, 577.15, 1746, 28, '[Xe] 4f14 5d10 6s2 6p1'],
    [82, 'Blei', 'Pb', 207.2, 6, 14, 'solid', 'Metall', 1.8, 2.33, 11.342, 600.75, 2022, 29, '[Xe] 4f14 5d10 6s2 6p2'],
    [83, 'Bismut', 'Bi', 208.9804, 6, 15, 'solid', 'Metall', 1.6, 2.02, 9.807, 544.67, 1837, 19, '[Xe] 4f14 5d10 6s2 6p3'],
    [84, 'Polonium', 'Po', 210, 6, 16, 'solid', 'Metalloid', 1.5, 2, 9.32, 527.15, 1235, 34, '[Xe] 4f14 5d10 6s2 6p4'],
    [85, 'Astat', 'At', 210, 6, 17, 'solid', 'Edelgas', 1.4, 2.2, 7, 575.15, 610, 21, '[Xe] 4f14 5d10 6s2 6p5'],
    [86, 'Radon', 'Rn', 222, 6, 18, 'gas', 'Alkalimetall', 1.3, None, 0.00973, 202.15, 211.3, 20, '[Xe] 4f14 5d10 6s2 6p6'],
    [87, 'Francium', 'Fr', 223, 7, 1, 'solid', 'Erdalkalimetall', None, 0.7, 1.87, 300.15, 950, 21, '[Rn] 7s1'],
    [88, 'Radium', 'Ra', 226, 7, 2, 'solid', 'Actinoid', None, 0.9, 5.5, 973.15, 2010, 15, '[Rn] 7s2'],
    [89, 'Actinium', 'Ac', 227, 7, 3, 'solid', 'Actinoid', None, 1.1, 10.07, 1323.15, 3471, 11, '[Rn] 6d1 7s2'],
    [90, 'Thorium', 'Th', 232.03806, 7, 19, 'solid', 'Actinoid', None, 1.3, 11.72, 2028.15, 5061, 12, '[Rn] 6d2 7s2'],
    [91, 'Protactinium', 'Pa', 231.03588, 7, 20, 'solid', 'Actinoid', None, 1.5, 15.37, 1873.15, 4300, 14, '[Rn] 5f2 6d1 7s2'],
    [92, 'Uran', 'U', 238.02891, 7, 21, 'solid', 'Actinoid', None, 1.38, 18.95, 1405.15, 4404, 15, '[Rn] 5f3 6d1 7s2'],
    [93, 'Neptunium', 'Np', 237, 7, 22, 'künstlich', 'Actinoid', None, 1.36, 20.45, 913.15, 4273, 153, '[Rn] 5f4 6d1 7s2'],
    [94, 'Plutonium', 'Pu', 244, 7, 23, 'künstlich', 'Actinoid', None, 1.28, 19.84, 913.15, 3501, 163, '[Rn] 5f6 7s2'],
    [95, 'Americium', 'Am', 243, 7, 24, 'künstlich', 'Actinoid', None, 1.3, 13.69, 1267.15, 2880, 133, '[Rn] 5f7 7s2'],
    [96, 'Curium', 'Cm', 247, 7, 25, 'künstlich', 'Actinoid', None, 1.3, 13.51, 1340.15, 3383, 133, None],
    [97, 'Berkelium', 'Bk', 247, 7, 26, 'künstlich', 'Actinoid', None, 1.3, 14.79, 1259.15, 983, 83, None],
    [98, 'Californium', 'Cf', 251, 7, 27, 'künstlich', 'Actinoid', None, 1.3, 15.1, 1925.15, 1173, 123, None],
    [99, 'Einsteinium', 'Es', 252, 7, 28, 'künstlich', 'Actinoid', None, 1.3, 13.5, 1133.15, None, 123, None],
    [100, 'Fermium', 'Fm', 257, 7, 29, 'künstlich', 'Actinoid', None, 1.3, None, None, None, 103, None],
    [101, 'Mendelevium', 'Md', 258, 7, 30, 'künstlich', 'Actinoid', None, 1.3, None, None, None, 33, None],
    [102, 'Nobelium', 'No', 259, 7, 31, 'künstlich', 'Actinoid', None, 1.3, None, None, None, 73, None],
    [103, 'Lawrencium', 'Lr', 262, 7, 32, 'künstlich', 'Actinoid', None, None, None, None, None, 203, None],
    [104, 'Rutherfordium', 'Rf', 261, 7, 4, 'künstlich', 'Lanthanoid', None, None, 18.1, None, None, None, None],
    [105, 'Dubnium', 'Db', 262, 7, 5, 'künstlich', 'Lanthanoid', None, None, 39, None, None, None, None],
    [106, 'Seaborgium', 'Sg', 266, 7, 6, 'künstlich', 'Lanthanoid', None, None, 35, None, None, None, None],
    [107, 'Bohrium', 'Bh', 264, 7, 7, 'künstlich', 'Lanthanoid', None, None, 37, None, None, None, None],
    [108, 'Hassium', 'Hs', 267, 7, 8, 'künstlich', 'Lanthanoid', None, None, 41, None, None, None, None],
    [109, 'Meitnerium', 'Mt', 268, 7, 9, 'künstlich', 'Lanthanoid', None, None, 35, None, None, None, None],
    [110, 'Darmstadtium', 'Ds', 271, 7, 10, 'künstlich', 'Lanthanoid', None, None, None, None, None, None, None],
    [111, 'Roentgenium', 'Rg', 272, 7, 11, 'künstlich', 'Lanthanoid', None, None, None, None, None, None, None],
    [112, 'Copernicium', 'Cn', 285, 7, 12, 'künstlich', 'Lanthanoid', None, None, None, None, None, None, None],
    [113, 'Ununtrium', 'Uut', 284, 7, 13, 'künstlich', None, None, None, None, None, None, None, None],
    [114, 'Ununquadium', 'Uuq', 289, 7, 14, 'künstlich', 'Lanthanoid', None, None, None, None, None, None, None],
    [115, 'Ununpentium', 'Uup', 288, 7, 15, 'künstlich', None, None, None, None, None, None, None, None],
    [116, 'Ununhexium', 'Uuh', 292, 7, 16, 'künstlich', 'Lanthanoid', None, None, None, None, None, None, None],
    [117, 'Ununseptium', 'Uus', 295, 7, 17, 'künstlich', None, None, None, None, None, None, None, None],
    [118, 'Ununoctium', 'Uuo', 294, 7, 18, 'künstlich', 'Edelgas', None, None, None, None, None, None, None],
]


class Element:
    protonen = 0
    name = ""
    symbol = ""

    data = {}


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


def tool_element_info():
    while True:
        inp = input("Symbol oder Name eingeben: ")
        el = get_best(lambda elem: max(-levenshtein_distance(elem.name, inp), -levenshtein_distance(elem.symbol, inp)), ELEMENTS)
        for h in PERIODIC_TABLE_HEADS:
            print(h.ljust(LONGEST_ELEMENT_DATA_HEADER), el.data[h])


if __name__ == '__main__':
    tools = {
        1: ["Element-Info", tool_element_info]
    }
    while True:
        for key, tool_info in tools.items():
            print(str(key).ljust(4), tool_info[0])
        choice = input("Toolnummer: ")
        if choice.isdigit() and int(choice) in tools:
            tools[int(choice)][1]()
        else:
            print("Ungültige Toolnummer.")
