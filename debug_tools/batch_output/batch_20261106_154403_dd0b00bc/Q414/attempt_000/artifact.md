```cardspec
{
  "title": "运动健康",
  "description": "运动健康卡片",
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
{"version":"v0.9","updateComponents":{"surfaceId":"surface_card","root":"root","components":[{"id":"root","component":"Column","children":["title","content_flow","action"],"itemMargin":0,"styles":{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","padding":12,"linearGradient":{"direction":"RightBottom","colors":[["#FFDBCCFF",0],["#FFF6F2FF",1]]}}},{"id":"title","component":"Row","children":["title_title","title_icon"],"styles":{"width":"matchParent","height":20,"flexShrink":0,"justifyContent":"spaceBetween","alignItems":"center"},"itemMargin":0},{"id":"title_title","component":"Text","content":"运动健康","styles":{"fontSize":12,"fontWeight":400,"lineHeight":1,"textAlign":"start","maxLines":1,"flexShrink":1,"width":"wrapContent","layoutWeight":1,"constraintSize":{"minWidth":0},"fontColor":"#99563D99"}},{"id":"title_icon","component":"Image","src":"resources/base/media/figure_run.svg","styles":{"width":20,"height":20,"objectFit":"contain","flexShrink":0,"fillColor":"#FF563D99"}},{"id":"content_flow","component":"Column","children":["primary","support"],"itemMargin":2,"styles":{"width":"matchParent","layoutWeight":1,"alignItems":"start","justifyContent":"start"}},{"id":"primary","component":"Row","children":["primary_value","primary_unit"],"itemMargin":2,"styles":{"justifyContent":"start","alignItems":"bottom","flexShrink":0,"width":"matchParent"}},{"id":"primary_value","component":"Text","content":"{{ ${/data/healthSport/dailySteps} }}","styles":{"height":30,"fontSize":30,"fontWeight":700,"lineHeight":1,"maxLines":1,"flexShrink":0,"fontColor":"#FF563D99","textOverflow":"clip"}},{"id":"primary_unit","component":"Text","content":"步","styles":{"height":14.0,"fontSize":12,"fontWeight":500,"lineHeight":1,"maxLines":1,"flexShrink":0,"fontColor":"#99563D99","padding":{"top":0,"right":0,"bottom":2,"left":0},"textOverflow":"clip"}},{"id":"support","component":"Column","children":["support_row0","support_row1","support_row2"],"itemMargin":2,"styles":{"width":"matchParent","alignItems":"start","flexShrink":1}},{"id":"support_item0_label","component":"Text","content":"热量","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#99563D99","textOverflow":"clip"}},{"id":"support_item0_value","component":"Text","content":"{{ ${/data/healthSport/dailyTotalCaloriesText} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF563D99","layoutWeight":1,"textOverflow":"clip"}},{"id":"support_item0","component":"Row","children":["support_item0_label","support_item0_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"support_row0","component":"Row","children":["support_item0"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"top","flexShrink":0}},{"id":"support_item1_label","component":"Text","content":"睡眠","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#99563D99","textOverflow":"clip"}},{"id":"support_item1_value","component":"Text","content":"{{ ${/data/healthSport/sleepStatus} + ' ' + ${/data/healthSport/sleepScore} + '分' }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF563D99","layoutWeight":1,"textOverflow":"clip"}},{"id":"support_item1","component":"Row","children":["support_item1_label","support_item1_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"support_row1","component":"Row","children":["support_item1"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"top","flexShrink":0}},{"id":"support_item2_label","component":"Text","content":"夜间睡眠","styles":{"height":12,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":0,"lineHeight":1,"fontColor":"#99563D99","textOverflow":"clip"}},{"id":"support_item2_value","component":"Text","content":"{{ ${/data/healthSport/nightSleepDurationText} }}","styles":{"height":12.0,"fontSize":12,"fontWeight":400,"maxLines":1,"flexShrink":1,"lineHeight":1,"fontColor":"#FF563D99","layoutWeight":1,"textOverflow":"clip"}},{"id":"support_item2","component":"Row","children":["support_item2_label","support_item2_value"],"itemMargin":4,"styles":{"height":12.0,"alignItems":"top","flexShrink":1,"constraintSize":{"minWidth":0},"layoutWeight":1}},{"id":"support_row2","component":"Row","children":["support_item2"],"itemMargin":0,"styles":{"width":"matchParent","height":12.0,"alignItems":"top","flexShrink":0}},{"id":"action","component":"Row","children":["action_icon","action_text"],"onClick":[{"call":"clickToDeeplink","args":{"abilityName":"","bundleName":"","intentName":"Health","uri":"huaweischeme://healthapp/home/sport?sportType=2"}}],"itemMargin":8,"styles":{"height":36,"borderRadius":30,"padding":0,"flexShrink":0,"width":"matchParent","backgroundColor":"#33563D99","justifyContent":"center","alignItems":"center"}},{"id":"action_icon","component":"Image","src":"resources/base/media/ic_sportsHealth_bule.svg","styles":{"width":20,"height":20,"objectFit":"contain","flexShrink":0}},{"id":"action_text","component":"Text","content":"打开运动健康","styles":{"maxWidth":96,"height":17,"fontSize":14,"fontWeight":500,"textAlign":"center","maxLines":1,"flexShrink":0,"fontColor":"#FF563D99","textOverflow":"clip"}}]}}
{"version":"v0.9","updateDataModel":{"surfaceId":"surface_card","path":"/","value":{"data":{"healthSport":{"dailySteps":6200,"dailyTotalCaloriesText":"420 千卡","sleepScore":82,"sleepStatus":"良好","nightSleepDurationText":"7小时1分"}}}}}
```
```schema
{
  "schemaVersion": "widget-artifact-v2"
}
```
```taskspec
{
  "userQuery": "生成运动健康的卡片，展示今日步数、热量消耗、睡眠情况等运动健康数据",
  "size": "2x2",
  "appVersion": "11.7.8.342",
  "eventCandidates": [
    {
      "id": "event.open.health.sport",
      "description": "打开华为运动健康应用的锻炼Tab页。",
      "call": "clickToDeeplink",
      "args": {
        "abilityName": "",
        "bundleName": "",
        "intentName": "Health",
        "uri": "huaweischeme://healthapp/home/sport?sportType=2"
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
        "nightSleepDurationText": {
          "type": "string",
          "description": "可直接显示的夜间正式睡眠总时长文本，已包含“小时”或“分”等时间单位；展示时不得再次追加时间单位。例如“7小时1分”。",
          "sampleValue": "7小时1分"
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
        },
        "exerciseCalorieText": {
          "type": "string",
          "description": "可直接显示的单次专业运动净热量消耗文本，已换算并包含“千卡”单位；展示时不得再次追加热量单位。例如“98 千卡”。",
          "sampleValue": "260 千卡"
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
      "id": "asset.emoji_calories_blue",
      "src": "resources/base/media/emoji_calories_blue.png",
      "description": "样式：亮蓝色圆形底上的白色渐变火焰图标，圆形外透明，原始尺寸为 64×64，PNG 位图需保留原色；适用：运动健康卡片中的日常或单次运动热量，可结合 GetHealthAndSportSummary 的 dailyTotalCaloriesText 或 exerciseCalorieText 展示，也可作为 event.open.health.activityRecord、event.open.health.sportsRecord 或 event.open.health.workoutDuration 的辅助入口图标。蓝色仅为视觉配色，不表示热量高低、目标完成或用户正在运动。"
    },
    {
      "id": "asset.figure_run",
      "src": "resources/base/media/figure_run.svg",
      "description": "样式：跑步人物图标，默认黑色，图形为人体奔跑动作侧视轮廓；适用：运动记录、跑步锻炼追踪、步数统计。"
    },
    {
      "id": "asset.flame_fill",
      "src": "resources/base/media/flame_fill.svg",
      "description": "样式：默认黑色的单色实心火焰图标；适用：运动热量消耗、燃烧、火焰或加热状态。"
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
      "id": "event.open.health.sport",
      "description": "打开华为运动健康应用的锻炼Tab页。",
      "call": "clickToDeeplink",
      "args": {
        "abilityName": "",
        "bundleName": "",
        "intentName": "Health",
        "uri": "huaweischeme://healthapp/home/sport?sportType=2"
      }
    }
  ],
  "asset": [
    "asset.ic_sportsHealth_bule",
    "asset.emoji_calories_blue",
    "asset.figure_run",
    "asset.flame_fill"
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
        "/dailyDistanceText",
        "/sleepScore",
        "/sleepStatus",
        "/nightSleepDurationText",
        "/exerciseTypeName",
        "/exerciseDurationText",
        "/exerciseCalorieText"
      ]
    }
  ],
  "candidateEventCandidates": [
    {
      "capabilityId": "event.open.health.sport",
      "action": {
        "call": "clickToDeeplink",
        "args": {
          "abilityName": "",
          "bundleName": "",
          "intentName": "Health",
          "uri": "huaweischeme://healthapp/home/sport?sportType=2"
        }
      }
    }
  ],
  "candidateAssetIds": [
    "asset.ic_sportsHealth_bule",
    "asset.emoji_calories_blue",
    "asset.figure_run",
    "asset.flame_fill"
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
  "artifactId": "3215554c-0f3f-4622-bc78-e19fe91dd17e",
  "createdAt": 1793951053143
}
```
```designcompactdsl
["root","Column",{"width":"matchParent","height":"matchParent","borderRadius":20,"clip":true,"alignItems":"start","justifyContent":"start","padding":12,"itemMargin":0},["title","content_flow","action"]]
["title","SingleLineTitle",{"title":"运动健康","icon":"resources/base/media/figure_run.svg","fontSize":12,"width":"matchParent"}]
["content_flow","Column",{"width":"matchParent","layoutWeight":1,"itemMargin":2,"alignItems":"start","justifyContent":"start"},["primary","support"]]
["primary","EmphasizedData",{"value":{"path":"/data/healthSport/dailySteps"},"unit":"步","fontSize":30,"width":"matchParent"}]
["support","SecondaryBody",{"items":[{"label":"热量 ","value":{"path":"/data/healthSport/dailyTotalCaloriesText"}},{"label":"睡眠 ","value":"{{ ${/data/healthSport/sleepStatus} + ' ' + ${/data/healthSport/sleepScore} + '分' }}"},{"label":"夜间睡眠 ","value":{"path":"/data/healthSport/nightSleepDurationText"}}],"columns":1,"fontSize":12,"width":"matchParent"}]
["action","PillButton",{"label":"打开运动健康","icon":"resources/base/media/ic_sportsHealth_bule.svg","onClick":[{"call":"clickToDeeplink","args":{"abilityName":"","bundleName":"","intentName":"Health","uri":"huaweischeme://healthapp/home/sport?sportType=2"}}]}]
["/data/healthSport/dailySteps",6200]
["/data/healthSport/dailyTotalCaloriesText","420 千卡"]
["/data/healthSport/sleepScore",82]
["/data/healthSport/sleepStatus","良好"]
["/data/healthSport/nightSleepDurationText","7小时1分"]
```
```request
{
  "content": {
    "size": "2x2",
    "functionName": "generateWidgetCardCompactDsl",
    "romVersion": "CMS-AL20 7.0.0.111",
    "candidateAssetIds": [
      "asset.ic_sportsHealth_bule",
      "asset.emoji_calories_blue",
      "asset.figure_run",
      "asset.flame_fill"
    ],
    "candidateEventCandidates": [
      {
        "capabilityId": "event.open.health.sport",
        "action": {
          "call": "clickToDeeplink",
          "args": {
            "abilityName": "",
            "bundleName": "",
            "intentName": "Health",
            "uri": "huaweischeme://healthapp/home/sport?sportType=2"
          }
        }
      }
    ],
    "bundleName": "com.huawei.genui",
    "description": "运动健康卡片",
    "userQuery": "生成运动健康的卡片，展示今日步数、热量消耗、睡眠情况等运动健康数据",
    "title": "运动健康",
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
          "/dailyDistanceText",
          "/sleepScore",
          "/sleepStatus",
          "/nightSleepDurationText",
          "/exerciseTypeName",
          "/exerciseDurationText",
          "/exerciseCalorieText"
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
    "prdVer": "11.7.8.342",
    "sysVer": "EmotionUI_9.0.0",
    "time": "20261101123925211"
  },
  "pagination": {
    "limit": 5,
    "start": ""
  },
  "session": {
    "interactionId": "Q414-000",
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
  "romVersion": "CMS-AL20 7.0.0.111",
  "candidateAssetIds": [
    "asset.ic_sportsHealth_bule",
    "asset.emoji_calories_blue",
    "asset.figure_run",
    "asset.flame_fill"
  ],
  "candidateEventCandidates": [
    {
      "capabilityId": "event.open.health.sport",
      "action": {
        "call": "clickToDeeplink",
        "args": {
          "abilityName": "",
          "bundleName": "",
          "intentName": "Health",
          "uri": "huaweischeme://healthapp/home/sport?sportType=2"
        }
      }
    }
  ],
  "bundleName": "com.huawei.genui",
  "description": "运动健康卡片",
  "userQuery": "生成运动健康的卡片，展示今日步数、热量消耗、睡眠情况等运动健康数据",
  "title": "运动健康",
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
        "/dailyDistanceText",
        "/sleepScore",
        "/sleepStatus",
        "/nightSleepDurationText",
        "/exerciseTypeName",
        "/exerciseDurationText",
        "/exerciseCalorieText"
      ]
    }
  ]
}
```
