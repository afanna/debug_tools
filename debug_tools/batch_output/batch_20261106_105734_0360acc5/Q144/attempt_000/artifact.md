```cardspec
{
  "title": "空气质量卡片",
  "description": "实时查看当前空气质量等级、温度、湿度等天气信息",
  "suggestSize": "2x2",
  "imageDomainWhitelist": [
    "hag-ability-test.obs.cn-north-1.myhuaweicloud.com",
    "lfcontentcenterdev.hwcloudtest.cn",
    "hagres-drcn.dbankcdn.com"
  ],
  "dataBindings": [
    {
      "capabilityId": "ViewWeather",
      "arguments": {},
      "writeResultTo": "/data/weather"
    }
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["title","__layout__root__body"],"itemMargin":6,"styles":{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","padding":12,"linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"title","component":"Row","children":["title_title"],"styles":{"width":"matchParent","height":12,"flexShrink":0,"justifyContent":"start","alignItems":"center"},"itemMargin":0},{"id":"title_title","component":"Text","content":"{{ ${/data/weather/location/prefectureName} }}","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":0,"width":"matchParent","fontColor":"#991F4799"}},{"id":"__layout__root__body","component":"Column","children":["__layout__root__primary","__layout__root__support"],"itemMargin":8,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__root__primary","component":"Column","children":["primary"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1,"flexShrink":0},"itemMargin":0},{"id":"primary","component":"Column","children":["primary_main"],"itemMargin":2,"styles":{"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"primary_main","component":"Text","content":"{{ '空气质量 ' + ${/data/weather/current/airQuality} }}","styles":{"height":18,"fontSize":18,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"__layout__root__support","component":"Column","children":["support"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"support","component":"Column","children":["support_row0","support_row1"],"itemMargin":2,"styles":{"width":"matchParent","alignItems":"start","flexShrink":1}},{"id":"support_item0_label","component":"Text","content":"温度","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"support_item0_value","component":"Text","content":"{{ ${/data/weather/current/temperatureText} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"support_item0","component":"Row","children":["support_item0_label","support_item0_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"support_row0","component":"Row","children":["support_item0"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"top","flexShrink":0}},{"id":"support_item1_label","component":"Text","content":"天气","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"support_item1_value","component":"Text","content":"{{ ${/data/weather/current/condition} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"support_item1","component":"Row","children":["support_item1_label","support_item1_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"support_row1","component":"Row","children":["support_item1"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"top","flexShrink":0}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"weather":{"location":{"prefectureName":"上海市"},"current":{"airQuality":"良","temperatureText":"29℃","condition":"多云"}}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "生成一个实时查看空气质量的卡片，显示当前空气质量等级和温度等信息",
  "size": "2x2",
  "appVersion": "11.7.8.339",
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
      }
    }
  },
  "assetCandidates": []
}
```
```effectivecapabilities
{
  "data": [
    "ViewWeather"
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
      "arguments": {},
      "writeResultTo": "/data/weather",
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
  "artifactId": "e9e9c07c-105d-4e90-bee2-aea5cf3f17dd",
  "createdAt": 1793933866555
}
```
```designcompactdsl
["root","Layout",{"layout":"S-title-dual-content"},["title","primary","support"]]
["title","SingleLineTitle",{"title":{"path":"/data/weather/location/prefectureName"},"fontSize":12}]
["primary","EmphasisText",{"mainText":"{{ '空气质量 ' + ${/data/weather/current/airQuality} }}","fontSize":18}]
["support","SecondaryBody",{"items":[{"label":"温度 ","value":{"path":"/data/weather/current/temperatureText"}},{"label":"天气 ","value":{"path":"/data/weather/current/condition"}}],"fontSize":14}]
["/data/weather/location/prefectureName","上海市"]
["/data/weather/current/airQuality","良"]
["/data/weather/current/temperatureText","29℃"]
["/data/weather/current/condition","多云"]
```
```request
{
  "content": {
    "title": "空气质量卡片",
    "description": "实时查看当前空气质量等级、温度、湿度等天气信息",
    "userQuery": "生成一个实时查看空气质量的卡片，显示当前空气质量等级和温度等信息",
    "size": "2x2",
    "bundleName": "com.huawei.genui",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "CMS-AL20 7.0.0.111",
    "candidateDataBindings": [
      {
        "capabilityId": "ViewWeather",
        "writeResultTo": "/data/weather"
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
    "phoneType": "CMS-AL20",
    "prdVer": "11.7.8.339",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261016085007614"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q144-000",
    "isNew": true,
    "sessionId": "batch-0360acc5"
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
  "romVersion": "CMS-AL20 7.0.0.111",
  "bundleName": "com.huawei.genui",
  "description": "实时查看当前空气质量等级、温度、湿度等天气信息",
  "userQuery": "生成一个实时查看空气质量的卡片，显示当前空气质量等级和温度等信息",
  "title": "空气质量卡片",
  "dataCapabilityIds": [
    "ViewWeather"
  ]
}
```
