# Project_02
**PhonePe Pulse - Data**

The digital payments scene in India has truly transformed the country's economic landscape, thanks to widespread mobile adoption and a solid financial framework. Since its launch in 2016, PhonePe has taken the lead in the API-led digitalization of payments across the nation. Committed to enhancing transparency and innovation, PhonePe now offers anonymized, comprehensive datasets that illuminate the intricacies of digital transactions. These datasets are made freely available under the CDLA-Permissive-2.0 license, inviting developers and data enthusiasts to explore and expand on this rich information resource.

**Announcements**
•	New Release - 2024 Q1 Data: Fresh datasets for January, February, and March 2024 have been published and are now available for detailed analysis.

**Table of Contents**
1.	PhonePe Pulse - Data
2.	Announcements
3.	Goal
4.	Guide
5.	Documentation
6.	Comprehensive Folder Structure
7.	Detailed JSON Structure / Syntax
8.	Aggregated Data
9.	Map Data
10.	Top Data
11.	FAQs
12.	LICENSE
    
**Goal**
Our mission is to democratize the availability of digital payment data, allowing researchers, developers, and analysts to derive meaningful insights and foster innovation in fintech across India and globally.

**Guide**
This data has been structured to provide details of following three sections with data cuts on Transactions, Users and Insurance of PhonePe Pulse - Explore tab.
1.	Aggregated - Aggregated values of various payment categories as shown under Categories section
2.	Map - Total values at the State and District levels.
3.	Top - Totals of top States / Districts /Pin Codes
All the data provided in these folders is of JSON format. For more details on the structure/syntax you can refer to the JSON Structure / Syntax section of the documentation.

**Documentation**
Comprehensive Folder Structure
The data is organized into specific categories and regions, covering extensive temporal spans from 2018 to 2024, broken down by quarters for granular analysis:
markdown
Copy code
data
|___ aggregated
|   |___ transactions
|   |   |___ country
|   |       |___ india
|   |           |___ yearly (2018-2024)
|   |___ user
|   |   |___ country
|   |       |___ india
|   |           |___ yearly (2018-2024)
|   |___ insurance
|       |___ country
|           |___ india
|               |___ yearly (2018-2024)
|
|___ map
|   |___ transactions
|   |   |___ hover
|   |       |___ country
|   |           |___ india
|   |               |___ yearly (2018-2024)
|   |___ user
|   |   |___ hover
|   |       |___ country
|   |           |___ india
|   |               |___ yearly (2018-2024)
|   |___ insurance
|       |___ hover
|           |___ country
|               |___ india
|                   |___ yearly (2018-2024)
|
|___ top
|   |___ transactions
|   |   |___ country
|   |       |___ india
|   |           |___ yearly (2018-2024)
|   |___ user
|   |   |___ country
|   |       |___ india
|   |           |___ yearly (2018-2024)
|   |___ insurance
|       |___ country
|           |___ india
|               |___ yearly (2018-2024)

