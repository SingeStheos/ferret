import math
import tkinter as tk

# Window dimensions and settings
WIDTH = 600
HEIGHT = WIDTH
PIXEL_SIZE = 1
FOV = 30
VIEWER_DISTANCE = 1500

# Default face color
DEFAULT_COLOR = "#FF5733"

# OBJ and MTL data as strings (paste your model data here)
OBJ_DATA = """
mtllib Ferret_1505.mtl
o Ferret_1505
v 8 8 -15
v 10 17 -18
v 6 8 -9
v 4 6 -13
v 8 3 -21
v 12 8 -22
v 11 8 -25
v 9 19 -29
v 8 18 -11
v 6 12 17
v 3 7 16
v -6 8 -9
v -4 6 -13
v 0 6 -29
v 6 7 -28
v 7 6 -25
v 8 2 -23
v 11 2 -22
v 12 2 -24
v 9 2 -26
v 9 15 -32
v 6 21 -31
v 5 25 -23
v 4 22 -8
v 6 17 20
v 11 10 20
v 10 6 20
v 5 5 22
v 3 8 30
v -3 7 16
v -6 12 17
v -8 18 -11
v -10 17 -18
v -8 8 -15
v -8 3 -21
v -7 6 -25
v -6 7 -28
v -8 15 -32
v -5 12 -36
v 0 8 -34
v 5 12 -36
v 8 0 -26
v 7 0 -20
v 10 3 -17
v 13 0 -24
v 9 0 -18
v 8 0 -15
v 11 0 -15
v 13 0 -19
v 9 9 24
v 6 16 28
v 8 3 25
v 9 1 23
v 3 21 27
v 7 18 32
v 2 12 34
v 0 10 35
v -3 8 30
v -5 5 22
v -9 6 20
v -11 10 20
v -6 17 20
v -4 22 -8
v -5 25 -23
v -6 21 -31
v -8 19 -29
v -11 8 -25
v -12 8 -22
v -8 2 -23
v -9 2 -26
v 6 2 23
v 7 1 21
v 7 0 21
v 5 0 25
v 8 2 27
v 11 0 24
v 8 0 27
v 6 0 27
v 8 0 29
v 10 0 26
v -5 0 25
v -7 0 21
v -6 2 23
v -7 3 25
v -8 2 27
v -6 0 27
v -8 0 27
v -11 0 24
v -7 1 21
v -9 9 24
v -9 1 23
v -10 0 26
v -8 0 29
v -6 16 28
v -3 21 27
v -3 20 17
v 3 20 17
v 3 22 -33
v -3 22 -33
v -12 2 -24
v -11 2 -22
v -7 0 -20
v -8 0 -26
v -13 0 -24
v 0 22 31
v 5 20 36
v 4 20 43
v 6 19 39
v 6 12 38
v 0 10 45
v -6 12 38
v -2 12 34
v -7 18 32
v -5 20 36
v 0 23 36
v 6 25 37
v 6 22 36
v 6 23 38
v 4 21 37
v 2 19 44
v 4 19 43
v 5 19 42
v 5 17 43
v 4 13 45
v 2 12 47
v 0 12 48
v -2 12 47
v -4 13 45
v -5 17 43
v -5 19 42
v -6 19 39
v -10 0 -18
v -8 0 -15
v -11 0 -15
v -13 0 -19
v -9 3 -17
v 0 12 49
v -2 13 48
v -3 16 48
v -4 17 44
v -4 19 43
v -4 20 43
v -3 21 37
v -4 23 38
v -6 22 36
v -5 25 37
v 0 22 41
v -2 19 44
v -2 17 48
v 0 20 47
v -2 16 51
v 0 13 51
v 0 15 52
v 0 17 52
v 2 17 48
v 3 16 48
v 4 17 44
v 2 16 51
v 2 13 48
v -2 17 -37
v -3 12 -43
v -3 9 -43
v 0 6 -42
v 3 9 -43
v 3 12 -43
v 2 17 -37
v -2 10 -50
v -3 8 -50
v 0 5 -50
v 3 8 -50
v 2 10 -50
v -2 11 -57
v -3 9 -58
v 0 6 -58
v 3 9 -58
v 2 11 -57
v 0 12 -61
v -2 10 -62
v 0 9 -63
v 2 10 -62
v 2 12 -61
v 2 16 -27
v 0 16 -23
v -2 16 -27
vn 941 549 -497
vn 1362 -253 -212
vn 1088 951 -331
vn -12 1720 -315
vn 78 630 -291
vn 1247 201 -516
vn 1177 -58 872
vn 983 -600 169
vn 1678 -743 -188
vn 1124 141 590
vn 159 1334 282
vn -1088 1441 -438
vn 12 1489 -200
vn -17 1787 667
vn 169 735 368
vn -577 751 687
vn -892 -123 -286
vn -199 -671 -345
vn 838 -423 434
vn -86 -72 1101
vn 1065 364 939
vn 964 -810 622
vn 566 -1202 27
vn 552 -1035 -154
vn 1385 -924 109
vn 1241 -115 102
vn 117 340 685
vn -472 635 -200
vn 733 1433 -717
vn -174 1350 247
vn -1127 177 582
vn -1702 -730 -170
vn -1338 -287 -183
vn -941 549 -497
vn -78 630 -291
vn 564 722 688
vn -185 706 367
vn -1155 338 891
vn -1663 372 688
vn 0 790 70
vn 1611 372 725
vn -373 134 371
vn -643 102 -68
vn 113 -1216 -269
vn 668 445 424
vn 0 1280 0
vn -202 198 -270
vn 204 223 -332
vn 386 194 -102
vn 850 159 -843
vn 1297 -302 -214
vn -216 -468 -735
vn 1182 -361 82
vn 753 -1156 161
vn 1580 -594 74
vn 633 563 -34
vn 0 1320 -140
vn -532 1035 -674
vn 521 650 -106
vn -222 513 1017
vn -1360 7 456
vn -1385 -924 109
vn -552 -1543 -224
vn -566 -1198 151
vn -1073 -741 583
vn -1029 -592 194
vn -1164 -95 915
vn -1247 201 -516
vn 892 -123 -286
vn 86 -72 1101
vn -1153 -162 345
vn 164 -135 594
vn -359 256 460
vn -766 258 -127
vn 270 -1106 -587
vn 655 215 297
vn 0 1280 0
vn -340 172 -255
vn 22 214 -298
vn 396 231 -230
vn 837 324 -153
vn 359 256 460
vn 1256 -71 450
vn 443 -495 -689
vn -184 -1171 -620
vn 340 172 -255
vn 0 1280 0
vn -655 215 297
vn -277 -7 937
vn -783 141 -884
vn -1064 -460 57
vn -396 231 -230
vn -22 214 -298
vn -1486 -180 -369
vn -753 -1412 186
vn -361 -878 0
vn 361 -1390 5
vn 475 -1034 780
vn -475 -951 911
vn -738 -288 448
vn 292 -529 -274
vn 688 165 -48
vn 373 134 371
vn -625 430 395
vn 0 -1586 166
vn 836 -608 273
vn 1027 -982 -669
vn 832 -410 -178
vn 1659 1010 -96
vn 0 1340 -420
vn -1659 1010 -96
vn -878 675 -25
vn -1356 -632 183
vn -750 -690 82
vn 23 -1157 -397
vn 40 -239 293
vn 342 43 192
vn 405 214 -743
vn 318 -639 -671
vn 851 -1067 -872
vn 852 -298 -1108
vn 1182 -261 -626
vn 1387 -357 -759
vn 783 152 -579
vn 381 97 -411
vn 0 182 -292
vn -381 -143 -531
vn -783 408 -451
vn -1387 -357 -759
vn -1182 -261 -626
vn -832 -410 -178
vn 0 1280 0
vn 240 247 -278
vn -170 189 -315
vn -323 138 -85
vn 95 -1074 -218
vn 0 1072 -344
vn -1213 683 -643
vn -943 -453 -399
vn -723 -809 -681
vn -852 -298 -1108
vn -963 -1050 -674
vn -276 -679 -677
vn -188 141 -1082
vn -250 34 -139
vn -8 -255 126
vn -50 -1202 -386
vn -877 -1061 -866
vn -1066 -1068 -481
vn 0 -994 -468
vn -1067 -96 -810
vn 0 868 -868
vn 0 204 -920
vn 0 -758 -850
vn 1066 -1068 -481
vn 943 -453 -399
vn 723 -809 -681
vn 1067 -96 -810
vn 1213 683 -643
vn -411 -764 752
vn -730 -568 408
vn -1309 424 55
vn 0 1094 -184
vn 1309 424 55
vn 730 -1013 643
vn 411 -725 788
vn -974 -1104 127
vn -1023 306 20
vn 0 1090 -52
vn 1023 306 20
vn 974 -1110 20
vn -647 -1204 -88
vn -1060 -10 101
vn 0 1424 476
vn 1060 -10 101
vn 726 -1008 -155
vn -213 -1000 349
vn -759 -118 477
vn 28 -56 912
vn 866 96 475
vn 320 -530 411
vn 0 256 0
vn 0 256 0
vn 0 256 0
usemtl m0
f 1 2 3

usemtl m0
f 1 3 4

usemtl m1
f 1 4 5

usemtl m1
f 1 5 6

usemtl m1
f 1 6 2

usemtl m1
f 2 6 7

usemtl m1
f 2 7 8

usemtl m0
f 2 8 9

usemtl m0
f 2 9 3

usemtl m0
f 3 9 10

usemtl m0
f 3 10 11

usemtl m0
f 3 11 12

usemtl m0
f 3 12 4

usemtl m0
f 4 12 13

usemtl m0
f 4 13 14

usemtl m0
f 4 14 15

usemtl m1
f 4 15 16

usemtl m1
f 4 16 5

usemtl m2
f 5 16 17

usemtl m2
f 5 17 6

usemtl m2
f 6 17 18

usemtl m2
f 6 18 19

usemtl m2
f 6 19 7

usemtl m2
f 7 19 20

usemtl m2
f 7 20 16

usemtl m1
f 7 16 21

usemtl m1
f 7 21 8

usemtl m0
f 8 21 22

usemtl m0
f 8 22 9

usemtl m0
f 9 22 23

usemtl m0
f 9 23 24

usemtl m0
f 9 24 25

usemtl m0
f 9 25 10

usemtl m1
f 10 25 26

usemtl m1
f 10 26 27

usemtl m1
f 10 27 11

usemtl m1
f 11 27 28

usemtl m1
f 11 28 29

usemtl m0
f 11 29 30

usemtl m0
f 11 30 12

usemtl m0
f 12 30 31

usemtl m0
f 12 31 32

usemtl m0
f 12 32 33

usemtl m0
f 12 33 34

usemtl m0
f 12 34 13

usemtl m1
f 13 34 35

usemtl m1
f 13 35 36

usemtl m1
f 13 36 37

usemtl m0
f 13 37 14

usemtl m0
f 14 37 38

usemtl m0
f 14 38 39

usemtl m0
f 14 39 40

usemtl m0
f 14 40 41

usemtl m0
f 14 41 21

usemtl m0
f 14 21 15

usemtl m1
f 15 21 16

usemtl m2
f 20 17 16

usemtl m2
f 17 20 42

usemtl m2
f 17 42 43

usemtl m2
f 17 43 18

usemtl m2
f 18 43 44

usemtl m2
f 18 44 19

usemtl m2
f 19 44 45

usemtl m2
f 19 45 20

usemtl m2
f 20 45 42

usemtl m2
f 42 45 43

usemtl m2
f 43 45 46

usemtl m2
f 43 46 47

usemtl m2
f 43 47 44

usemtl m2
f 44 47 48

usemtl m2
f 44 48 49

usemtl m2
f 44 49 45

usemtl m2
f 45 49 46

usemtl m2
f 46 49 48

usemtl m2
f 46 48 47

usemtl m1
f 50 51 29

usemtl m1
f 50 29 28

usemtl m2
f 50 28 52

usemtl m2
f 50 52 53

usemtl m2
f 50 53 26

usemtl m1
f 50 26 51

usemtl m1
f 51 26 25

usemtl m0
f 51 25 54

usemtl m0
f 51 54 55

usemtl m0
f 51 55 29

usemtl m0
f 29 55 56

usemtl m0
f 29 56 57

usemtl m0
f 29 57 58

usemtl m0
f 29 58 30

usemtl m1
f 30 58 59

usemtl m1
f 30 59 60

usemtl m1
f 30 60 31

usemtl m1
f 31 60 61

usemtl m1
f 31 61 62

usemtl m0
f 31 62 32

usemtl m0
f 32 62 63

usemtl m0
f 32 63 64

usemtl m0
f 32 64 65

usemtl m0
f 32 65 66

usemtl m0
f 32 66 33

usemtl m1
f 33 66 67

usemtl m1
f 33 67 68

usemtl m1
f 33 68 34

usemtl m1
f 34 68 35

usemtl m2
f 35 68 69

usemtl m2
f 35 69 36

usemtl m2
f 36 69 70

usemtl m2
f 36 70 67

usemtl m1
f 36 67 38

usemtl m1
f 36 38 37

usemtl m2
f 71 52 28

usemtl m2
f 71 28 27

usemtl m2
f 71 27 72

usemtl m2
f 71 72 73

usemtl m2
f 71 73 74

usemtl m2
f 71 74 52

usemtl m2
f 52 74 75

usemtl m2
f 52 75 53

usemtl m2
f 53 75 76

usemtl m2
f 53 76 72

usemtl m2
f 53 72 26

usemtl m2
f 26 72 27

usemtl m2
f 72 76 73

usemtl m2
f 73 76 74

usemtl m2
f 74 76 77

usemtl m2
f 74 77 78

usemtl m2
f 74 78 75

usemtl m2
f 75 78 79

usemtl m2
f 75 79 80

usemtl m2
f 75 80 76

usemtl m2
f 76 80 77

usemtl m2
f 77 80 79

usemtl m2
f 77 79 78

usemtl m2
f 81 82 83

usemtl m2
f 81 83 84

usemtl m2
f 81 84 85

usemtl m2
f 81 85 86

usemtl m2
f 81 86 87

usemtl m2
f 81 87 88

usemtl m2
f 81 88 82

usemtl m2
f 82 88 89

usemtl m2
f 82 89 83

usemtl m2
f 83 89 60

usemtl m2
f 83 60 59

usemtl m2
f 83 59 84

usemtl m2
f 84 59 90

usemtl m2
f 84 90 91

usemtl m2
f 84 91 85

usemtl m2
f 85 91 88

usemtl m2
f 85 88 92

usemtl m2
f 85 92 93

usemtl m2
f 85 93 86

usemtl m2
f 86 93 87

usemtl m2
f 87 93 92

usemtl m2
f 87 92 88

usemtl m2
f 88 91 89

usemtl m2
f 89 91 61

usemtl m2
f 89 61 60

usemtl m1
f 58 94 90

usemtl m1
f 58 90 59

usemtl m1
f 62 61 94

usemtl m0
f 62 94 95

usemtl m0
f 62 95 96

usemtl m0
f 62 96 63

usemtl m0
f 63 96 97

usemtl m0
f 63 97 24

usemtl m0
f 63 24 23

usemtl m0
f 63 23 64

usemtl m0
f 64 23 98

usemtl m0
f 64 98 99

usemtl m0
f 64 99 65

usemtl m0
f 65 99 39

usemtl m0
f 65 39 38

usemtl m0
f 65 38 66

usemtl m1
f 66 38 67

usemtl m1
f 61 90 94

usemtl m2
f 90 61 91

usemtl m2
f 68 100 101

usemtl m2
f 68 101 69

usemtl m2
f 69 101 102

usemtl m2
f 69 102 103

usemtl m2
f 69 103 70

usemtl m2
f 70 103 104

usemtl m2
f 70 104 100

usemtl m2
f 70 100 67

usemtl m2
f 67 100 68

usemtl m0
f 24 97 25

usemtl m0
f 25 97 54

usemtl m0
f 54 97 95

usemtl m0
f 54 95 105

usemtl m0
f 54 105 55

usemtl m0
f 55 105 106

usemtl m3
f 55 106 107

usemtl m3
f 55 107 108

usemtl m3
f 55 108 109

usemtl m3
f 55 109 56

usemtl m3
f 56 109 57

usemtl m3
f 57 109 110

usemtl m3
f 57 110 111

usemtl m3
f 57 111 112

usemtl m0
f 57 112 58

usemtl m0
f 58 112 94

usemtl m0
f 94 112 113

usemtl m0
f 94 113 95

usemtl m0
f 95 113 105

usemtl m0
f 105 113 114

usemtl m0
f 105 114 115

usemtl m0
f 105 115 106

usemtl m0
f 106 115 116

usemtl m0
f 106 116 117

usemtl m4
f 106 117 118

usemtl m0
f 106 118 119

usemtl m3
f 106 119 107

usemtl m3
f 107 119 120

usemtl m5
f 107 120 121

usemtl m5
f 107 121 122

usemtl m1
f 107 122 108

usemtl m1
f 108 122 109

usemtl m1
f 109 122 123

usemtl m3
f 109 123 124

usemtl m3
f 109 124 125

usemtl m3
f 109 125 110

usemtl m3
f 110 125 126

usemtl m3
f 110 126 127

usemtl m3
f 110 127 111

usemtl m3
f 111 127 128

usemtl m3
f 111 128 129

usemtl m1
f 111 129 130

usemtl m1
f 111 130 131

usemtl m3
f 111 131 113

usemtl m3
f 111 113 112

usemtl m2
f 132 104 102

usemtl m2
f 132 102 133

usemtl m2
f 132 133 134

usemtl m2
f 132 134 135

usemtl m2
f 132 135 104

usemtl m2
f 104 135 136

usemtl m2
f 104 136 100

usemtl m2
f 100 136 101

usemtl m2
f 101 136 102

usemtl m2
f 102 136 133

usemtl m2
f 133 136 134

usemtl m2
f 134 136 135

usemtl m2
f 104 103 102

usemtl m3
f 126 125 127

usemtl m3
f 127 125 124

usemtl m3
f 127 124 128

usemtl m3
f 128 124 137

usemtl m3
f 128 137 138

usemtl m3
f 128 138 129

usemtl m3
f 129 138 139

usemtl m3
f 129 139 140

usemtl m5
f 129 140 141

usemtl m5
f 129 141 130

usemtl m5
f 130 141 142

usemtl m1
f 130 142 131

usemtl m3
f 131 142 113

usemtl m3
f 113 142 114

usemtl m3
f 114 142 143

usemtl m0
f 114 143 144

usemtl m4
f 114 144 145

usemtl m0
f 114 145 146

usemtl m0
f 114 146 115

usemtl m4
f 115 146 144

usemtl m0
f 115 144 143

usemtl m0
f 115 143 147

usemtl m0
f 115 147 119

usemtl m0
f 115 119 118

usemtl m4
f 115 118 116

usemtl m4
f 116 118 117

usemtl m1
f 148 140 149

usemtl m0
f 148 149 150

usemtl m3
f 148 150 147

usemtl m3
f 148 147 143

usemtl m3
f 148 143 142

usemtl m5
f 148 142 141

usemtl m5
f 148 141 140

usemtl m3
f 151 149 139

usemtl m3
f 151 139 138

usemtl m3
f 151 138 152

usemtl m4
f 151 152 153

usemtl m4
f 151 153 154

usemtl m0
f 151 154 149

usemtl m0
f 149 154 150

usemtl m0
f 150 154 155

usemtl m0
f 150 155 120

usemtl m3
f 150 120 147

usemtl m3
f 147 120 119

usemtl m3
f 149 140 139

usemtl m3
f 155 156 157

usemtl m1
f 155 157 120

usemtl m5
f 120 157 121

usemtl m5
f 121 157 123

usemtl m5
f 121 123 122

usemtl m3
f 158 156 155

usemtl m0
f 158 155 154

usemtl m4
f 158 154 153

usemtl m4
f 158 153 152

usemtl m3
f 158 152 159

usemtl m3
f 158 159 156

usemtl m3
f 156 159 123

usemtl m3
f 156 123 157

usemtl m3
f 137 152 138

usemtl m3
f 152 137 159

usemtl m3
f 159 137 124

usemtl m3
f 159 124 123

usemtl m4
f 144 146 145

usemtl m0
f 96 95 97

usemtl m0
f 99 160 39

usemtl m1
f 39 160 161

usemtl m1
f 39 161 162

usemtl m1
f 39 162 163

usemtl m1
f 39 163 40

usemtl m1
f 40 163 41

usemtl m1
f 41 163 164

usemtl m1
f 41 164 165

usemtl m1
f 41 165 166

usemtl m0
f 41 166 98

usemtl m0
f 41 98 22

usemtl m0
f 41 22 21

usemtl m0
f 166 99 98

usemtl m0
f 99 166 160

usemtl m1
f 160 166 165

usemtl m1
f 160 165 161

usemtl m6
f 161 165 167

usemtl m6
f 161 167 162

usemtl m6
f 162 167 168

usemtl m6
f 162 168 169

usemtl m6
f 162 169 163

usemtl m6
f 163 169 164

usemtl m6
f 164 169 170

usemtl m6
f 164 170 171

usemtl m6
f 164 171 165

usemtl m6
f 165 171 167

usemtl m2
f 167 171 172

usemtl m2
f 167 172 173

usemtl m2
f 167 173 168

usemtl m2
f 168 173 174

usemtl m2
f 168 174 169

usemtl m2
f 169 174 170

usemtl m2
f 170 174 175

usemtl m2
f 170 175 171

usemtl m2
f 171 175 176

usemtl m2
f 171 176 172

usemtl m2
f 172 176 177

usemtl m2
f 172 177 178

usemtl m2
f 172 178 173

usemtl m2
f 173 178 174

usemtl m2
f 174 178 179

usemtl m2
f 174 179 180

usemtl m2
f 174 180 175

usemtl m2
f 175 180 176

usemtl m2
f 176 180 181

usemtl m2
f 176 181 177

usemtl m2
f 177 181 179

usemtl m2
f 177 179 178

usemtl m0
f 23 22 98

usemtl m2
f 181 180 179

usemtl m0
f 182 183 184
"""
MTL_DATA = """
newmtl m0
Kd 0.33725490196078434 0.3058823529411765 0.2901960784313726
newmtl m1
Kd 0.2196078431372549 0.18823529411764706 0.18823529411764706
newmtl m2
Kd 0.0784313725490196 0.06666666666666667 0.06666666666666667
newmtl m3
Kd 0.7803921568627451 0.7803921568627451 0.7803921568627451
newmtl m4
Kd 0.4470588235294118 0.34509803921568627 0.3215686274509804
newmtl m5
Kd 0.0 0.0 0.0
newmtl m6
Kd 0.1568627450980392 0.13333333333333333 0.13333333333333333
"""

