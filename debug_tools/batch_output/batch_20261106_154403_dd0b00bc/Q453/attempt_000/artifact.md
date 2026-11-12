```cardspec
{
  "title": "杭州天气与耳机电量",
  "description": "展示杭州当前天气和蓝牙耳机电量信息",
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
    },
    {
      "capabilityId": "GetEarphoneInfo",
      "arguments": {},
      "writeResultTo": "/data/earphone"
    }
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["__layout__root__row0","__layout__root__row1"],"itemMargin":8,"styles":{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","padding":12,"linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"__layout__root__row0","component":"Row","children":["top_left","top_right"],"itemMargin":8,"styles":{"width":"matchParent","layoutWeight":1}},{"id":"top_left","component":"Column","children":["top_left_primary","top_left_support"],"itemMargin":2,"styles":{"alignItems":"start","justifyContent":"start","height":"matchParent","layoutWeight":59.0}},{"id":"top_left_primary","component":"Column","children":["top_left_primary_main"],"itemMargin":2,"styles":{"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"top_left_primary_main","component":"Text","content":"{{ ${/data/weather/current/temperatureText} }}","styles":{"height":18,"fontSize":18,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"top_left_support","component":"Column","children":["top_left_support_row0"],"itemMargin":2,"styles":{"width":"matchParent","alignItems":"start","flexShrink":1}},{"id":"top_left_support_item0_value","component":"Text","content":"{{ '杭州 ' + ${/data/weather/current/condition} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"top_left_support_item0","component":"Row","children":["top_left_support_item0_value"],"itemMargin":0,"styles":{"height":12.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"top_left_support_row0","component":"Row","children":["top_left_support_item0"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"top","flexShrink":0}},{"id":"top_right","component":"Column","children":["top_right_primary","top_right_support"],"itemMargin":2,"styles":{"alignItems":"start","justifyContent":"start","height":"matchParent","layoutWeight":59.0}},{"id":"top_right_primary","component":"Column","children":["top_right_primary_main"],"itemMargin":2,"styles":{"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"top_right_primary_main","component":"Text","content":"{{ ${/data/earphone/batteryLevel} + '%' }}","styles":{"height":18,"fontSize":18,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"top_right_support","component":"Column","children":["top_right_support_row0"],"itemMargin":2,"styles":{"width":"matchParent","alignItems":"start","flexShrink":1}},{"id":"top_right_support_item0_value","component":"Text","content":"耳机盒电量","styles":{"height":24.0,"fontSize":12,"fontWeight":400,"maxLines":2,"flexShrink":1,"lineHeight":1,"fontColor":"#991F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"top_right_support_item0","component":"Row","children":["top_right_support_item0_value"],"itemMargin":0,"styles":{"height":24.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"top_right_support_row0","component":"Row","children":["top_right_support_item0"],"itemMargin":0,"styles":{"width":"matchParent","height":24.0,"alignItems":"top","flexShrink":0}},{"id":"__layout__root__row1","component":"Row","children":["bottom_left","bottom_right"],"itemMargin":8,"styles":{"width":"matchParent","layoutWeight":1}},{"id":"bottom_left","component":"Column","children":["bottom_left_primary","bottom_left_support"],"itemMargin":2,"styles":{"alignItems":"start","justifyContent":"start","height":"matchParent","layoutWeight":59.0}},{"id":"bottom_left_primary","component":"Column","children":["bottom_left_primary_main"],"itemMargin":2,"styles":{"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"bottom_left_primary_main","component":"Text","content":"{{ ${/data/earphone/leftBatteryLevel} + '%' }}","styles":{"height":18,"fontSize":18,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"bottom_left_support","component":"Column","children":["bottom_left_support_row0"],"itemMargin":2,"styles":{"width":"matchParent","alignItems":"start","flexShrink":1}},{"id":"bottom_left_support_item0_value","component":"Text","content":"左耳电量","styles":{"height":14.0,"fontSize":14,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#991F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"bottom_left_support_item0","component":"Row","children":["bottom_left_support_item0_value"],"itemMargin":0,"styles":{"height":14.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"bottom_left_support_row0","component":"Row","children":["bottom_left_support_item0"],"itemMargin":0,"styles":{"width":"matchParent","height":14.0,"alignItems":"top","flexShrink":0}},{"id":"bottom_right","component":"Column","children":["bottom_right_primary","bottom_right_support"],"itemMargin":2,"styles":{"alignItems":"start","justifyContent":"start","height":"matchParent","layoutWeight":59.0}},{"id":"bottom_right_primary","component":"Column","children":["bottom_right_primary_main"],"itemMargin":2,"styles":{"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"bottom_right_primary_main","component":"Text","content":"{{ ${/data/earphone/rightBatteryLevel} + '%' }}","styles":{"height":18,"fontSize":18,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"bottom_right_support","component":"Column","children":["bottom_right_support_row0"],"itemMargin":2,"styles":{"width":"matchParent","alignItems":"start","flexShrink":1}},{"id":"bottom_right_support_item0_value","component":"Text","content":"右耳电量","styles":{"height":14.0,"fontSize":14,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#991F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"bottom_right_support_item0","component":"Row","children":["bottom_right_support_item0_value"],"itemMargin":0,"styles":{"height":14.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"bottom_right_support_row0","component":"Row","children":["bottom_right_support_item0"],"itemMargin":0,"styles":{"width":"matchParent","height":14.0,"alignItems":"top","flexShrink":0}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"weather":{"current":{"temperatureText":"29℃","condition":"多云"}},"earphone":{"batteryLevel":80,"leftBatteryLevel":76,"rightBatteryLevel":78}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "帮我生成杭州天气加耳机电量的卡片。展示杭州的天气信息（当前温度、天气状况）和蓝牙耳机的电量信息（耳机盒、左右耳电量）。",
  "size": "2x2",
  "appVersion": "11.7.8.340",
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
      "earphone": {
        "isConnected": {
          "type": "boolean",
          "description": "当前是否有蓝牙耳机处于连接活跃状态。",
          "sampleValue": true
        },
        "earphoneName": {
          "type": "string",
          "description": "耳机的设备广播名称，如果未连接则返回'未连接耳机'。如: 'FreeBuds Pro 3'。",
          "sampleValue": "示例耳机"
        },
        "batteryLevel": {
          "type": "integer",
          "description": "耳机盒（或整体）当前剩余电量的纯整数百分比，取值范围为 0 到 100，返回值不包含“%”。若直接用于文本展示，必须在数值后追加“%”。",
          "sampleValue": 80
        },
        "chargingStatusDesc": {
          "type": "string",
          "description": "耳机盒（或整体）当前的充电状态中文语义描述，'充电中' 或 '未充电'。",
          "sampleValue": "未充电"
        },
        "leftBatteryLevel": {
          "type": "integer",
          "description": "左耳机当前剩余电量的纯整数百分比，取值范围为 0 到 100，返回值不包含“%”；未连接时为 0。若直接用于文本展示，必须在数值后追加“%”。",
          "sampleValue": 76
        },
        "leftChargingStatusDesc": {
          "type": "string",
          "description": "左耳机当前的充电状态中文语义描述，'充电中' 或 '未充电'。",
          "sampleValue": "未充电"
        },
        "rightBatteryLevel": {
          "type": "integer",
          "description": "右耳机当前剩余电量的纯整数百分比，取值范围为 0 到 100，返回值不包含“%”；未连接时为 0。若直接用于文本展示，必须在数值后追加“%”。",
          "sampleValue": 78
        },
        "rightChargingStatusDesc": {
          "type": "string",
          "description": "右耳机当前的充电状态中文语义描述，'充电中' 或 '未充电'。",
          "sampleValue": "未充电"
        },
        "updatedAt": {
          "type": "string",
          "description": "端侧完成多源数据感知和融合的时间戳字符串。如：2026-07-02 20:15",
          "sampleValue": "2026-08-06 09:00"
        }
      }
    }
  },
  "assetCandidates": [
    {
      "id": "asset.emoji_default_weather_blue",
      "src": "resources/base/media/emoji_default_weather_blue.png",
      "description": "样式：蓝灰色圆形底上的白色渐变云朵图标，圆形外透明，原始尺寸为 64×64，PNG 位图需保留原色；适用：通用天气概览或未匹配到更具体天气素材的卡片，可结合 ViewWeather 的 current.condition 或 daily.condition 展示，也可与 event.open.weather 组成天气详情入口。云朵图形仅表示天气主题，不可据此推断实际为多云、阴天或存在降水。"
    },
    {
      "id": "asset.emoji_earbud_case_black",
      "src": "resources/base/media/emoji_earbud_case_black.png",
      "description": "样式：深灰到黑色渐变的封闭式蓝牙耳机充电盒，盒体呈圆润横向椭圆并带高光，透明背景，原始尺寸为 64×64，PNG 位图需保留原色；适用：蓝牙耳机盒或整体电量与充电状态卡片，可结合 GetEarphoneInfo 的 batteryLevel 和 chargingStatusDesc 展示，也可作为 event.open.settings.bluetooth 的蓝牙设置入口。图标不表示耳机盒当前正在充电、已经打开或具有特定电量。"
    },
    {
      "id": "asset.icon_earphone",
      "src": "resources/base/media/icon_earphone.svg",
      "description": "样式：默认黑色的单色左右分体式开放耳机，局部通过镂空表现高光与分隔，支持通过 fillColor 与卡片配色统一；适用：无线耳机本体、耳机连接、左右耳设备状态。"
    }
  ]
}
```
```effectivecapabilities
{
  "data": [
    "ViewWeather",
    "GetEarphoneInfo"
  ],
  "event": [],
  "asset": [
    "asset.emoji_default_weather_blue",
    "asset.emoji_earbud_case_black",
    "asset.icon_earphone"
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
      "arguments": {},
      "writeResultTo": "/data/weather",
      "candidateOutputFields": [
        "/location/cityCode",
        "/location/districtName",
        "/location/prefectureName",
        "/current/temperatureC",
        "/current/temperatureText",
        "/current/condition",
        "/current/feelsLikeC",
        "/current/humidityPercent",
        "/current/airQuality",
        "/current/windDirection",
        "/current/windLevel",
        "/current/uvIndex",
        "/current/coldLevel",
        "/current/alertLevel",
        "/daily/0/date",
        "/daily/0/weekday",
        "/daily/0/condition",
        "/daily/0/temperatureRangeText",
        "/daily/0/rainProbabilityPercent",
        "/daily/0/airQuality",
        "/daily/0/uvIndex",
        "/daily/0/coldLevel",
        "/updatedAt"
      ]
    },
    {
      "capabilityId": "GetEarphoneInfo",
      "arguments": {},
      "writeResultTo": "/data/earphone",
      "candidateOutputFields": [
        "/isConnected",
        "/earphoneName",
        "/batteryLevel",
        "/chargingStatusDesc",
        "/leftBatteryLevel",
        "/leftChargingStatusDesc",
        "/rightBatteryLevel",
        "/rightChargingStatusDesc",
        "/updatedAt"
      ]
    }
  ],
  "candidateEventCandidates": [],
  "candidateAssetIds": [
    "asset.emoji_default_weather_blue",
    "asset.emoji_earbud_case_black",
    "asset.icon_earphone"
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
  "artifactId": "efb03f4e-48de-45c4-9b19-72e54ed3b3c5",
  "createdAt": 1793951124148
}
```
```designcompactdsl
["root","Layout",{"layout":"S-quad-content"},["top_left","top_right","bottom_left","bottom_right"]]
["top_left","Group",{"variant":"hero-support"},["top_left_primary","top_left_support"]]
["top_left_primary","EmphasisText",{"mainText":{"path":"/data/weather/current/temperatureText"},"fontSize":18}]
["top_left_support","SecondaryBody",{"items":[{"value":"{{ '杭州 ' + ${/data/weather/current/condition} }}"}],"fontSize":12}]
["top_right","Group",{"variant":"hero-support"},["top_right_primary","top_right_support"]]
["top_right_primary","EmphasisText",{"mainText":"{{ ${/data/earphone/batteryLevel} + '%' }}","fontSize":18}]
["top_right_support","SecondaryBody",{"items":[{"value":"耳机盒电量"}],"fontSize":12}]
["bottom_left","Group",{"variant":"hero-support"},["bottom_left_primary","bottom_left_support"]]
["bottom_left_primary","EmphasisText",{"mainText":"{{ ${/data/earphone/leftBatteryLevel} + '%' }}","fontSize":18}]
["bottom_left_support","SecondaryBody",{"items":[{"value":"左耳电量"}],"fontSize":12}]
["bottom_right","Group",{"variant":"hero-support"},["bottom_right_primary","bottom_right_support"]]
["bottom_right_primary","EmphasisText",{"mainText":"{{ ${/data/earphone/rightBatteryLevel} + '%' }}","fontSize":18}]
["bottom_right_support","SecondaryBody",{"items":[{"value":"右耳电量"}],"fontSize":12}]
["/data/weather/current/temperatureText","29℃"]
["/data/weather/current/condition","多云"]
["/data/earphone/batteryLevel",80]
["/data/earphone/leftBatteryLevel",76]
["/data/earphone/rightBatteryLevel",78]
```
```request
{
  "content": {
    "size": "2x2",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "ICL-AL10 7.0.0.111",
    "candidateAssetIds": [
      "asset.emoji_default_weather_blue",
      "asset.emoji_earbud_case_black",
      "asset.icon_earphone"
    ],
    "candidateEventCandidates": [],
    "bundleName": "com.huawei.genui",
    "description": "展示杭州当前天气和蓝牙耳机电量信息",
    "userQuery": "帮我生成杭州天气加耳机电量的卡片。展示杭州的天气信息（当前温度、天气状况）和蓝牙耳机的电量信息（耳机盒、左右耳电量）。",
    "title": "杭州天气与耳机电量",
    "candidateDataBindings": [
      {
        "capabilityId": "ViewWeather",
        "arguments": {},
        "writeResultTo": "/data/weather",
        "candidateOutputFields": [
          "/location/cityCode",
          "/location/districtName",
          "/location/prefectureName",
          "/current/temperatureC",
          "/current/temperatureText",
          "/current/condition",
          "/current/feelsLikeC",
          "/current/humidityPercent",
          "/current/airQuality",
          "/current/windDirection",
          "/current/windLevel",
          "/current/uvIndex",
          "/current/coldLevel",
          "/current/alertLevel",
          "/daily/0/date",
          "/daily/0/weekday",
          "/daily/0/condition",
          "/daily/0/temperatureRangeText",
          "/daily/0/rainProbabilityPercent",
          "/daily/0/airQuality",
          "/daily/0/uvIndex",
          "/daily/0/coldLevel",
          "/updatedAt"
        ]
      },
      {
        "capabilityId": "GetEarphoneInfo",
        "arguments": {},
        "writeResultTo": "/data/earphone",
        "candidateOutputFields": [
          "/isConnected",
          "/earphoneName",
          "/batteryLevel",
          "/chargingStatusDesc",
          "/leftBatteryLevel",
          "/leftChargingStatusDesc",
          "/rightBatteryLevel",
          "/rightChargingStatusDesc",
          "/updatedAt"
        ]
      }
    ]
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "ICL-AL10",
    "prdVer": "11.7.8.340",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261105073944491"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q453-000",
    "isNew": true,
    "sessionId": "batch-dd0b00bc"
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
  "romVersion": "ICL-AL10 7.0.0.111",
  "candidateAssetIds": [
    "asset.emoji_default_weather_blue",
    "asset.emoji_earbud_case_black",
    "asset.icon_earphone"
  ],
  "candidateEventCandidates": [],
  "bundleName": "com.huawei.genui",
  "description": "展示杭州当前天气和蓝牙耳机电量信息",
  "userQuery": "帮我生成杭州天气加耳机电量的卡片。展示杭州的天气信息（当前温度、天气状况）和蓝牙耳机的电量信息（耳机盒、左右耳电量）。",
  "title": "杭州天气与耳机电量",
  "candidateDataBindings": [
    {
      "capabilityId": "ViewWeather",
      "arguments": {},
      "writeResultTo": "/data/weather",
      "candidateOutputFields": [
        "/location/cityCode",
        "/location/districtName",
        "/location/prefectureName",
        "/current/temperatureC",
        "/current/temperatureText",
        "/current/condition",
        "/current/feelsLikeC",
        "/current/humidityPercent",
        "/current/airQuality",
        "/current/windDirection",
        "/current/windLevel",
        "/current/uvIndex",
        "/current/coldLevel",
        "/current/alertLevel",
        "/daily/0/date",
        "/daily/0/weekday",
        "/daily/0/condition",
        "/daily/0/temperatureRangeText",
        "/daily/0/rainProbabilityPercent",
        "/daily/0/airQuality",
        "/daily/0/uvIndex",
        "/daily/0/coldLevel",
        "/updatedAt"
      ]
    },
    {
      "capabilityId": "GetEarphoneInfo",
      "arguments": {},
      "writeResultTo": "/data/earphone",
      "candidateOutputFields": [
        "/isConnected",
        "/earphoneName",
        "/batteryLevel",
        "/chargingStatusDesc",
        "/leftBatteryLevel",
        "/leftChargingStatusDesc",
        "/rightBatteryLevel",
        "/rightChargingStatusDesc",
        "/updatedAt"
      ]
    }
  ]
}
```
```repair-1
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"S-quad-content\"},[\"top_left\",\"top_right\",\"bottom_left\",\"bottom_right\"]]\n[\"top_left\",\"Group\",{\"variant\":\"hero-support\"},[\"top_left_primary\",\"top_left_support\"]]\n[\"top_left_primary\",\"EmphasisText\",{\"mainText\":{\"path\":\"/data/weather/current/temperatureText\"},\"fontSize\":18}]\n[\"top_left_support\",\"SecondaryBody\",{\"items\":[{\"value\":\"{{ '杭州 ' + ${/data/weather/current/condition} }}\"}],\"fontSize\":12}]\n[\"top_right\",\"Group\",{\"variant\":\"hero-support\"},[\"top_right_primary\",\"top_right_support\"]]\n[\"top_right_primary\",\"EmphasisText\",{\"mainText\":\"{{ ${/data/earphone/batteryLevel} + '%' }}\",\"fontSize\":18}]\n[\"top_right_support\",\"SecondaryBody\",{\"items\":[{\"value\":\"耳机盒电量\"}],\"fontSize\":12}]\n[\"bottom_left\",\"Group\",{\"variant\":\"hero-support\"},[\"bottom_left_primary\",\"bottom_left_support\"]]\n[\"bottom_left_primary\",\"EmphasisText\",{\"mainText\":\"{{ ${/data/earphone/leftBatteryLevel} + '%' }}\",\"fontSize\":18}]\n[\"bottom_left_support\",\"SecondaryBody\",{\"items\":[{\"value\":\"左耳电量\"}],\"fontSize\":12}]\n[\"bottom_right\",\"Group\",{\"variant\":\"hero-support\"},[\"bottom_right_primary\",\"bottom_right_support\"]]\n[\"bottom_right_primary\",\"EmphasisText\",{\"mainText\":\"{{ ${/data/earphone/rightBatteryLevel} + '%' }}\",\"fontSize\":18}]\n[\"bottom_right_support\",\"SecondaryBody\",{\"items\":[{\"value\":\"右耳电量\"}],\"fontSize\":12}]\n[\"/data/weather/current/temperatureText\",\"29℃\"]\n[\"/data/weather/current/condition\",\"多云\"]\n[\"/data/earphone/batteryLevel\",80]\n[\"/data/earphone/leftBatteryLevel\",76]\n[\"/data/earphone/rightBatteryLevel\",78]",
  "generatedDsl": "{\"version\":\"v0.9\",\"createSurface\":{\"surfaceId\":\"surface_card\",\"catalogId\":\"ohos.a2ui.extended.catalog.form\"}}\n{\"version\":\"v0.9\",\"updateComponents\":{\"surfaceId\":\"surface_card\",\"root\":\"root\",\"components\":[{\"id\":\"root\",\"component\":\"Column\",\"children\":[\"__layout__root__row0\",\"__layout__root__row1\"],\"itemMargin\":8,\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"borderRadius\":20,\"clip\":true,\"alignItems\":\"start\",\"justifyContent\":\"start\",\"padding\":12}},{\"id\":\"__layout__root__row0\",\"component\":\"Row\",\"children\":[\"top_left\",\"top_right\"],\"itemMargin\":8,\"styles\":{\"width\":\"matchParent\",\"layoutWeight\":1}},{\"id\":\"top_left\",\"component\":\"Column\",\"children\":[\"top_left_primary\",\"top_left_support\"],\"itemMargin\":2,\"styles\":{\"alignItems\":\"start\",\"justifyContent\":\"start\",\"height\":\"matchParent\",\"layoutWeight\":59.0}},{\"id\":\"top_left_primary\",\"component\":\"Column\",\"children\":[\"top_left_primary_main\"],\"itemMargin\":2,\"styles\":{\"alignItems\":\"start\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"width\":\"matchParent\"}},{\"id\":\"top_left_primary_main\",\"component\":\"Text\",\"content\":\"{{ ${/data/weather/current/temperatureText} }}\",\"styles\":{\"height\":18,\"fontSize\":18,\"fontWeight\":700,\"lineHeight\":1,\"maxLines\":1,\"flexShrink\":1,\"width\":\"matchParent\",\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"top_left_support\",\"component\":\"Column\",\"children\":[\"top_left_support_row0\"],\"itemMargin\":2,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"flexShrink\":1}},{\"id\":\"top_left_support_item0_value\",\"component\":\"Text\",\"content\":\"{{ '杭州 ' + ${/data/weather/current/condition} }}\",\"styles\":{\"height\":12.0,\"fontSize\":12,\"fontWeight\":400,\"maxLines\":1,\"flexShrink\":1,\"lineHeight\":1,\"fontColor\":\"@theme:primary/1\",\"layoutWeight\":1,\"textOverflow\":\"clip\"}},{\"id\":\"top_left_support_item0\",\"component\":\"Row\",\"children\":[\"top_left_support_item0_value\"],\"itemMargin\":0,\"styles\":{\"height\":12.0,\"alignItems\":\"top\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"layoutWeight\":1}},{\"id\":\"top_left_support_row0\",\"component\":\"Row\",\"children\":[\"top_left_support_item0\"],\"itemMargin\":0,\"styles\":{\"width\":\"matchParent\",\"height\":12.0,\"alignItems\":\"top\",\"flexShrink\":0}},{\"id\":\"top_right\",\"component\":\"Column\",\"children\":[\"top_right_primary\",\"top_right_support\"],\"itemMargin\":2,\"styles\":{\"alignItems\":\"start\",\"justifyContent\":\"start\",\"height\":\"matchParent\",\"layoutWeight\":59.0}},{\"id\":\"top_right_primary\",\"component\":\"Column\",\"children\":[\"top_right_primary_main\"],\"itemMargin\":2,\"styles\":{\"alignItems\":\"start\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"width\":\"matchParent\"}},{\"id\":\"top_right_primary_main\",\"component\":\"Text\",\"content\":\"{{ ${/data/earphone/batteryLevel} + '%' }}\",\"styles\":{\"height\":18,\"fontSize\":18,\"fontWeight\":700,\"lineHeight\":1,\"maxLines\":1,\"flexShrink\":1,\"width\":\"matchParent\",\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"top_right_support\",\"component\":\"Column\",\"children\":[\"top_right_support_row0\"],\"itemMargin\":2,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"flexShrink\":1}},{\"id\":\"top_right_support_item0_value\",\"component\":\"Text\",\"content\":\"耳机盒电量\",\"styles\":{\"height\":24.0,\"fontSize\":12,\"fontWeight\":400,\"maxLines\":2,\"flexShrink\":1,\"lineHeight\":1,\"fontColor\":\"@theme:primary/0.6\",\"layoutWeight\":1,\"textOverflow\":\"clip\"}},{\"id\":\"top_right_support_item0\",\"component\":\"Row\",\"children\":[\"top_right_support_item0_value\"],\"itemMargin\":0,\"styles\":{\"height\":24.0,\"alignItems\":\"top\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"layoutWeight\":1}},{\"id\":\"top_right_support_row0\",\"component\":\"Row\",\"children\":[\"top_right_support_item0\"],\"itemMargin\":0,\"styles\":{\"width\":\"matchParent\",\"height\":24.0,\"alignItems\":\"top\",\"flexShrink\":0}},{\"id\":\"__layout__root__row1\",\"component\":\"Row\",\"children\":[\"bottom_left\",\"bottom_right\"],\"itemMargin\":8,\"styles\":{\"width\":\"matchParent\",\"layoutWeight\":1}},{\"id\":\"bottom_left\",\"component\":\"Column\",\"children\":[\"bottom_left_primary\",\"bottom_left_support\"],\"itemMargin\":2,\"styles\":{\"alignItems\":\"start\",\"justifyContent\":\"start\",\"height\":\"matchParent\",\"layoutWeight\":59.0}},{\"id\":\"bottom_left_primary\",\"component\":\"Column\",\"children\":[\"bottom_left_primary_main\"],\"itemMargin\":2,\"styles\":{\"alignItems\":\"start\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"width\":\"matchParent\"}},{\"id\":\"bottom_left_primary_main\",\"component\":\"Text\",\"content\":\"{{ ${/data/earphone/leftBatteryLevel} + '%' }}\",\"styles\":{\"height\":18,\"fontSize\":18,\"fontWeight\":700,\"lineHeight\":1,\"maxLines\":1,\"flexShrink\":1,\"width\":\"matchParent\",\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"bottom_left_support\",\"component\":\"Column\",\"children\":[\"bottom_left_support_row0\"],\"itemMargin\":2,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"flexShrink\":1}},{\"id\":\"bottom_left_support_item0_value\",\"component\":\"Text\",\"content\":\"左耳电量\",\"styles\":{\"height\":14.0,\"fontSize\":14,\"fontWeight\":400,\"maxLines\":1,\"flexShrink\":1,\"lineHeight\":1,\"fontColor\":\"@theme:primary/0.6\",\"layoutWeight\":1,\"textOverflow\":\"clip\"}},{\"id\":\"bottom_left_support_item0\",\"component\":\"Row\",\"children\":[\"bottom_left_support_item0_value\"],\"itemMargin\":0,\"styles\":{\"height\":14.0,\"alignItems\":\"top\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"layoutWeight\":1}},{\"id\":\"bottom_left_support_row0\",\"component\":\"Row\",\"children\":[\"bottom_left_support_item0\"],\"itemMargin\":0,\"styles\":{\"width\":\"matchParent\",\"height\":14.0,\"alignItems\":\"top\",\"flexShrink\":0}},{\"id\":\"bottom_right\",\"component\":\"Column\",\"children\":[\"bottom_right_primary\",\"bottom_right_support\"],\"itemMargin\":2,\"styles\":{\"alignItems\":\"start\",\"justifyContent\":\"start\",\"height\":\"matchParent\",\"layoutWeight\":59.0}},{\"id\":\"bottom_right_primary\",\"component\":\"Column\",\"children\":[\"bottom_right_primary_main\"],\"itemMargin\":2,\"styles\":{\"alignItems\":\"start\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"width\":\"matchParent\"}},{\"id\":\"bottom_right_primary_main\",\"component\":\"Text\",\"content\":\"{{ ${/data/earphone/rightBatteryLevel} + '%' }}\",\"styles\":{\"height\":18,\"fontSize\":18,\"fontWeight\":700,\"lineHeight\":1,\"maxLines\":1,\"flexShrink\":1,\"width\":\"matchParent\",\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"bottom_right_support\",\"component\":\"Column\",\"children\":[\"bottom_right_support_row0\"],\"itemMargin\":2,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"flexShrink\":1}},{\"id\":\"bottom_right_support_item0_value\",\"component\":\"Text\",\"content\":\"右耳电量\",\"styles\":{\"height\":14.0,\"fontSize\":14,\"fontWeight\":400,\"maxLines\":1,\"flexShrink\":1,\"lineHeight\":1,\"fontColor\":\"@theme:primary/0.6\",\"layoutWeight\":1,\"textOverflow\":\"clip\"}},{\"id\":\"bottom_right_support_item0\",\"component\":\"Row\",\"children\":[\"bottom_right_support_item0_value\"],\"itemMargin\":0,\"styles\":{\"height\":14.0,\"alignItems\":\"top\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"layoutWeight\":1}},{\"id\":\"bottom_right_support_row0\",\"component\":\"Row\",\"children\":[\"bottom_right_support_item0\"],\"itemMargin\":0,\"styles\":{\"width\":\"matchParent\",\"height\":14.0,\"alignItems\":\"top\",\"flexShrink\":0}}]}}\n{\"version\":\"v0.9\",\"updateDataModel\":{\"surfaceId\":\"surface_card\",\"path\":\"/\",\"value\":{\"data\":{\"weather\":{\"current\":{\"temperatureText\":\"29℃\",\"condition\":\"多云\"}},\"earphone\":{\"batteryLevel\":80,\"leftBatteryLevel\":76,\"rightBatteryLevel\":78}}}}}",
  "validationErrors": []
}
```
