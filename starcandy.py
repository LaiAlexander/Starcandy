"""
    A short script to calculate stardust and candy cost when
    powering up Pokemon in Pokemon Go.
    Data pulled from https://pokemongo.gamepress.gg/power-up-costs
"""

CUMULATIVE_STARDUST = {
    # Cumulative cost of getting to that level from level 1
    1: 0,
    1.5: 200,
    2: 400,
    2.5: 600,
    3: 800,
    3.5: 1200,
    4: 1600,
    4.5: 2000,
    5: 2400,
    5.5: 3000,
    6: 3600,
    6.5: 4200,
    7: 4800,
    7.5: 5600,
    8: 6400,
    8.5: 7200,
    9: 8000,
    9.5: 9000,
    10: 10000,
    10.5: 11000,
    11: 12000,
    11.5: 13300,
    12: 14600,
    12.5: 15900,
    13: 17200,
    13.5: 18800,
    14: 20400,
    14.5: 22000,
    15: 23600,
    15.5: 25500,
    16: 27400,
    16.5: 29300,
    17: 31200,
    17.5: 33400,
    18: 35600,
    18.5: 37800,
    19: 40000,
    19.5: 42500,
    20: 45000,
    20.5: 47500,
    21: 50000,
    21.5: 53000,
    22: 56000,
    22.5: 59000,
    23: 62000,
    23.5: 65500,
    24: 69000,
    24.5: 72500,
    25: 76000,
    25.5: 80000,
    26: 84000,
    26.5: 88000,
    27: 92000,
    27.5: 96500,
    28: 101000,
    28.5: 105500,
    29: 110000,
    29.5: 115000,
    30: 120000,
    30.5: 125000,
    31: 130000,
    31.5: 136000,
    32: 142000,
    32.5: 148000,
    33: 154000,
    33.5: 161000,
    34: 168000,
    34.5: 175000,
    35: 182000,
    35.5: 190000,
    36: 198000,
    36.5: 206000,
    37: 214000,
    37.5: 223000,
    38: 232000,
    38.5: 241000,
    39: 250000,
    39.5: 260000,
    40: 270000,
}

CUMULATIVE_CANDY = {
    # Cumulative cost of getting to that level from level 1
    1: 0,
    1.5: 1,
    2: 2,
    2.5: 3,
    3: 4,
    3.5: 5,
    4: 6,
    4.5: 7,
    5: 8,
    5.5: 9,
    6: 10,
    6.5: 11,
    7: 12,
    7.5: 13,
    8: 14,
    8.5: 15,
    9: 16,
    9.5: 17,
    10: 18,
    10.5: 19,
    11: 20,
    11.5: 22,
    12: 24,
    12.5: 26,
    13: 28,
    13.5: 30,
    14: 32,
    14.5: 34,
    15: 36,
    15.5: 38,
    16: 40,
    16.5: 42,
    17: 44,
    17.5: 46,
    18: 48,
    18.5: 50,
    19: 52,
    19.5: 54,
    20: 56,
    20.5: 58,
    21: 60,
    21.5: 63,
    22: 66,
    22.5: 69,
    23: 72,
    23.5: 75,
    24: 78,
    24.5: 81,
    25: 84,
    25.5: 87,
    26: 90,
    26.5: 94,
    27: 98,
    27.5: 102,
    28: 104,
    28.5: 110,
    29: 114,
    29.5: 118,
    30: 122,
    30.5: 126,
    31: 130,
    31.5: 136,
    32: 142,
    32.5: 148,
    33: 154,
    33: 162,
    34.5: 170,
    34.5: 178,
    35: 186,
    35.5: 196,
    36: 206,
    36.5: 216,
    37: 226,
    37.5: 238,
    38: 250,
    38.5: 262,
    39: 274,
    39.5: 289,
    40: 304,
}

def calc_cost(start_lvl, end_lvl):
    """
    Calcualtes stardust and candy cost.

    Args:
        start_lvl:
        end_lvl

    Returns:
        Stardust cost, candy cost
    """

    return (CUMULATIVE_STARDUST[end_lvl] - CUMULATIVE_STARDUST[start_lvl],
            CUMULATIVE_CANDY[end_lvl] - CUMULATIVE_CANDY[start_lvl])

def print_cost(stardust_cost, candy_cost):
    """
        Prints the cost given.
    """
    print("Stardust needed: " + str(stardust_cost) + "\n"
          "Candy needed: " + str(candy_cost) + "\n")


if __name__ == "__main__":
    star_cost, cand_cost = calc_cost(float(input("Start level: ")), float(input("End level: ")))
    print_cost(star_cost, cand_cost)