# Perspective projection function without aspect ratio distortion
def project_vertex(vertex, fov, viewer_distance):
    x, y, z = vertex
    factor = fov / (viewer_distance + z + 1e-5)
    x_proj = x * factor
    y_proj = y * factor
    return x_proj, y_proj, z

# Rotate vertices around X, Y, Z axes
def rotate_vertex(vertex, angle_x, angle_y, angle_z):
    x, y, z = vertex
    y, z = y * math.cos(angle_x) - z * math.sin(angle_x), y * math.sin(angle_x) + z * math.cos(angle_x)
    x, z = x * math.cos(angle_y) + z * math.sin(angle_y), -x * math.sin(angle_y) + z * math.cos(angle_y)
    x, y = x * math.cos(angle_z) - y * math.sin(angle_z), x * math.sin(angle_z) + y * math.cos(angle_z)
    return x, y, z

# Compute average Z for a face
def average_z(face_vertices):
    return sum(vertex[2] for vertex in face_vertices) / len(face_vertices)

# Parse OBJ data from the OBJ_DATA string
def load_obj_data():
    vertices = []
    faces = []
    materials = load_mtl_data()  # Load materials from MTL_DATA
    current_material = DEFAULT_COLOR

    for line in OBJ_DATA.splitlines():
        if line.startswith("v "):  # Vertex data
            _, x, y, z = line.split()
            vertices.append((float(x), float(y), float(z)))
        elif line.startswith("f "):  # Face data
            face = [int(idx.split('/')[0]) - 1 for idx in line.split()[1:]]
            faces.append((face, current_material))
        elif line.startswith("usemtl "):  # Use material
            material_name = line.split()[1]
            current_material = materials.get(material_name, DEFAULT_COLOR)

    return vertices, faces

