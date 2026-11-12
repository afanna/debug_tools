```cardspec
{
  "title": "步数监测",
  "description": "今日步数监测卡片",
  "suggestSize": "2x2",
  "imageDomainWhitelist": [
    "hag-ability-test.obs.cn-north-1.myhuaweicloud.com",
    "lfcontentcenterdev.hwcloudtest.cn",
    "hagres-drcn.dbankcdn.com"
  ],
  "dataBindings": [
    {
      "capabilityId": "GetHealthAndSportSummary",
      "arguments": {
        "targetDayOffset": 0
      },
      "writeResultTo": "/data/healthSport"
    }
  ]
}
```
```genui
{"version":"v0.9","createSurface":{"surfaceId":"surface_card","catalogId":"ohos.a2ui.extended.catalog.form"}}
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["title","__layout__root__body"],"itemMargin":6,"styles":{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","padding":12,"linearGradient":{"direction":"RightBottom","colors":[["#FFDBCCFF",0],["#FFF6F2FF",1]]}}},{"id":"title","component":"Row","children":["title_title","title_icon"],"styles":{"width":"matchParent","height":20,"flexShrink":0,"justifyContent":"spaceBetween","alignItems":"center"},"itemMargin":0},{"id":"title_title","component":"Text","content":"今日活动","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":1,"width":"wrapContent","layoutWeight":1,"constraintSize":{"minWidth":0},"fontColor":"#99563D99"}},{"id":"title_icon","component":"Image","src":"resources/base/media/figure_run.svg","styles":{"width":20,"height":20,"objectFit":"contain","flexShrink":0,"fillColor":"#FF563D99"}},{"id":"__layout__root__body","component":"Column","children":["__layout__root__primary","__layout__root__support"],"itemMargin":8,"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1}},{"id":"__layout__root__primary","component":"Column","children":["primary"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","layoutWeight":1,"flexShrink":0},"itemMargin":0},{"id":"primary","component":"Row","children":["primary_value","primary_unit"],"itemMargin":2,"styles":{"justifyContent":"start","alignItems":"bottom","flexShrink":0,"width":"matchParent"}},{"id":"primary_value","component":"Text","content":"{{ ${/data/healthSport/dailySteps} }}","styles":{"height":30,"fontSize":30,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":0,"fontColor":"#FF563D99","textOverflow":"clip"}},{"id":"primary_unit","component":"Text","content":"步","styles":{"height":14.0,"fontSize":12,"fontWeight":500,"lineHeight":1,"maxLines":1,"flexShrink":0,"fontColor":"#99563D99","padding":{"top":0,"right":0,"bottom":2,"left":0},"textOverflow":"clip"}},{"id":"__layout__root__support","component":"Column","children":["support"],"styles":{"width":"matchParent","alignItems":"start","justifyContent":"start","flexShrink":0},"itemMargin":0},{"id":"support","component":"Column","children":["support_row0","support_row1"],"itemMargin":2,"styles":{"width":"matchParent","alignItems":"start","flexShrink":1}},{"id":"support_item0_label","component":"Text","content":"热量","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#99563D99","textOverflow":"clip"}},{"id":"support_item0_value","component":"Text","content":"{{ ${/data/healthSport/dailyTotalCaloriesText} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF563D99","layoutWeight":1,"textOverflow":"clip"}},{"id":"support_item0","component":"Row","children":["support_item0_label","support_item0_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"support_row0","component":"Row","children":["support_item0"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"top","flexShrink":0}},{"id":"support_item1_label","component":"Text","content":"距离","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#99563D99","textOverflow":"clip"}},{"id":"support_item1_value","component":"Text","content":"{{ ${/data/healthSport/dailyDistanceText} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF563D99","layoutWeight":1,"textOverflow":"clip"}},{"id":"support_item1","component":"Row","children":["support_item1_label","support_item1_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"support_row1","component":"Row","children":["support_item1"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"top","flexShrink":0}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"healthSport":{"dailySteps":6200,"dailyTotalCaloriesText":"420 千卡","dailyDistanceText":"4.60 公里"}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "创建一个桌面卡片，展示今日步数监测数据，包括当日步数、热量消耗和活动距离。",
  "size": "2x2",
  "appVersion": "11.7.8.342",
  "eventCandidates": [
    {
      "id": "event.open.health.activityRecord",
      "description": "打开华为运动健康应用的活动记录页。",
      "call": "clickToDeeplink",
      "args": {
        "abilityName": "",
        "bundleName": "",
        "intentName": "Health",
        "uri": "huaweischeme://healthapp/router/openwith?address=com.huawei.health.h5.sports-record?h5pro=true&urlType=4&pName=com.huawei.health&path=ActiveRecord"
      }
    }
  ],
  "dataModelSchema": {
    "data": {
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
        "dailyDistanceText": {
          "type": "string",
          "description": "可直接显示的日常活动总距离文本，端侧已根据数值大小换算并包含“米”或“公里”单位；展示时不得再次追加距离单位。例如“5.42 公里”或“755 米”。",
          "sampleValue": "4.60 公里"
        }
      }
    }
  },
  "assetCandidates": [
    {
      "id": "asset.ic_sportsHealth_bule",
      "src": "resources/base/media/ic_sportsHealth_bule.svg",
      "description": "样式：蓝色纵向渐变圆形底上的白色运动火焰图标，原始尺寸为 20×20，SVG 矢量图（保留原色，禁止染色）需保留原始渐变配色，禁止染色；适用：运动健康、日常活动或锻炼摘要卡片，可结合 GetHealthAndSportSummary 展示步数、热量、距离和运动记录，也可作为 event.open.health.sport、event.open.health.sportsRecord、event.open.health.activityRecord 或 event.open.health.workoutDuration 的辅助入口图标。图标不表示运动目标已达成或用户当前正在运动。"
    },
    {
      "id": "asset.figure_run",
      "src": "resources/base/media/figure_run.svg",
      "description": "样式：跑步人物图标，默认黑色，图形为人体奔跑动作侧视轮廓；适用：运动记录、跑步锻炼追踪、步数统计。"
    }
  ]
}
```
```effectivecapabilities
{
  "data": [
    "GetHealthAndSportSummary"
  ],
  "event": [
    {
      "id": "event.open.health.activityRecord",
      "description": "打开华为运动健康应用的活动记录页。",
      "call": "clickToDeeplink",
      "args": {
        "abilityName": "",
        "bundleName": "",
        "intentName": "Health",
        "uri": "huaweischeme://healthapp/router/openwith?address=com.huawei.health.h5.sports-record?h5pro=true&urlType=4&pName=com.huawei.health&path=ActiveRecord"
      }
    }
  ],
  "asset": [
    "asset.ic_sportsHealth_bule",
    "asset.figure_run"
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
      "capabilityId": "GetHealthAndSportSummary",
      "arguments": {
        "targetDayOffset": 0
      },
      "writeResultTo": "/data/healthSport",
      "candidateOutputFields": [
        "/dailySteps",
        "/dailyTotalCaloriesText",
        "/dailyDistanceText"
      ]
    }
  ],
  "candidateEventCandidates": [
    {
      "capabilityId": "event.open.health.activityRecord",
      "action": {
        "call": "clickToDeeplink",
        "args": {
          "abilityName": "",
          "bundleName": "",
          "intentName": "Health",
          "uri": "huaweischeme://healthapp/router/openwith?address=com.huawei.health.h5.sports-record?h5pro=true&urlType=4&pName=com.huawei.health&path=ActiveRecord"
        }
      }
    }
  ],
  "candidateAssetIds": [
    "asset.ic_sportsHealth_bule",
    "asset.figure_run"
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
  "artifactId": "d5e1196b-b01d-4c31-ad8b-2de03910d94b",
  "createdAt": 1793934565911
}
```
```designcompactdsl
["root","Layout",{"layout":"S-title-dual-content"},["title","primary","support"]]
["title","SingleLineTitle",{"title":"今日活动","icon":"resources/base/media/figure_run.svg","fontSize":12}]
["primary","EmphasizedData",{"value":{"path":"/data/healthSport/dailySteps"},"unit":"步","fontSize":30}]
["support","SecondaryBody",{"items":[{"label":"热量 ","value":{"path":"/data/healthSport/dailyTotalCaloriesText"}},{"label":"距离 ","value":{"path":"/data/healthSport/dailyDistanceText"}}],"separator":" | ","fontSize":14}]
["/data/healthSport/dailySteps",6200]
["/data/healthSport/dailyTotalCaloriesText","420 千卡"]
["/data/healthSport/dailyDistanceText","4.60 公里"]
```
```request
{
  "content": {
    "bundleName": "com.huawei.genui",
    "userQuery": "创建一个桌面卡片，展示今日步数监测数据，包括当日步数、热量消耗和活动距离。",
    "candidateDataBindings": [
      {
        "capabilityId": "GetHealthAndSportSummary",
        "arguments": {
          "targetDayOffset": 0
        },
        "writeResultTo": "/data/healthSport",
        "candidateOutputFields": [
          "/dailySteps",
          "/dailyTotalCaloriesText",
          "/dailyDistanceText"
        ]
      }
    ],
    "title": "步数监测",
    "size": "2x2",
    "candidateEventCandidates": [
      {
        "capabilityId": "event.open.health.activityRecord",
        "action": {
          "call": "clickToDeeplink",
          "args": {
            "abilityName": "",
            "bundleName": "",
            "intentName": "Health",
            "uri": "huaweischeme://healthapp/router/openwith?address=com.huawei.health.h5.sports-record?h5pro=true&urlType=4&pName=com.huawei.health&path=ActiveRecord"
          }
        }
      }
    ],
    "description": "今日步数监测卡片",
    "candidateAssetIds": [
      "asset.ic_sportsHealth_bule",
      "asset.figure_run"
    ]
  },
  "deviceInfo": {
    "countryCode": "CN",
    "deviceFormation": "HDSpeaker",
    "deviceType": 0,
    "locale": "zh-CN",
    "phoneType": "CMS-AL20",
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261029144928763"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q323-000",
    "isNew": true,
    "sessionId": "batch-7664fcb9"
  },
  "userAuth": {
    "user": {}
  },
  "utterance": {
    "original": "创建一个桌面卡片，展示今日步数监测数据，包括当日步数、热量消耗和活动距离。",
    "type": "text"
  },
  "version": "1.0",
  "functionName": "generateWidgetCardCompactDsl",
  "romVersion": "CMS-AL20 7.0.0.111",
  "bundleName": "com.huawei.genui",
  "userQuery": "创建一个桌面卡片，展示今日步数监测数据，包括当日步数、热量消耗和活动距离。",
  "candidateDataBindings": [
    {
      "capabilityId": "GetHealthAndSportSummary",
      "arguments": {
        "targetDayOffset": 0
      },
      "writeResultTo": "/data/healthSport",
      "candidateOutputFields": [
        "/dailySteps",
        "/dailyTotalCaloriesText",
        "/dailyDistanceText"
      ]
    }
  ],
  "title": "步数监测",
  "size": "2x2",
  "candidateEventCandidates": [
    {
      "capabilityId": "event.open.health.activityRecord",
      "action": {
        "call": "clickToDeeplink",
        "args": {
          "abilityName": "",
          "bundleName": "",
          "intentName": "Health",
          "uri": "huaweischeme://healthapp/router/openwith?address=com.huawei.health.h5.sports-record?h5pro=true&urlType=4&pName=com.huawei.health&path=ActiveRecord"
        }
      }
    }
  ],
  "description": "今日步数监测卡片",
  "candidateAssetIds": [
    "asset.ic_sportsHealth_bule",
    "asset.figure_run"
  ]
}
```
