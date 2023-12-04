test = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

input = """Card   1: 34 55 49 53 46  7 82 22 59 33 | 33 29  7 66 22 51 59 21 55 85 53 26 94 46 24 82  6 47 38  2 34 89 49 41 76
Card   2: 92 73 47  1 91 82 52 98 84 63 | 39 31 73 63 67 91 97 44  8  1 52 20 25 92 43 81 10 36 45 82 47 84  2 98 23
Card   3: 94 35 26 78 66 40 64  7 31 65 | 26 40 65 35 94 36 69 20  7 76 56 27 91 83 66 14 72 31 43 64 34 67 38 78  9
Card   4: 85 11 22  6 20 39 91 69 60 49 | 11 82 68 71 98  3  6 26 32 20 69 35 38 24 93 28 61 18 49 15 40 91 58 75 81
Card   5: 81 89 38 24 64 17 48 69 43 60 | 26 45 49 48  8 19 33 38 28 60 83 27 12 23 89 13 36 88 95 65  4 20 64 62 69
Card   6: 64 37 38 44 63 21 15 43 17 84 | 27 47  5 34 38  8 21 44 41 76 84 64 51 43 25 85 56 32 63  6 15 37 57 17 65
Card   7: 82 97  2 91 92 24 18 19 12 42 | 26 82 79 50 67 92 42 76 97 19 24 91 72 71 15 95 59 88 74  5 18 31 12 46  2
Card   8: 32 90 25 17 85 19 83 59 18 31 | 82 70 53 31 11 19 35 76 85 90  8 40 95 25 18 79 60 59 17 26 28 81 32 83 99
Card   9: 81 51 84 95 88 69 26 75 52  7 | 29 87 12 76 67 95 71 44 91 30  3 43 17 34 64  9 84 53 15 28 72 40 46 10 22
Card  10: 45 36 13 80 75 57 40 99 28 92 | 18 62 75 91 45 90 13 64 61 36 84 67 71 59 82 12 57  7 40 51 46 98 92 28 35
Card  11: 25  3 71 81 17 38 99 30 93 92 | 64 42 24 92 31 73 21 80 41 58 15  8  7 87 88  1 77 94 45 65  5 40 20 79  6
Card  12: 65  1 43 86 88 68 90 54 57 20 | 37 42 46 64 63 21 12 57 55 91 14 44 26 82 95 74 68 85 98 25 67 70 94 32  2
Card  13:  7 40 31 50 37 83 99 62 58 19 | 58 30 99  1 33 19 20 50  7 68 40 62 85 37 31 13 41 51 67 83 84 14 42 43 12
Card  14: 19 76 40 22 77 18 86  7 47 50 | 90  4 96 40 38  5  7 65 50 98 16 63 60 76 58 52 78 80 45 32 23 19  3 42 61
Card  15: 69 12 99 89  8 41 11 65 34 18 | 28 99 11 38  5 92 65 74 31 20 35 88 12 51 83 63 24 56 30 34 64 41 69 18 67
Card  16: 49 14 22 53 35  9 55 88 21 72 | 34  3 64 35 29  7 53 60 58 88 55 16 91 59 49 22 33 46 45 37  9 69 70 54 85
Card  17: 74 96 63 61 78 76 91 41 94 66 | 18 43 14 73  2 31 60 99 39 16 80 59 91 97 23 53 72 96 61 33 88 63 47 41 25
Card  18: 68 59 62 34 38 55  2  5 45 92 | 43 19 37 45 12 99 10  5 73 39 33 92 25 44 79 11 54 95 55 24 17 71 94 56 57
Card  19: 91 47 50  5 59 21  2 43 22 73 | 75 61 89 73 28  5 74 72 48 33 43 20 85 22 97 86 36 77 39 38 53 62 92 32 88
Card  20: 55 48  7 90 95 40 29 44 11 96 | 25 55 75 45  6 82 17 38 20 97 28 53  2 68 50 37 30 87 92 78 31 65 73 74 88
Card  21: 57 91 72 82 71 65 66 21 12 96 |  5 21 59 85 17 91 94  3 56 46 68 67 95 23 50 57 84 22  9 52  6 61 97 48 40
Card  22: 72 15 12 41 98 33 82 71 60 85 | 64 14 58 92 63 76 54 75 13 30  4 20 85 96 42 36 86  1 40  7 49 90 52 70 89
Card  23: 24 15 72 94 71 93 30 19 74 69 | 96 49 37 20 79 83 58 99 11 65 66 89 18  4 86 68 70 90 81 82 54 62 16 67 44
Card  24: 27 64 69 87 33 71 19  2  4 50 | 26 63 94  9 83 80 32 88 79 14 55 78 51 74 56 77 11  5 30 92 28  1 91 89 24
Card  25: 41 38 36 83 87 86  8 72 91 48 | 91  8 87  9 90 86 53 39 72 88 41 59 37 12  7 48 13 67 76 55 83 96 36 38 77
Card  26: 57 32  6 11 49  4 98 40 26 84 |  3 87 14  4 26 73 63 66 44 81 71 39 25  6 89 94 93 98 49 32 12 92 42 28  1
Card  27: 22 37 80  2 68 18 65 82 99  4 | 80 26 67 85 84  2 21 59 18 68 98 65 44 15 22 79 41  9 99 92 88 55 13 24 89
Card  28: 27 12 13 64 74 88  3 41 24 89 | 45 58 15 33 64 27 56 79 35 24 21 73 44 87 98 18 67  2 62 11 39  5 12 96 31
Card  29: 90 72 87 78 32  3 25 52 14 81 | 17 40 22 78 11 15 60 52 90 14 65 83 38  1 32 63 80  4 48 81 29 85 25 88 87
Card  30: 39 16 50  2 68 85 23 66 83 44 |  2 89 61 98 23 39 71 22 68 42 50 83 33 72 18 12 69 51 85 16 67 58 44 20 66
Card  31: 67 35 37 76 93 22 61 15 13  2 | 52 40 89 13 82 53 27 35 56  5 94  7 97 47 72  1 93 62 28 70 69 38 65 59 87
Card  32: 68 76 25 30 45 26 31 24 81 91 | 23 68 57 38 36 94  8 22 85 97 31 44 91 17 59 63 80 95  2 30 90  5 21 67 26
Card  33: 45 66 29 63 57  3 79 97 90 82 | 43 89 16 85 44 52 45 11 40 78 33 86 57 69 99 29 79 55  3 35 62 97 81 98 27
Card  34: 16 33  7 42 73 50 22  2 98 99 | 66 73 65  1 48 95 61 81 16 91 46 53 84 43  4 87 79 69 86 30 77 92 49 14 29
Card  35: 60 93 65 85  3 54 89  4 75 92 | 52 16 92 85 90 76 54 67 46 45 53 75 70 73 89 31 99 11  4 93 48 25 49 15 60
Card  36: 55 43 21 59 86 65 54 74  6 96 | 25 51 83  6 16 74 41 34 78 38 96 73 49 92 15 17 33 86 39 55 54 36 50 71 23
Card  37:  3 92 52 27 34 99 67 21 32 88 | 14 73 33 52 88 40 75 92 15 38 27 44 60 59 21 77 58 35 66 98 99 31 90 30 86
Card  38: 50  6 78 43  9 62 86 53 24 83 | 34 28 62 23 55 85 18 92  5 81 59 95 64 87 71 50 16 90  8 15 65 48 39 37 60
Card  39: 69 43 32 14 83 29  3 81 73 25 |  7 30 42 96 31 29 33 35 40 54 41 39 84 98 38 82 15 64 23 83 37 46 80  3 50
Card  40: 75 92 89 37 72 83 30 54 49 25 | 83 73 82 38 22 93  2 53 97 44 47 40 42 79 26  6 16 12 86 68 45 81 19 65 34
Card  41: 33 23 24 43 65 91 13 67 53 56 | 74 30 27 83 88 61 89 20 59 46 41 35 19 55  7 54 57 63 49 77 78 34 12 15 93
Card  42:  3 26 28 11  4 12  9 74 65 23 | 32 58 13 67 94 50 71 20 56 76 26 92 88 63 15  5  1 84 51 81 40  7 54 79 24
Card  43: 76 21 38 14  3 40 10 73 96 31 | 27 74 58 46 19  1 44 22  9 95  2 56 64 39 85 15 84 88 94 45 61 71 90 83 18
Card  44: 62 63 90 91 26 25 66 70 52 49 | 45 76 91 26 52 18 89 44 78 63 90 70 20 35 59 25 80 66 74 62 57 40 49 22 23
Card  45: 61 92 64 78 67 60 31 84 56 40 |  3 21  5 99 37 56 64 98 13 16 34 87 20 54 33 23  2 61 52 14 78 36 32 24  8
Card  46: 34 90 20 93 80 89 45 91 81 79 | 88 89 44 59 93 98 80 52 54 83 84 48 46 91 20 45 34 29 79 18 73 32 90 53 81
Card  47: 12 87 52 18 55 30 47 36 49  3 | 67 54 26 47 20 36 55 30 22 82 49 84 42 97 75 86 12 39 53 68 87 96 33 14 15
Card  48: 96 64 65 40 53 82 51 63 32 28 | 74 51  9 65 82 30 32  3 86 81 42 14 49 16 38 47 29 15 45 79  5 33 41 36 56
Card  49: 78 18 95 35 17 56 10 34  3 61 | 38 63 52 76 79 23  6 82 61 77  9 66 21 75 71 93 67 12  4 33 24 10 78  1 16
Card  50: 47 62 18 10 53 16 83 34 72 40 |  9 60 80 10 82 46 92 14 94 79 72 86 44 93 47 19 75 35 37 54 74 38  7  3 34
Card  51: 95 33 76  6 93 68 36 13 22 46 | 53  1  5  7 32 76  8 79 28 93 10  9 39 78 85 25 31 56 83 46 98 96  6 34 36
Card  52: 64 25 74 77 11 26 99 48 19  6 | 64 74 24 77 34 40 32 75 11 26 58 31 23  7 46 95 19 99  6 60  2 25 48 72 88
Card  53: 18 62 50 26 93 20 87 42 90  6 |  6 67 96 28 55 91 88 44 86 50 58 87  3 60 62 42 49 70 33 19 94 99 52 17 68
Card  54: 93 12 16  6 73 74  4 86  1 69 | 26 13 23 62 95 25 71 10 29 59 70 32 15 18 28 39 38 41  3 50 27 58 44 85 87
Card  55: 92 57 85 89 28 60 72 22  5 25 | 91 21 79 19 89 41 84  7 13  5 98 47 92 30 37 34  3 85 44 99 74 72 87  8  6
Card  56: 94 92 98 86 77 46 55 95 96 66 | 40 12 35 71 59 73  3 53 84 38 68 60 18 13 45 67 85  6  4 23 88 75 28 89 51
Card  57: 76 13 77 33 86 56 22 59  9 10 | 88 34 89 33 13  4 74 86 39 85 98  7 67 68 94 48 73 11 41 65 24 17 28 32 69
Card  58: 66 52 33 57 72 29 71 92 96 19 | 13 73 20 33 70 53 55 37  6 35  3 94 15 90 66 47  1 59 50 80 62 30 44  5 23
Card  59: 13 35 33  3 37 54 42 73 47 92 | 25 81 41 24 21 37 44 88 72 47 46 87 31 70 67 86 84 78 66 54  5  7 79 60 55
Card  60: 43 12 91 87 63 20 67 90 31 62 | 84 11 48 27  3 94 85 18 82  8  5 66 21 64 77 57 71 61 55 32 23 42 95 79  9
Card  61: 59 10 17 55 91 41 47 61 69 90 | 20  9 93 89 34  2 68 42 36 88 38 75 22 48 92 64  3 28 17 18 27 10 40 14 76
Card  62: 75 98 17 83 97  2 78 79 56 92 | 37 64 97 18  8 86 62 90 43 25 28 46 33 38  9 93 95 22 42 26 63 67 49 82 44
Card  63: 60  7 99 28 54 87 79 73 18 74 | 44 89  9 11 67 14 22 98 56 76  1  6 10 90 50 29 63 41 94 13 84 26 45 17 34
Card  64: 66 12 15 17 89 43 47 23 49 68 | 47 43 98 93 41 48 12 72 17 89 26 66 44  6 96 68 39 15 23 40  4 49 52 69 51
Card  65:  6  7 18 78  2 88 79 57 80 59 | 15  7 59 25 18 14 71 64 19 88 69  6 97 27 46 67 79  2 21 98 89 60 70 33 85
Card  66: 67 23 83 79 86 59 62 40 12 38 | 82 22 74 96 62 86 67 59 70 23 38 51 12 26 89 75 57 34 79 13 43 40 18 87 21
Card  67:  2 37  7 92 56 77 21 53 80 44 | 56 53 37  7 39 45 84 58 80 77  5 89 85  9 92 46 71 10 62 14 68  2 44 78 21
Card  68:  5 83 37 72 90 48 85 33 40  7 | 28 25 80 98 76 37 51 97  3 72 84 13 54 15 18 62 21 64 50 34 70  1 22 32 31
Card  69: 87 65 28 11 62 98 13 12 31 53 | 24 62 89  7 52 72 13 20 87 48 96 29 98 11 74 99 47 39 53 19 65 59 69 78 31
Card  70: 84 25 14 26 15 83 81 93 64 39 | 81 83 39 61 26 64 84 99 93 12 65 31 25 77 14 20 73 74 87 41 15 51 46 70 85
Card  71: 32 81 46 30  2 38 89 61 93 71 | 22 34 41 84 78 12 29 72 80 58 69 47 99 50 60 79 55 18 48 75 31 44 21 14 81
Card  72: 98  2 68 91 63 99 38 45 19 75 | 68 19 33 75 63 23 56 98 45 37 82 15  2 21 78 81  6 38 85 91 90 25 99 87 12
Card  73: 79 66 31 12 99  8 43 33 81 37 | 76 58 79 99  8  5 61 31 97 81 78 44 33 98 37 40 68 89 66 43 50 14  2 12 72
Card  74: 49 27 85 90 69 23 20 13 59 62 | 70 16 74 43 53 50 35 42 79 87 55 83 12 95 58 13 37 98 45 24 66 64 62 51 30
Card  75: 33 20 86 34 23 49 43 42 31 11 | 92 33  5 43 46 22 91 18 23 70 34 17 25 41 48 81 11 52  9 42 45 20 53 32 58
Card  76: 99 87 16  3 79 32 65 38 39 44 | 50 51 29 91 88 58 27 70 82 95 93 90 46  1 85 72 61 49 33 66 59 31 12 57 13
Card  77: 15 13 25 91 67 76 21  6 55 28 |  4 87 72 78 47 54 26 11 10 45 60 83 32 16 73 92 74 53 59 17 94 18  1 29 69
Card  78: 15 65 40 13 89 19 75 30 67 52 | 85 21 63 61 48 54 49 97 33 38 22 56 43 81 91 62 37 11 39 50 80 82 94 23 72
Card  79: 78 28 27 77 94 87 91 21 35 26 | 77 58 10 42 60 78 50 22 33 54 23  5 75 34 96 87  2 70  4 90 44 99 64 11 91
Card  80: 39 88 45 80 99 82 84 25 64 17 | 19 67 47 44 89 75 24  2 32 39 54 23 51 93 88 48 99 13 27 72 28 87 59 11 57
Card  81: 79 43 98 14 53  4 65 76 19  7 | 10 60 50 94 47  4 77 34 27 15 67 32 35 99 90 61 42 45 51 31 84 29 63 49 11
Card  82: 50 14 77 57 36 81 75 11 15 21 | 95 33 37 99  1 35 68 11 24 62 72 70 63 98 39 34  5  8 10 79 25  9 22 94  3
Card  83: 12 36  2 87 98 77 18 23  3 52 | 28 24 44  7 41 89 59 75 79 56 83 25 14 99 11 61 66 70 76 26 38 46 33  1 54
Card  84: 25  1 95 31  9 66 13 22 39 74 | 22 20  1 98 14 97 32 26 46 39 25 76 13 59  9 78 93 47 64 31 74 95  7 66 55
Card  85: 39 27 43 28 47 88 56 36 38 14 | 42 43 85 28 27 81 16 47 36 23 51 96 88 14 25 67 46 56 18 66 97 39 37 38 86
Card  86: 79 84 47 46 66 44 75 51 10  7 | 63 46 21 47 40 53 10 75 25 93 74 51  7 79 66 58 44 94 84 65 89 96  8 78  2
Card  87:  8 29 89 79 41 36 99 67 97  3 | 19 87 54 97 83 86 33 17 99 67 41  5 16  3 57  8 29 47 36 79 98 40 89 80 76
Card  88: 46 31 53 19 49 29 90 43 52 98 | 37  2 36 86 96 55 30 71 99 45 12 27 97 66 73 78 92 48 40 33 28 85 32 42 68
Card  89: 37 93 31 72 91 33 15 88 97 12 | 63 99 75 76 43  9 50 12 59 86 35 31 19 84 38 60 48 89 22 79 65 26 47 69 23
Card  90: 19 30  1 65 18 42 59 31 37 77 | 78 94 73 57 91 19 59 68 83 33 80 47 76 67 88 96 58 64 69 25 89  3 21 35 81
Card  91: 94 53 75 83 68 34 69 46 60 16 | 33 41 88 58 73 28 90 53 55 21 51 23 67 75 20 45 71 54  8  1 18 22  7 34 61
Card  92: 39 77 41 95 75 58 44 35 62 28 | 55 72 16 17 41 44 24 38 98 23 39 75 28  6 65 76 77 79 51 40 81 49 95 35 34
Card  93: 96 33 12 95 42 23 71 28 89  9 | 44 96 76 12 54 93 58 67 22 92  3 13 79 65 43  6 35 45 49 36 48 99  1  7 66
Card  94: 36 25 65 72 67  6 85 31 13 44 | 43 50 21 44 42 85  7 62 34 83 65 10  3  4 13 31 76 75 40 98  9 11 20 48 30
Card  95: 79 61 43 23 70 13  9 95 31 51 | 40 58 35 89 21 48 88 33  2 24 72 36 16 32 73 57 19 84 96 41 45  7 14 39 18
Card  96: 70 55 11 37 86 67 85 64 54 92 | 98 11 62 12 74 46 93 67  9 18 22 81 23 86 85 60 27 88 17 90 64 75 20 54 28
Card  97: 56 27 20 40 17 37 16 47 82 22 | 34 82 11 96 44 81 43 86 95 89 24  5 62 50 84 41 14 61 48 39 65 26 55 78 87
Card  98: 70 92 96 99 48 40 34 18 42 51 | 80 86 91 64 10 45 74 82 25 81 42  1  6 67 78 24 22 47 28  8 79 14 38 87 27
Card  99: 60 85 42 12 54 23 53 92 40 45 | 77 98 10 97 67 75 57 88  8 26 15 39 35 37 50 55 17 52 82 49 66  4 69 96 93
Card 100: 96 90 88 64 54 70 68 11 58 75 | 91 16 99 39 97  1  6 96 32 93 50 61 28 22 60 88 51 19 78 67 81 56 14 48 45
Card 101: 71 54 42 24 87  4 44 82 26 75 | 84 85 97 21 22 93 62  9 20 36 80 53 10 96 67  6 76 95 33 19 52 78 73 72 50
Card 102: 19 48 82 67 13 31 36 58 75 71 | 92 69 42 89 76 61 40 73 68 43 80 57 23  9 12 88 99  3 47 34 45 39 26 98 52
Card 103: 28 36 73 83 78 26 22  5 65 79 | 91 83 78 73 98 19 66 84 89 26 54 40 79 72 86 95 28 32  5 36 80 92 22 68 65
Card 104: 26 49 10  2 46 15 41 83 44 63 | 12 75 76 67 70 42 31 99 80 16 83 23 17 55 27 66 30 68 74 48 59 57  5 50 39
Card 105: 49  5 41 83 87 73 43  2 66 92 | 21  5 35 92 78 73 34 37 29 17 58 10 49 87 65 44 54 59 46 27  7 80 40 12 70
Card 106: 98 13 87 19 43 97  7 26 25 61 | 40 35  4  7 16 65 96 97 67 25 24 26 64 33 99 19 13 61 52 83 42 59 14 48 34
Card 107: 36 25  8 63 47 76 50 86 82  7 | 24 58 72 48 13 16 75 40 97 12 69 70 89 67 14 54 41 59 88 83 87 91 17 32 39
Card 108: 97 90  9 94 15 93 63 38  2 46 |  9 46 68 59 65 78 50 89 23 43 88 38 93  3 62 64 20 15 94 63 74 21 32 83 90
Card 109: 58 92 73 39 20 22 18 19 90 96 | 54 27  2 38 74 78 77 60 28 75 85 81 59 87 45 16 21 57 34 12 52 32 97 37 69
Card 110: 51 47 77 42 12 81 49 18 16 46 | 64 26 53  9 98 59 49 20  4 44 67 27 45 55 84 97 33 75 50 76 62 90 31 17 69
Card 111: 16  7 47 95 37 32 83 67 91 86 | 68 95 73  8 14 11 43 21 94 39 25 79 17 27 62 36 51 52 42 38 63  2 97 56 13
Card 112: 73 63 57 54 92 47 53 22 90  1 | 41 49 78  9  7 84 98 57 76 12 10 85 50 38 66 87 68 97 36 27 51 94 95 56 83
Card 113: 86 85 42 16 49 34  4 55 60 84 |  4 41 68 49 89 29 53 69 50 88 91 32 12 24 33 70 63 17 22 54 59 67 74 86 39
Card 114: 47 54 98 63 17 82 18 61  6 12 | 94 41 15 64 14 32 23 10 90 38 84 87 50 42 35 60 91  2  3 86 95 13 67 24 25
Card 115: 69 12 36 43 33 82 52 19 38  6 | 61 18 75 30 70 66 50 91 77 60 46 13 97  5 83 76 80 16 24 87 48 78  1 86 28
Card 116: 94 92 61 48 59 71 47 98 15 77 | 96 10 73 74 51 33 56 52 58 78 65 89 55 43 92 11 76  4 88 83 64 54  7 95 16
Card 117: 12 99 63 10 28 78 41  9 71 81 | 21 59 16 25 76  8 36 79 70 37 35 38 68 98 90 67 14 27  7 75 47 24 46 18 91
Card 118: 18 69 86 59 58 62  4 98  8 10 | 30  4 62 92 84 33 25 23 59  5 38 96 93 14 58 72 73 37 49 53  8 18 46 48 98
Card 119: 69 77 16 39 78 85 49 33 96 27 | 85 47 99 20 50 49 77 35 16 14 15 12 27 81 19  4  3 59  9 57 69 87 97 55 96
Card 120: 58 57  1 27 93 83 54 43 23 98 | 60 87 20 18 34 98  5 93 12 39 25 31 45 51 70  1 83 32 43 85 27 11 40 78 57
Card 121: 57 26  6 75 82 16 91 37 33 73 | 75 71 43  8 10 63 59 17 98 95 20 96 79 94 23 36 48 11 19  1 14 34 15  9 74
Card 122: 60 58 66 54 74 71 73 67 42 39 | 42 58 57 59 67 25 18  9 26 29 53 66 24 73 71 75 86 39 74 54 44 81 19 20 80
Card 123: 62 22 41 53 18 87 45 24 29  8 | 29 14 95 19  9 45 58 53 62 88 47 91 12 41 63 27 52 99 78  8 44 76 90 22 25
Card 124: 14 46  1 23 17 65 16 61 19 41 | 92 73 17 64 16 32 77 65 88 23 11 68 86 59 21 37 50  3 19 85 38 30 71 41 46
Card 125: 70 34 41 61 25  6 51 73 56 90 |  5 71 16  4  7 98 77 65 38 49 67 91 66 78 92 40 64 48 57 59 15 86 56 50 34
Card 126: 53 13 42 40 30 46 57  8 77 90 | 11 73 74 19 71 24  6 41 63 62 47 39 78 26 58 86 52  7 51  9 82 59  4 45 28
Card 127: 16 46 78 25 28 32 47 49 43 35 | 88 16  7 77 83 32 35 19 11 99 94 73 37 29 95 80 46 18 54 78 25  2 40 51 53
Card 128: 66 59 53 68 48 77 50 34 43 67 | 62 53 36 11 61 44 66 87 78 84 72 29  1 22 86 59 50 89 93 13 73 39 12 80 18
Card 129: 77 94 53 31 47 98 60 86 32 67 | 94 44 32 43  8 82 18 30 45  9 15 22 53 29 61 57 36 13 71 47 48 74 56 49 23
Card 130: 57 76  7 25 58 73 67 93  1 48 | 49 56 41 83  3 82 37 55 39 64  8 86 52 42 10 85 20 46 54 81 35 40 80 70 38
Card 131: 49 17 65 88 74 68 24 99 16 29 | 25 43 41 93 87 33 27 71 75 20 32  2 31 30 21 70 13 96 89 95 36 76 18 62 26
Card 132: 61 49 15 52 76 82 87 42 65  8 | 91 78 57  6 84 87 13 56 68 24 81 21 38 66 92 47  1 85 80 55 93 96 59 41 46
Card 133: 48 71 17 97 73  2 19 36 62 67 |  5  1  7 74 46 15 30  4 28 12 47 75 33 23 66 95  9 11 42 14 89 50 24 92 54
Card 134: 23 31 47 48 85 19 62 34 44 24 | 14 20 29 16  6 85 31 91 23 44 62 34 24 19 96 42 22 35 86 47 75 79 53 48 73
Card 135: 28 83  2 52 47 19 64 70 25 46 | 91 83 85 52 95 16 96 70 11  7 87 82 77 46 79 44 64  2 19 24 59 40 14 28 47
Card 136: 41  3 81 53 21 98 33 36  9 13 | 13  9 28 57 50 36 15 54 21 53 29  8 56 98 81 63 33 71 18 41 40 19 20 82  3
Card 137: 54 89 31 72 10  4 58 81 48 55 |  9 89 76 72 23 55 83 74 52 93 58 43 13 78 81 35 26 48 31 10 54 97 25 64  4
Card 138: 60 74  7 45 82 89 31 96 70 85 | 80 85 74  2  8 60 12 78 70 91 44 56 57 95  7 96 89 34 61 45 82 90 62 31 76
Card 139: 46 75  8 64 59  9 44 96 76 79 |  6 20 49 52 98 11 83 23 58 25 79 36 67 63 61 47 44 68 17 33 95 24 54 41 84
Card 140: 60 89 76 25 20 77 36 45 31 86 |  4 77 80 88 91 33 93 39 22 78 57 65 54 17 50 16 18 96 99 55 83  5 13 89 14
Card 141: 47 42 45 15 43 57  8 94  3 40 |  3 43 32  8 97 59 47 84 85 57  1 55 42 74 45 15 50 56 83 24 94 19 39 81 40
Card 142: 67 35 95 20 52 70 80 75  6 86 | 86  4 25 61 47 82 57 88 10 43 97  5 19 72 55 83 42 92 41 52 35 89 20  6 26
Card 143: 72 34 67 97 38 96 49 36 77 19 | 28 34  1 61 85 36  6 98 72 71 77 96 83 38 67 65 78 58 31 60 16 91 66 14  9
Card 144: 66 48 39 24 79 77  3 68 18 89 | 24 58 66 40 33  1 29 70 94 28 18 93 11 86 64 21 82  8 45 35 84  9  3 79 63
Card 145: 66 41 60 45 53 46 97 14 99 26 | 64 26 40 61 27 69 52 66 28 41 12 80 90 53 36 87 77 17 21 60 10 50 39 97 99
Card 146: 91 10 34 69 94 45 12 93 82 60 | 44 91 30 99 57 83 68 90 16 92 28 13 72 46  6 66  4 95 35 88 71 81 12 27  3
Card 147: 79 60 55 23 83 22 65 42 78 88 | 19 40 81 96 79 50 43 64 17 31 59 36 55  5 98 25 38  4 48 93 23 45 21 62 88
Card 148: 73 33 62 78 54 39 84 61 81  9 | 69  6 12 91 57 45 78 39 67 60 86 40 63 16 50 49 46 99 52 77 21 76 27 22 73
Card 149: 44 24 82  9 30 85 21 71  3 47 | 19 32 40  3 21 15 74 70 71 75 26 41 31 55 98 89 50 23 65 17 14 16 79 61 86
Card 150: 26 12 44 47 75 49 89 58 14 70 | 32 97 68 42 30 45 17 28 95  1 64 29 39 87 91 18  7 22 65 59 82  6 63 21 15
Card 151: 17 52 86 44 12 87 95 88 72  5 | 32 95 31 14  9 57 53 92 60 89 13 25 98 40 38 96 21 77 33 97 75 29 86 63 70
Card 152: 18  2 62 44 42 57  5 47 16 89 | 37 82 38 68 36 28 17  5 59 26 99 92 97 75 85 79 60 33 64  6 45 77 86 40  8
Card 153: 10 14 50 36 95 72 48 81 21  4 | 88 41 86 53 51 84 28 75 98 76 54 65 57 99 64  9 70 67 33 96 74 93  7  3 85
Card 154: 83  2 53 70 55 63 92 98 86 96 |  8 92 10 52 20  4 99 93 82 24 53 46 70 69 32 98  7 83 51 21 16 22 38 44 96
Card 155: 12 89 16 41 59 49 46 42 93 62 | 12 18 74 65 59 49 42 25  2 16 82 62 41 28 39 13 52 26 40 46 73 93  7 78 89
Card 156: 58 62 32 11 81 13 90 98 59 91 | 57 43 32 64 54 33 91 98 48 74 28 81 95 10 47  9 59 62 82 89 27 86 13 11 58
Card 157: 70 19 28 83 14 77 60 95 11 65 | 22 68 50 87 78  8 49 99 98 89 57 71 81 35 73 85  9 32 66 20 33 94 54 69 39
Card 158:  5 91 19 81 32 57 35 74 70 54 | 52 66 31 29  2 12 30  9 33 62 23 42 50 22 73 95 98 55 26 44 74 83 85 20 71
Card 159: 83 25  7 47 89 50 82 28 84  8 | 49 92 51 87 50  7 90 35 88 77 23 15 72 64  2 34 62 10 58 53 37 48 29 75  1
Card 160:  6 75 74 16 48 50 49 56 33 52 | 67 15 27  2 83 85 56  4 92 43 12 39 57 77 38 17 91 50 63 36  7 29 66  9 62
Card 161: 73 49 36 20 27 21 17 65 95 84 | 45 81 27 88 38 25  1 80 39 78 95 58 73 56 84 36 66 64 62 20 49 21 17 65 48
Card 162: 51 37  7 55  8 33 97 80 17 43 | 67 10  9 54 65 52 71 82 17 42 33 62 83 91 86 14 72 43 37 99 34 38 60 31 15
Card 163: 10 36 79 29 68 60  4 25  8 63 | 62 24 54 17  1 89 87 81 38  7 76 41 95 51 50 19 88 46 48 64  3 22 33 71 42
Card 164: 60 20 73 99 77 37 78 53  2 27 | 68 69 11 99 27 81 17 60 14 54 72 61 98 53 66 52 25 57 92 77 55 38 50  7 43
Card 165:  2 54  7 72  8 85 60 24 90 45 |  6 94 44 38 96 50 84 92 56 26 21 68 18 70 33 88 91 29 63 81 47 71 12 22 80
Card 166: 10  6 57 18  2  4  7 26  8 25 | 93 94 26 13 32 44 89  7 86 16 57 27  8 35 17 82  2 19 69 81 62  6 80 38 72
Card 167: 62  1 19 95 46 18 28 80 70 74 | 25 86 57  2 48 30 50  3 60 26 28 55 10 47  5 84 73 56 11  8 36 12 19 13 35
Card 168: 77 32 12 19 76 90 10 38 96 57 | 48 12 79 46  8 15 90 16 17 68 70 59 28  2 91 96 36 33 11 30 57 27  6 73 77
Card 169: 85 28  4 26 47 98 66 42 52  6 | 25  7 82 68 44  6  4  8 24 46 37 51 92 10 69 40 90 84 79  2 47 98 38 20 50
Card 170: 33 43 49 70 76 25 71 78  1 87 | 57 10 93 86 66 35 51 97 13 62 52 81  8 67 38 70 48 32 54 19  2 64 60 89 87
Card 171: 84 16 90 21 17 50 28 40 78 34 | 84 28  8 72 94 37 10 44 79 96  1  7 25 86 27  4 29 97 18 52 53 33 69 81 75
Card 172:  9 86 27 40 68  8 89 26 23 57 | 46 79 56 43 28 70  7 26 53 29 94 64 54 97 73 76 58  3 38 24 21 47 66 67 88
Card 173: 46 33 61 72 75 82 58 69 83 89 | 18 65 41 30 20 74 52 21 24 97 84 59 91 37 73 53 56 78 17 71 14 92 99 49 81
Card 174: 95 31 30 64 49 85 34 29 69 40 | 84 40 64 45 49  5 78 29 95 60 53 31 97 28 85 69 41 74 18 70 34 99 50 30 10
Card 175: 43 67  3 25  1 18 56 78 29 70 | 58 62  1 78 51 29 20 57 54 71 70 89 27 95  4 43  6 56 25 94 18 67  3 92 14
Card 176: 85 31 77  6 10 61 30 22 37 21 | 29 56 93 66 86 11 21 77 46 31 73 30 61 10 51 72  4 27 92  6 96 12 22 59 40
Card 177: 28 46 71 94 42 83 91 84 96 52 |  3 76 43  8 84 83 98 25 91 27 20 46 33 52 55 60 67 72 28 71 97 23 94 42 96
Card 178: 91 25 79  8 71 50 83 47  6 36 | 90 48 57 41 85 68 15 78 73 74  7 91 62 97 49  2 54 13 19 11 33 23 79 37  1
Card 179: 75  2 43 78 32 56 21 80  3 48 | 48 91 46 94  6 80 21 75 65 43 63 78 88 81  3 32 68 72 54  7 89 36 61  2 56
Card 180: 61 50 45 17 26 21 81 39 68 40 | 17 72 26 39  5 21 59 55 61 56 29 28 38 41 50 22 81 40  1 71 34 45 86 68 46
Card 181: 76 91 39 11 34 36 25 47 26 46 | 83 46 58 22 16 82  6  2 19  3 56 41 68 64 25 32 54 72 98 93 37 33 53 39 48
Card 182: 94 96 30 64  9 35 33 39 89 46 | 77 34 14 82 45 63  4 76  2 69 87 30  3 13 60 66 81 44 97 28 88 93 57 65 55
Card 183:  7 27 31 77 13 61 26 70 18 93 | 49 57 26 13 77  5 18  3 80 31 70  7 89 54 74 82 27 61 15 53 67 63 28 93 76
Card 184: 22 20 67 52 95 90 98 59 25 46 | 50  1 10 43 44 69 52 67 80 16 58 99 92 59 71 75 91 90 46  2 84 40 85 39 53
Card 185: 60 90  2 88 29  7  5 38 43 84 | 34 10 58 60  5  2 53 88 57 44 47 84 29 55 43  9 30 19 61 76  8 74 38 83 14
Card 186: 21 73 64 62 54 80 79 70 36 17 | 41 64 50 96 36 32 62 86 65 94 33  2  4 59 85 44 53 40 28 21 54  8 11 42 72
Card 187: 69  1 12 25 31 26 35 94  8 73 | 89 25 58 94 11 69 78 35 73 80 17  1 43 91 88  7 97 12 44 70 26 31 33 57 99
Card 188: 72 93 80 60 41 89 54  1 99 23 | 64 94 33 51 97 18 74 35 45 57 26 79  6 96 38 82 92 37 84 47 42 43 24 52 27
Card 189: 86 29 92 62 20  8 12 67 52 70 | 96 38 65 64 86 19 27 68 22 56 26 23 39 87 21 41 36 25 92 48 73 35  4 13 84
Card 190: 81 21 82 32 88 39 61 34 75 18 | 27 56 29 81 53 52 13 61 62 15 94 84 75 66 16 91 31 63 47 26 49 32 77 51 40
Card 191:  9 83 88 73 61 44 81 40 50 75 | 21 12 96 87 34 74  6 60 80 43 63 23 26 16 51 27 70 24 11 38 32 86 53 46 99
Card 192: 77 57 73 80 41 32 22 29 76 50 | 53 12 55  1 64 11 30 93 23 17 15 44 99 13 97 76 58  8 37 47 90 33 38 92 62
Card 193:  7 62 19 40 89 54  2 70 45  1 | 20 82  9  7 80 22  4  8 60  3 37 61 64 13 12 14 75 86 90 89 40 55 57 59 33
Card 194: 50 26 68 51 65 44 76 89 69  3 | 63 87 66 39 76 16 48 32  3 36 81  2 34 40 64 91 29 96  9 46 28 11 62 55 33
Card 195: 23 33 19 46 92 64 32 54 71 25 | 18 75 29 42 39 26 59 12 53 78 85 28 48 32 96 23 44 10 58 37  7 66  2  1 93
Card 196: 96 32 55 61 82  9 77 18 99 28 | 64  5 26 97 54 62 69 19  7 29 27 47 56 33 44 50 83 43 88 72 91 10 12 51 35
Card 197: 43 22 47 86 64 70  3 59 87 13 | 56 24 57 38 36 76 85 96 63 62 18 44  8 25 69 54 75 39  2 81  6 77 58 33 83"""