# Parse MTL data from the MTL_DATA string
def load_mtl_data():
    materials = {}
    current_material = None

    for line in MTL_DATA.splitlines():
        if line.startswith("newmtl "):  # Start new material
            current_material = line.split()[1]
        elif line.startswith("Kd ") and current_material:  # Diffuse color
            r, g, b = map(float, line.split()[1:])
            hex_color = f"#{int(r * 255):02x}{int(g * 255):02x}{int(b * 255):02x}"
            materials[current_material] = hex_color

    return materials

# Render 3D object with flat-colored faces and Z sorting
def render_object(canvas, vertices, faces, angle_x, angle_y, angle_z, fov, viewer_distance):
    canvas.delete("all")  # Clear previous frame
    face_data = []

    for face, color in faces:
        face_rotated = [rotate_vertex(vertices[i], angle_x, angle_y, angle_z) for i in face]
        avg_z = average_z(face_rotated)
        projected_vertices = [project_vertex(v, fov, viewer_distance) for v in face_rotated]
        face_data.append((projected_vertices, avg_z, color))

    # Sort faces by average Z, farthest first
    face_data.sort(key=lambda item: item[1], reverse=True)

    for projected_vertices, _, color in face_data:
        screen_coords = [
            (int(WIDTH / 2 + vx * WIDTH / 2), int(HEIGHT / 2 - vy * HEIGHT / 2))
            for vx, vy, vz in projected_vertices
        ]
        canvas.create_polygon(screen_coords, fill=color, outline="")

    canvas.update()

# Main animation loop
def animate():
    global angle_x, angle_y, angle_z
    render_object(canvas, vertices, faces, angle_x, angle_y, angle_z, fov=FOV, viewer_distance=VIEWER_DISTANCE)
    angle_x += 0.02
    angle_y += 0.015
    angle_z += 0.01
    root.after(16, animate)  # ~60 FPS

# Initialize tkinter window
root = tk.Tk()
root.title("ferret.exe")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

# Set initial rotation angles
angle_x = angle_y = angle_z = 0

# Load OBJ and MTL data
vertices, faces = load_obj_data()

# Start animation
animate()
root.mainloop()
