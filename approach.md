Step 1 : We will generat all the combination of the given number

Step 2 : Make a list of all the posible combination

Step 3 : After that we will try to find the prime numbers from the list of the combination

Step 4 : After that we will try to remove the element which is greater than a configurable threshold and not exceed a configurable limit

Step 5 :After thet try to see if there is any number which have more the k even numbers and if then remove that and also remove number which have consecutive repeating digits and palindromic substrings of length ≥ 3

tests = [

    	{
    		"name": "TC1 – Simple Ascending Digits",

    		"input": (137, 1, 1000, 2),

    		"expected": [3, 7, 13, 17, 37, 137, 173, 317]

            "my output": [3, 7, 13, 17, 31, 37, 71, 73, 137, 173, 317]
    	},

    	{

    		"name": "TC2 – Zero With Upper Bound Cut",

    		"input": (709, 1, 100, 2),

    		"expected": [7, 79]

            "my output": [7, 79, 97]
    	},

    	{

    		"name": "TC3 – Duplicate With Strict Order",

    		"input": (449, 1, 1000, 2),

    		"expected": []

            "my output": []
    	},

    	{

    		"name": "TC4 – Even Digit Saturation",

    		"input": (864, 1, 1000, 1),

    		"expected": []

            "my output": []
    	},

    	{

    		"name": "TC5 – High Lower Bound",

    		"input": (379, 100, 1000, 2),

    		"expected": [379, 397, 739, 937]

            "my output": [379, 397, 739, 937]
    	},

    	{

    		"name": "TC6 – Palindrome Source, Safe Outputs",

    		"input": (272, 1, 1000, 1),

    		"expected": [2, 7]

            "my output": [2, 7]
    	},

    	{

    		"name": "TC7 – Multi-Zero Handling",

    		"input": (1009, 1, 1000, 1),

    		"expected": [19, 109]

            "my output": [19, 109]

    	},

    	{

    		"name": "TC8 – Tight Window With Rejection",

    		"input": (681, 10, 50, 1),

    		"expected": []

            "my output": []
    	},

    	{

    		"name": "TC9 – Large Digits, Safe Prime",

    		"input": (149, 1, 500, 2),

    		"expected": [19, 149, 419, 491]

            "my output": [19, 41, 149, 419, 491]
    	},

    	{

    		"name": "TC10 – Single Valid Construction",

    		"input": (358, 1, 200, 2),

    		"expected": [3, 5]

            "my output": [3, 5, 53, 83]
    	}

    ]
