```cardspec
{
  "title": "时间天气",
  "description": "大字体时钟与天气",
  "suggestSize": "2x4",
  "imageDomainWhitelist": [
    "hag-ability-test.obs.cn-north-1.myhuaweicloud.com",
    "lfcontentcenterdev.hwcloudtest.cn",
    "hagres-drcn.dbankcdn.com"
  ],
  "dataBindings": [
    {
      "capabilityId": "GetCurrentTime",
      "arguments": {},
      "writeResultTo": "/data/time"
    },
    {
      "capabilityId": "ViewWeather",
      "arguments": {
        "forecastDays": 1
      },
      "writeResultTo": "/data/weather"
    }
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Row","children":["left","right"],"itemMargin":12,"styles":{"width":"matchParent","height":"matchParent","padding":12,"borderRadius":20,"clip":true,"alignItems":"center","justifyContent":"start","linearGradient":{"direction":"RightBottom","colors":[["#FFCBDDFE",0],["#FFF1F6FE",1]]}}},{"id":"left","component":"Column","children":["__layout__left__sub"],"styles":{"height":"matchParent","layoutWeight":1,"padding":8,"borderRadius":16,"clip":true,"backgroundColor":"#99FFFFFF"},"itemMargin":0},{"id":"__layout__left__sub","component":"Column","children":["left_title","__layout__left__body"],"itemMargin":6,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":110.0}},{"id":"left_title","component":"Row","children":["left_title_title","left_title_icon"],"styles":{"width":"matchParent","height":20,"flexShrink":0,"justifyContent":"spaceBetween","alignItems":"center"},"itemMargin":0},{"id":"left_title_title","component":"Text","content":"时间","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":1,"width":"wrapContent","layoutWeight":1,"constraintSize":{"minWidth":0},"fontColor":"#991F4799"}},{"id":"left_title_icon","component":"Image","src":"resources/base/media/emoji_time.png","styles":{"width":20,"height":20,"objectFit":"contain","flexShrink":0}},{"id":"__layout__left__body","component":"Column","children":["left_body"],"itemMargin":0,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"end","layoutWeight":1}},{"id":"left_body","component":"Column","children":["left_body_main","left_body_secondary"],"itemMargin":2,"styles":{"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"width":"matchParent"}},{"id":"left_body_main","component":"Text","content":"示例","styles":{"height":18,"fontSize":18,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"left_body_secondary","component":"Text","content":"{{ ${/data/time/currentDate} + ' | ' + ${/data/time/dayOfWeek} + ' | ' + ${/data/time/lunarDate} }}","styles":{"height":16,"fontSize":12,"fontWeight":400,"lineHeight":1.3333333333333333,"maxLines":1,"flexShrink":1,"width":"matchParent","fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"right","component":"Column","children":["__layout__right__sub"],"styles":{"height":"matchParent","layoutWeight":1,"padding":8,"borderRadius":16,"clip":true,"backgroundColor":"#99FFFFFF"},"itemMargin":0},{"id":"__layout__right__sub","component":"Column","children":["right_title","__layout__right__body"],"itemMargin":6,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":110.0}},{"id":"right_title","component":"Row","children":["right_title_title","right_title_icon"],"styles":{"width":"matchParent","height":20,"flexShrink":0,"justifyContent":"spaceBetween","alignItems":"center"},"itemMargin":0},{"id":"right_title_title","component":"Text","content":"{{ ${/data/weather/location/prefectureName} }}","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":1,"width":"wrapContent","layoutWeight":1,"constraintSize":{"minWidth":0},"fontColor":"#991F4799"}},{"id":"right_title_icon","component":"Image","src":"resources/base/media/emoji_location_blue.png","styles":{"width":20,"height":20,"objectFit":"contain","flexShrink":0}},{"id":"__layout__right__body","component":"Column","children":["__layout__right__primary","__layout__right__details"],"itemMargin":6,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__right__primary","component":"Column","children":["right_primary"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1},"itemMargin":0},{"id":"right_primary","component":"Row","children":["right_primary_value"],"itemMargin":0,"styles":{"justifyContent":"start","alignItems":"bottom","flexShrink":0,"width":"matchParent"}},{"id":"right_primary_value","component":"Text","content":"{{ ${/data/weather/current/temperatureText} }}","styles":{"height":30,"fontSize":30,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":0,"fontColor":"#FF1F4799","textOverflow":"clip"}},{"id":"__layout__right__details","component":"Column","children":["right_support"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"right_support","component":"Column","children":["right_support_row0","right_support_row1"],"itemMargin":2,"styles":{"width":"matchParent","alignItems":"start","flexShrink":1}},{"id":"right_support_item0_label","component":"Text","content":"天气","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"right_support_item0_value","component":"Text","content":"{{ ${/data/weather/current/condition} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"right_support_item0","component":"Row","children":["right_support_item0_label","right_support_item0_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"right_support_row0","component":"Row","children":["right_support_item0"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"start","flexShrink":0}},{"id":"right_support_item1_label","component":"Text","content":"区域","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#991F4799","textOverflow":"clip"}},{"id":"right_support_item1_value","component":"Text","content":"{{ ${/data/weather/location/districtName} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF1F4799","layoutWeight":1,"textOverflow":"clip"}},{"id":"right_support_item1","component":"Row","children":["right_support_item1_label","right_support_item1_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"start","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"right_support_row1","component":"Row","children":["right_support_item1"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"start","flexShrink":0}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"time":{"currentDate":"示例","dayOfWeek":"示例","lunarDate":"示例"},"weather":{"location":{"prefectureName":"上海市","districtName":"青浦区"},"current":{"temperatureText":"29℃","condition":"多云"}}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "创建一张大尺寸时间天气卡片，时钟时间字体最大最醒目，显示当前时间、日期、星期、农历，同时显示当前所在位置的天气（温度、天气现象）和地点名称。",
  "size": "2x4",
  "appVersion": "11.7.8.342",
  "eventCandidates": [],
  "dataModelSchema": {
    "data": {
      "time": {
        "currentDate": {
          "type": "string",
          "description": "格式化的当前公历日期（年-月-日），例如 '2026-07-09'。",
          "sampleValue": "示例"
        },
        "dayOfWeek": {
          "type": "string",
          "description": "中文的星期描述，例如 '星期四'。",
          "sampleValue": "示例"
        },
        "lunarDate": {
          "type": "string",
          "description": "格式化的中国传统农历日期，例如 '五月廿六'。若系统获取失败则可能为空字符串。",
          "sampleValue": "示例"
        }
      },
      "weather": {
        "location": {
          "prefectureName": {
            "type": "string",
            "description": "城市名称",
            "sampleValue": "上海市"
          },
          "districtName": {
            "type": "string",
            "description": "区或县名称",
            "sampleValue": "青浦区"
          }
        },
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
      }
    }
  },
  "assetCandidates": [
    {
      "id": "asset.emoji_time",
      "src": "resources/base/media/emoji_time.png",
      "description": "样式：蓝色圆形外框与浅蓝表盘组成的写实 3D 时钟，白色指针和刻度清晰，透明背景，原始尺寸为 512×512，PNG 位图需保留原色；适用：当前时间、计时或时长统计相关卡片。不适用：只含时间字段的日程或会议卡片。"
    },
    {
      "id": "asset.emoji_location_blue",
      "src": "resources/base/media/emoji_location_blue.png",
      "description": "样式：亮蓝色圆形底上的白色定位标记与浅蓝色地图基座图标，圆形外透明，原始尺寸为 64×64，PNG 位图需保留原色；适用：天气卡片中的查询地点，可结合 ViewWeather 的 location.districtName、location.prefectureName 或 location.cityCode 展示并配合 event.open.weather 打开对应城市天气页，也可作为 event.setLocationSwitch 的位置设置操作图标。蓝色仅为视觉配色，不表示定位开关状态或定位成功。"
    },
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
    "GetCurrentTime",
    "ViewWeather"
  ],
  "event": [],
  "asset": [
    "asset.emoji_time",
    "asset.emoji_location_blue",
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
      "capabilityId": "GetCurrentTime",
      "arguments": {},
      "writeResultTo": "/data/time",
      "candidateOutputFields": [
        "/currentDate",
        "/dayOfWeek",
        "/lunarDate"
      ]
    },
    {
      "capabilityId": "ViewWeather",
      "arguments": {
        "forecastDays": 1
      },
      "writeResultTo": "/data/weather",
      "candidateOutputFields": [
        "/location/prefectureName",
        "/location/districtName",
        "/current/temperatureText",
        "/current/condition"
      ]
    }
  ],
  "candidateEventCandidates": [],
  "candidateAssetIds": [
    "asset.emoji_time",
    "asset.emoji_location_blue",
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
  "artifactId": "27376f46-f824-4f4f-a45b-a40e3ec8e875",
  "createdAt": 1793952287230
}
```
```designcompactdsl
["root","Layout",{"layout":"W-split-panels"},["left","right"]]
["left","Region",{"variant":"title-content"},["left_title","left_body"]]
["left_title","SingleLineTitle",{"title":"时间","icon":"resources/base/media/emoji_time.png","fontSize":12}]
["left_body","EmphasisText",{"mainText":"示例","secondaryText":[{"path":"/data/time/currentDate"},{"path":"/data/time/dayOfWeek"},{"path":"/data/time/lunarDate"}],"fontSize":18}]
["right","Region",{"variant":"title-hero-support"},["right_title","right_primary","right_support"]]
["right_title","SingleLineTitle",{"title":{"path":"/data/weather/location/prefectureName"},"icon":"resources/base/media/emoji_location_blue.png","fontSize":12}]
["right_primary","EmphasizedData",{"value":{"path":"/data/weather/current/temperatureText"},"fontSize":30}]
["right_support","SecondaryBody",{"items":[{"label":"天气 ","value":{"path":"/data/weather/current/condition"}},{"label":"区域 ","value":{"path":"/data/weather/location/districtName"}}],"columns":1,"fontSize":12}]
["/data/time/currentDate","示例"]
["/data/time/dayOfWeek","示例"]
["/data/time/lunarDate","示例"]
["/data/weather/location/prefectureName","上海市"]
["/data/weather/location/districtName","青浦区"]
["/data/weather/current/temperatureText","29℃"]
["/data/weather/current/condition","多云"]
```
```request
{
  "content": {
    "size": "2x4",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "CMM-AL10P 7.0.0.111",
    "candidateAssetIds": [
      "asset.emoji_time",
      "asset.emoji_location_blue",
      "asset.ic_weather_monochrome"
    ],
    "candidateEventCandidates": [],
    "bundleName": "com.huawei.genui",
    "description": "大字体时钟与天气",
    "userQuery": "创建一张大尺寸时间天气卡片，时钟时间字体最大最醒目，显示当前时间、日期、星期、农历，同时显示当前所在位置的天气（温度、天气现象）和地点名称。",
    "title": "时间天气",
    "candidateDataBindings": [
      {
        "capabilityId": "GetCurrentTime",
        "arguments": {},
        "writeResultTo": "/data/time",
        "candidateOutputFields": [
          "/currentDate",
          "/dayOfWeek",
          "/lunarDate"
        ]
      },
      {
        "capabilityId": "ViewWeather",
        "arguments": {
          "forecastDays": 1
        },
        "writeResultTo": "/data/weather",
        "candidateOutputFields": [
          "/location/prefectureName",
          "/location/districtName",
          "/current/temperatureText",
          "/current/condition"
        ]
      }
    ]
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "CMM-AL10",
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261101163439722"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q486-000",
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
  "size": "2x4",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "CMM-AL10P 7.0.0.111",
  "candidateAssetIds": [
    "asset.emoji_time",
    "asset.emoji_location_blue",
    "asset.ic_weather_monochrome"
  ],
  "candidateEventCandidates": [],
  "bundleName": "com.huawei.genui",
  "description": "大字体时钟与天气",
  "userQuery": "创建一张大尺寸时间天气卡片，时钟时间字体最大最醒目，显示当前时间、日期、星期、农历，同时显示当前所在位置的天气（温度、天气现象）和地点名称。",
  "title": "时间天气",
  "candidateDataBindings": [
    {
      "capabilityId": "GetCurrentTime",
      "arguments": {},
      "writeResultTo": "/data/time",
      "candidateOutputFields": [
        "/currentDate",
        "/dayOfWeek",
        "/lunarDate"
      ]
    },
    {
      "capabilityId": "ViewWeather",
      "arguments": {
        "forecastDays": 1
      },
      "writeResultTo": "/data/weather",
      "candidateOutputFields": [
        "/location/prefectureName",
        "/location/districtName",
        "/current/temperatureText",
        "/current/condition"
      ]
    }
  ]
}
```
```repair-1
{
  "modelGeneratedCompactDsl": "[\"root\",\"Layout\",{\"layout\":\"W-split-panels\"},[\"left\",\"right\"]]\n[\"left_title\",\"SingleLineTitle\",{\"title\":\"时间\",\"icon\":\"resources/base/media/emoji_time.png\",\"fontSize\":12}]\n[\"left_body\",\"EmphasisText\",{\"mainText\":\"示例\",\"secondaryText\":[{\"path\":\"/data/time/currentDate\"},{\"path\":\"/data/time/dayOfWeek\"},{\"path\":\"/data/time/lunarDate\"}],\"fontSize\":18}]\n[\"left\",\"Region\",{\"variant\":\"title-content\"},[\"left_title\",\"left_body\"]]\n[\"right_title\",\"SingleLineTitle\",{\"title\":{\"path\":\"/data/weather/location/prefectureName\"},\"icon\":\"resources/base/media/emoji_location_blue.png\",\"fontSize\":12}]\n[\"right_primary\",\"EmphasizedData\",{\"value\":{\"path\":\"/data/weather/current/temperatureText\"},\"fontSize\":30}]\n[\"right_support\",\"SecondaryBody\",{\"items\":[{\"label\":\"天气 \",\"value\":{\"path\":\"/data/weather/current/condition\"}},{\"label\":\"区域 \",\"value\":{\"path\":\"/data/weather/location/districtName\"}}],\"columns\":1,\"fontSize\":12}]\n[\"right\",\"Region\",{\"variant\":\"title-hero-support\"},[\"right_title\",\"right_primary\",\"right_support\"]]\n[\"/data/time/currentDate\",\"示例\"]\n[\"/data/time/dayOfWeek\",\"示例\"]\n[\"/data/time/lunarDate\",\"示例\"]\n[\"/data/weather/location/prefectureName\",\"上海市\"]\n[\"/data/weather/location/districtName\",\"青浦区\"]\n[\"/data/weather/current/temperatureText\",\"29℃\"]\n[\"/data/weather/current/condition\",\"多云\"]",
  "generatedDsl": "{\"version\":\"v0.9\",\"createSurface\":{\"surfaceId\":\"surface_card\",\"catalogId\":\"ohos.a2ui.extended.catalog.form\"}}\n{\"version\":\"v0.9\",\"updateComponents\":{\"surfaceId\":\"surface_card\",\"root\":\"root\",\"components\":[{\"id\":\"root\",\"component\":\"Row\",\"children\":[\"left\",\"right\"],\"itemMargin\":12,\"styles\":{\"width\":\"matchParent\",\"height\":\"matchParent\",\"padding\":12,\"borderRadius\":20,\"clip\":true,\"alignItems\":\"center\",\"justifyContent\":\"start\"}},{\"id\":\"left\",\"component\":\"Column\",\"children\":[\"__layout__left__sub\"],\"styles\":{\"height\":\"matchParent\",\"layoutWeight\":1,\"padding\":8,\"borderRadius\":16,\"clip\":true,\"backgroundColor\":\"@theme:panel/1\"},\"itemMargin\":0},{\"id\":\"__layout__left__sub\",\"component\":\"Column\",\"children\":[\"left_title\",\"__layout__left__body\"],\"itemMargin\":6,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":110.0}},{\"id\":\"left_title\",\"component\":\"Row\",\"children\":[\"left_title_title\",\"left_title_icon\"],\"styles\":{\"width\":\"matchParent\",\"height\":20,\"flexShrink\":0,\"justifyContent\":\"spaceBetween\",\"alignItems\":\"center\"},\"itemMargin\":0},{\"id\":\"left_title_title\",\"component\":\"Text\",\"content\":\"时间\",\"styles\":{\"fontSize\":12,\"fontWeight\":400,\"lineHeight\":1,\"textAlign\":\"start\",\"maxLines\":1,\"flexShrink\":1,\"width\":\"wrapContent\",\"layoutWeight\":1,\"constraintSize\":{\"minWidth\":0},\"fontColor\":\"@theme:secondary/1\"}},{\"id\":\"left_title_icon\",\"component\":\"Image\",\"src\":\"resources/base/media/emoji_time.png\",\"styles\":{\"width\":20,\"height\":20,\"objectFit\":\"contain\",\"flexShrink\":0}},{\"id\":\"__layout__left__body\",\"component\":\"Column\",\"children\":[\"left_body\"],\"itemMargin\":0,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"end\",\"layoutWeight\":1}},{\"id\":\"left_body\",\"component\":\"Column\",\"children\":[\"left_body_main\",\"left_body_secondary\"],\"itemMargin\":2,\"styles\":{\"alignItems\":\"start\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"width\":\"matchParent\"}},{\"id\":\"left_body_main\",\"component\":\"Text\",\"content\":\"示例\",\"styles\":{\"height\":18,\"fontSize\":18,\"fontWeight\":700,\"lineHeight\":1,\"maxLines\":1,\"flexShrink\":1,\"width\":\"matchParent\",\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"left_body_secondary\",\"component\":\"Text\",\"content\":\"{{ ${/data/time/currentDate} + ' | ' + ${/data/time/dayOfWeek} + ' | ' + ${/data/time/lunarDate} }}\",\"styles\":{\"height\":16,\"fontSize\":12,\"fontWeight\":400,\"lineHeight\":1.3333333333333333,\"maxLines\":1,\"flexShrink\":1,\"width\":\"matchParent\",\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"right\",\"component\":\"Column\",\"children\":[\"__layout__right__sub\"],\"styles\":{\"height\":\"matchParent\",\"layoutWeight\":1,\"padding\":8,\"borderRadius\":16,\"clip\":true,\"backgroundColor\":\"@theme:panel/1\"},\"itemMargin\":0},{\"id\":\"__layout__right__sub\",\"component\":\"Column\",\"children\":[\"right_title\",\"__layout__right__body\"],\"itemMargin\":6,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":110.0}},{\"id\":\"right_title\",\"component\":\"Row\",\"children\":[\"right_title_title\",\"right_title_icon\"],\"styles\":{\"width\":\"matchParent\",\"height\":20,\"flexShrink\":0,\"justifyContent\":\"spaceBetween\",\"alignItems\":\"center\"},\"itemMargin\":0},{\"id\":\"right_title_title\",\"component\":\"Text\",\"content\":\"{{ ${/data/weather/location/prefectureName} }}\",\"styles\":{\"fontSize\":12,\"fontWeight\":400,\"lineHeight\":1,\"textAlign\":\"start\",\"maxLines\":1,\"flexShrink\":1,\"width\":\"wrapContent\",\"layoutWeight\":1,\"constraintSize\":{\"minWidth\":0},\"fontColor\":\"@theme:secondary/1\"}},{\"id\":\"right_title_icon\",\"component\":\"Image\",\"src\":\"resources/base/media/emoji_location_blue.png\",\"styles\":{\"width\":20,\"height\":20,\"objectFit\":\"contain\",\"flexShrink\":0}},{\"id\":\"__layout__right__body\",\"component\":\"Column\",\"children\":[\"__layout__right__primary\",\"__layout__right__details\"],\"itemMargin\":6,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":1}},{\"id\":\"__layout__right__primary\",\"component\":\"Column\",\"children\":[\"right_primary\"],\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"layoutWeight\":1},\"itemMargin\":0},{\"id\":\"right_primary\",\"component\":\"Row\",\"children\":[\"right_primary_value\"],\"itemMargin\":0,\"styles\":{\"justifyContent\":\"start\",\"alignItems\":\"bottom\",\"flexShrink\":0,\"width\":\"matchParent\"}},{\"id\":\"right_primary_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/weather/current/temperatureText} }}\",\"styles\":{\"height\":30,\"fontSize\":30,\"fontWeight\":700,\"lineHeight\":1,\"maxLines\":1,\"flexShrink\":0,\"fontColor\":\"@theme:primary/1\",\"textOverflow\":\"clip\"}},{\"id\":\"__layout__right__details\",\"component\":\"Column\",\"children\":[\"right_support\"],\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"justifyContent\":\"start\",\"flexShrink\":0},\"itemMargin\":0},{\"id\":\"right_support\",\"component\":\"Column\",\"children\":[\"right_support_row0\",\"right_support_row1\"],\"itemMargin\":2,\"styles\":{\"width\":\"matchParent\",\"alignItems\":\"start\",\"flexShrink\":1}},{\"id\":\"right_support_item0_label\",\"component\":\"Text\",\"content\":\"天气\",\"styles\":{\"height\":12,\"fontSize\":12,\"fontWeight\":400,\"maxLines\":1,\"flexShrink\":0,\"lineHeight\":1,\"fontColor\":\"@theme:primary/0.6\",\"textOverflow\":\"clip\"}},{\"id\":\"right_support_item0_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/weather/current/condition} }}\",\"styles\":{\"height\":12.0,\"fontSize\":12,\"fontWeight\":400,\"maxLines\":1,\"flexShrink\":1,\"lineHeight\":1,\"fontColor\":\"@theme:primary/1\",\"layoutWeight\":1,\"textOverflow\":\"clip\"}},{\"id\":\"right_support_item0\",\"component\":\"Row\",\"children\":[\"right_support_item0_label\",\"right_support_item0_value\"],\"itemMargin\":4,\"styles\":{\"height\":12.0,\"alignItems\":\"start\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"layoutWeight\":1}},{\"id\":\"right_support_row0\",\"component\":\"Row\",\"children\":[\"right_support_item0\"],\"itemMargin\":0,\"styles\":{\"width\":\"matchParent\",\"height\":12.0,\"alignItems\":\"start\",\"flexShrink\":0}},{\"id\":\"right_support_item1_label\",\"component\":\"Text\",\"content\":\"区域\",\"styles\":{\"height\":12,\"fontSize\":12,\"fontWeight\":400,\"maxLines\":1,\"flexShrink\":0,\"lineHeight\":1,\"fontColor\":\"@theme:primary/0.6\",\"textOverflow\":\"clip\"}},{\"id\":\"right_support_item1_value\",\"component\":\"Text\",\"content\":\"{{ ${/data/weather/location/districtName} }}\",\"styles\":{\"height\":12.0,\"fontSize\":12,\"fontWeight\":400,\"maxLines\":1,\"flexShrink\":1,\"lineHeight\":1,\"fontColor\":\"@theme:primary/1\",\"layoutWeight\":1,\"textOverflow\":\"clip\"}},{\"id\":\"right_support_item1\",\"component\":\"Row\",\"children\":[\"right_support_item1_label\",\"right_support_item1_value\"],\"itemMargin\":4,\"styles\":{\"height\":12.0,\"alignItems\":\"start\",\"flexShrink\":1,\"constraintSize\":{\"minWidth\":0},\"layoutWeight\":1}},{\"id\":\"right_support_row1\",\"component\":\"Row\",\"children\":[\"right_support_item1\"],\"itemMargin\":0,\"styles\":{\"width\":\"matchParent\",\"height\":12.0,\"alignItems\":\"start\",\"flexShrink\":0}}]}}\n{\"version\":\"v0.9\",\"updateDataModel\":{\"surfaceId\":\"surface_card\",\"path\":\"/\",\"value\":{\"data\":{\"time\":{\"currentDate\":\"示例\",\"dayOfWeek\":\"示例\",\"lunarDate\":\"示例\"},\"weather\":{\"location\":{\"prefectureName\":\"上海市\",\"districtName\":\"青浦区\"},\"current\":{\"temperatureText\":\"29℃\",\"condition\":\"多云\"}}}}}}",
  "validationErrors": []
}
```
