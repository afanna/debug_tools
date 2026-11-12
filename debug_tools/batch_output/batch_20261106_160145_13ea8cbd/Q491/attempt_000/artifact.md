```cardspec
{
  "title": "南京天气",
  "description": "实时天气速览",
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
        "forecastDays": 1,
        "prefectureName": "南京市"
      },
      "writeResultTo": "/data/weather"
    }
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["title","__layout__root__body"],"itemMargin":6,"onClick":[{"call":"clickToDeeplink","args":{"abilityName":"","bundleName":"","intentName":"Weather_CityCode","uri":"{{ 'hww://www.huawei.com/totemweather?enterType=share&cityCode=' + ${/data/weather/location/cityCode} }}"}}],"styles":{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","padding":12,"linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"title","component":"Row","children":["title_title"],"styles":{"width":"matchParent","height":12,"flexShrink":0,"justifyContent":"start","alignItems":"center"},"itemMargin":0},{"id":"title_title","component":"Text","content":"{{ ${/data/weather/location/prefectureName} }}","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":0,"width":"matchParent","fontColor":"#991F4799"}},{"id":"__layout__root__body","component":"Column","children":["__layout__root__primary","__layout__root__support"],"itemMargin":8,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__root__primary","component":"Column","children":["primary"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1,"flexShrink":0},"itemMargin":0},{"id":"primary","component":"Row","children":["primary_value"],"itemMargin":0,"styles":{"justifyContent":"start","alignItems":"bottom","flexShrink":0,"width":"matchParent"}},{"id":"primary_value","component":"Text","content":"{{ ${/data/weather/current/temperatureText} }}","styles":{"height":30,"fontSize":30,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":0,"fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"__layout__root__support","component":"Column","children":["support"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"support","component":"Column","children":["support_row0"],"itemMargin":2,"styles":{"width":"matchParent","alignItems":"start","flexShrink":1}},{"id":"support_item0_label","component":"Text","content":"天气","styles":{"height":14,"fontSize":14,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"support_item0_value","component":"Text","content":"{{ ${/data/weather/current/condition} }}","styles":{"height":14.0,"fontSize":14,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"support_item0","component":"Row","children":["support_item0_label","support_item0_value"],"itemMargin":4,"styles":{"height":14.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"support_row0","component":"Row","children":["support_item0"],"itemMargin":0,"styles":{"width":"matchParent","height":14.0,"alignItems":"top","flexShrink":0}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"weather":{"location":{"prefectureName":"上海市","cityCode":"60814"},"current":{"temperatureText":"29℃","condition":"多云"}}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "创建一张桌面卡片显示南京天气，展示当前天气状况和温度",
  "size": "2x2",
  "appVersion": "11.7.9.300",
  "eventCandidates": [
    {
      "id": "event.open.weather",
      "description": "打开华为天气应用某城市页，uri为固定值勿更改。cityCode来自于数据能力中ViewWeather出参cityCode字段，进行动态拼接，表示跳转到指定城市天气页。",
      "call": "clickToDeeplink",
      "args": {
        "abilityName": "",
        "bundleName": "",
        "intentName": "Weather_CityCode",
        "uri": "{{ 'hww://www.huawei.com/totemweather?enterType=share&cityCode=' + ${/data/weather/location/cityCode} }}"
      }
    }
  ],
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
        },
        "location": {
          "prefectureName": {
            "type": "string",
            "description": "城市名称",
            "sampleValue": "上海市"
          },
          "cityCode": {
            "type": "string",
            "description": "城市代码，如60814代表青浦区",
            "sampleValue": "60814"
          }
        },
        "daily": [
          {
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
            }
          }
        ]
      }
    }
  },
  "assetCandidates": [
    {
      "id": "asset.ic_weather_monochrome",
      "src": "resources/base/media/ic_weather_monochrome.svg",
      "description": "样式：黑色单色云朵图标，原始尺寸为 24×24，可随主题染成白色或黑色；选择：普通天气或天气详情需求的首选云朵图标。适用：天气卡片中配合 ViewWeather 的 current.condition 或 daily.condition 展示天气现象，也可与 event.open.weather 组成天气详情入口。图标仅表示天气主题，不代表晴、阴、雨等具体天气状态。"
    }
  ]
}
```
```effectivecapabilities
{
  "data": [
    "ViewWeather"
  ],
  "event": [
    {
      "id": "event.open.weather",
      "description": "打开华为天气应用某城市页，uri为固定值勿更改。cityCode来自于数据能力中ViewWeather出参cityCode字段，进行动态拼接，表示跳转到指定城市天气页。",
      "call": "clickToDeeplink",
      "args": {
        "abilityName": "",
        "bundleName": "",
        "intentName": "Weather_CityCode",
        "uri": "{{ 'hww://www.huawei.com/totemweather?enterType=share&cityCode=' + ${/data/weather/location/cityCode} }}"
      }
    }
  ],
  "asset": [
    "asset.ic_weather_monochrome"
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
        "forecastDays": 1,
        "prefectureName": "南京市"
      },
      "writeResultTo": "/data/weather",
      "candidateOutputFields": [
        "/current/temperatureText",
        "/current/condition",
        "/location/prefectureName",
        "/daily/0/weekday",
        "/daily/0/condition",
        "/daily/0/temperatureRangeText"
      ]
    }
  ],
  "candidateEventCandidates": [
    {
      "capabilityId": "event.open.weather",
      "action": {
        "call": "clickToDeeplink",
        "args": {
          "abilityName": "",
          "bundleName": "",
          "intentName": "Weather_CityCode",
          "uri": "{{ 'hww://www.huawei.com/totemweather?enterType=share&cityCode=' + ${/data/weather/location/cityCode} }}"
        }
      }
    }
  ],
  "candidateAssetIds": [
    "asset.ic_weather_monochrome"
  ]
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
  "artifactId": "2328d2f4-46d7-4632-993d-314c7ab5fcf3",
  "createdAt": 1793952302656
}
```
```designcompactdsl
["root","Layout",{"layout":"S-title-dual-content","onClick":[{"call":"clickToDeeplink","args":{"abilityName":"","bundleName":"","intentName":"Weather_CityCode","uri":"{{ 'hww://www.huawei.com/totemweather?enterType=share&cityCode=' + ${/data/weather/location/cityCode} }}"}}]},["title","primary","support"]]
["title","SingleLineTitle",{"title":{"path":"/data/weather/location/prefectureName"},"fontSize":12}]
["primary","EmphasizedData",{"value":{"path":"/data/weather/current/temperatureText"},"fontSize":30}]
["support","SecondaryBody",{"items":[{"label":"天气","value":{"path":"/data/weather/current/condition"}}],"fontSize":14}]
["/data/weather/location/prefectureName","上海市"]
["/data/weather/location/cityCode","60814"]
["/data/weather/current/temperatureText","29℃"]
["/data/weather/current/condition","多云"]
```
```request
{
  "content": {
    "size": "2x2",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "CMS-AL20 7.0.0.120",
    "candidateAssetIds": [
      "asset.ic_weather_monochrome"
    ],
    "candidateEventCandidates": [
      {
        "capabilityId": "event.open.weather",
        "action": {
          "call": "clickToDeeplink",
          "args": {
            "abilityName": "",
            "bundleName": "",
            "intentName": "Weather_CityCode",
            "uri": "{{ 'hww://www.huawei.com/totemweather?enterType=share&cityCode=' + ${/data/weather/location/cityCode} }}"
          }
        }
      }
    ],
    "bundleName": "com.huawei.genui",
    "description": "实时天气速览",
    "userQuery": "创建一张桌面卡片显示南京天气，展示当前天气状况和温度",
    "title": "南京天气",
    "candidateDataBindings": [
      {
        "capabilityId": "ViewWeather",
        "arguments": {
          "forecastDays": 1,
          "prefectureName": "南京市"
        },
        "writeResultTo": "/data/weather",
        "candidateOutputFields": [
          "/current/temperatureText",
          "/current/condition",
          "/location/prefectureName",
          "/daily/0/weekday",
          "/daily/0/condition",
          "/daily/0/temperatureRangeText"
        ]
      }
    ]
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "CMS-AL20",
    "prdVer": "11.7.9.300",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261104065110402"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q491-000",
    "isNew": true,
    "sessionId": "batch-13ea8cbd"
  },
  "userAuth": {
    "user": {}
  },
  "utterance": {
    "original": "",
    "type": "text"
  },
  "version": "1.0",
  "size": "2x2",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "CMS-AL20 7.0.0.120",
  "candidateAssetIds": [
    "asset.ic_weather_monochrome"
  ],
  "candidateEventCandidates": [
    {
      "capabilityId": "event.open.weather",
      "action": {
        "call": "clickToDeeplink",
        "args": {
          "abilityName": "",
          "bundleName": "",
          "intentName": "Weather_CityCode",
          "uri": "{{ 'hww://www.huawei.com/totemweather?enterType=share&cityCode=' + ${/data/weather/location/cityCode} }}"
        }
      }
    }
  ],
  "bundleName": "com.huawei.genui",
  "description": "实时天气速览",
  "userQuery": "创建一张桌面卡片显示南京天气，展示当前天气状况和温度",
  "title": "南京天气",
  "candidateDataBindings": [
    {
      "capabilityId": "ViewWeather",
      "arguments": {
        "forecastDays": 1,
        "prefectureName": "南京市"
      },
      "writeResultTo": "/data/weather",
      "candidateOutputFields": [
        "/current/temperatureText",
        "/current/condition",
        "/location/prefectureName",
        "/daily/0/weekday",
        "/daily/0/condition",
        "/daily/0/temperatureRangeText"
      ]
    }
  ]
}
```
