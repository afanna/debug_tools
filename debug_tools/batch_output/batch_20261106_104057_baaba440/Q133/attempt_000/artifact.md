```cardspec
{
  "title": "运动天气卡片",
  "description": "展示昨天的累计步数和今天的实时温度",
  "suggestSize": "2x2",
  "imageDomainWhitelist": [
    "hag-ability-test.obs.cn-north-1.myhuaweicloud.com",
    "lfcontentcenterdev.hwcloudtest.cn",
    "hagres-drcn.dbankcdn.com"
  ],
  "dataBindings": [
    {
      "capabilityId": "ViewWeather",
      "arguments": {
        "districtName": "雨花台区",
        "forecastDays": 1,
        "prefectureName": "南京市"
      },
      "writeResultTo": "/data/weather"
    },
    {
      "capabilityId": "GetHealthAndSportSummary",
      "arguments": {
        "targetDayOffset": -1
      },
      "writeResultTo": "/data/healthSport"
    }
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Stack","children":["__post_theme_background","__genui_render_component__root"],"styles":{"width":"matchParent","height":"matchParent","padding":0,"alignContent":"topStart","clip":true,"borderRadius":20,"backgroundColor":"#FF1F1F99"}},{"id":"__post_theme_background","component":"Stack","children":["fusionBallBackground","__post_theme_base"],"styles":{"width":"matchParent","height":"matchParent","alignContent":"topStart"}},{"id":"__post_theme_base","component":"Image","src":"https://lfcontentcenterdev.hwcloudtest.cn/pub_5/FaStore_fa_900_9/bb/v3/fa/osms/1/1/38675ca3e6c14da9ae3eee0ecb937e5a/df692143c72b44a490306ade859e7700.jpg","styles":{"width":"matchParent","height":"matchParent","objectFit":"fill"}},{"id":"fusionBallBackground","component":"Stack","children":["fusionBallLargeSlot","fusionBallMediumSlot","fusionBallSmallSlot","fusionBallGlassLayer"],"styles":{"width":"100%","height":"100%","borderRadius":20,"alignContent":"topStart","clip":true}},{"id":"fusionBallLargeSlot","component":"Stack","children":["fusionBallLarge"],"styles":{"width":"112.5%","height":"27.5%","alignContent":"center"}},{"id":"fusionBallLarge","component":"Divider","styles":{"width":"116.666667%","height":"477.272727%","strokeWidth":0,"color":"#00000000","borderRadius":105,"backgroundColor":"#FF1F1F99","clip":true}},{"id":"fusionBallMediumSlot","component":"Stack","children":["fusionBallMedium"],"styles":{"width":"50%","height":"137.5%","alignContent":"bottom"}},{"id":"fusionBallMedium","component":"Divider","styles":{"width":"200%","height":"72.727273%","strokeWidth":0,"color":"#00000000","borderRadius":80,"backgroundColor":"#FF2B65D9","clip":true}},{"id":"fusionBallSmallSlot","component":"Stack","children":["fusionBallSmall"],"styles":{"width":"121.875%","height":"118.75%","alignContent":"bottomEnd"}},{"id":"fusionBallSmall","component":"Divider","styles":{"width":"51.282051%","height":"52.631579%","strokeWidth":0,"color":"#00000000","borderRadius":50,"backgroundColor":"#FF57AED9","clip":true}},{"id":"fusionBallGlassLayer","component":"Divider","styles":{"width":"100%","height":"100%","strokeWidth":0,"color":"#00000000","backgroundColor":"#0DFFFFFF","backdropBlur":{"radius":210}}},{"id":"__genui_render_component__root","component":"Column","children":["title","body"],"itemMargin":6,"styles":{"width":"matchParent","height":"matchParent","padding":12,"borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start"}},{"id":"title","component":"Row","children":["title_title"],"styles":{"width":"matchParent","height":12,"flexShrink":0,"justifyContent":"start","alignItems":"center"},"itemMargin":0},{"id":"title_title","component":"Text","content":"Design Compact Mock","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":0,"width":"matchParent","fontColor":"#CCFFFFFF"}},{"id":"body","component":"Column","children":["content"],"styles":{"width":"matchParent","layoutWeight":1},"itemMargin":0},{"id":"content","component":"Column","children":["content_main"],"itemMargin":2,"styles":{"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"content_main","component":"Text","content":"Mock ready","styles":{"height":18,"fontSize":18,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FFFFFFFF","textOverflow":"clip"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"ui":{"state":"ready"}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "显示昨天的累计步数和今天的实时温度",
  "size": "2x2",
  "appVersion": "11.7.8.341",
  "eventCandidates": [],
  "dataModelSchema": {
    "data": {
      "weather": {
        "location": {
          "cityCode": {
            "type": "string",
            "description": "城市代码，如60814代表青浦区",
            "sampleValue": "60814"
          },
          "districtName": {
            "type": "string",
            "description": "区或县名称",
            "sampleValue": "青浦区"
          },
          "prefectureName": {
            "type": "string",
            "description": "城市名称",
            "sampleValue": "上海市"
          }
        },
        "current": {
          "temperatureC": {
            "type": "number",
            "description": "当前温度的纯数值，单位为摄氏度，返回值不包含单位。若直接用于文本展示，必须在数值后追加“℃”；优先使用 temperatureText。",
            "sampleValue": 29
          },
          "temperatureText": {
            "type": "string",
            "description": "可直接显示的当前温度文本，已包含“℃”单位；展示时不得再次追加温度单位。例如“29℃”。",
            "sampleValue": "29℃"
          },
          "condition": {
            "type": "string",
            "description": "当前天气现象，例如“阴”“多云”“小雨”。",
            "sampleValue": "多云"
          },
          "feelsLikeC": {
            "type": "number",
            "description": "当前体感温度的纯数值，单位为摄氏度，返回值不包含单位。若直接用于文本展示，必须在数值后追加“℃”。",
            "sampleValue": 31
          },
          "humidityPercent": {
            "type": "number",
            "description": "当前相对湿度的纯数值百分比，取值范围为 0 到 100，返回值不包含“%”。若直接用于文本展示，必须在数值后追加“%”。",
            "sampleValue": 68
          },
          "airQuality": {
            "type": "string",
            "description": "当前空气质量等级，例如“优”“良”。",
            "sampleValue": "良"
          },
          "windDirection": {
            "type": "string",
            "description": "当前风向。",
            "sampleValue": "东南风"
          },
          "windLevel": {
            "type": "integer",
            "description": "当前风力等级的纯整数，返回值不包含“级”。若直接用于文本展示，必须在数值后追加“级”。",
            "sampleValue": 2
          },
          "uvIndex": {
            "type": "string",
            "description": "当前紫外线等级，例如“弱”“中等”“强”。",
            "sampleValue": "中等"
          },
          "coldLevel": {
            "type": "string",
            "description": "感冒指数。",
            "sampleValue": "低"
          },
          "alertLevel": {
            "type": "string",
            "description": "预警信息。当前气象预警信息，例如'暴雨橙色预警'、'高温黄色预警'、'台风蓝色预警'。无预警时为空字符串。",
            "sampleValue": "大风蓝色预警"
          }
        },
        "daily": [
          {
            "date": {
              "type": "string",
              "description": "预报日期，来源于 day_time。以端侧本次刷新日期为基准，daily[0]为明天日期，daily[1]为后天日期，不包含今天。",
              "sampleValue": "2026-08-06"
            },
            "weekday": {
              "type": "string",
              "description": "星期文本，例如“星期日”。",
              "sampleValue": "星期四"
            },
            "condition": {
              "type": "string",
              "description": "白天天气现象，来源于weather_icon。",
              "sampleValue": "多云"
            },
            "temperatureRangeText": {
              "type": "string",
              "description": "可直接显示的最低温与最高温范围文本，每个温度值均已包含“℃”单位；展示时不得再次追加温度单位。例如“25℃ / 32℃”。",
              "sampleValue": "25℃ / 32℃"
            },
            "rainProbabilityPercent": {
              "type": "number",
              "description": "白天降雨概率的百分数数值，返回值不包含单位，例如 20 表示 20%；文本展示必须追加一个“%”，进度组件直接使用数值。",
              "sampleValue": 20
            },
            "airQuality": {
              "type": "string",
              "description": "当天空气质量等级。",
              "sampleValue": "良"
            },
            "uvIndex": {
              "type": "string",
              "description": "当天紫外线等级。",
              "sampleValue": "中等"
            },
            "coldLevel": {
              "type": "string",
              "description": "感冒指数。",
              "sampleValue": "低"
            }
          }
        ],
        "updatedAt": {
          "type": "string",
          "description": "端侧完成天气查询和归一化的时间。如：2026-06-14 15:30",
          "sampleValue": "2026-08-06 09:00"
        }
      },
      "healthSport": {
        "targetDateText": {
          "type": "string",
          "description": "该组健康与运动数据所归属的确切日期文本，格式为 YYYY-MM-DD，例如 '2026-07-06'。用于明确展示当前查阅的是哪一天的数据。",
          "sampleValue": "2026-08-06"
        },
        "sleepScore": {
          "type": "integer",
          "description": "睡眠综合得分，取值范围 0-100。",
          "sampleValue": 82
        },
        "sleepStatus": {
          "type": "string",
          "description": "基于得分智能生成的睡眠状态语义判定，包括：'优秀'、'良好'、'一般'、'较差'。",
          "sampleValue": "良好"
        },
        "sleepTypeDesc": {
          "type": "string",
          "description": "睡眠记录方式或类型的描述，例如“科学睡眠”、“普通睡眠”、“手动输入睡眠”、“手机记录睡眠”。",
          "sampleValue": "科学睡眠"
        },
        "nightSleepDurationText": {
          "type": "string",
          "description": "可直接显示的夜间正式睡眠总时长文本，已包含“小时”或“分”等时间单位；展示时不得再次追加时间单位。例如“7小时1分”。",
          "sampleValue": "7小时1分"
        },
        "deepSleepDurationText": {
          "type": "string",
          "description": "可直接显示的夜间正式睡眠深睡总时长文本，已包含“小时”或“分”等时间单位；展示时不得再次追加时间单位。例如“2小时15分”。",
          "sampleValue": "2小时15分"
        },
        "totalNapDurationText": {
          "type": "string",
          "description": "可直接显示的白天零星小睡累计总时长文本，已包含“小时”或“分”等时间单位；展示时不得再次追加时间单位。例如“45分”或“0分”。",
          "sampleValue": "0分"
        },
        "fallAsleepTimeText": {
          "type": "string",
          "description": "格式化后的确切入睡时刻短文本（HH:mm），例如“23:15”。",
          "sampleValue": "23:15"
        },
        "wakeupTimeText": {
          "type": "string",
          "description": "格式化后的确切醒来时刻短文本（HH:mm），例如“07:30”。",
          "sampleValue": "07:30"
        },
        "dailySteps": {
          "type": "integer",
          "description": "与最新睡眠同属一天的日常全天累计活动总步数纯整数，返回值不包含“步”。若直接用于文本展示，必须在数值后追加“步”。",
          "sampleValue": 6200
        },
        "dailyTotalCaloriesText": {
          "type": "string",
          "description": "可直接显示的日常活动总消耗热量文本，已完成千分位归一化并包含“千卡”单位；展示时不得再次追加热量单位。例如“998 千卡”。",
          "sampleValue": "420 千卡"
        },
        "dailyDistanceText": {
          "type": "string",
          "description": "可直接显示的日常活动总距离文本，端侧已根据数值大小换算并包含“米”或“公里”单位；展示时不得再次追加距离单位。例如“5.42 公里”或“755 米”。",
          "sampleValue": "4.60 公里"
        },
        "exerciseTypeName": {
          "type": "string",
          "description": "最近一次发生的单次专业运动训练类型的中文映射名称，如“羽毛球”、“自由训练”、“户外跑步”。若无记录则返回“暂无运动”。",
          "sampleValue": "户外跑步"
        },
        "exerciseStartTimeText": {
          "type": "string",
          "description": "专业运动开始的确切时刻文本（HH:mm），例如“18:30”。",
          "sampleValue": "18:30"
        },
        "exerciseEndTimeText": {
          "type": "string",
          "description": "专业运动结束的确切时刻文本（HH:mm），例如“19:50”。",
          "sampleValue": "19:10"
        },
        "exerciseDurationText": {
          "type": "string",
          "description": "可直接显示的单次专业运动实际持续时长文本，已包含“小时”或“分”等时间单位；展示时不得再次追加时间单位。例如“1小时40分”。",
          "sampleValue": "40分"
        },
        "exerciseCalorieText": {
          "type": "string",
          "description": "可直接显示的单次专业运动净热量消耗文本，已换算并包含“千卡”单位；展示时不得再次追加热量单位。例如“98 千卡”。",
          "sampleValue": "260 千卡"
        },
        "exerciseHeartRateAvg": {
          "type": "integer",
          "description": "专业运动期间平均心率的纯整数，单位为次/分钟，返回值不包含单位。若直接用于文本展示，必须在数值后追加“次/分钟”。",
          "sampleValue": 135
        },
        "exerciseHeartRateMax": {
          "type": "integer",
          "description": "专业运动期间最大心率的纯整数，单位为次/分钟，返回值不包含单位。若直接用于文本展示，必须在数值后追加“次/分钟”。",
          "sampleValue": 168
        },
        "exerciseHeartRateMin": {
          "type": "integer",
          "description": "专业运动期间最低心率的纯整数，单位为次/分钟，返回值不包含单位。若直接用于文本展示，必须在数值后追加“次/分钟”。",
          "sampleValue": 96
        },
        "updatedAt": {
          "type": "string",
          "description": "端侧完成多实体规整转换的系统格式化时间戳字符串，如 '2026-07-03 14:57'。",
          "sampleValue": "2026-08-06 09:00"
        }
      }
    }
  },
  "assetCandidates": [
    {
      "id": "photo-ux-texture-orange-diagonal-square",
      "src": "https://lfcontentcenterdev.hwcloudtest.cn/pub_5/FaStore_fa_900_9/bb/v3/fa/osms/1/1/38675ca3e6c14da9ae3eee0ecb937e5a/df692143c72b44a490306ade859e7700.jpg",
      "description": "主题背景"
    }
  ]
}
```
```effectivecapabilities
{
  "data": [
    "ViewWeather",
    "GetHealthAndSportSummary"
  ],
  "event": [],
  "asset": [
    "photo-ux-texture-orange-diagonal-square"
  ]
}
```
```removedcapabilities
[]
```
```generationplan
{
  "candidateDataBindings": [
    {
      "capabilityId": "ViewWeather",
      "arguments": {
        "districtName": "雨花台区",
        "forecastDays": 1,
        "prefectureName": "南京市"
      },
      "writeResultTo": "/data/weather",
      "candidateOutputFields": []
    },
    {
      "capabilityId": "GetHealthAndSportSummary",
      "arguments": {
        "targetDayOffset": -1
      },
      "writeResultTo": "/data/healthSport",
      "candidateOutputFields": []
    }
  ],
  "candidateEventCandidates": [],
  "candidateAssetIds": []
}
```
```meta
{
  "apiVersion": "v1",
  "taskSpecVersion": "task-spec-v1",
  "cardSpecVersion": "card-spec-v1",
  "dslProtocolVersion": "v0.9",
  "skillVersion": "skill-widget-v1",
  "protocolProfileId": "a2ui-form-rom6.0-v1",
  "capabilityRegistryVersion": "app-11.7.7.300_rom-7.0",
  "artifactSchemaVersion": "widget-artifact-v2",
  "generationMode": "create",
  "artifactId": "d23263ca-896f-4d35-b032-3ac26f0e78f7",
  "createdAt": 1793932858319
}
```
```designcompactdsl
["root","Column",{"width":"matchParent","height":"matchParent","padding":12,"borderRadius":20,"clip":true,"itemMargin":6,"alignItems":"start","justifyContent":"start"},["title","body"]]
["title","SingleLineTitle",{"title":"Design Compact Mock"}]
["body","Column",{"width":"matchParent","layoutWeight":1},["content"]]
["content","EmphasisText",{"mainText":"Mock ready"}]
["/ui/state","ready"]
```
```request
{
  "content": {
    "title": "运动天气卡片",
    "description": "展示昨天的累计步数和今天的实时温度",
    "userQuery": "显示昨天的累计步数和今天的实时温度",
    "size": "2x2",
    "bundleName": "com.huawei.genui",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "CMM-AL10 7.0.0.111",
    "candidateDataBindings": [
      {
        "capabilityId": "ViewWeather",
        "arguments": {
          "districtName": "雨花台区",
          "forecastDays": 1,
          "prefectureName": "南京市"
        },
        "writeResultTo": "/data/weather"
      },
      {
        "capabilityId": "GetHealthAndSportSummary",
        "arguments": {
          "targetDayOffset": -1
        },
        "writeResultTo": "/data/healthSport"
      }
    ],
    "candidateEventCandidates": [],
    "candidateAssetIds": []
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "CMM-AL10",
    "prdVer": "11.7.8.341",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261020025324697"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q133-000",
    "isNew": true,
    "sessionId": "batch-baaba440"
  },
  "userAuth": {
    "user": {}
  },
  "utterance": {
    "original": "",
    "type": "text"
  },
  "version": "1.0",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "CMM-AL10 7.0.0.111",
  "bundleName": "com.huawei.genui",
  "description": "展示昨天的累计步数和今天的实时温度",
  "dataCapabilityParams": {
    "GetHealthAndSportSummary": {
      "targetDayOffset": -1
    },
    "ViewWeather": {
      "districtName": "雨花台区",
      "forecastDays": 1,
      "prefectureName": "南京市"
    }
  },
  "userQuery": "显示昨天的累计步数和今天的实时温度",
  "title": "运动天气卡片",
  "dataCapabilityIds": [
    "ViewWeather",
    "GetHealthAndSportSummary"
  ]
}
```
