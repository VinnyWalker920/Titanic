# 0,1,2 first,second,third class inner index 0,1,2 women,children,men
classGenderTable = [
    [.97, .86, .32],
    [.86, 1, .08],
    [.49, .31, .13]
]

# 0,1,2 first,second,third class inner JSON is Nationality breakdown
nationalityBreakdown = [
    # First Class
    {
        "American": .67,
        "Austro Hungarian": 0,
        "Belgian": 1,
        "British": .44,
        "Canadian": .48,
        "Dutch": 0,
        "French": .92,
        "German": 1,
        "Italian": .5,
        "Irish": 0,
        "Mexican": 0,
        "Spanish": .67,
        "Swedish": .67,
        "Swiss": 1,
        "Turkish": 1,
        "Uruguayan": 0,
    },

    # Second Class
    {
        "American": .47,
        "Australian": 0,
        "Austro Hungarian": .25,
        "Belgian": 0,
        "British": .41,
        "Canadian": .5,
        "Danish": 0,
        "Finn": .5,
        "French": .5,
        "German": 0,
        "Italian": .5,
        "Irish": .25,
        "Japanese": 1,
        "Norwegian": 0,
        "Portugese": 0,
        "Russian": .33,
        "South African": .5,
        "Spanish": 1,
        "Swedish": .33,
        "Swiss": 1,
        "Syrian": .5

    },

    # Third Class
    {
        "American": .28,
        "Australian": 1,
        "Austro Hungarian": .16,
        "Belgian": .23,
        "British": .15,
        "Bulgarian": 0,
        "Canadian": 0,
        "Chinese": .75,
        "Danish": .14,
        "Finn": .31,
        "French": 0,
        "German": .25,
        "Greek": 0,
        "Italian": .25,
        "Irish": .36,
        "Norwegian": .32,
        "Portugese": 0,
        "Russian": .33,
        "South African": 0,
        "Swedish": .22,
        "Swiss": 0,
        "Syrian": .39,
        "Turkish": .25
    }

]

# 0,1,2 female, child, male | first,second,third class Inner JSON is Lifeboat Breakdown
lifeBoatBreakdown = [
    # Female
    [
        # First Class
        {
            "Lifeboat 1": .20,
            "Lifeboat 2": .27,
            "Lifeboat 3": .38,
            "Lifeboat 4": .22,
            "Lifeboat 5": .05,
            "Lifeboat 6": 1,
            "Lifeboat 7": 1,
            "Lifeboat 9": .15,
            "Lifeboat 10": .09,
            "Lifeboat 12": .05,
            "Lifeboat 13": .12,
            "Lifeboat 14": .11,
            "Lifeboat 15": .25,
            "Lifeboat 16": .52,
            "Lifeboat 17": .25,
            "Lifeboat 18": .08,
            "Lifeboat 19": .08,

        },

        # Second Class
        {
            "Lifeboat 8": .20,
            "Lifeboat 9": .48,
            "Lifeboat 10": .29,
            "Lifeboat 11": .49,
            "Lifeboat 12": .48,
            "Lifeboat 13": .19,
            "Lifeboat 14": .11,
            "Lifeboat 18": .08,
            "Lifeboat 19": .08,
        },

        # Third Class
        {
            "Lifeboat 8": .45,
            "Lifeboat 9": .15,
            "Lifeboat 10": .09,
            "Lifeboat 12": .15,
            "Lifeboat 13": .31,
            "Lifeboat 14": .31,
            "Lifeboat 15": .25,
            "Lifeboat 17": .35,
            "Lifeboat 18": .08,
            "Lifeboat 19": .08,
        }

    ],

    # Child
    [
        # First Class
        {
            "Lifeboat 1": .20,
            "Lifeboat 2": .27,
            "Lifeboat 3": .98,
            "Lifeboat 4": .22,
            "Lifeboat 5": .05,
            "Lifeboat 6": 1,
            "Lifeboat 7": 1,
            "Lifeboat 9": .15,
            "Lifeboat 10": .09,
            "Lifeboat 12": .05,
            "Lifeboat 13": .12,
            "Lifeboat 14": .11,
            "Lifeboat 15": .25,
            "Lifeboat 16": .52,
            "Lifeboat 17": .25,
            "Lifeboat 18": .08,
            "Lifeboat 19": .08,

        },

        # Second Class
        {
            "Lifeboat 8": .20,
            "Lifeboat 9": .48,
            "Lifeboat 10": .29,
            "Lifeboat 11": .49,
            "Lifeboat 12": .48,
            "Lifeboat 13": .19,
            "Lifeboat 14": .11,
            "Lifeboat 18": .08,
            "Lifeboat 19": .08,
        },

        # Third Class
        {
            "Lifeboat 8": .45,
            "Lifeboat 9": .15,
            "Lifeboat 10": .09,
            "Lifeboat 12": .15,
            "Lifeboat 13": .31,
            "Lifeboat 14": .31,
            "Lifeboat 15": .25,
            "Lifeboat 17": .35,
            "Lifeboat 18": .08,
            "Lifeboat 19": .08,
        }
    ],

    # Male
    [
        # First Class
        {
            "Lifeboat 1": .22,
            "Lifeboat 2": .27,
            "Lifeboat 3": .02,
            "Lifeboat 4": .26,
            "Lifeboat 5": .25,
            "Lifeboat 10": .03,
            "Lifeboat 12": .02,
            "Lifeboat 13": .05,
            "Lifeboat 14": .08,
            "Lifeboat 15": .02,
            "Lifeboat 17": .08,
            "Lifeboat 18": .03,
            "Lifeboat 19": .08,
            "Lifeboat 20": .18
        },

        # Second Class
        {

            "Lifeboat 10": .06,
            "Lifeboat 12": .05,
            "Lifeboat 13": .08,
            "Lifeboat 14": .08,
            "Lifeboat 18": .03,
            "Lifeboat 19": .08,
            "Lifeboat 20": .18
        },

        # Third Class
        {
            "Lifeboat 10": .03,
            "Lifeboat 12": .02,
            "Lifeboat 13": .08,
            "Lifeboat 14": .20,
            "Lifeboat 17": .12,
            "Lifeboat 18": .03,
            "Lifeboat 19": .08,
            "Lifeboat 20": .18
        }
    ]
]