**JSON Structure / Syntax**
1. Aggregated
1.1 data/aggregated/transaction/country/india/2018/1.json
Transaction data broken down by type of payment at country level.
For complete details on syntax find the comments in below code
NOTE: Similar syntax is followed for state level too. Ex: data/aggregated/transaction/country/india/state/delhi/2018/1.json
{
    "success": true, //Ignore. For internal use only
    "code": "SUCCESS", //Ignore. For internal use only
    "data": {
        "from": 1514745000000, //Data duration
        "to": 1522175400000,
        "transactionData": [
            {
                "name": "Recharge & bill payments", //Type of payment category
                "paymentInstruments": [
                    {
                        "type": "TOTAL",
                        "count": 72550406, //Total number of transactions for the above payment category
                        "amount": 1.4472713558652578E10 //Total value
                    }
                ]
            },
            
            ...,

            ...,
                        
            {
                "name": "Others",
                "paymentInstruments": [
                    {
                        "type": "TOTAL",
                        "count": 5761576,
                        "amount": 4.643217301269438E9
                    }
                ]
            }
        ]
    },
    "responseTimestamp": 1630346628866 //Ignore. For internal use only.
}
1.2 data/aggregated/user/country/india/2021/1.json
Users data broken down by devices at country level.
For complete details on syntax find the comments in below code
NOTE: Similar syntax is followed for state level too. Ex: data/aggregated/user/country/india/state/delhi/2021/1.json
{
    "success": true, //Ignore. For internal use only.
    "code": "SUCCESS", //Ignore. For internal use only.
    "data": {
        "aggregated": {
            "registeredUsers": 284985430, //Total number of registered users for the selected quarter.
            "appOpens": 8635508502 //Number of app opens by users for the selected quarter
        },
        "usersByDevice": [ //Users by individual device
            {
                "brand": "Xiaomi", //Brand name of the device
                "count": 71553154, //Number of registered users by this brand.
                "percentage": 0.2510765339828075 //Percentage of share of current device type compared to all devices.
            },
            
            ...,

            ...,

            {
                "brand": "Others", //All unrecognized device types grouped here. 
                "count": 23564639, //Number of registered users by all unrecognized device types.
                "percentage": 0.08268717105993804 //Percentage of share of all unrecognized device types compared to overall devices that users are registered with.
            }
        ]
    },
    "responseTimestamp": 1630346630074 //Ignore. For internal use only.
}
1.3 data/aggregated/insurance/country/india/2021/1.json
Insurance data at country level.
For complete details on syntax find the comments in below code
NOTE: Similar syntax is followed for state level too. Ex: data/aggregated/insurance/country/india/state/delhi/2021/1.json
{
    "success": true, //Ignore. For internal use only
    "code": "SUCCESS", //Ignore. For internal use only
    "data": {
        "from": 1609439400000, //Data duration
        "to": 1616869800000,
        "transactionData": [
            {
                "name": "Insurance", //Type of payment category
                "paymentInstruments": [
                    {
                        "type": "TOTAL",
                        "count": 318119, //Total number of insurance done for the above duration
                        "amount": 1.206307024 //Total value
                    }
                ]
            },
        ]
    },
    "responseTimestamp": 1630346628866 //Ignore. For internal use only.
}
2. Map
2.1 data/map/transaction/hover/country/india/2021/1.json
Total number of transactions and total value of all transactions at the state level.
For complete details on syntax find the comments in below code
NOTE: Similar syntax is followed for district level too. Ex: data/map/transaction/hover/country/india/state/delhi/2021/1.json
{
    "success": true, //Ignore. For internal use only.
    "code": "SUCCESS", //Ignore. For internal use only.
    "data": {
        "hoverDataList": [ //Internally, this being used to show state/district level data whenever a user hovers on a particular state/district.
            {
                "name": "puducherry", //State / district name
                "metric": [
                    {
                        "type": "TOTAL", 
                        "count": 3309432, //Total number of transactions done within the selected year-quarter for the current state/district.
                        "amount": 5.899309571743641E9 //Total transaction value within the selected year-quarter for the current state/district.
                    }
                ]
            },

            ...,

            ...,

            {
                "name": "tamil nadu",
                "metric": [
                    {
                        "type": "TOTAL",
                        "count": 136556674,
                        "amount": 2.4866814387365314E11
                    }
                ]
            }            
        ]
    },
    "responseTimestamp": 1630346628834 //Ignore. For internal use only.
}
2.2 data/map/user/hover/country/india/2021/1.json
Total number of registered users and number of app opens by these registered users at the state level.
For complete details on syntax find the comments in below code
NOTE: Similar syntax is followed for district level too. Ex: data/map/user/hover/country/india/state/delhi/2021/1.json
{
    "success": true, //Ignore. For internal use only.
    "code": "SUCCESS", //Ignore. For internal use only.
    "data": {
        "hoverData": { //Internally, this being used to show state/district level data whenever a user hovers on a particular state/district.
            "puducherry": {
                "registeredUsers": 346279, //Total number of registered users for the selected state/district
                "appOpens": 7914507 //Total number of app opens by the registered users for the selected state/district
            },

            ...,

            ...,

            "tamil nadu": {
                "registeredUsers": 16632608,
                "appOpens": 348801714
            }
        }
    },
    "responseTimestamp": 1630346628866 //Ignore. For internal use only.
}
2.3 data/map/insurance/hover/country/india/2021/1.json
Total number of insurance and total value of all insurance at the state level.
For complete details on syntax find the comments in below code
NOTE: Similar syntax is followed for district level too. Ex: data/map/insurance/hover/country/india/state/delhi/2021/1.json
{
    "success": true, //Ignore. For internal use only.
    "code": "SUCCESS", //Ignore. For internal use only.
    "data": {
        "hoverDataList": [ //Internally, this being used to show state/district level data whenever a user hovers on a particular state/district.
            {
                "name": "puducherry", //State / district name
                "metric": [
                    {
                        "type": "TOTAL", 
                        "count": 3309432, //Total number of insurance done within the selected year-quarter for the current state/district.
                        "amount": 5.899309571743641E9 //Total insurance value within the selected year-quarter for the current state/district.
                    }
                ]
            },

            ...,

            ...,

            {
                "name": "tamil nadu",
                "metric": [
                    {
                        "type": "TOTAL",
                        "count": 136556674,
                        "amount": 2.4866814387365314E11
                    }
                ]
            }            
        ]
    },
    "responseTimestamp": 1630346628834 //Ignore. For internal use only.
}
3. Top
3.1 data/top/transaction/country/india/2021/1.json
Top 10 states / districts / pin codes where the most number of the transactions happened for a selected year-quarter combination.
For complete details on syntax find the comments in below code
NOTE: Similar syntax is followed for state level too. The only exception is, it won't have data for states. Ex: data/top/transaction/country/india/state/delhi/2021/1.json
{
    "success": true, //Ignore. For internal use only.
    "code": "SUCCESS", //Ignore. For internal use only.
    "data": {
        "states": [ //List of states where most number of transactions happened along with total value for a selected year-quarter combination.
            {
                "entityName": "karnataka", // State name
                "metric": {
                    "type": "TOTAL",
                    "count": 523797492, //Total number of transactions
                    "amount": 7.549953574123948E11 //Total value of all transactions
                }
            },
            
            ...,
        ],
        "districts": [ //List of districts where most number of transactions happened along with total value for a selected year-quarter combination.
            {
                "entityName": "bengaluru urban", //District name
                "metric": {
                    "type": "TOTAL",
                    "count": 348712787, //Total number of transactions
                    "amount": 4.324013412317671E11 //Total value of all transactions
                }
            },
            
            ...,
        ],
        "pincodes": [ //List of pin codes where most number of transactions happened along with total value for a selected year-quarter combination.
            {
                "entityName": "560001", //Pin code
                "metric": {
                    "type": "TOTAL",
                    "count": 111898471, //Total number of transactions
                    "amount": 1.5427512629157785E11 //Total value of all transactions
                }
            },
            
            ...,
        ]
    },
    "responseTimestamp": 1630346629360 //Ignore. For internal use only.
}
3.2 data/top/user/country/india/2021/1.json
Top 10 states / districts / pin codes where most number of users registered from, for a selected year-quarter combination.
For complete details on syntax find the comments in below code
NOTE: Similar syntax is followed for state level too. The only exception is, it won't have data for states. Ex: data/top/user/country/india/state/delhi/2021/1.json
{
    "success": true, //Ignore. For internal use only.
    "code": "SUCCESS", //Ignore. For internal use only.
    "data": {
        "states": [ //List of states where the most number of users registered from, for a selected year-quarter combination.
            {
                "name": "maharashtra", //State name
                "registeredUsers": 37077537 //Number of registered users
            },
            
            ...,
        ],
        "districts": [ //List of districts where the most number of users registered from, for a selected year-quarter combination.
            {
                "name": "bengaluru urban", //State name
                "registeredUsers": 9955387 //Number of registered users
            },
            
            ...,
        ],
        "pincodes": [ //List of pin codes where most number of users registered from, for a selected year-quarter combination.
            {
                "name": "201301", //Pin code
                "registeredUsers": 541127 //Number of registered users
            },
            
            ...,
        ]
    },
    "responseTimestamp": 1630346630074 //Ignore. For internal use only.
}
3.3 data/top/insurance/country/india/2021/1.json
Top 10 states / districts / pin codes where the most number of the insurance happened for a selected year-quarter combination.
For complete details on syntax find the comments in below code
NOTE: Similar syntax is followed for state level too. The only exception is, it won't have data for states. Ex: data/top/insurance/country/india/state/delhi/2021/1.json
{
    "success": true, //Ignore. For internal use only.
    "code": "SUCCESS", //Ignore. For internal use only.
    "data": {
        "states": [ //List of states where most number of insurance happened along with total value for a selected year-quarter combination.
            {
                "entityName": "karnataka", // State name
                "metric": {
                    "type": "TOTAL",
                    "count": 523797492, //Total number of insurance
                    "amount": 7.549953574123948E11 //Total value of all insurance
                }
            },
            
            ...,
        ],
        "districts": [ //List of districts where most number of insurance happened along with total value for a selected year-quarter combination.
            {
                "entityName": "bengaluru urban", //District name
                "metric": {
                    "type": "TOTAL",
                    "count": 348712787, //Total number of insurance
                    "amount": 4.324013412317671E11 //Total value of all insurance
                }
            },
            
            ...,
        ],
        "pincodes": [ //List of pin codes where most number of insurance happened along with total value for a selected year-quarter combination.
            {
                "entityName": "560001", //Pin code
                "metric": {
                    "type": "TOTAL",
                    "count": 111898471, //Total number of insurance
                    "amount": 1.5427512629157785E11 //Total value of all insurance
                }
            },
            
            ...,
        ]
    },
    "responseTimestamp": 1630346629360 //Ignore. For internal use only.
}

**FAQs**
•	Data Update Frequency: How often is the dataset updated? Quarterly updates are provided to ensure timeliness and relevance.
•	Reporting Issues: How can I report data issues or inaccuracies? Please submit any issues through our dedicated GitHub repository issue tracker.

**LICENSE**
This project is shared under the Community Data License Agreement – Permissive – Version 2.0, designed to ensure wide accessibility while protecting the integrity of the dataset.


