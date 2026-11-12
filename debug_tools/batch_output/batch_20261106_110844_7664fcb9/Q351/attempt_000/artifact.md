```cardspec
{
  "title": "桌面聚合卡片",
  "description": "聚合天气、电量、健康和耗电排行的桌面卡片",
  "suggestSize": "2x4",
  "imageDomainWhitelist": [
    "hag-ability-test.obs.cn-north-1.myhuaweicloud.com",
    "lfcontentcenterdev.hwcloudtest.cn",
    "hagres-drcn.dbankcdn.com"
  ],
  "dataBindings": [
    {
      "capabilityId": "ViewWeather",
      "arguments": {
        "forecastDays": 1
      },
      "writeResultTo": "/data/weather"
    },
    {
      "capabilityId": "GetPhoneBatteryInfo",
      "arguments": {},
      "writeResultTo": "/data/phoneBattery"
    },
    {
      "capabilityId": "GetHealthAndSportSummary",
      "arguments": {},
      "writeResultTo": "/data/healthSport"
    },
    {
      "capabilityId": "GetAppPowerConsumptionRanking",
      "arguments": {
        "limit": 3
      },
      "writeResultTo": "/data/powerRanking"
    }
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["title","__layout__root__body"],"itemMargin":6,"styles":{"width":"matchParent","height":"matchParent","padding":12,"borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"title","component":"Row","children":["title_title"],"styles":{"width":"matchParent","height":12,"flexShrink":0,"justifyContent":"start","alignItems":"center"},"itemMargin":0},{"id":"title_title","component":"Text","content":"今日概览","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":0,"width":"matchParent","fontColor":"#991F4799"}},{"id":"__layout__root__body","component":"Column","children":["__layout__root__primary","__layout__root__details"],"itemMargin":8,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__root__primary","component":"Column","children":["primary"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"primary","component":"Column","children":["primary_main","primary_secondary"],"itemMargin":2,"styles":{"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"primary_main","component":"Text","content":"{{ ${/data/weather/current/temperatureText} }}","styles":{"height":18,"fontSize":18,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"primary_secondary","component":"Text","content":"{{ ${/data/weather/current/condition} }}","styles":{"height":16,"fontSize":12,"fontWeight":400,"lineHeight":1.3333333333333333,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"__layout__root__details","component":"Column","children":["details"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1},"itemMargin":0},{"id":"details","component":"Row","children":["details_item0","details_item1","details_item2","details_item3"],"itemMargin":8,"styles":{"width":"matchParent","height":"matchParent","alignItems":"top","justifyContent":"start","layoutWeight":1,"flexShrink":1,"constraintSize":{"minHeight":48}}},{"id":"details_item0","component":"Column","children":["details_item0_label_slot","details_item0_value_slot"],"itemMargin":2,"styles":{"height":"matchParent","backgroundColor":"#99FFFFFF","padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","layoutWeight":1,"flexShrink":1,"constraintSize":{"minWidth":0,"minHeight":0}}},{"id":"details_item0_label_slot","component":"Row","children":["details_item0_label"],"styles":{"width":"matchParent","height":18,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item0_label","component":"Text","content":"电量","styles":{"width":"matchParent","fontSize":12,"fontWeight":700,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#991F4799"}},{"id":"details_item0_value_slot","component":"Row","children":["details_item0_value"],"styles":{"width":"matchParent","height":16,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item0_value","component":"Text","content":"{{ ${/data/phoneBattery/batterySOCText} }}","styles":{"width":"matchParent","fontSize":10,"fontWeight":500,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#FF1F4799"}},{"id":"details_item1","component":"Column","children":["details_item1_label_slot","details_item1_value_slot"],"itemMargin":2,"styles":{"height":"matchParent","backgroundColor":"#99FFFFFF","padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","layoutWeight":1,"flexShrink":1,"constraintSize":{"minWidth":0,"minHeight":0}}},{"id":"details_item1_label_slot","component":"Row","children":["details_item1_label"],"styles":{"width":"matchParent","height":18,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item1_label","component":"Text","content":"步数","styles":{"width":"matchParent","fontSize":12,"fontWeight":700,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#991F4799"}},{"id":"details_item1_value_slot","component":"Row","children":["details_item1_value"],"styles":{"width":"matchParent","height":16,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item1_value","component":"Text","content":"{{ ${/data/healthSport/dailySteps} + '步' }}","styles":{"width":"matchParent","fontSize":10,"fontWeight":500,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#FF1F4799"}},{"id":"details_item2","component":"Column","children":["details_item2_label_slot","details_item2_value_slot"],"itemMargin":2,"styles":{"height":"matchParent","backgroundColor":"#99FFFFFF","padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","layoutWeight":1,"flexShrink":1,"constraintSize":{"minWidth":0,"minHeight":0}}},{"id":"details_item2_label_slot","component":"Row","children":["details_item2_label"],"styles":{"width":"matchParent","height":18,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item2_label","component":"Text","content":"消耗","styles":{"width":"matchParent","fontSize":12,"fontWeight":700,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#991F4799"}},{"id":"details_item2_value_slot","component":"Row","children":["details_item2_value"],"styles":{"width":"matchParent","height":16,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item2_value","component":"Text","content":"{{ ${/data/healthSport/dailyTotalCaloriesText} }}","styles":{"width":"matchParent","fontSize":10,"fontWeight":500,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#FF1F4799"}},{"id":"details_item3","component":"Column","children":["details_item3_label_slot","details_item3_value_slot"],"itemMargin":2,"styles":{"height":"matchParent","backgroundColor":"#99FFFFFF","padding":{"left":8,"right":8},"borderRadius":16,"alignItems":"start","justifyContent":"center","layoutWeight":1,"flexShrink":1,"constraintSize":{"minWidth":0,"minHeight":0}}},{"id":"details_item3_label_slot","component":"Row","children":["details_item3_label"],"styles":{"width":"matchParent","height":18,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item3_label","component":"Text","content":"运动","styles":{"width":"matchParent","fontSize":12,"fontWeight":700,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#991F4799"}},{"id":"details_item3_value_slot","component":"Row","children":["details_item3_value"],"styles":{"width":"matchParent","height":16,"alignItems":"center","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"details_item3_value","component":"Text","content":"{{ ${/data/healthSport/exerciseTypeName} }}","styles":{"width":"matchParent","fontSize":10,"fontWeight":500,"textAlign":"start","maxLines":1,"textOverflow":"ellipsis","fontColor":"#FF1F4799"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"weather":{"current":{"temperatureText":"29℃","condition":"多云"}},"phoneBattery":{"batterySOCText":"68%","chargingStatusDesc":"未充电","batterySOC":68},"healthSport":{"dailySteps":6200,"dailyTotalCaloriesText":"420 千卡","exerciseTypeName":"户外跑步","exerciseDurationText":"40分"},"powerRanking":{"rankingList":[{"appName":"示例","powerText":"示例"},{"appName":"示例","powerText":"示例"},{"appName":"示例","powerText":"示例"}]}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "创建一张聚合卡片，显示当前天气、手机电量、今日运动健康数据和耗电应用排行。",
  "size": "2x4",
  "appVersion": "11.7.8.342",
  "eventCandidates": [],
  "dataModelSchema": {
    "data": {
      "weather": {
        "current": {
          "temperatureText": {
            "type": "string",
            "description": "可直接显示的当前温度文本，已包含“℃”单位；展示时不得再次追加温度单位。例如“29℃”。",
            "sampleValue": "29℃"
          },
          "condition": {
            "type": "string",
            "description": "当前天气现象，例如“阴”“多云”“小雨”。",
            "sampleValue": "多云"
          }
        }
      },
      "phoneBattery": {
        "batterySOCText": {
          "type": "string",
          "description": "可直接显示的当前手机设备剩余电量文本，已包含“%”单位；展示时不得再次追加“%”。",
          "sampleValue": "68%",
          "numericSource": "/data/phoneBattery/batterySOC"
        },
        "chargingStatusDesc": {
          "type": "string",
          "description": "当前设备电池的充电状态文本描述。",
          "sampleValue": "未充电"
        },
        "batterySOC": {
          "type": "integer",
          "description": "当前手机设备剩余电量的纯整数百分比，取值范围为 0 到 100，返回值不包含“%”。若直接用于文本展示，必须在数值后追加“%”；优先使用 batterySOCText。",
          "sampleValue": 68
        }
      },
      "healthSport": {
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
        "exerciseTypeName": {
          "type": "string",
          "description": "最近一次发生的单次专业运动训练类型的中文映射名称，如“羽毛球”、“自由训练”、“户外跑步”。若无记录则返回“暂无运动”。",
          "sampleValue": "户外跑步"
        },
        "exerciseDurationText": {
          "type": "string",
          "description": "可直接显示的单次专业运动实际持续时长文本，已包含“小时”或“分”等时间单位；展示时不得再次追加时间单位。例如“1小时40分”。",
          "sampleValue": "40分"
        }
      },
      "powerRanking": {
        "rankingList": [
          {
            "appName": {
              "type": "string",
              "description": "应用名称文本，例如：“微信”、“设置”。",
              "sampleValue": "示例"
            },
            "powerText": {
              "type": "string",
              "description": "应用的耗电量或耗电占比格式化文本，例如：“53%”、“--”。",
              "sampleValue": "示例"
            }
          },
          {
            "appName": {
              "type": "string",
              "description": "应用名称文本，例如：“微信”、“设置”。",
              "sampleValue": "示例"
            },
            "powerText": {
              "type": "string",
              "description": "应用的耗电量或耗电占比格式化文本，例如：“53%”、“--”。",
              "sampleValue": "示例"
            }
          },
          {
            "appName": {
              "type": "string",
              "description": "应用名称文本，例如：“微信”、“设置”。",
              "sampleValue": "示例"
            },
            "powerText": {
              "type": "string",
              "description": "应用的耗电量或耗电占比格式化文本，例如：“53%”、“--”。",
              "sampleValue": "示例"
            }
          }
        ]
      }
    }
  },
  "assetCandidates": []
}
```
```effectivecapabilities
{
  "data": [
    "ViewWeather",
    "GetPhoneBatteryInfo",
    "GetHealthAndSportSummary",
    "GetAppPowerConsumptionRanking"
  ],
  "event": [],
  "asset": []
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
        "forecastDays": 1
      },
      "writeResultTo": "/data/weather",
      "candidateOutputFields": [
        "/current/temperatureText",
        "/current/condition"
      ]
    },
    {
      "capabilityId": "GetPhoneBatteryInfo",
      "arguments": {},
      "writeResultTo": "/data/phoneBattery",
      "candidateOutputFields": [
        "/batterySOCText",
        "/chargingStatusDesc",
        "/batterySOC"
      ]
    },
    {
      "capabilityId": "GetHealthAndSportSummary",
      "arguments": {},
      "writeResultTo": "/data/healthSport",
      "candidateOutputFields": [
        "/dailySteps",
        "/dailyTotalCaloriesText",
        "/exerciseTypeName",
        "/exerciseDurationText"
      ]
    },
    {
      "capabilityId": "GetAppPowerConsumptionRanking",
      "arguments": {
        "limit": 3
      },
      "writeResultTo": "/data/powerRanking",
      "candidateOutputFields": [
        "/rankingList/0/appName",
        "/rankingList/0/powerText",
        "/rankingList/1/appName",
        "/rankingList/1/powerText",
        "/rankingList/2/appName",
        "/rankingList/2/powerText"
      ]
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
  "artifactId": "980ee403-58ff-4180-9edd-4a37f25a4a2c",
  "createdAt": 1793934592107
}
```
```designcompactdsl
["root","Layout",{"layout":"W-top-bottom","variant":"continuous"},["title","primary","details"]]
["title","SingleLineTitle",{"title":"今日概览","fontSize":12}]
["primary","EmphasisText",{"mainText":{"path":"/data/weather/current/temperatureText"},"secondaryText":{"path":"/data/weather/current/condition"},"fontSize":18}]
["details","TextBlock",{"items":[{"label":"电量","value":{"path":"/data/phoneBattery/batterySOCText"}},{"label":"步数","value":"{{ ${/data/healthSport/dailySteps} + '步' }}"},{"label":"消耗","value":{"path":"/data/healthSport/dailyTotalCaloriesText"}},{"label":"运动","value":{"path":"/data/healthSport/exerciseTypeName"}}]}]
["/data/weather/current/temperatureText","29℃"]
["/data/weather/current/condition","多云"]
["/data/phoneBattery/batterySOCText","68%"]
["/data/phoneBattery/chargingStatusDesc","未充电"]
["/data/phoneBattery/batterySOC",68]
["/data/healthSport/dailySteps",6200]
["/data/healthSport/dailyTotalCaloriesText","420 千卡"]
["/data/healthSport/exerciseTypeName","户外跑步"]
["/data/healthSport/exerciseDurationText","40分"]
["/data/powerRanking/rankingList/0/appName","示例"]
["/data/powerRanking/rankingList/0/powerText","示例"]
["/data/powerRanking/rankingList/1/appName","示例"]
["/data/powerRanking/rankingList/1/powerText","示例"]
["/data/powerRanking/rankingList/2/appName","示例"]
["/data/powerRanking/rankingList/2/powerText","示例"]
```
```request
{
  "content": {
    "bundleName": "com.huawei.genui",
    "userQuery": "创建一张聚合卡片，显示当前天气、手机电量、今日运动健康数据和耗电应用排行。",
    "candidateDataBindings": [
      {
        "capabilityId": "ViewWeather",
        "arguments": {
          "forecastDays": 1
        },
        "writeResultTo": "/data/weather",
        "candidateOutputFields": [
          "/current/temperatureText",
          "/current/condition"
        ]
      },
      {
        "capabilityId": "GetPhoneBatteryInfo",
        "arguments": {},
        "writeResultTo": "/data/phoneBattery",
        "candidateOutputFields": [
          "/batterySOCText",
          "/chargingStatusDesc",
          "/batterySOC"
        ]
      },
      {
        "capabilityId": "GetHealthAndSportSummary",
        "arguments": {},
        "writeResultTo": "/data/healthSport",
        "candidateOutputFields": [
          "/dailySteps",
          "/dailyTotalCaloriesText",
          "/exerciseTypeName",
          "/exerciseDurationText"
        ]
      },
      {
        "capabilityId": "GetAppPowerConsumptionRanking",
        "arguments": {
          "limit": 3
        },
        "writeResultTo": "/data/powerRanking",
        "candidateOutputFields": [
          "/rankingList/0/appName",
          "/rankingList/0/powerText",
          "/rankingList/1/appName",
          "/rankingList/1/powerText",
          "/rankingList/2/appName",
          "/rankingList/2/powerText"
        ]
      }
    ],
    "title": "桌面聚合卡片",
    "size": "2x4",
    "candidateEventCandidates": [],
    "description": "聚合天气、电量、健康和耗电排行的桌面卡片",
    "candidateAssetIds": []
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "CMS-AL20",
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261030100829720"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q351-000",
    "isNew": true,
    "sessionId": "batch-7664fcb9"
  },
  "userAuth": {
    "user": {}
  },
  "utterance": {
    "original": "创建一张聚合卡片，显示当前天气、手机电量、今日运动健康数据和耗电应用排行。",
    "type": "text"
  },
  "version": "1.0",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "CMS-AL20 7.0.0.111",
  "bundleName": "com.huawei.genui",
  "userQuery": "创建一张聚合卡片，显示当前天气、手机电量、今日运动健康数据和耗电应用排行。",
  "candidateDataBindings": [
    {
      "capabilityId": "ViewWeather",
      "arguments": {
        "forecastDays": 1
      },
      "writeResultTo": "/data/weather",
      "candidateOutputFields": [
        "/current/temperatureText",
        "/current/condition"
      ]
    },
    {
      "capabilityId": "GetPhoneBatteryInfo",
      "arguments": {},
      "writeResultTo": "/data/phoneBattery",
      "candidateOutputFields": [
        "/batterySOCText",
        "/chargingStatusDesc",
        "/batterySOC"
      ]
    },
    {
      "capabilityId": "GetHealthAndSportSummary",
      "arguments": {},
      "writeResultTo": "/data/healthSport",
      "candidateOutputFields": [
        "/dailySteps",
        "/dailyTotalCaloriesText",
        "/exerciseTypeName",
        "/exerciseDurationText"
      ]
    },
    {
      "capabilityId": "GetAppPowerConsumptionRanking",
      "arguments": {
        "limit": 3
      },
      "writeResultTo": "/data/powerRanking",
      "candidateOutputFields": [
        "/rankingList/0/appName",
        "/rankingList/0/powerText",
        "/rankingList/1/appName",
        "/rankingList/1/powerText",
        "/rankingList/2/appName",
        "/rankingList/2/powerText"
      ]
    }
  ],
  "title": "桌面聚合卡片",
  "size": "2x4",
  "candidateEventCandidates": [],
  "description": "聚合天气、电量、健康和耗电排行的桌面卡片",
  "candidateAssetIds": []
}
```
```repair-1
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"W-split-panels\"},[\"left\",\"right\"]]\n[\"left_title\",\"SingleLineTitle\",{\"title\":\"天气与电量\",\"fontSize\":12}]\n[\"left_weather\",\"EmphasisText\",{\"mainText\":{\"path\":\"/data/weather/current/temperatureText\"},\"secondaryText\":{\"path\":\"/data/weather/current/condition\"},\"fontSize\":18}]\n[\"left_battery\",\"InfoBlock\",{\"variant\":\"slot\",\"primaryText\":{\"path\":\"/data/phoneBattery/batterySOCText\"},\"secondaryText\":{\"path\":\"/data/phoneBattery/chargingStatusDesc\"}}]\n[\"left_group\",\"Group\",{\"variant\":\"hero-support\"},[\"left_weather\",\"left_battery\"]]\n[\"left\",\"Region\",{\"variant\":\"title-content\"},[\"left_title\",\"left_group\"]]\n[\"right_title\",\"SingleLineTitle\",{\"title\":\"今日运动与耗电排行\",\"fontSize\":12}]\n[\"right_sport\",\"TextBlock\",{\"items\":[{\"label\":\"步数\",\"value\":\"{{ ${/data/healthSport/dailySteps} + '步' }}\"},{\"label\":\"消耗\",\"value\":{\"path\":\"/data/healthSport/dailyTotalCaloriesText\"}},{\"label\":\"运动\",\"value\":{\"path\":\"/data/healthSport/exerciseTypeName\"}}]}]\n[\"right\",\"Region\",{\"variant\":\"title-content\"},[\"right_title\",\"right_sport\"]]\n[\"/data/weather/current/temperatureText\",\"29℃\"]\n[\"/data/weather/current/condition\",\"多云\"]\n[\"/data/phoneBattery/batterySOCText\",\"68%\"]\n[\"/data/phoneBattery/chargingStatusDesc\",\"未充电\"]\n[\"/data/phoneBattery/batterySOC\",68]\n[\"/data/healthSport/dailySteps\",6200]\n[\"/data/healthSport/dailyTotalCaloriesText\",\"420 千卡\"]\n[\"/data/healthSport/exerciseTypeName\",\"户外跑步\"]\n[\"/data/healthSport/exerciseDurationText\",\"40分\"]\n[\"/data/powerRanking/rankingList/0/appName\",\"示例\"]\n[\"/data/powerRanking/rankingList/0/powerText\",\"示例\"]\n[\"/data/powerRanking/rankingList/1/appName\",\"示例\"]\n[\"/data/powerRanking/rankingList/1/powerText\",\"示例\"]\n[\"/data/powerRanking/rankingList/2/appName\",\"示例\"]\n[\"/data/powerRanking/rankingList/2/powerText\",\"示例\"]",
  "generatedDsl": "",
  "validationErrors": [
    {
      "stage": "validation",
      "code": "COMPACT_DSL_VALIDATION_FAILED",
      "message": "语义布局不符合合同：节点 left：InfoBlock 只能放在固定槽，不能进入 Region 或其 Group。请选择已登记的 Layout、Region 或 Group 变体，不要修改展开后的几何。"
    }
  ]
}
```
```repair-2
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"W-split-panels\"},[\"left\",\"right\"]]\n[\"left_title\",\"SingleLineTitle\",{\"title\":\"天气与电量\",\"fontSize\":12}]\n[\"left_weather\",\"EmphasisText\",{\"mainText\":{\"path\":\"/data/weather/current/temperatureText\"},\"secondaryText\":{\"path\":\"/data/weather/current/condition\"},\"fontSize\":18}]\n[\"left_battery\",\"EmphasisText\",{\"mainText\":{\"path\":\"/data/phoneBattery/batterySOCText\"},\"secondaryText\":{\"path\":\"/data/phoneBattery/chargingStatusDesc\"},\"fontSize\":18}]\n[\"left_group\",\"Group\",{\"variant\":\"hero-support\"},[\"left_weather\",\"left_battery\"]]\n[\"left\",\"Region\",{\"variant\":\"title-content\"},[\"left_title\",\"left_group\"]]\n[\"right_title\",\"SingleLineTitle\",{\"title\":\"今日运动\",\"fontSize\":12}]\n[\"right_sport\",\"TextBlock\",{\"items\":[{\"label\":\"步数\",\"value\":\"{{ ${/data/healthSport/dailySteps} + '步' }}\"},{\"label\":\"消耗\",\"value\":{\"path\":\"/data/healthSport/dailyTotalCaloriesText\"}},{\"label\":\"运动\",\"value\":{\"path\":\"/data/healthSport/exerciseTypeName\"}}]}]\n[\"right\",\"Region\",{\"variant\":\"title-content\"},[\"right_title\",\"right_sport\"]]\n[\"/data/weather/current/temperatureText\",\"29℃\"]\n[\"/data/weather/current/condition\",\"多云\"]\n[\"/data/phoneBattery/batterySOCText\",\"68%\"]\n[\"/data/phoneBattery/chargingStatusDesc\",\"未充电\"]\n[\"/data/phoneBattery/batterySOC\",68]\n[\"/data/healthSport/dailySteps\",6200]\n[\"/data/healthSport/dailyTotalCaloriesText\",\"420 千卡\"]\n[\"/data/healthSport/exerciseTypeName\",\"户外跑步\"]\n[\"/data/healthSport/exerciseDurationText\",\"40分\"]\n[\"/data/powerRanking/rankingList/0/appName\",\"示例\"]\n[\"/data/powerRanking/rankingList/0/powerText\",\"示例\"]\n[\"/data/powerRanking/rankingList/1/appName\",\"示例\"]\n[\"/data/powerRanking/rankingList/1/powerText\",\"示例\"]\n[\"/data/powerRanking/rankingList/2/appName\",\"示例\"]\n[\"/data/powerRanking/rankingList/2/powerText\",\"示例\"]",
  "generatedDsl": "",
  "validationErrors": [
    {
      "stage": "validation",
      "code": "COMPACT_DSL_VALIDATION_FAILED",
      "message": "component right_sport: horizontal layout requires at least 208vp within 116vp; it overflows by 92vp.",
      "compactDiagnostics": [
        {
          "code": "COMPACT_LAYOUT_WIDTH_OVERFLOW",
          "validationClass": "semantic",
          "category": "layout",
          "severity": "error",
          "message": "component right_sport: horizontal layout requires at least 208vp within 116vp; it overflows by 92vp.",
          "legacyMessage": "component right_sport: horizontal layout requires at least 208vp within 116vp; it overflows by 92vp.",
          "expected": {
            "maximumWidth": 116.0,
            "preserveFixedContent": true
          },
          "actual": {
            "minimumRequiredWidth": 208.0,
            "overflow": 92.0,
            "occupancy": [
              {
                "componentId": "right_sport_item0",
                "minimumWidth": 64.0,
                "margin": 0.0
              },
              {
                "componentId": "right_sport_item1",
                "minimumWidth": 64.0,
                "margin": 0.0
              },
              {
                "componentId": "right_sport_item2",
                "minimumWidth": 64.0,
                "margin": 0.0
              },
              {
                "gaps": 16.0
              }
            ]
          },
          "evidenceSource": "expanded",
          "fixHint": "根据子项占用与可用宽度调整区域分配，或改用合法组合。保留全部必要读数、标签、绑定和动作；尺寸与字号调整须遵守对应组件的设计约束和最小可读尺寸。调整后重新校验，不能依靠裁切、遮挡或丢失内容消除报错。"
        }
      ]
    },
    {
      "stage": "validation",
      "code": "COMPACT_DSL_VALIDATION_FAILED",
      "message": "Compact layout does not match scope W-plan-guided (W-top-bottom, W-split-panels, W-content-side-slots, W-four-slots): closest W-split-panels: component right_sport: TextBlock is only allowed in W-top-bottom.details for 2x4, but the current structure matches W-split-panels; switch the complete layout to W-top-bottom or replace TextBlock with a component allowed by W-split-panels. Alternatives (choose one complete variant): W-top-bottom variant 3: slot root must use Column, got Row; slot root/0 must use SingleLineTitle, got Column | W-split-panels variant 1: component right_sport: TextBlock is only allowed in W-top-bottom.details for 2x4, but the current structure matches W-split-panels; switch the complete layout to W-top-bottom or replace TextBlock with a component allowed by W-split-panels | W-content-side-slots variant 1: slot root/1.itemMargin must be 12, got None; slot root/1 must have 2 children, got 1; slot root/1/0.width must resolve to 132, got 116.0; slot root/1/0.height must resolve to 57, got 110.0; slot root/1/1 is missing | W-four-slots variant 1: slot root must use Column, got Row; slot root/0 must use Row, got Column; slot root/0.width must be 276, got 132.0; slot root/0.height must be 57, got 126.0; slot root/0.itemMargin must be 12, got None; slot root/0 must have 2 children, got 1; slot root/1 must use Row, got Column; slot root/1.width must be 276, got 132.0; slot root/1.height must be 57, got 126.0; slot root/1.itemMargin must be 12, got None; slot root/1 must have 2 children, got 1; slot root/0/0.width must resolve to 132, got 116.0; slot root/0/0.height must resolve to 57, got 110.0; slot root/0/1 is missing; slot root/1/0.width must resolve to 132, got 116.0; slot root/1/0.height must resolve to 57, got 110.0; slot root/1/1 is missing."
    }
  ]
}
```
```repair-3
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"W-top-bottom\",\"variant\":\"continuous\"},[\"title\",\"primary\",\"details\"]]\n[\"title\",\"SingleLineTitle\",{\"title\":\"今日概览\",\"fontSize\":12}]\n[\"primary\",\"EmphasisText\",{\"mainText\":{\"path\":\"/data/weather/current/temperatureText\"},\"secondaryText\":{\"path\":\"/data/weather/current/condition\"},\"fontSize\":18}]\n[\"details\",\"TextBlock\",{\"items\":[{\"label\":\"电量\",\"value\":{\"path\":\"/data/phoneBattery/batterySOCText\"}},{\"label\":\"步数\",\"value\":\"{{ ${/data/healthSport/dailySteps} + '步' }}\"},{\"label\":\"消耗\",\"value\":{\"path\":\"/data/healthSport/dailyTotalCaloriesText\"}},{\"label\":\"运动\",\"value\":{\"path\":\"/data/healthSport/exerciseTypeName\"}}]}]\n[\"/data/weather/current/temperatureText\",\"29℃\"]\n[\"/data/weather/current/condition\",\"多云\"]\n[\"/data/phoneBattery/batterySOCText\",\"68%\"]\n[\"/data/phoneBattery/chargingStatusDesc\",\"未充电\"]\n[\"/data/phoneBattery/batterySOC\",68]\n[\"/data/healthSport/dailySteps\",6200]\n[\"/data/healthSport/dailyTotalCaloriesText\",\"420 千卡\"]\n[\"/data/healthSport/exerciseTypeName\",\"户外跑步\"]\n[\"/data/healthSport/exerciseDurationText\",\"40分\"]\n[\"/data/powerRanking/rankingList/0/appName\",\"示例\"]\n[\"/data/powerRanking/rankingList/0/powerText\",\"示例\"]\n[\"/data/powerRanking/rankingList/1/appName\",\"示例\"]\n[\"/data/powerRanking/rankingList/1/powerText\",\"示例\"]\n[\"/data/powerRanking/rankingList/2/appName\",\"示例\"]\n[\"/data/powerRanking/rankingList/2/powerText\",\"示例\"]",
  "generatedDsl": "{\"version\":\"v0.9\",\"createSurface\":{\"surfaceId\":\"surface_card\",\"catalogId\":\"ohos.a2ui.extended.catalog.form\"}}\n{\"version\":\"v0.9\",\"updateComponents\":{\"surfaceId\":\"surface_card\",\"root\":\"root\",\"components\":[{\"id\":\"root\",\"component\":\"Column\",\"children\":[\"title\",\"__layout__root__body\"],\"itemMargin\":6,\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"padding\":12,\"borderRadius\":20,\"clip\":true,\"alignItems\":\"start\",\"justifyContent\":\"start\"}},{\"id\":\"title\",\"component\":\"Row\",\"children\":[\"title_title\"],\"styles\":{\"width\":\"matchParent\",\"height\":12,\"flexShrink\":0,\"justifyContent\":\"start\",\"alignItems\":\"center\"},\"itemMargin\":0},{\"id\":\"title_title\",\"component\":\"Text\",\"content\":\"今日概览\",\"styles\":{\"fontSize\":12,\"fontWeight\":400,\"lineHeight\":1,\"textAlign\":\"start\",\"maxLines\":1,\"flexShrink\":0,\"width\":\"matchParent\",\"fontColor\":\"@theme:secondary/1\"}},{\"id\":\"__layout__root__body\",\"component\":\"Column\",\"children\":[\"__layout__root__primary\",\"__layout__root__details\"],\"itemMargin\":8,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":1}},{\"id\":\"__layout__root__primary\",\"component\":\"Column\",\"children\":[\"primary\"],\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"primary\",\"component\":\"Column\",\"children\":[\"primary_main\",\"primary_secondary\"],\"itemMargin\":2,\"styles\":{\"alignItems\":\"start\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"width\":\"matchParent\"}},{\"id\":\"primary_main\",\"component\":\"Text\",\"content\":\"{{ ${/data/weather/current/temperatureText} }}\",\"styles\":{\"height\":18,\"fontSize\":18,\"fontWeight\":700,\"lineHeight\":1,\"maxLines\":1,\"flexShrink\":1,\"width\":\"matchParent\",\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"primary_secondary\",\"component\":\"Text\",\"content\":\"{{ ${/data/weather/current/condition} }}\",\"styles\":{\"height\":16,\"fontSize\":12,\"fontWeight\":400,\"lineHeight\":1.3333333333333333,\"maxLines\":1,\"flexShrink\":1,\"width\":\"matchParent\",\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"__layout__root__details\",\"component\":\"Column\",\"children\":[\"details\"],\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":1},\"itemMargin\":0},{\"id\":\"details\",\"component\":\"Row\",\"children\":[\"details_item0\",\"details_item1\",\"details_item2\",\"details_item3\"],\"itemMargin\":8,\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"alignItems\":\"top\",\"justifyContent\":\"start\",\"layoutWeight\":1,\"flexShrink\":1,\"constraintSize\":{\"minHeight\":48}}},{\"id\":\"details_item0\",\"component\":\"Column\",\"children\":[\"details_item0_label_slot\",\"details_item0_value_slot\"],\"itemMargin\":2,\"styles\":{\"height\":\"matchParent\",\"backgroundColor\":\"@theme:panel/1\",\"padding\":{\"left\":8,\"right\":8},\"borderRadius\":16,\"alignItems\":\"start\",\"justifyContent\":\"center\",\"layoutWeight\":1,\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0,\"minHeight\":0}}},{\"id\":\"details_item0_label_slot\",\"component\":\"Row\",\"children\":[\"details_item0_label\"],\"styles\":{\"width\":\"matchParent\",\"height\":18,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item0_label\",\"component\":\"Text\",\"content\":\"电量\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":12,\"fontWeight\":700,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/0.6\"}},{\"id\":\"details_item0_value_slot\",\"component\":\"Row\",\"children\":[\"details_item0_value\"],\"styles\":{\"width\":\"matchParent\",\"height\":16,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item0_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/phoneBattery/batterySOCText} }}\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":10,\"fontWeight\":500,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/1\"}},{\"id\":\"details_item1\",\"component\":\"Column\",\"children\":[\"details_item1_label_slot\",\"details_item1_value_slot\"],\"itemMargin\":2,\"styles\":{\"height\":\"matchParent\",\"backgroundColor\":\"@theme:panel/1\",\"padding\":{\"left\":8,\"right\":8},\"borderRadius\":16,\"alignItems\":\"start\",\"justifyContent\":\"center\",\"layoutWeight\":1,\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0,\"minHeight\":0}}},{\"id\":\"details_item1_label_slot\",\"component\":\"Row\",\"children\":[\"details_item1_label\"],\"styles\":{\"width\":\"matchParent\",\"height\":18,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item1_label\",\"component\":\"Text\",\"content\":\"步数\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":12,\"fontWeight\":700,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/0.6\"}},{\"id\":\"details_item1_value_slot\",\"component\":\"Row\",\"children\":[\"details_item1_value\"],\"styles\":{\"width\":\"matchParent\",\"height\":16,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item1_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/healthSport/dailySteps} + '步' }}\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":10,\"fontWeight\":500,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/1\"}},{\"id\":\"details_item2\",\"component\":\"Column\",\"children\":[\"details_item2_label_slot\",\"details_item2_value_slot\"],\"itemMargin\":2,\"styles\":{\"height\":\"matchParent\",\"backgroundColor\":\"@theme:panel/1\",\"padding\":{\"left\":8,\"right\":8},\"borderRadius\":16,\"alignItems\":\"start\",\"justifyContent\":\"center\",\"layoutWeight\":1,\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0,\"minHeight\":0}}},{\"id\":\"details_item2_label_slot\",\"component\":\"Row\",\"children\":[\"details_item2_label\"],\"styles\":{\"width\":\"matchParent\",\"height\":18,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item2_label\",\"component\":\"Text\",\"content\":\"消耗\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":12,\"fontWeight\":700,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/0.6\"}},{\"id\":\"details_item2_value_slot\",\"component\":\"Row\",\"children\":[\"details_item2_value\"],\"styles\":{\"width\":\"matchParent\",\"height\":16,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item2_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/healthSport/dailyTotalCaloriesText} }}\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":10,\"fontWeight\":500,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/1\"}},{\"id\":\"details_item3\",\"component\":\"Column\",\"children\":[\"details_item3_label_slot\",\"details_item3_value_slot\"],\"itemMargin\":2,\"styles\":{\"height\":\"matchParent\",\"backgroundColor\":\"@theme:panel/1\",\"padding\":{\"left\":8,\"right\":8},\"borderRadius\":16,\"alignItems\":\"start\",\"justifyContent\":\"center\",\"layoutWeight\":1,\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0,\"minHeight\":0}}},{\"id\":\"details_item3_label_slot\",\"component\":\"Row\",\"children\":[\"details_item3_label\"],\"styles\":{\"width\":\"matchParent\",\"height\":18,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item3_label\",\"component\":\"Text\",\"content\":\"运动\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":12,\"fontWeight\":700,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/0.6\"}},{\"id\":\"details_item3_value_slot\",\"component\":\"Row\",\"children\":[\"details_item3_value\"],\"styles\":{\"width\":\"matchParent\",\"height\":16,\"alignItems\":\"center\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"details_item3_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/healthSport/exerciseTypeName} }}\",\"styles\":{\"width\":\"matchParent\",\"fontSize\":10,\"fontWeight\":500,\"textAlign\":\"start\",\"maxLines\":1,\"textOverflow\":\"ellipsis\",\"fontColor\":\"@theme:primary/1\"}}]}}\n{\"version\":\"v0.9\",\"updateDataModel\":{\"surfaceId\":\"surface_card\",\"path\":\"/\",\"value\":{\"data\":{\"weather\":{\"current\":{\"temperatureText\":\"29℃\",\"condition\":\"多云\"}},\"phoneBattery\":{\"batterySOCText\":\"68%\",\"chargingStatusDesc\":\"未充电\",\"batterySOC\":68},\"healthSport\":{\"dailySteps\":6200,\"dailyTotalCaloriesText\":\"420 千卡\",\"exerciseTypeName\":\"户外跑步\",\"exerciseDurationText\":\"40分\"},\"powerRanking\":{\"rankingList\":[{\"appName\":\"示例\",\"powerText\":\"示例\"},{\"appName\":\"示例\",\"powerText\":\"示例\"},{\"appName\":\"示例\",\"powerText\":\"示例\"}]}}}}}",
  "validationErrors": []
}
```
