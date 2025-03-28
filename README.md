Liturgical Calendar API
============

Liturgical Calendar is a simple tool for getting the dates of the Liturgical Calendar. It returns the dates of the Liturgical Calendar for a given year.

![Build Status](https://img.shields.io/badge/build-passing-green)
![Code Climate](https://img.shields.io/badge/maintainability-B-purple)
![Prod Ready](https://img.shields.io/badge/production-ready-blue)

This is a Python API Wrapper for the [Liturgical Calendar API](https://apiverve.com/marketplace/api/liturgicalcalendar)

---

## Installation
	pip install apiverve-liturgicalcalendar

---

## Configuration

Before using the liturgicalcalendar API client, you have to setup your account and obtain your API Key.  
You can get it by signing up at [https://apiverve.com](https://apiverve.com)

---

## Usage

The Liturgical Calendar API documentation is found here: [https://docs.apiverve.com/api/liturgicalcalendar](https://docs.apiverve.com/api/liturgicalcalendar).  
You can find parameters, example responses, and status codes documented here.

### Setup

```
# Import the client module
from apiverve_liturgicalcalendar.apiClient import LiturgicalcalendarAPIClient

# Initialize the client with your APIVerve API key
api = LiturgicalcalendarAPIClient("[YOUR_API_KEY]")
```

---


### Perform Request
Using the API client, you can perform requests to the API.

###### Define Query

```
query = { "month": 02,  "year": 2025 }
```

###### Simple Request

```
# Make a request to the API
result = api.execute(query)

# Print the result
print(result)
```

###### Example Response

```
{
  "status": "ok",
  "error": null,
  "data": {
    "2025-03-01": [
      {
        "id": "ordinary_time_7_saturday",
        "date": "2025-03-01",
        "dateDef": {
          "dateFn": "dateOfOrdinaryTime",
          "dateArgs": [
            6,
            7
          ],
          "yearOffset": 0
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "WEEKDAY_13",
        "rank": "WEEKDAY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": false,
        "i18nDef": [
          "seasons:ordinary_time.weekday",
          {
            "week": 7,
            "dow": 6
          }
        ],
        "seasons": [
          "ORDINARY_TIME"
        ],
        "periods": [
          "EARLY_ORDINARY_TIME"
        ],
        "colors": [
          "GREEN"
        ],
        "commonsDef": [],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 7,
          "dayOfSeason": 48,
          "dayOfWeek": 6,
          "nthDayOfWeekInMonth": 1,
          "startOfSeason": "2025-01-13",
          "endOfSeason": "2025-11-29",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "ORDINARY_TIME"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_TIME",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_3"
        },
        "fromCalendarId": "ProperOfTime",
        "fromExtendedCalendars": []
      }
    ],
    "2025-03-02": [
      {
        "id": "ordinary_time_8_sunday",
        "date": "2025-03-02",
        "dateDef": {
          "dateFn": "dateOfOrdinaryTime",
          "dateArgs": [
            0,
            8
          ],
          "yearOffset": 0
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "UNPRIVILEGED_SUNDAY_6",
        "rank": "SUNDAY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": true,
        "isOptional": false,
        "i18nDef": [
          "seasons:ordinary_time.sunday",
          {
            "week": 8
          }
        ],
        "seasons": [
          "ORDINARY_TIME"
        ],
        "periods": [
          "EARLY_ORDINARY_TIME"
        ],
        "colors": [
          "GREEN"
        ],
        "commonsDef": [],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 8,
          "dayOfSeason": 49,
          "dayOfWeek": 0,
          "nthDayOfWeekInMonth": 1,
          "startOfSeason": "2025-01-13",
          "endOfSeason": "2025-11-29",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "ORDINARY_TIME"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_TIME",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_4"
        },
        "fromCalendarId": "ProperOfTime",
        "fromExtendedCalendars": []
      }
    ],
    "2025-03-03": [
      {
        "id": "ordinary_time_8_monday",
        "date": "2025-03-03",
        "dateDef": {
          "dateFn": "dateOfOrdinaryTime",
          "dateArgs": [
            1,
            8
          ],
          "yearOffset": 0
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "WEEKDAY_13",
        "rank": "WEEKDAY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": false,
        "i18nDef": [
          "seasons:ordinary_time.weekday",
          {
            "week": 8,
            "dow": 1
          }
        ],
        "seasons": [
          "ORDINARY_TIME"
        ],
        "periods": [
          "EARLY_ORDINARY_TIME"
        ],
        "colors": [
          "GREEN"
        ],
        "commonsDef": [],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 8,
          "dayOfSeason": 50,
          "dayOfWeek": 1,
          "nthDayOfWeekInMonth": 1,
          "startOfSeason": "2025-01-13",
          "endOfSeason": "2025-11-29",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "ORDINARY_TIME"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_TIME",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_4"
        },
        "fromCalendarId": "ProperOfTime",
        "fromExtendedCalendars": []
      }
    ],
    "2025-03-04": [
      {
        "id": "ordinary_time_8_tuesday",
        "date": "2025-03-04",
        "dateDef": {
          "dateFn": "dateOfOrdinaryTime",
          "dateArgs": [
            2,
            8
          ],
          "yearOffset": 0
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "WEEKDAY_13",
        "rank": "WEEKDAY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": false,
        "i18nDef": [
          "seasons:ordinary_time.weekday",
          {
            "week": 8,
            "dow": 2
          }
        ],
        "seasons": [
          "ORDINARY_TIME"
        ],
        "periods": [
          "EARLY_ORDINARY_TIME"
        ],
        "colors": [
          "GREEN"
        ],
        "commonsDef": [],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 8,
          "dayOfSeason": 51,
          "dayOfWeek": 2,
          "nthDayOfWeekInMonth": 1,
          "startOfSeason": "2025-01-13",
          "endOfSeason": "2025-11-29",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "ORDINARY_TIME"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_TIME",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_4"
        },
        "fromCalendarId": "ProperOfTime",
        "fromExtendedCalendars": []
      },
      {
        "id": "casimir_of_poland",
        "date": "2025-03-04",
        "dateDef": {
          "month": 3,
          "date": 4
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "OPTIONAL_MEMORIAL_12",
        "rank": "OPTIONAL_MEMORIAL",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": true,
        "i18nDef": [
          "names:casimir_of_poland"
        ],
        "seasons": [
          "ORDINARY_TIME"
        ],
        "periods": [
          "EARLY_ORDINARY_TIME"
        ],
        "colors": [
          "WHITE"
        ],
        "commonsDef": [
          "Saints"
        ],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 8,
          "dayOfSeason": 51,
          "dayOfWeek": 2,
          "nthDayOfWeekInMonth": 1,
          "startOfSeason": "2025-01-13",
          "endOfSeason": "2025-11-29",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "ORDINARY_TIME"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_SAINTS",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_4"
        },
        "fromCalendarId": "ma",
        "fromExtendedCalendars": [],
        "weekday": {
          "id": "ordinary_time_8_tuesday",
          "date": "2025-03-04",
          "dateDef": {
            "dateFn": "dateOfOrdinaryTime",
            "dateArgs": [
              2,
              8
            ],
            "yearOffset": 0
          },
          "dateExceptions": [],
          "alternativeTransferDateDefs": [],
          "precedence": "WEEKDAY_13",
          "rank": "WEEKDAY",
          "allowSimilarRankItems": false,
          "isHolyDayOfObligation": false,
          "isOptional": false,
          "i18nDef": [
            "seasons:ordinary_time.weekday",
            {
              "week": 8,
              "dow": 2
            }
          ],
          "seasons": [
            "ORDINARY_TIME"
          ],
          "periods": [
            "EARLY_ORDINARY_TIME"
          ],
          "colors": [
            "GREEN"
          ],
          "commonsDef": [],
          "martyrology": [],
          "titles": [],
          "calendar": {
            "weekOfSeason": 8,
            "dayOfSeason": 51,
            "dayOfWeek": 2,
            "nthDayOfWeekInMonth": 1,
            "startOfSeason": "2025-01-13",
            "endOfSeason": "2025-11-29",
            "startOfLiturgicalYear": "2024-12-01",
            "endOfLiturgicalYear": "2025-11-29",
            "seasons": [
              "ORDINARY_TIME"
            ]
          },
          "cycles": {
            "properCycle": "PROPER_OF_TIME",
            "sundayCycle": "YEAR_C",
            "weekdayCycle": "YEAR_1",
            "psalterWeek": "WEEK_4"
          },
          "fromCalendarId": "ProperOfTime",
          "fromExtendedCalendars": []
        }
      }
    ],
    "2025-03-05": [
      {
        "id": "ash_wednesday",
        "date": "2025-03-05",
        "dateDef": {
          "dateFn": "ashWednesday",
          "yearOffset": 0
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "ASH_WEDNESDAY_2",
        "rank": "WEEKDAY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": false,
        "i18nDef": [
          "names:ash_wednesday"
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [
          "PURPLE"
        ],
        "commonsDef": [],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 0,
          "dayOfSeason": 1,
          "dayOfWeek": 3,
          "nthDayOfWeekInMonth": 1,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_TIME",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_4"
        },
        "fromCalendarId": "ProperOfTime",
        "fromExtendedCalendars": []
      }
    ],
    "2025-03-06": [
      {
        "id": "thursday_after_ash_wednesday",
        "date": "2025-03-06",
        "dateDef": {
          "dateFn": "ashWednesday",
          "addDay": 1,
          "yearOffset": 0
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "PRIVILEGED_WEEKDAY_9",
        "rank": "WEEKDAY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": false,
        "i18nDef": [
          "seasons:lent.day_after_ash_wed",
          {
            "dow": 4
          }
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [
          "PURPLE"
        ],
        "commonsDef": [],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 0,
          "dayOfSeason": 2,
          "dayOfWeek": 4,
          "nthDayOfWeekInMonth": 1,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_TIME",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_4"
        },
        "fromCalendarId": "ProperOfTime",
        "fromExtendedCalendars": []
      }
    ],
    "2025-03-07": [
      {
        "id": "friday_after_ash_wednesday",
        "date": "2025-03-07",
        "dateDef": {
          "dateFn": "ashWednesday",
          "addDay": 2,
          "yearOffset": 0
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "PRIVILEGED_WEEKDAY_9",
        "rank": "WEEKDAY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": false,
        "i18nDef": [
          "seasons:lent.day_after_ash_wed",
          {
            "dow": 5
          }
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [
          "PURPLE"
        ],
        "commonsDef": [],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 0,
          "dayOfSeason": 3,
          "dayOfWeek": 5,
          "nthDayOfWeekInMonth": 1,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_TIME",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_4"
        },
        "fromCalendarId": "ProperOfTime",
        "fromExtendedCalendars": []
      },
      {
        "id": "perpetua_of_carthage_and_felicity_of_carthage_martyrs",
        "date": "2025-03-07",
        "dateDef": {
          "month": 3,
          "date": 7
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "GENERAL_MEMORIAL_10",
        "rank": "MEMORIAL",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": true,
        "i18nDef": [
          "names:perpetua_of_carthage_and_felicity_of_carthage_martyrs"
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [],
        "commonsDef": [
          "None"
        ],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 0,
          "dayOfSeason": 3,
          "dayOfWeek": 5,
          "nthDayOfWeekInMonth": 1,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_SAINTS",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_4"
        },
        "fromCalendarId": "ma",
        "fromExtendedCalendars": [],
        "weekday": {
          "id": "friday_after_ash_wednesday",
          "date": "2025-03-07",
          "dateDef": {
            "dateFn": "ashWednesday",
            "addDay": 2,
            "yearOffset": 0
          },
          "dateExceptions": [],
          "alternativeTransferDateDefs": [],
          "precedence": "PRIVILEGED_WEEKDAY_9",
          "rank": "WEEKDAY",
          "allowSimilarRankItems": false,
          "isHolyDayOfObligation": false,
          "isOptional": false,
          "i18nDef": [
            "seasons:lent.day_after_ash_wed",
            {
              "dow": 5
            }
          ],
          "seasons": [
            "LENT"
          ],
          "periods": [
            "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
          ],
          "colors": [
            "PURPLE"
          ],
          "commonsDef": [],
          "martyrology": [],
          "titles": [],
          "calendar": {
            "weekOfSeason": 0,
            "dayOfSeason": 3,
            "dayOfWeek": 5,
            "nthDayOfWeekInMonth": 1,
            "startOfSeason": "2025-03-05",
            "endOfSeason": "2025-04-17",
            "startOfLiturgicalYear": "2024-12-01",
            "endOfLiturgicalYear": "2025-11-29",
            "seasons": [
              "LENT"
            ]
          },
          "cycles": {
            "properCycle": "PROPER_OF_TIME",
            "sundayCycle": "YEAR_C",
            "weekdayCycle": "YEAR_1",
            "psalterWeek": "WEEK_4"
          },
          "fromCalendarId": "ProperOfTime",
          "fromExtendedCalendars": []
        }
      }
    ],
    "2025-03-08": [
      {
        "id": "saturday_after_ash_wednesday",
        "date": "2025-03-08",
        "dateDef": {
          "dateFn": "ashWednesday",
          "addDay": 3,
          "yearOffset": 0
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "PRIVILEGED_WEEKDAY_9",
        "rank": "WEEKDAY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": false,
        "i18nDef": [
          "seasons:lent.day_after_ash_wed",
          {
            "dow": 6
          }
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [
          "PURPLE"
        ],
        "commonsDef": [],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 0,
          "dayOfSeason": 4,
          "dayOfWeek": 6,
          "nthDayOfWeekInMonth": 2,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_TIME",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_4"
        },
        "fromCalendarId": "ProperOfTime",
        "fromExtendedCalendars": []
      },
      {
        "id": "john_of_god_duarte_cidade_religious",
        "date": "2025-03-08",
        "dateDef": {
          "month": 3,
          "date": 8
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "OPTIONAL_MEMORIAL_12",
        "rank": "OPTIONAL_MEMORIAL",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": true,
        "i18nDef": [
          "names:john_of_god_duarte_cidade_religious"
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [],
        "commonsDef": [
          "Religious",
          "MercyWorkers"
        ],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 0,
          "dayOfSeason": 4,
          "dayOfWeek": 6,
          "nthDayOfWeekInMonth": 2,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_SAINTS",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_4"
        },
        "fromCalendarId": "ma",
        "fromExtendedCalendars": [],
        "weekday": {
          "id": "saturday_after_ash_wednesday",
          "date": "2025-03-08",
          "dateDef": {
            "dateFn": "ashWednesday",
            "addDay": 3,
            "yearOffset": 0
          },
          "dateExceptions": [],
          "alternativeTransferDateDefs": [],
          "precedence": "PRIVILEGED_WEEKDAY_9",
          "rank": "WEEKDAY",
          "allowSimilarRankItems": false,
          "isHolyDayOfObligation": false,
          "isOptional": false,
          "i18nDef": [
            "seasons:lent.day_after_ash_wed",
            {
              "dow": 6
            }
          ],
          "seasons": [
            "LENT"
          ],
          "periods": [
            "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
          ],
          "colors": [
            "PURPLE"
          ],
          "commonsDef": [],
          "martyrology": [],
          "titles": [],
          "calendar": {
            "weekOfSeason": 0,
            "dayOfSeason": 4,
            "dayOfWeek": 6,
            "nthDayOfWeekInMonth": 2,
            "startOfSeason": "2025-03-05",
            "endOfSeason": "2025-04-17",
            "startOfLiturgicalYear": "2024-12-01",
            "endOfLiturgicalYear": "2025-11-29",
            "seasons": [
              "LENT"
            ]
          },
          "cycles": {
            "properCycle": "PROPER_OF_TIME",
            "sundayCycle": "YEAR_C",
            "weekdayCycle": "YEAR_1",
            "psalterWeek": "WEEK_4"
          },
          "fromCalendarId": "ProperOfTime",
          "fromExtendedCalendars": []
        }
      }
    ],
    "2025-03-09": [
      {
        "id": "lent_1_sunday",
        "date": "2025-03-09",
        "dateDef": {
          "dateFn": "ashWednesday",
          "addDay": 4,
          "yearOffset": 0
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "PRIVILEGED_SUNDAY_2",
        "rank": "SUNDAY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": true,
        "isOptional": false,
        "i18nDef": [
          "seasons:lent.sunday",
          {
            "week": 1
          }
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [
          "PURPLE"
        ],
        "commonsDef": [],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 1,
          "dayOfSeason": 5,
          "dayOfWeek": 0,
          "nthDayOfWeekInMonth": 2,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_TIME",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_1"
        },
        "fromCalendarId": "ProperOfTime",
        "fromExtendedCalendars": []
      }
    ],
    "2025-03-10": [
      {
        "id": "lent_1_monday",
        "date": "2025-03-10",
        "dateDef": {
          "dateFn": "ashWednesday",
          "addDay": 5,
          "yearOffset": 0
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "PRIVILEGED_WEEKDAY_9",
        "rank": "WEEKDAY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": false,
        "i18nDef": [
          "seasons:lent.weekday",
          {
            "week": 1,
            "dow": 1
          }
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [
          "PURPLE"
        ],
        "commonsDef": [],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 1,
          "dayOfSeason": 6,
          "dayOfWeek": 1,
          "nthDayOfWeekInMonth": 2,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_TIME",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_1"
        },
        "fromCalendarId": "ProperOfTime",
        "fromExtendedCalendars": []
      }
    ],
    "2025-03-11": [
      {
        "id": "lent_1_tuesday",
        "date": "2025-03-11",
        "dateDef": {
          "dateFn": "ashWednesday",
          "addDay": 6,
          "yearOffset": 0
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "PRIVILEGED_WEEKDAY_9",
        "rank": "WEEKDAY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": false,
        "i18nDef": [
          "seasons:lent.weekday",
          {
            "week": 1,
            "dow": 2
          }
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [
          "PURPLE"
        ],
        "commonsDef": [],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 1,
          "dayOfSeason": 7,
          "dayOfWeek": 2,
          "nthDayOfWeekInMonth": 2,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_TIME",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_1"
        },
        "fromCalendarId": "ProperOfTime",
        "fromExtendedCalendars": []
      }
    ],
    "2025-03-12": [
      {
        "id": "lent_1_wednesday",
        "date": "2025-03-12",
        "dateDef": {
          "dateFn": "ashWednesday",
          "addDay": 7,
          "yearOffset": 0
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "PRIVILEGED_WEEKDAY_9",
        "rank": "WEEKDAY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": false,
        "i18nDef": [
          "seasons:lent.weekday",
          {
            "week": 1,
            "dow": 3
          }
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [
          "PURPLE"
        ],
        "commonsDef": [],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 1,
          "dayOfSeason": 8,
          "dayOfWeek": 3,
          "nthDayOfWeekInMonth": 2,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_TIME",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_1"
        },
        "fromCalendarId": "ProperOfTime",
        "fromExtendedCalendars": []
      }
    ],
    "2025-03-13": [
      {
        "id": "lent_1_thursday",
        "date": "2025-03-13",
        "dateDef": {
          "dateFn": "ashWednesday",
          "addDay": 8,
          "yearOffset": 0
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "PRIVILEGED_WEEKDAY_9",
        "rank": "WEEKDAY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": false,
        "i18nDef": [
          "seasons:lent.weekday",
          {
            "week": 1,
            "dow": 4
          }
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [
          "PURPLE"
        ],
        "commonsDef": [],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 1,
          "dayOfSeason": 9,
          "dayOfWeek": 4,
          "nthDayOfWeekInMonth": 2,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_TIME",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_1"
        },
        "fromCalendarId": "ProperOfTime",
        "fromExtendedCalendars": []
      }
    ],
    "2025-03-14": [
      {
        "id": "lent_1_friday",
        "date": "2025-03-14",
        "dateDef": {
          "dateFn": "ashWednesday",
          "addDay": 9,
          "yearOffset": 0
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "PRIVILEGED_WEEKDAY_9",
        "rank": "WEEKDAY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": false,
        "i18nDef": [
          "seasons:lent.weekday",
          {
            "week": 1,
            "dow": 5
          }
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [
          "PURPLE"
        ],
        "commonsDef": [],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 1,
          "dayOfSeason": 10,
          "dayOfWeek": 5,
          "nthDayOfWeekInMonth": 2,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_TIME",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_1"
        },
        "fromCalendarId": "ProperOfTime",
        "fromExtendedCalendars": []
      }
    ],
    "2025-03-15": [
      {
        "id": "lent_1_saturday",
        "date": "2025-03-15",
        "dateDef": {
          "dateFn": "ashWednesday",
          "addDay": 10,
          "yearOffset": 0
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "PRIVILEGED_WEEKDAY_9",
        "rank": "WEEKDAY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": false,
        "i18nDef": [
          "seasons:lent.weekday",
          {
            "week": 1,
            "dow": 6
          }
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [
          "PURPLE"
        ],
        "commonsDef": [],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 1,
          "dayOfSeason": 11,
          "dayOfWeek": 6,
          "nthDayOfWeekInMonth": 3,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_TIME",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_1"
        },
        "fromCalendarId": "ProperOfTime",
        "fromExtendedCalendars": []
      }
    ],
    "2025-03-16": [
      {
        "id": "lent_2_sunday",
        "date": "2025-03-16",
        "dateDef": {
          "dateFn": "ashWednesday",
          "addDay": 11,
          "yearOffset": 0
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "PRIVILEGED_SUNDAY_2",
        "rank": "SUNDAY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": true,
        "isOptional": false,
        "i18nDef": [
          "seasons:lent.sunday",
          {
            "week": 2
          }
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [
          "PURPLE"
        ],
        "commonsDef": [],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 2,
          "dayOfSeason": 12,
          "dayOfWeek": 0,
          "nthDayOfWeekInMonth": 3,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_TIME",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_2"
        },
        "fromCalendarId": "ProperOfTime",
        "fromExtendedCalendars": []
      }
    ],
    "2025-03-17": [
      {
        "id": "lent_2_monday",
        "date": "2025-03-17",
        "dateDef": {
          "dateFn": "ashWednesday",
          "addDay": 12,
          "yearOffset": 0
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "PRIVILEGED_WEEKDAY_9",
        "rank": "WEEKDAY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": false,
        "i18nDef": [
          "seasons:lent.weekday",
          {
            "week": 2,
            "dow": 1
          }
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [
          "PURPLE"
        ],
        "commonsDef": [],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 2,
          "dayOfSeason": 13,
          "dayOfWeek": 1,
          "nthDayOfWeekInMonth": 3,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_TIME",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_2"
        },
        "fromCalendarId": "ProperOfTime",
        "fromExtendedCalendars": []
      },
      {
        "id": "patrick_of_ireland_bishop",
        "date": "2025-03-17",
        "dateDef": {
          "month": 3,
          "date": 17
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "OPTIONAL_MEMORIAL_12",
        "rank": "OPTIONAL_MEMORIAL",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": true,
        "i18nDef": [
          "names:patrick_of_ireland_bishop"
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [],
        "commonsDef": [
          "Missionaries",
          "Bishops"
        ],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 2,
          "dayOfSeason": 13,
          "dayOfWeek": 1,
          "nthDayOfWeekInMonth": 3,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_SAINTS",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_2"
        },
        "fromCalendarId": "ma",
        "fromExtendedCalendars": [],
        "weekday": {
          "id": "lent_2_monday",
          "date": "2025-03-17",
          "dateDef": {
            "dateFn": "ashWednesday",
            "addDay": 12,
            "yearOffset": 0
          },
          "dateExceptions": [],
          "alternativeTransferDateDefs": [],
          "precedence": "PRIVILEGED_WEEKDAY_9",
          "rank": "WEEKDAY",
          "allowSimilarRankItems": false,
          "isHolyDayOfObligation": false,
          "isOptional": false,
          "i18nDef": [
            "seasons:lent.weekday",
            {
              "week": 2,
              "dow": 1
            }
          ],
          "seasons": [
            "LENT"
          ],
          "periods": [
            "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
          ],
          "colors": [
            "PURPLE"
          ],
          "commonsDef": [],
          "martyrology": [],
          "titles": [],
          "calendar": {
            "weekOfSeason": 2,
            "dayOfSeason": 13,
            "dayOfWeek": 1,
            "nthDayOfWeekInMonth": 3,
            "startOfSeason": "2025-03-05",
            "endOfSeason": "2025-04-17",
            "startOfLiturgicalYear": "2024-12-01",
            "endOfLiturgicalYear": "2025-11-29",
            "seasons": [
              "LENT"
            ]
          },
          "cycles": {
            "properCycle": "PROPER_OF_TIME",
            "sundayCycle": "YEAR_C",
            "weekdayCycle": "YEAR_1",
            "psalterWeek": "WEEK_2"
          },
          "fromCalendarId": "ProperOfTime",
          "fromExtendedCalendars": []
        }
      }
    ],
    "2025-03-18": [
      {
        "id": "lent_2_tuesday",
        "date": "2025-03-18",
        "dateDef": {
          "dateFn": "ashWednesday",
          "addDay": 13,
          "yearOffset": 0
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "PRIVILEGED_WEEKDAY_9",
        "rank": "WEEKDAY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": false,
        "i18nDef": [
          "seasons:lent.weekday",
          {
            "week": 2,
            "dow": 2
          }
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [
          "PURPLE"
        ],
        "commonsDef": [],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 2,
          "dayOfSeason": 14,
          "dayOfWeek": 2,
          "nthDayOfWeekInMonth": 3,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_TIME",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_2"
        },
        "fromCalendarId": "ProperOfTime",
        "fromExtendedCalendars": []
      },
      {
        "id": "cyril_of_jerusalem_bishop",
        "date": "2025-03-18",
        "dateDef": {
          "month": 3,
          "date": 18
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "OPTIONAL_MEMORIAL_12",
        "rank": "OPTIONAL_MEMORIAL",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": true,
        "i18nDef": [
          "names:cyril_of_jerusalem_bishop"
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [],
        "commonsDef": [
          "Bishops",
          "DoctorsOfTheChurch"
        ],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 2,
          "dayOfSeason": 14,
          "dayOfWeek": 2,
          "nthDayOfWeekInMonth": 3,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_SAINTS",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_2"
        },
        "fromCalendarId": "ma",
        "fromExtendedCalendars": [],
        "weekday": {
          "id": "lent_2_tuesday",
          "date": "2025-03-18",
          "dateDef": {
            "dateFn": "ashWednesday",
            "addDay": 13,
            "yearOffset": 0
          },
          "dateExceptions": [],
          "alternativeTransferDateDefs": [],
          "precedence": "PRIVILEGED_WEEKDAY_9",
          "rank": "WEEKDAY",
          "allowSimilarRankItems": false,
          "isHolyDayOfObligation": false,
          "isOptional": false,
          "i18nDef": [
            "seasons:lent.weekday",
            {
              "week": 2,
              "dow": 2
            }
          ],
          "seasons": [
            "LENT"
          ],
          "periods": [
            "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
          ],
          "colors": [
            "PURPLE"
          ],
          "commonsDef": [],
          "martyrology": [],
          "titles": [],
          "calendar": {
            "weekOfSeason": 2,
            "dayOfSeason": 14,
            "dayOfWeek": 2,
            "nthDayOfWeekInMonth": 3,
            "startOfSeason": "2025-03-05",
            "endOfSeason": "2025-04-17",
            "startOfLiturgicalYear": "2024-12-01",
            "endOfLiturgicalYear": "2025-11-29",
            "seasons": [
              "LENT"
            ]
          },
          "cycles": {
            "properCycle": "PROPER_OF_TIME",
            "sundayCycle": "YEAR_C",
            "weekdayCycle": "YEAR_1",
            "psalterWeek": "WEEK_2"
          },
          "fromCalendarId": "ProperOfTime",
          "fromExtendedCalendars": []
        }
      }
    ],
    "2025-03-19": [
      {
        "id": "joseph_spouse_of_mary",
        "date": "2025-03-19",
        "dateDef": {
          "month": 3,
          "date": 19
        },
        "dateExceptions": [
          {
            "ifIsDayOfWeek": 0,
            "setDate": {
              "addDay": 1
            }
          },
          {
            "ifIsBetween": {
              "from": {
                "dateFn": "palmSunday"
              },
              "to": {
                "dateFn": "divineMercySunday"
              },
              "inclusive": true
            },
            "setDate": {
              "dateFn": "palmSunday",
              "subtractDay": 1
            }
          }
        ],
        "alternativeTransferDateDefs": [],
        "precedence": "GENERAL_SOLEMNITY_3",
        "rank": "SOLEMNITY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": true,
        "isOptional": false,
        "i18nDef": [
          "names:joseph_spouse_of_mary"
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [
          "WHITE"
        ],
        "commonsDef": [
          "None"
        ],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 2,
          "dayOfSeason": 15,
          "dayOfWeek": 3,
          "nthDayOfWeekInMonth": 3,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_SAINTS",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_2"
        },
        "fromCalendarId": "ma",
        "fromExtendedCalendars": []
      }
    ],
    "2025-03-20": [
      {
        "id": "lent_2_thursday",
        "date": "2025-03-20",
        "dateDef": {
          "dateFn": "ashWednesday",
          "addDay": 15,
          "yearOffset": 0
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "PRIVILEGED_WEEKDAY_9",
        "rank": "WEEKDAY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": false,
        "i18nDef": [
          "seasons:lent.weekday",
          {
            "week": 2,
            "dow": 4
          }
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [
          "PURPLE"
        ],
        "commonsDef": [],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 2,
          "dayOfSeason": 16,
          "dayOfWeek": 4,
          "nthDayOfWeekInMonth": 3,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_TIME",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_2"
        },
        "fromCalendarId": "ProperOfTime",
        "fromExtendedCalendars": []
      }
    ],
    "2025-03-21": [
      {
        "id": "lent_2_friday",
        "date": "2025-03-21",
        "dateDef": {
          "dateFn": "ashWednesday",
          "addDay": 16,
          "yearOffset": 0
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "PRIVILEGED_WEEKDAY_9",
        "rank": "WEEKDAY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": false,
        "i18nDef": [
          "seasons:lent.weekday",
          {
            "week": 2,
            "dow": 5
          }
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [
          "PURPLE"
        ],
        "commonsDef": [],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 2,
          "dayOfSeason": 17,
          "dayOfWeek": 5,
          "nthDayOfWeekInMonth": 3,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_TIME",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_2"
        },
        "fromCalendarId": "ProperOfTime",
        "fromExtendedCalendars": []
      }
    ],
    "2025-03-22": [
      {
        "id": "lent_2_saturday",
        "date": "2025-03-22",
        "dateDef": {
          "dateFn": "ashWednesday",
          "addDay": 17,
          "yearOffset": 0
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "PRIVILEGED_WEEKDAY_9",
        "rank": "WEEKDAY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": false,
        "i18nDef": [
          "seasons:lent.weekday",
          {
            "week": 2,
            "dow": 6
          }
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [
          "PURPLE"
        ],
        "commonsDef": [],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 2,
          "dayOfSeason": 18,
          "dayOfWeek": 6,
          "nthDayOfWeekInMonth": 4,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_TIME",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_2"
        },
        "fromCalendarId": "ProperOfTime",
        "fromExtendedCalendars": []
      }
    ],
    "2025-03-23": [
      {
        "id": "lent_3_sunday",
        "date": "2025-03-23",
        "dateDef": {
          "dateFn": "ashWednesday",
          "addDay": 18,
          "yearOffset": 0
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "PRIVILEGED_SUNDAY_2",
        "rank": "SUNDAY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": true,
        "isOptional": false,
        "i18nDef": [
          "seasons:lent.sunday",
          {
            "week": 3
          }
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [
          "PURPLE"
        ],
        "commonsDef": [],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 3,
          "dayOfSeason": 19,
          "dayOfWeek": 0,
          "nthDayOfWeekInMonth": 4,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_TIME",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_3"
        },
        "fromCalendarId": "ProperOfTime",
        "fromExtendedCalendars": []
      }
    ],
    "2025-03-24": [
      {
        "id": "lent_3_monday",
        "date": "2025-03-24",
        "dateDef": {
          "dateFn": "ashWednesday",
          "addDay": 19,
          "yearOffset": 0
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "PRIVILEGED_WEEKDAY_9",
        "rank": "WEEKDAY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": false,
        "i18nDef": [
          "seasons:lent.weekday",
          {
            "week": 3,
            "dow": 1
          }
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [
          "PURPLE"
        ],
        "commonsDef": [],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 3,
          "dayOfSeason": 20,
          "dayOfWeek": 1,
          "nthDayOfWeekInMonth": 4,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_TIME",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_3"
        },
        "fromCalendarId": "ProperOfTime",
        "fromExtendedCalendars": []
      }
    ],
    "2025-03-25": [
      {
        "id": "annunciation_of_the_lord",
        "date": "2025-03-25",
        "dateDef": {
          "dateFn": "annunciation"
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "GENERAL_SOLEMNITY_3",
        "rank": "SOLEMNITY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": false,
        "i18nDef": [
          "names:annunciation_of_the_lord"
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [
          "WHITE"
        ],
        "commonsDef": [
          "None"
        ],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 3,
          "dayOfSeason": 21,
          "dayOfWeek": 2,
          "nthDayOfWeekInMonth": 4,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_SAINTS",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_3"
        },
        "fromCalendarId": "ma",
        "fromExtendedCalendars": []
      }
    ],
    "2025-03-26": [
      {
        "id": "lent_3_wednesday",
        "date": "2025-03-26",
        "dateDef": {
          "dateFn": "ashWednesday",
          "addDay": 21,
          "yearOffset": 0
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "PRIVILEGED_WEEKDAY_9",
        "rank": "WEEKDAY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": false,
        "i18nDef": [
          "seasons:lent.weekday",
          {
            "week": 3,
            "dow": 3
          }
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [
          "PURPLE"
        ],
        "commonsDef": [],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 3,
          "dayOfSeason": 22,
          "dayOfWeek": 3,
          "nthDayOfWeekInMonth": 4,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_TIME",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_3"
        },
        "fromCalendarId": "ProperOfTime",
        "fromExtendedCalendars": []
      }
    ],
    "2025-03-27": [
      {
        "id": "lent_3_thursday",
        "date": "2025-03-27",
        "dateDef": {
          "dateFn": "ashWednesday",
          "addDay": 22,
          "yearOffset": 0
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "PRIVILEGED_WEEKDAY_9",
        "rank": "WEEKDAY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": false,
        "i18nDef": [
          "seasons:lent.weekday",
          {
            "week": 3,
            "dow": 4
          }
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [
          "PURPLE"
        ],
        "commonsDef": [],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 3,
          "dayOfSeason": 23,
          "dayOfWeek": 4,
          "nthDayOfWeekInMonth": 4,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_TIME",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_3"
        },
        "fromCalendarId": "ProperOfTime",
        "fromExtendedCalendars": []
      }
    ],
    "2025-03-28": [
      {
        "id": "lent_3_friday",
        "date": "2025-03-28",
        "dateDef": {
          "dateFn": "ashWednesday",
          "addDay": 23,
          "yearOffset": 0
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "PRIVILEGED_WEEKDAY_9",
        "rank": "WEEKDAY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": false,
        "i18nDef": [
          "seasons:lent.weekday",
          {
            "week": 3,
            "dow": 5
          }
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [
          "PURPLE"
        ],
        "commonsDef": [],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 3,
          "dayOfSeason": 24,
          "dayOfWeek": 5,
          "nthDayOfWeekInMonth": 4,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_TIME",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_3"
        },
        "fromCalendarId": "ProperOfTime",
        "fromExtendedCalendars": []
      }
    ],
    "2025-03-29": [
      {
        "id": "lent_3_saturday",
        "date": "2025-03-29",
        "dateDef": {
          "dateFn": "ashWednesday",
          "addDay": 24,
          "yearOffset": 0
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "PRIVILEGED_WEEKDAY_9",
        "rank": "WEEKDAY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": false,
        "i18nDef": [
          "seasons:lent.weekday",
          {
            "week": 3,
            "dow": 6
          }
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [
          "PURPLE"
        ],
        "commonsDef": [],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 3,
          "dayOfSeason": 25,
          "dayOfWeek": 6,
          "nthDayOfWeekInMonth": 5,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_TIME",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_3"
        },
        "fromCalendarId": "ProperOfTime",
        "fromExtendedCalendars": []
      }
    ],
    "2025-03-30": [
      {
        "id": "lent_4_sunday",
        "date": "2025-03-30",
        "dateDef": {
          "dateFn": "ashWednesday",
          "addDay": 25,
          "yearOffset": 0
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "PRIVILEGED_SUNDAY_2",
        "rank": "SUNDAY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": true,
        "isOptional": false,
        "i18nDef": [
          "seasons:lent.sunday",
          {
            "week": 4
          }
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [
          "ROSE",
          "PURPLE"
        ],
        "commonsDef": [],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 4,
          "dayOfSeason": 26,
          "dayOfWeek": 0,
          "nthDayOfWeekInMonth": 5,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_TIME",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_4"
        },
        "fromCalendarId": "ProperOfTime",
        "fromExtendedCalendars": []
      }
    ],
    "2025-03-31": [
      {
        "id": "lent_4_monday",
        "date": "2025-03-31",
        "dateDef": {
          "dateFn": "ashWednesday",
          "addDay": 26,
          "yearOffset": 0
        },
        "dateExceptions": [],
        "alternativeTransferDateDefs": [],
        "precedence": "PRIVILEGED_WEEKDAY_9",
        "rank": "WEEKDAY",
        "allowSimilarRankItems": false,
        "isHolyDayOfObligation": false,
        "isOptional": false,
        "i18nDef": [
          "seasons:lent.weekday",
          {
            "week": 4,
            "dow": 1
          }
        ],
        "seasons": [
          "LENT"
        ],
        "periods": [
          "PRESENTATION_OF_THE_LORD_TO_HOLY_THURSDAY"
        ],
        "colors": [
          "PURPLE"
        ],
        "commonsDef": [],
        "martyrology": [],
        "titles": [],
        "calendar": {
          "weekOfSeason": 4,
          "dayOfSeason": 27,
          "dayOfWeek": 1,
          "nthDayOfWeekInMonth": 5,
          "startOfSeason": "2025-03-05",
          "endOfSeason": "2025-04-17",
          "startOfLiturgicalYear": "2024-12-01",
          "endOfLiturgicalYear": "2025-11-29",
          "seasons": [
            "LENT"
          ]
        },
        "cycles": {
          "properCycle": "PROPER_OF_TIME",
          "sundayCycle": "YEAR_C",
          "weekdayCycle": "YEAR_1",
          "psalterWeek": "WEEK_4"
        },
        "fromCalendarId": "ProperOfTime",
        "fromExtendedCalendars": []
      }
    ]
  },
  "code": 200
}
```

---

## Customer Support

Need any assistance? [Get in touch with Customer Support](https://apiverve.com/contact).

---

## Updates
Stay up to date by following [@apiverveHQ](https://twitter.com/apiverveHQ) on Twitter.

---

## Legal

All usage of the APIVerve website, API, and services is subject to the [APIVerve Terms of Service](https://apiverve.com/terms) and all legal documents and agreements.

---

## License
Licensed under the The MIT License (MIT)

Copyright (&copy;) 2025 APIVerve, and EvlarSoft LLC

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.